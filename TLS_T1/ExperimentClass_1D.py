"""
This file contains useful python functions meant to simplify the Jupyter notebook.
ExperimentHandle.exp1D
written by Mo Chen in Oct. 2023
"""
from qm.qua import *
from qm.QuantumMachinesManager import QuantumMachinesManager
from qm import SimulationConfig, LoopbackInterface, generate_qua_script
from qm.octave import *
from qm.octave.octave_manager import ClockMode
from configuration import *
from scipy import signal
from qualang_tools.bakery import baking
from qualang_tools.units import unit
from qm.octave import QmOctaveConfig
from set_octave import ElementsSettings, octave_settings
from quam import QuAM
from scipy.io import savemat, loadmat
from scipy.optimize import curve_fit, minimize
from scipy.signal import savgol_filter
from qutip import *
from typing import Union
from macros import *
import datetime
import os
import time
import warnings
import json
import matplotlib.pyplot as plt
import numpy as np
import Labber

warnings.filterwarnings("ignore")

class EH_RR: # sub
	"""
	class in ExperimentHandle, for Readout Resonator (RR) related 1D experiments
	Methods:
		update_tPath
		update_str_datetime
		time_of_flight(self, qubit_index, res_index, n_avg, cd_time, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000)
		rr_freq(self, res_freq_sweep, qubit_index, res_index, flux_index, n_avg, cd_time, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000)
	"""
	def __init__(self, ref_to_update_tPath, ref_to_update_str_datetime):
		self.update_tPath = ref_to_update_tPath
		self.update_str_datetime = ref_to_update_str_datetime

	def time_of_flight(self, qubit_index, res_index, flux_index, n_avg = 5E3, cd_time = 20E3, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, machine = None):
		"""
		time of flight 1D experiment
		this experiment calibrates
			1. the time delay between when the RO tone is sent, and when it is received by the adc/digitizer.
				Note it could be different for different qubit, due to resonator Q. Although I do not calibrate for individual qubits.
			2. the dc offset for I, Q readout signal.
			3. if we need to adjust the attenuation of RO on the output side, s.t. the signal fully span the +-0.5V adc range, but does not exceed it (and be cutoff)

		Args:
		:param qubit_index:
		:param res_index:
		:param flux_index:
		:param n_avg: repetition of expeirment
		:param cd_time: cooldown time between subsequent experiments
		:param tPath: target path/folder for saving the data. Default is today.
		:param f_str_datetime: datetime string for saving the data. Default is now.
		:param simulate_flag: True-run simulation; False (default)-run experiment.
		:param simulation_len: Length of the sequence to simulate. In clock cycles (4ns).
		:param machine: None (default), will read from quam_state.json
		Return:
			machine
			adc1
			adc2
			adc1_single_run
			adc2_single_run
		"""

		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)

		with program() as raw_trace_prog:
			n = declare(int)
			adc_st = declare_stream(adc_trace=True)
			n_st = declare_stream()

			with for_(n, 0, n < n_avg, n + 1):
				reset_phase(machine.resonators[res_index].name)
				measure("readout", machine.resonators[res_index].name, adc_st)
				wait(cd_time * u.ns, machine.resonators[res_index].name)
				save(n,n_st)
			with stream_processing():
				# Will save average:
				adc_st.input1().average().save("adc1")
				adc_st.input2().average().save("adc2")
				# # Will save only last run:
				adc_st.input1().save("adc1_single_run")
				adc_st.input2().save("adc2_single_run")
				n_st.save('iteration')

		#####################################
		#  Open Communication with the QOP  #
		#####################################
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config, log_level = "ERROR")

		if simulate_flag:
			simulation_config = SimulationConfig(duration=simulation_len)
			job = qmm.simulate(config, raw_trace_prog, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			qm = qmm.open_qm(config)
			job = qm.execute(raw_trace_prog)
			res_handles = job.result_handles
			res_handles.wait_for_all_values()
			adc1 = u.raw2volts(res_handles.get("adc1").fetch_all())
			adc2 = u.raw2volts(res_handles.get("adc2").fetch_all())
			adc1_single_run = u.raw2volts(res_handles.get("adc1_single_run").fetch_all())
			adc2_single_run = u.raw2volts(res_handles.get("adc2_single_run").fetch_all())

			# save data
			exp_name = 'time_of_flight'
			qubit_name = 'Q' + str(res_index+1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name), {"adc1": adc1, "adc2": adc2, "adc1_single_run": adc1_single_run, "adc2_single_run": adc2_single_run})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, adc1,adc2,adc1_single_run,adc2_single_run

	def rr_freq(self, res_freq_sweep, qubit_index, res_index, flux_index, n_avg = 1E3, cd_time = 20E3, readout_state = 'g', tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
		resonator spectroscopy experiment
		this experiment find the resonance frequency by localizing the minima in pulsed transmission signal.

		Args:
		:param res_freq_sweep: 1D array for resonator frequency sweep
		:param qubit_index:
		:param res_index:
		:param flux_index:
		:param n_avg: repetition of expeirment
		:param cd_time: cooldown time between subsequent experiments
		:param readout_state: 'g' (default). If 'e', readout done for |e>. If anything else, return error. Expandable for 'f' etc in the future.
		:param tPath: target path/folder for saving the data. Default is today.
		:param f_str_datetime: datetime string for saving the data. Default is now.
		:param simulate_flag: True-run simulation; False (default)-run experiment.
		:param simulation_len: Length of the sequence to simulate. In clock cycles (4ns).
		:param plot_flag: True (default) plot the experiment. False, do not plot.
		:param machine: None (default), will read from quam_state.json
		Return:
			machine
			res_freq_sweep
			sig_amp
		"""

		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)
		res_lo = machine.resonators[res_index].lo
		res_if_sweep = res_freq_sweep - res_lo
		res_if_sweep = np.round(res_if_sweep)

		if np.max(abs(res_if_sweep)) > 400E6: # check if parameters are within hardware limit
			print("res if range > 400MHz")
			return None, None, None

		with program() as rr_freq_prog:
			[I,Q,n,I_st,Q_st,n_st] = declare_vars()
			df = declare(int)

			with for_(n, 0, n < n_avg, n+1):
				with for_(*from_array(df,res_if_sweep)):
					if readout_state == 'g':
						pass
					elif readout_state == 'e':
						play("pi", machine.qubits[qubit_index].name)
						align()
					else:
						print("readout state does not exist")
						return None, None, None
					update_frequency(machine.resonators[res_index].name, df)
					readout_avg_macro(machine.resonators[res_index].name,I,Q)
					wait(cd_time * u.ns, machine.resonators[res_index].name)
					save(I, I_st)
					save(Q, Q_st)
					save(n, n_st)
			with stream_processing():
				n_st.save('iteration')
				I_st.buffer(len(res_if_sweep)).average().save("I")
				Q_st.buffer(len(res_if_sweep)).average().save("Q")

		#####################################
		#  Open Communication with the QOP  #
		#####################################
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config, log_level = "ERROR")
		# Simulate or execute #
		if simulate_flag: # simulation is useful to see the sequence, especially the timing (clock cycle vs ns)
			simulation_config = SimulationConfig(duration=simulation_len)
			job = qmm.simulate(config, rr_freq_prog, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			qm = qmm.open_qm(config)
			job = qm.execute(rr_freq_prog)
			# Get results from QUA program
			results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
			# Live plotting
		    #%matplotlib qt
			if plot_flag == True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [8, 4]
				interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

			while results.is_processing():
				# Fetch results
				I, Q, iteration = results.fetch_all()
				I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
				Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
				# progress bar
				progress_counter(iteration, n_avg, start_time=results.get_start_time())

				if plot_flag == True:
					plt.cla()
					plt.title("Resonator spectroscopy")
					plt.plot((res_freq_sweep) / u.MHz, np.sqrt(I**2 +  Q**2), ".")
					plt.xlabel("Frequency [MHz]")
					plt.ylabel(r"$\sqrt{I^2 + Q^2}$ [V]")

			# fetch all data after live-updating
			I, Q, iteration = results.fetch_all()
			# Convert I & Q to Volts
			I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
			Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
			sig_amp = np.sqrt(I**2 + Q**2)
			sig_phase = np.angle(I + 1j * Q)

			# save data
			exp_name = 'RR_freq'
			qubit_name = 'Q' + str(res_index+1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name), {"RR_freq": res_freq_sweep, "sig_amp": sig_amp, "sig_phase": sig_phase, "readout_state": readout_state})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, res_freq_sweep, sig_amp

	def rr_switch_delay(self, rr_switch_delay_sweep, qubit_index, res_index, flux_index, n_avg = 10E3, cd_time = 20E3, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
		1D experiment to calibrate switch delay for the resonator.

		Args:
			rr_switch_delay_sweep (): in ns
			qubit_index ():
			res_index ():
			flux_index ():
			n_avg ():
			cd_time ():
			tPath ():
			f_str_datetime ():
			simulate_flag ():
			simulation_len ():
			plot_flag ():
			machine ():

		Returns:
			machine
			rr_switch_delay_sweep
			sig_amp
		"""
		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)
		res_lo = machine.resonators[res_index].lo
		res_if = machine.resonators[res_index].f_readout - res_lo

		if abs(res_if) > 400E6: # check if parameters are within hardware limit
			print("res if > 400MHz")
			return None

		with program() as rr_switch_delay_prog:
			[I,Q,n,I_st,Q_st,n_st] = declare_vars()

			with for_(n, 0, n < n_avg, n+1):
				update_frequency(machine.resonators[res_index].name, res_if)
				readout_avg_macro(machine.resonators[res_index].name,I,Q)
				wait(cd_time * u.ns, machine.resonators[res_index].name)
				save(I, I_st)
				save(Q, Q_st)
			with stream_processing():
				I_st.average().save("I")
				Q_st.average().save("Q")

		#####################################
		#  Open Communication with the QOP  #
		#####################################
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config, log_level = "ERROR")
		# Simulate or execute #
		if simulate_flag: # simulation is useful to see the sequence, especially the timing (clock cycle vs ns)
			simulation_config = SimulationConfig(duration=simulation_len)
			job = qmm.simulate(config, rr_switch_delay_prog, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			start_time = time.time()
			I_tot = []
			Q_tot = []
			if plot_flag == True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [8, 4]

			for delay_index, delay_value in enumerate(rr_switch_delay_sweep):
				machine.resonators[res_index].digital_marker.delay = int(delay_value)
				config = build_config(machine)

				qm = qmm.open_qm(config)
				job = qm.execute(rr_switch_delay_prog)
				# Get results from QUA program
				results = fetching_tool(job, data_list=["I", "Q"], mode = "live")

				if plot_flag:
					interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
				while results.is_processing():
					# Fetch results
					time.sleep(0.1)

				I, Q = results.fetch_all()
				I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
				Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
				I_tot.append(I)
				Q_tot.append(Q)

				# progress bar
				progress_counter(delay_index, len(rr_switch_delay_sweep), start_time=start_time)

			I_tot = np.array(I_tot)
			Q_tot = np.array(Q_tot)
			sigs_qubit = I_tot + 1j * Q_tot
			sig_amp = np.abs(sigs_qubit)  # Amplitude
			sig_phase = np.angle(sigs_qubit)  # Phase

			if plot_flag == True:
				plt.cla()
				plt.title("res. switch delay")
				plt.plot(rr_switch_delay_sweep, sig_amp, ".")
				plt.xlabel("switch delay [ns]")
				plt.ylabel("Signal [V]")

			# save data
			exp_name = 'res_switch_delay'
			qubit_name = 'Q' + str(res_index+1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name), {"res_delay": rr_switch_delay_sweep, "sig_amp": sig_amp, "sig_phase": sig_phase})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, rr_switch_delay_sweep, sig_amp

	def rr_switch_buffer(self, rr_switch_buffer_sweep, qubit_index, res_index, flux_index, n_avg = 10E3, cd_time = 20E3, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
		1D experiment to calibrate switch delay for the resonator.

		Args:
			rr_switch_buffer_sweep (): in ns, this will be added to both sides of the switch (x2), to account for the rise and fall
			qubit_index ():
			res_index ():
			flux_index ():
			n_avg ():
			cd_time ():
			tPath ():
			f_str_datetime ():
			simulate_flag ():
			simulation_len ():
			plot_flag ():
			machine ():

		Returns:

		"""
		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)
		res_lo = machine.resonators[res_index].lo
		res_if = machine.resonators[res_index].f_readout - res_lo

		if abs(res_if) > 400E6: # check if parameters are within hardware limit
			print("res if > 400MHz")
			return None

		with program() as rr_switch_buffer_prog:
			[I,Q,n,I_st,Q_st,n_st] = declare_vars()

			with for_(n, 0, n < n_avg, n+1):
				update_frequency(machine.resonators[res_index].name, res_if)
				readout_avg_macro(machine.resonators[res_index].name,I,Q)
				wait(cd_time * u.ns, machine.resonators[res_index].name)
				save(I, I_st)
				save(Q, Q_st)
			with stream_processing():
				I_st.average().save("I")
				Q_st.average().save("Q")

		#####################################
		#  Open Communication with the QOP  #
		#####################################
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config, log_level = "ERROR")
		# Simulate or execute #
		if simulate_flag: # simulation is useful to see the sequence, especially the timing (clock cycle vs ns)
			simulation_config = SimulationConfig(duration=simulation_len)
			job = qmm.simulate(config, rr_switch_buffer_prog, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			start_time = time.time()
			I_tot = []
			Q_tot = []
			if plot_flag == True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [8, 4]

			for buffer_index, buffer_value in enumerate(rr_switch_buffer_sweep):
				machine.resonators[res_index].digital_marker.buffer = int(buffer_value)
				config = build_config(machine)

				qm = qmm.open_qm(config)
				job = qm.execute(rr_switch_buffer_prog)
				# Get results from QUA program
				results = fetching_tool(job, data_list=["I", "Q"], mode = "live")

				if plot_flag:
					interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
				while results.is_processing():
					# Fetch results
					time.sleep(0.1)

				I, Q = results.fetch_all()
				I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
				Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
				I_tot.append(I)
				Q_tot.append(Q)

				# progress bar
				progress_counter(buffer_index, len(rr_switch_buffer_sweep), start_time=start_time)

			I_tot = np.array(I_tot)
			Q_tot = np.array(Q_tot)
			sigs_qubit = I_tot + 1j * Q_tot
			sig_amp = np.abs(sigs_qubit)  # Amplitude
			sig_phase = np.angle(sigs_qubit)  # Phase

			if plot_flag == True:
				plt.cla()
				plt.title("res. switch buffer")
				plt.plot(rr_switch_buffer_sweep, sig_amp, ".")
				plt.xlabel("switch buffer [ns]")
				plt.ylabel("Signal [V]")

			# save data
			exp_name = 'res_switch_buffer'
			qubit_name = 'Q' + str(res_index+1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name), {"res_buffer": rr_switch_buffer_sweep, "sig_amp": sig_amp, "sig_phase": sig_phase})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, rr_switch_buffer_sweep, sig_amp

	def single_shot_IQ_blob(self, res_freq, qubit_index, res_index, flux_index, n_avg = 1E3, cd_time = 20E3, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):

		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if machine is None:
			machine = QuAM("quam_state.json")

		config = build_config(machine)
		res_lo = machine.resonators[res_index].lo
		res_if = np.round(res_freq - res_lo)

		if abs(res_if) > 400E6: # check if parameters are within hardware limit
			print("res if > 400MHz")
			return None, None, None

		with program() as rr_IQ_prog:
			n = declare(int)
			I_g = declare(fixed)
			Q_g = declare(fixed)
			I_g_st = declare_stream()
			Q_g_st = declare_stream()
			I_e = declare(fixed)
			Q_e = declare(fixed)
			I_e_st = declare_stream()
			Q_e_st = declare_stream()

			with for_(n, 0, n < n_avg, n+1):
				measure(
					"readout",
					machine.resonators[res_index].name,
					None,
					dual_demod.full("rotated_cos", "out1", "rotated_sin", "out2", I_g),
					dual_demod.full("rotated_minus_sin", "out1", "rotated_cos", "out2", Q_g),
				)
				save(I_g, I_g_st)
				save(Q_g, Q_g_st)
				wait(cd_time * u.ns, machine.resonators[res_index].name)

				align()  # global align

				play("pi", machine.qubits[qubit_index].name)
				align(machine.qubits[qubit_index].name, machine.resonators[res_index].name)
				measure(
					"readout",
					machine.resonators[res_index].name,
					None,
					dual_demod.full("rotated_cos", "out1", "rotated_sin", "out2", I_e),
					dual_demod.full("rotated_minus_sin", "out1", "rotated_cos", "out2", Q_e),
				)

				save(I_e, I_e_st)
				save(Q_e, Q_e_st)
				wait(cd_time * u.ns, machine.resonators[res_index].name)

			with stream_processing():
				I_g_st.save_all("I_g")
				Q_g_st.save_all("Q_g")
				I_e_st.save_all("I_e")
				Q_e_st.save_all("Q_e")

		#####################################
		#  Open Communication with the QOP  #
		#####################################
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config, log_level = "ERROR")
		# Simulate or execute #
		if simulate_flag: # simulation is useful to see the sequence, especially the timing (clock cycle vs ns)
			simulation_config = SimulationConfig(duration=simulation_len)
			job = qmm.simulate(config, rr_IQ_prog, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			qm = qmm.open_qm(config)
			job = qm.execute(rr_IQ_prog)
			# Get results from QUA program
			res_handles = job.result_handles

			# Waits (blocks the Python console) until all results have been acquired
			res_handles.wait_for_all_values()
			# Fetch the 'I' & 'Q' points for the qubit in the ground and excited states
			Ig = res_handles.get("I_g").fetch_all()["value"]
			Qg = res_handles.get("Q_g").fetch_all()["value"]
			Ie = res_handles.get("I_e").fetch_all()["value"]
			Qe = res_handles.get("Q_e").fetch_all()["value"]

			if plot_flag == True:
				fig = plt.figure()
				ax = plt.gca()
				plt.rcParams['figure.figsize'] = [8, 4]
				plt.plot(Ig, Qg, ".", alpha=0.1, label="Ground", markersize=3)
				plt.plot(Ie, Qe, ".", alpha=0.1, label="Excited", markersize=3)
				ax.set_aspect("equal","box")
				plt.legend(["Ground", "Excited"])
				plt.xlabel("I")
				plt.ylabel("Q")
				plt.title("Original Data")
				ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), fancybox=True, shadow=True, ncol=5,
						   markerscale=5)
				plt.show()

			# save data
			exp_name = 'single_shot_IQ'
			qubit_name = 'Q' + str(res_index+1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name), {"I_g": I_g, "Q_g": Q_g, "I_e": I_e, "Q_e": Q_e})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, Ig, Qg, Ie, Qe

	def single_shot_freq_optimization(self, res_freq_sweep, qubit_index, res_index, flux_index, n_avg = 10E3, cd_time = 20E3, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
		        READOUT OPTIMISATION: FREQUENCY
		This sequence involves measuring the state of the resonator in two scenarios: first, after thermalization
		(with the qubit in the |g> state) and then after applying a pi pulse to the qubit (transitioning the qubit to the
		|e> state). This is done while varying the readout frequency.
		The average I & Q quadratures for the qubit states |g> and |e>, along with their variances, are extracted to
		determine the Signal-to-Noise Ratio (SNR). The readout frequency that yields the highest SNR is selected as the
		optimal choice.

		:param res_freq_sweep:
		:param qubit_index:
		:param res_index:
		:param flux_index:
		:param n_avg:
		:param cd_time:
		:param tPath:
		:param f_str_datetime:
		:param simulate_flag:
		:param simulation_len:
		:param plot_flag:
		:param machine:
		:return:
			machine
			SNR
			res_freq_opt
		"""

		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if machine is None:
			machine = QuAM("quam_state.json")

		config = build_config(machine)
		res_lo = machine.resonators[res_index].lo
		res_if_sweep = res_freq_sweep - res_lo
		res_if_sweep = np.round(res_if_sweep)

		if np.max(abs(res_if_sweep)) > 400E6:  # check if parameters are within hardware limit
			print("res if range > 400MHz")
			return None, None, None

		with program() as ro_freq_opt:
			n = declare(int)  # QUA variable for the averaging loop
			df = declare(int)  # QUA variable for the readout IF frequency
			I_g = declare(fixed)  # QUA variable for the 'I' quadrature when the qubit is in |g>
			Q_g = declare(fixed)  # QUA variable for the 'Q' quadrature when the qubit is in |g>
			Ig_st = declare_stream()
			Qg_st = declare_stream()
			I_e = declare(fixed)  # QUA variable for the 'I' quadrature when the qubit is in |e>
			Q_e = declare(fixed)  # QUA variable for the 'Q' quadrature when the qubit is in |e>
			Ie_st = declare_stream()
			Qe_st = declare_stream()
			n_st = declare_stream()

			with for_(n, 0, n < n_avg, n + 1):
				with for_(*from_array(df, res_if_sweep)):
					# Update the frequency of the digital oscillator linked to the resonator element
					update_frequency(machine.resonators[res_index].name, df)
					# Measure the state of the resonator
					measure(
						"readout",
						machine.resonators[res_index].name,
						None,
						dual_demod.full("rotated_cos", "out1", "rotated_sin", "out2", I_g),
						dual_demod.full("rotated_minus_sin", "out1", "rotated_cos", "out2", Q_g),
					)
					# Wait for the qubit to decay to the ground state
					wait(cd_time * u.ns, machine.resonators[res_index].name)
					# Save the 'I_e' & 'Q_e' quadratures to their respective streams
					save(I_g, Ig_st)
					save(Q_g, Qg_st)

					align()  # global align
					# Play the x180 gate to put the qubit in the excited state
					play("pi", machine.qubits[qubit_index].name)
					# Align the two elements to measure after playing the qubit pulse.
					align(machine.qubits[qubit_index].name, machine.resonators[res_index].name)
					# Measure the state of the resonator
					measure(
						"readout",
						machine.resonators[res_index].name,
						None,
						dual_demod.full("rotated_cos", "out1", "rotated_sin", "out2", I_e),
						dual_demod.full("rotated_minus_sin", "out1", "rotated_cos", "out2", Q_e),
					)
					# Wait for the qubit to decay to the ground state
					wait(cd_time * u.ns, machine.resonators[res_index].name)
					# Save the 'I_e' & 'Q_e' quadratures to their respective streams
					save(I_e, Ie_st)
					save(Q_e, Qe_st)
				# Save the averaging iteration to get the progress bar
				save(n, n_st)

			with stream_processing():
				n_st.save("iteration")
				# mean values
				Ig_st.buffer(len(res_if_sweep)).average().save("Ig_avg")
				Qg_st.buffer(len(res_if_sweep)).average().save("Qg_avg")
				Ie_st.buffer(len(res_if_sweep)).average().save("Ie_avg")
				Qe_st.buffer(len(res_if_sweep)).average().save("Qe_avg")
				# variances to get the SNR
				(
						((Ig_st.buffer(len(res_if_sweep)) * Ig_st.buffer(len(res_if_sweep))).average())
						- (Ig_st.buffer(len(res_if_sweep)).average() * Ig_st.buffer(len(res_if_sweep)).average())
				).save("Ig_var")
				(
						((Qg_st.buffer(len(res_if_sweep)) * Qg_st.buffer(len(res_if_sweep))).average())
						- (Qg_st.buffer(len(res_if_sweep)).average() * Qg_st.buffer(len(res_if_sweep)).average())
				).save("Qg_var")
				(
						((Ie_st.buffer(len(res_if_sweep)) * Ie_st.buffer(len(res_if_sweep))).average())
						- (Ie_st.buffer(len(res_if_sweep)).average() * Ie_st.buffer(len(res_if_sweep)).average())
				).save("Ie_var")
				(
						((Qe_st.buffer(len(res_if_sweep)) * Qe_st.buffer(len(res_if_sweep))).average())
						- (Qe_st.buffer(len(res_if_sweep)).average() * Qe_st.buffer(len(res_if_sweep)).average())
				).save("Qe_var")

		#####################################
		#  Open Communication with the QOP  #
		#####################################
		qmm = QuantumMachinesManager(machine.network.qop_ip, port='9510', octave=octave_config, log_level="ERROR")
		# Simulate or execute #
		if simulate_flag:  # simulation is useful to see the sequence, especially the timing (clock cycle vs ns)
			simulation_config = SimulationConfig(duration=simulation_len)
			job = qmm.simulate(config, ro_freq_opt, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			# Open the quantum machine
			qm = qmm.open_qm(config)
			# Send the QUA program to the OPX, which compiles and executes it
			job = qm.execute(ro_freq_opt)  # execute QUA program
			# Get results from QUA program
			results = fetching_tool(
				job,
				data_list=["Ig_avg", "Qg_avg", "Ie_avg", "Qe_avg", "Ig_var", "Qg_var", "Ie_var", "Qe_var", "iteration"],
				mode="live",
			)

			if plot_flag == True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [8, 4]
				interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

			while results.is_processing():
				# Fetch results
				Ig_avg, Qg_avg, Ie_avg, Qe_avg, Ig_var, Qg_var, Ie_var, Qe_var, iteration = results.fetch_all()
				# Progress bar
				progress_counter(iteration, n_avg, start_time=results.get_start_time())
				# Derive the SNR
				Z = (Ie_avg - Ig_avg) + 1j * (Qe_avg - Qg_avg)
				var = (Ig_var + Qg_var + Ie_var + Qe_var) / 4
				SNR = ((np.abs(Z)) ** 2) / (2 * var)

				# Plot results
				if plot_flag == True:
					plt.cla()
					plt.plot(res_freq_sweep / u.MHz, SNR, ".-")
					plt.title("Readout frequency optimization")
					plt.xlabel("Readout frequency [MHz]")
					plt.ylabel("SNR")
					plt.grid("on")
					plt.pause(0.1)

			print(f"The optimal readout frequency is {res_freq_sweep[np.argmax(SNR)]} Hz (SNR={max(SNR)})")

			# save data
			exp_name = 'single_shot_freq_optimization'
			qubit_name = 'Q' + str(res_index + 1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name),
					{"RR_freq": res_freq_sweep, "SNR": SNR, "Ig_avg": Ig_avg, "Ie_avg": Ie_avg, "Ig_var": Ig_var, "Ie_var": Ie_var})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, SNR, res_freq_sweep[np.argmax(SNR)]

	def single_shot_amp_optimization(self, res_amp_rel_sweep, qubit_index, res_index, flux_index, n_avg = 10E3, cd_time = 20E3, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
				READOUT OPTIMISATION: AMPLITUDE
		The sequence consists in measuring the state of the resonator after thermalization (qubit in |g>) and after
		playing a pi pulse to the qubit (qubit in |e>) successively while sweeping the readout amplitude.
		The 'I' & 'Q' quadratures when the qubit is in |g> and |e> are extracted to derive the readout fidelity.
		The optimal readout amplitude is chosen as to maximize the readout fidelity.

		:param res_amp_sweep:
		:param qubit_index:
		:param res_index:
		:param flux_index:
		:param n_avg:
		:param cd_time:
		:param tPath:
		:param f_str_datetime:
		:param simulate_flag:
		:param simulation_len:
		:param plot_flag:
		:param machine:
		:return:
			machine
			res_amp_sweep_abs: in V
			fidelity
			res_amp_opt
		"""

		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if machine is None:
			machine = QuAM("quam_state.json")

		config = build_config(machine)

		if max(abs(res_amp_rel_sweep)) > 2.0:
			print("some rel amps > 2.0, removed from experiment run")
			res_amp_rel_sweep = res_amp_rel_sweep[abs(res_amp_rel_sweep) < 2.0]

		readout_amp = machine.resonators[res_index].readout_pulse_amp
		res_amp_abs_sweep = readout_amp * res_amp_rel_sweep
		if max(abs(res_amp_abs_sweep)) > 0.5:
			print("some abs amps > 0.5, removed from experiment run")
			res_amp_rel_sweep = res_amp_rel_sweep[abs(res_amp_abs_sweep) < 0.5]

		with program() as ro_amp_opt:
			n = declare(int)  # QUA variable for the number of runs
			counter = declare(int, value=0)  # Counter for the progress bar
			a = declare(fixed)  # QUA variable for the readout amplitude
			I_g = declare(fixed)  # QUA variable for the 'I' quadrature when the qubit is in |g>
			Q_g = declare(fixed)  # QUA variable for the 'Q' quadrature when the qubit is in |g>
			Ig_st = declare_stream()
			Qg_st = declare_stream()
			I_e = declare(fixed)  # QUA variable for the 'I' quadrature when the qubit is in |e>
			Q_e = declare(fixed)  # QUA variable for the 'Q' quadrature when the qubit is in |e>
			Ie_st = declare_stream()
			Qe_st = declare_stream()
			n_st = declare_stream()

			with for_(*from_array(a, res_amp_rel_sweep)):
				save(counter, n_st)
				with for_(n, 0, n < n_avg, n + 1):
					# Measure the state of the resonator
					measure(
						"readout" * amp(a),
						machine.resonators[res_index].name,
						None,
						dual_demod.full("rotated_cos", "out1", "rotated_sin", "out2", I_g),
						dual_demod.full("rotated_minus_sin", "out1", "rotated_cos", "out2", Q_g),
					)
					# Wait for the qubit to decay to the ground state
					wait(cd_time * u.ns, machine.resonators[res_index].name)
					# Save the 'I_e' & 'Q_e' quadratures to their respective streams
					save(I_g, Ig_st)
					save(Q_g, Qg_st)

					align()  # global align
					# Play the x180 gate to put the qubit in the excited state
					play("pi", machine.qubits[qubit_index].name)
					# Align the two elements to measure after playing the qubit pulse.
					align(machine.qubits[qubit_index].name, machine.resonators[res_index].name)
					# Measure the state of the resonator
					measure(
						"readout" * amp(a),
						machine.resonators[res_index].name,
						None,
						dual_demod.full("rotated_cos", "out1", "rotated_sin", "out2", I_e),
						dual_demod.full("rotated_minus_sin", "out1", "rotated_cos", "out2", Q_e),
					)
					# Wait for the qubit to decay to the ground state
					wait(cd_time * u.ns, machine.resonators[res_index].name)
					# Save the 'I_e' & 'Q_e' quadratures to their respective streams
					save(I_e, Ie_st)
					save(Q_e, Qe_st)
				# Save the counter to get the progress bar
				assign(counter, counter + 1)

			with stream_processing():
				# mean values
				Ig_st.buffer(n_avg).buffer(len(res_amp_rel_sweep)).save("I_g")
				Qg_st.buffer(n_avg).buffer(len(res_amp_rel_sweep)).save("Q_g")
				Ie_st.buffer(n_avg).buffer(len(res_amp_rel_sweep)).save("I_e")
				Qe_st.buffer(n_avg).buffer(len(res_amp_rel_sweep)).save("Q_e")
				n_st.save("iteration")

		#####################################
		#  Open Communication with the QOP  #
		#####################################
		qmm = QuantumMachinesManager(machine.network.qop_ip, port='9510', octave=octave_config, log_level="ERROR")
		# Simulate or execute #
		if simulate_flag:  # simulation is useful to see the sequence, especially the timing (clock cycle vs ns)
			simulation_config = SimulationConfig(duration=simulation_len)
			job = qmm.simulate(config, ro_amp_opt, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			# Open the quantum machine
			qm = qmm.open_qm(config)
			# Send the QUA program to the OPX, which compiles and executes it
			job = qm.execute(ro_amp_opt)  # execute QUA program
			# Get results from QUA program
			results = fetching_tool(job, data_list=["iteration"], mode="live")
			# Get progress counter to monitor runtime of the program
			while results.is_processing():
				# Fetch results
				iteration = results.fetch_all()
				# Progress bar
				progress_counter(iteration[0], len(res_amp_rel_sweep), start_time=results.get_start_time())

			# Fetch the results at the end
			results = fetching_tool(job, data_list=["I_g", "Q_g", "I_e", "Q_e"])
			I_g, Q_g, I_e, Q_e = results.fetch_all()

			# Process the data
			fidelity_vec = []
			for i in range(len(res_amp_rel_sweep)):
				angle, threshold, fidelity, gg, ge, eg, ee = self.two_state_discriminator(
					I_g[i], Q_g[i], I_e[i], Q_e[i], plot_flag = False, print_flag = False
				)
				fidelity_vec.append(fidelity)

			# Plot the data
			if plot_flag == True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [8, 4]
				plt.plot(res_amp_rel_sweep * readout_amp, fidelity_vec, ".-")
				plt.title("Readout amplitude optimization")
				plt.xlabel("Readout amplitude [V]")
				plt.ylabel("Readout fidelity [%]")

			res_amp_opt = readout_amp * res_amp_rel_sweep[np.argmax(fidelity_vec)]
			print(
				f"The optimal readout amplitude is {res_amp_opt / u.mV:.3f} mV (Fidelity={max(fidelity_vec):.1f}%)"
			)

			# save data
			exp_name = 'single_shot_amp_optimization'
			qubit_name = 'Q' + str(res_index + 1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name),
					{"RR_amp": res_amp_rel_sweep * readout_amp, "fidelity": fidelity_vec})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, res_amp_rel_sweep * readout_amp, fidelity_vec, res_amp_opt

	def single_shot_duration_optimization(self, readout_len, ringdown_len, division_length , qubit_index, res_index, flux_index, n_avg = 10E3, cd_time = 20E3, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
				READOUT OPTIMISATION: DURATION
		This sequence involves measuring the state of the resonator in two scenarios: first, after thermalization
		(with the qubit in the |g> state) and then after applying a pi pulse to the qubit (transitioning the qubit to the
		|e> state). The "demod.accumulated" method is employed to assess the state of the resonator over varying durations.
		Reference: (https://docs.quantum-machines.co/0.1/qm-qua-sdk/docs/Guides/features/?h=accumulated#accumulated-demodulation)
		The average I & Q quadratures for the qubit states |g> and |e>, along with their variances, are extracted to determine
		the Signal-to-Noise Ratio (SNR). The readout duration that offers the highest SNR is identified as the optimal choice.
		Note: To observe the resonator's behavior during ringdown, the integration weights length should exceed the readout_pulse length.

		:param readout_len: Readout pulse duration, something much longer than what I typically use, like 2us. In ns
		:param ringdown_len: integration time after readout pulse to observe the ringdown of the resonator, could be 0. In ns
		:param division_length : Size of each demodulation slice in clock cycles
		:param qubit_index:
		:param res_index:
		:param flux_index:
		:param n_avg:
		:param cd_time:
		:param tPath:
		:param f_str_datetime:
		:param simulate_flag:
		:param simulation_len:
		:param plot_flag:
		:param machine:
		:return:
			machine
			x_plot: in ns, different readout duration
			SNR
			opt_readout_length
		"""

		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if machine is None:
			machine = QuAM("quam_state.json")

		config = build_config(machine)

		def update_readout_length(new_readout_length, ringdown_length):
			config["pulses"][f"readout_pulse_q{res_index}" ]["length"] = new_readout_length
			config["integration_weights"][f"cosine_weights{res_index}"] = {
				"cosine": [(1.0, new_readout_length + ringdown_length)],
				"sine": [(0.0, new_readout_length + ringdown_length)],
			}
			config["integration_weights"][f"sine_weights{res_index}"] = {
				"cosine": [(0.0, new_readout_length + ringdown_length)],
				"sine": [(1.0, new_readout_length + ringdown_length)],
			}
			config["integration_weights"][f"minus_sine_weights{res_index}"] = {
				"cosine": [(0.0, new_readout_length + ringdown_length)],
				"sine": [(-1.0, new_readout_length + ringdown_length)],
			}


		###################
		# The QUA program #
		###################
		# Set maximum readout duration for this scan and update the configuration accordingly
		update_readout_length(readout_len * u.ns, ringdown_len * u.ns)
		# Set the accumulated demod parameters
		number_of_divisions = int((readout_len + ringdown_len) / (4 * division_length))
		print("Integration weights chunk-size length in clock cycles:", division_length)
		print("The readout has been sliced in the following number of divisions", number_of_divisions)

		# Time axis for the plots at the end
		x_plot = np.arange(division_length * 4, readout_len + ringdown_len + 1, division_length * 4)


		with program() as ro_duration_opt:
			n = declare(int)
			II = declare(fixed, size=number_of_divisions)
			IQ = declare(fixed, size=number_of_divisions)
			QI = declare(fixed, size=number_of_divisions)
			QQ = declare(fixed, size=number_of_divisions)
			I = declare(fixed, size=number_of_divisions)
			Q = declare(fixed, size=number_of_divisions)
			ind = declare(int)

			n_st = declare_stream()
			Ig_st = declare_stream()
			Qg_st = declare_stream()
			Ie_st = declare_stream()
			Qe_st = declare_stream()

			with for_(n, 0, n < n_avg, n + 1):
				# Measure the ground state of the resonator
				# With demod.accumulated, the results are QUA vectors with 1 point for each accumulated chunk
				measure(
					"readout",
					machine.resonators[res_index].name,
					None,
					demod.accumulated("cos", II, division_length, "out1"),
					demod.accumulated("sin", IQ, division_length, "out2"),
					demod.accumulated("minus_sin", QI, division_length, "out1"),
					demod.accumulated("cos", QQ, division_length, "out2"),
				)
				# Save the QUA vectors to their corresponding streams
				with for_(ind, 0, ind < number_of_divisions, ind + 1):
					assign(I[ind], II[ind] + IQ[ind])
					save(I[ind], Ig_st)
					assign(Q[ind], QQ[ind] + QI[ind])
					save(Q[ind], Qg_st)
				# Wait for the qubit to decay to the ground state
				wait(cd_time * u.ns, machine.resonators[res_index].name)

				align()

				# Measure the excited state.
				# With demod.accumulated, the results are QUA vectors with 1 point for each accumulated chunk
				play("pi", machine.qubits[qubit_index].name)
				align()
				measure(
					"readout",
					machine.resonators[res_index].name,
					None,
					demod.accumulated("cos", II, division_length, "out1"),
					demod.accumulated("sin", IQ, division_length, "out2"),
					demod.accumulated("minus_sin", QI, division_length, "out1"),
					demod.accumulated("cos", QQ, division_length, "out2"),
				)
				# Save the QUA vectors to their corresponding streams
				with for_(ind, 0, ind < number_of_divisions, ind + 1):
					assign(I[ind], II[ind] + IQ[ind])
					save(I[ind], Ie_st)
					assign(Q[ind], QQ[ind] + QI[ind])
					save(Q[ind], Qe_st)

				# Wait for the qubit to decay to the ground state
				wait(cd_time * u.ns, machine.resonators[res_index].name)
				# Save the averaging iteration to get the progress bar
				save(n, n_st)

			with stream_processing():
				n_st.save("iteration")
				# mean values
				Ig_st.buffer(number_of_divisions).average().save("Ig_avg")
				Qg_st.buffer(number_of_divisions).average().save("Qg_avg")
				Ie_st.buffer(number_of_divisions).average().save("Ie_avg")
				Qe_st.buffer(number_of_divisions).average().save("Qe_avg")
				# variances
				(
						((Ig_st.buffer(number_of_divisions) * Ig_st.buffer(number_of_divisions)).average())
						- (Ig_st.buffer(number_of_divisions).average() * Ig_st.buffer(number_of_divisions).average())
				).save("Ig_var")
				(
						((Qg_st.buffer(number_of_divisions) * Qg_st.buffer(number_of_divisions)).average())
						- (Qg_st.buffer(number_of_divisions).average() * Qg_st.buffer(number_of_divisions).average())
				).save("Qg_var")
				(
						((Ie_st.buffer(number_of_divisions) * Ie_st.buffer(number_of_divisions)).average())
						- (Ie_st.buffer(number_of_divisions).average() * Ie_st.buffer(number_of_divisions).average())
				).save("Ie_var")
				(
						((Qe_st.buffer(number_of_divisions) * Qe_st.buffer(number_of_divisions)).average())
						- (Qe_st.buffer(number_of_divisions).average() * Qe_st.buffer(number_of_divisions).average())
				).save("Qe_var")

		#####################################
		#  Open Communication with the QOP  #
		#####################################
		qmm = QuantumMachinesManager(machine.network.qop_ip, port='9510', octave=octave_config, log_level="ERROR")
		# Simulate or execute #
		if simulate_flag:  # simulation is useful to see the sequence, especially the timing (clock cycle vs ns)
			simulation_config = SimulationConfig(duration=simulation_len)
			job = qmm.simulate(config, ro_duration_opt, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			# Open the quantum machine
			qm = qmm.open_qm(config)
			# Send the QUA program to the OPX, which compiles and executes it
			job = qm.execute(ro_duration_opt)  # execute QUA program
			# Get results from QUA program
			results = fetching_tool(
				job,
				data_list=["Ig_avg", "Qg_avg", "Ie_avg", "Qe_avg", "Ig_var", "Qg_var", "Ie_var", "Qe_var", "iteration"],
				mode="live",
			)
			# Live plotting
			if plot_flag == True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [8, 4]
				interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

			while results.is_processing():
				# Fetch results
				Ig_avg, Qg_avg, Ie_avg, Qe_avg, Ig_var, Qg_var, Ie_var, Qe_var, iteration = results.fetch_all()
				# Progress bar
				progress_counter(iteration, n_avg, start_time=results.get_start_time())
				# Derive the SNR
				ground_trace = Ig_avg + 1j * Qg_avg
				excited_trace = Ie_avg + 1j * Qe_avg
				var = (Ie_var + Qe_var + Ig_var + Qg_var) / 4
				SNR = (np.abs(excited_trace - ground_trace) ** 2) / (2 * var)

				# Plot results
				plt.subplot(221)
				plt.cla()
				plt.plot(x_plot, ground_trace.real, label="ground")
				plt.plot(x_plot, excited_trace.real, label="excited")
				plt.xlabel("Readout duration [ns]")
				plt.ylabel("demodulated traces [a.u.]")
				plt.title("Real part")
				plt.legend()

				plt.subplot(222)
				plt.cla()
				plt.plot(x_plot, ground_trace.imag, label="ground")
				plt.plot(x_plot, excited_trace.imag, label="excited")
				plt.xlabel("Readout duration [ns]")
				plt.title("Imaginary part")
				plt.legend()

				plt.subplot(212)
				plt.cla()
				plt.plot(x_plot, SNR, ".-")
				plt.xlabel("Readout duration [ns]")
				plt.ylabel("SNR")
				plt.title("SNR")
				plt.pause(0.1)
				plt.tight_layout()
			# Get the optimal readout length in ns
			opt_readout_length = int(np.round(np.argmax(SNR) * division_length / 4.0) * 4 * 4)
			print(f"The optimal readout length is {opt_readout_length} ns (SNR={max(SNR)})")

			# save data
			exp_name = 'single_shot_duration_optimization'
			qubit_name = 'Q' + str(res_index + 1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name),
					{"RR_duration": x_plot, "SNR": SNR, "Ig": Ig_avg, "Ie": Ie_avg, "Qg": Qg_avg, "Qe": Qe_avg})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, x_plot, SNR, opt_readout_length


	# these are functions required for the single shot optimization
	def two_state_discriminator(self, Ig, Qg, Ie, Qe, plot_flag = True, print_flag = True):
		"""
		Given two blobs in the IQ plane representing two states, finds the optimal threshold to discriminate between them
		and calculates the fidelity. Also returns the angle in which the data needs to be rotated in order to have all the
		information in the `I` (`X`) axis.

		.. note::
			This function assumes that there are only two blobs in the IQ plane representing two states (ground and excited)
			Unexpected output will be returned in other cases.


		:param float Ig: A vector containing the `I` quadrature of data points in the ground state
		:param float Qg: A vector containing the `Q` quadrature of data points in the ground state
		:param float Ie: A vector containing the `I` quadrature of data points in the excited state
		:param float Qe: A vector containing the `Q` quadrature of data points in the excited state
		:param bool plot_flag: When true (default), plot the results
		:param bool print_flag: When true (default), print the results
		:returns: A tuple of (angle, threshold, fidelity, gg, ge, eg, ee).
			angle - The angle (in radians) in which the IQ plane has to be rotated in order to have all the information in
				the `I` axis.
			threshold - The threshold in the rotated `I` axis. The excited state will be when the `I` is larger (>) than
				the threshold.
			fidelity - The fidelity for discriminating the states.
			gg - The matrix element indicating a state prepared in the ground state and measured in the ground state.
			ge - The matrix element indicating a state prepared in the ground state and measured in the excited state.
			eg - The matrix element indicating a state prepared in the excited state and measured in the ground state.
			ee - The matrix element indicating a state prepared in the excited state and measured in the excited state.
		"""

		# Condition to have the Q equal for both states:
		angle = np.arctan2(np.mean(Qe) - np.mean(Qg), np.mean(Ig) - np.mean(Ie))
		C = np.cos(angle)
		S = np.sin(angle)
		# Condition for having e > Ig
		if np.mean((Ig - Ie) * C - (Qg - Qe) * S) > 0:
			angle += np.pi
			C = np.cos(angle)
			S = np.sin(angle)

		Ig_rotated = Ig * C - Qg * S
		Qg_rotated = Ig * S + Qg * C

		Ie_rotated = Ie * C - Qe * S
		Qe_rotated = Ie * S + Qe * C

		fit = minimize(
			self._false_detections,
			0.5 * (np.mean(Ig_rotated) + np.mean(Ie_rotated)),
			(Ig_rotated, Ie_rotated),
			method="Nelder-Mead",
		)
		threshold = fit.x[0]

		gg = np.sum(Ig_rotated < threshold) / len(Ig_rotated)
		ge = np.sum(Ig_rotated > threshold) / len(Ig_rotated)
		eg = np.sum(Ie_rotated < threshold) / len(Ie_rotated)
		ee = np.sum(Ie_rotated > threshold) / len(Ie_rotated)

		fidelity = 100 * (gg + ee) / 2

		if print_flag == True:
			# print out the confusion matrix
			print(
				f"""
			Fidelity Matrix:
			-----------------
			| {gg:.3f} | {ge:.3f} |
			----------------
			| {eg:.3f} | {ee:.3f} |
			-----------------
			IQ plane rotated by: {180 / np.pi * angle:.1f}{chr(176)}
			Threshold: {threshold:.3e}
			Fidelity: {fidelity:.1f}%
			"""
			)

		if plot_flag:
			fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
			plt.rcParams['figure.figsize'] = [9, 8]
			ax1.plot(Ig, Qg, ".", alpha=0.1, label="Ground", markersize=3)
			ax1.plot(Ie, Qe, ".", alpha=0.1, label="Excited", markersize=3)
			ax1.axis("equal")
			ax1.legend(["Ground", "Excited"])
			ax1.set_xlabel("I")
			ax1.set_ylabel("Q")
			ax1.set_title("Original Data")
			ax1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), fancybox=True, shadow=True, ncol=5,
					   markerscale=5)

			ax2.plot(Ig_rotated, Qg_rotated, ".", alpha=0.1, label="Ground", markersize=3)
			ax2.plot(Ie_rotated, Qe_rotated, ".", alpha=0.1, label="Excited", markersize=3)
			ax2.axis("equal")
			ax2.set_xlabel("I")
			ax2.set_ylabel("Q")
			ax2.set_title("Rotated Data")
			ax2.legend(["Ground", "Excited"])
			ax2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), fancybox=True, shadow=True, ncol=5,
					   markerscale=5)

			ax3.hist(Ig_rotated, bins=50, alpha=0.75, label="Ground")
			ax3.hist(Ie_rotated, bins=50, alpha=0.75, label="Excited")
			ax3.axvline(x=threshold, color="k", ls="--", alpha=0.5)
			text_props = dict(
				horizontalalignment="center",
				verticalalignment="center",
				transform=ax3.transAxes,
			)
			ax3.text(0.7, 0.9, f"Threshold:\n {threshold:.3e}", text_props)
			ax3.set_xlabel("I")
			ax3.set_ylabel("Counts")
			ax3.set_title("1D Histogram")

			ax4.imshow(np.array([[gg, ge], [eg, ee]]))
			ax4.set_xticks([0, 1])
			ax4.set_yticks([0, 1])
			ax4.set_xticklabels(labels=["|g>", "|e>"])
			ax4.set_yticklabels(labels=["|g>", "|e>"])
			ax4.set_ylabel("Prepared")
			ax4.set_xlabel("Measured")
			ax4.text(0, 0, f"{100 * gg:.1f}%", ha="center", va="center", color="k")
			ax4.text(1, 0, f"{100 * ge:.1f}%", ha="center", va="center", color="w")
			ax4.text(0, 1, f"{100 * eg:.1f}%", ha="center", va="center", color="w")
			ax4.text(1, 1, f"{100 * ee:.1f}%", ha="center", va="center", color="k")
			ax4.set_title("Fidelities")
			fig.tight_layout()
			fig.subplots_adjust(hspace=.5)
			plt.show()
		return angle, threshold, fidelity, gg, ge, eg, ee

	def _false_detections(self, threshold, Ig, Ie):
		if np.mean(Ig) < np.mean(Ie):
			false_detections_var = np.sum(Ig > threshold) + np.sum(Ie < threshold)
		else:
			false_detections_var = np.sum(Ig < threshold) + np.sum(Ie > threshold)
		return false_detections_var

class EH_Rabi:
	"""
	class in ExperimentHandle, for Rabi sequence related 1D experiments
	Methods:
		update_tPath
		update_str_datetime
		qubit_freq(self, qubit_freq_sweep, qubit_index, res_index, flux_index, n_avg, cd_time, ff_amp = 1.0, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000)
	"""
	def __init__(self, ref_to_update_tPath, ref_to_update_str_datetime,ref_to_octave_calibration):
		self.update_tPath = ref_to_update_tPath
		self.update_str_datetime = ref_to_update_str_datetime
		self.octave_calibration = ref_to_octave_calibration

	def qubit_freq(self, qubit_freq_sweep, qubit_index, res_index, flux_index, pi_amp_rel = 1.0, ff_amp = 0.0, n_avg = 1E3, cd_time = 10E3, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
		qubit spectroscopy experiment in 1D (equivalent of ESR for spin qubit)

		Args:
		:param qubit_freq_sweep: 1D array of qubit frequency sweep
		:param qubit_index:
		:param res_index:
		:param flux_index:
		:param n_avg: repetition of the experiments
		:param cd_time: cooldown time between subsequent experiments
		:param ff_amp: fast flux amplitude the overlaps with the Rabi pulse. The ff pulse is 40ns longer than Rabi pulse, and share the same center time.
		:param tPath: target path/folder for saving the data. Default is today.
		:param f_str_datetime: datetime string for saving the data. Default is now.
		:param simulate_flag: True-run simulation; False (default)-run experiment.
		:param simulation_len: Length of the sequence to simulate. In clock cycles (4ns).
		:param plot_flag: True (default) plot the experiment. False, do not plot.
		:param machine: None (default), will read from quam_state.json
		Return:
			machine
			qubit_freq_sweep
			sig_amp
		"""
		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)
		qubit_lo = machine.qubits[qubit_index].lo
		qubit_if_sweep = qubit_freq_sweep - qubit_lo
		qubit_if_sweep = np.round(qubit_if_sweep)
		ff_duration = machine.qubits[qubit_index].pi_length[0] + 40

		if np.max(abs(qubit_if_sweep)) > 400E6: # check if parameters are within hardware limit
			print("qubit if range > 400MHz")
			return None, None, None

		with program() as qubit_freq_prog:
			[I,Q,n,I_st,Q_st,n_st] = declare_vars()
			df = declare(int)

			with for_(n, 0, n < n_avg, n+1):
				with for_(*from_array(df,qubit_if_sweep)):
					update_frequency(machine.qubits[qubit_index].name, df)
					play("const" * amp(ff_amp), machine.flux_lines[flux_index].name, duration=ff_duration * u.ns)
					wait(5, machine.qubits[qubit_index].name)
					play('pi'*amp(pi_amp_rel), machine.qubits[qubit_index].name)
					align(machine.qubits[qubit_index].name, machine.flux_lines[flux_index].name,
						  machine.resonators[res_index].name)
					#wait(4) # avoid overlap between Z and RO
					readout_avg_macro(machine.resonators[res_index].name,I,Q)
					align()
					wait(50)
					# eliminate charge accumulation
					play("const" * amp(-1 * ff_amp), machine.flux_lines[flux_index].name, duration=ff_duration * u.ns)
					wait(cd_time * u.ns, machine.resonators[res_index].name)
					save(I, I_st)
					save(Q, Q_st)
				save(n, n_st)
			with stream_processing():
				n_st.save('iteration')
				I_st.buffer(len(qubit_if_sweep)).average().save("I")
				Q_st.buffer(len(qubit_if_sweep)).average().save("Q")

		#####################################
		#  Open Communication with the QOP  #
		#####################################
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config, log_level = "ERROR")
		# Simulate or execute #
		if simulate_flag: # simulation is useful to see the sequence, especially the timing (clock cycle vs ns)
			simulation_config = SimulationConfig(duration=simulation_len)
			job = qmm.simulate(config, qubit_freq_prog, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			qm = qmm.open_qm(config)
			job = qm.execute(qubit_freq_prog)
			# Get results from QUA program
			results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
			# Live plotting
		    #%matplotlib qt
			if plot_flag == True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [8, 4]
				interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
			while results.is_processing():
				# Fetch results
				I, Q, iteration = results.fetch_all()
				I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
				Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
				# progress bar
				progress_counter(iteration, n_avg, start_time=results.get_start_time())

				if plot_flag == True:
					plt.cla()
					plt.title("qubit spectroscopy")
					plt.plot((qubit_freq_sweep) / u.MHz, np.sqrt(I**2 +  Q**2), ".")
					#plt.plot((qubit_freq_sweep) / u.MHz, I, "o")
					#plt.plot((qubit_freq_sweep) / u.MHz, Q, "x")
					plt.xlabel("Frequency [MHz]")
					plt.ylabel(r"$\sqrt{I^2 + Q^2}$ [V]")

			# fetch all data after live-updating
			I, Q, iteration = results.fetch_all()
			# Convert I & Q to Volts
			I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
			Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
			sig_amp = np.sqrt(I**2 + Q**2)
			sig_phase = np.angle(I + 1j * Q)

			# save data
			exp_name = 'freq'
			qubit_name = 'Q' + str(qubit_index + 1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name), {"Q_freq": qubit_freq_sweep, "sig_amp": sig_amp, "sig_phase": sig_phase})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, qubit_freq_sweep, sig_amp

	def rabi_length(self, rabi_duration_sweep, qubit_index, res_index, flux_index, pi_amp_rel = 1.0, n_avg = 1E3, cd_time = 10E3, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
		qubit rabi experiment in 1D (sweeps length of rabi pulse)

		:param rabi_duration_sweep: in clock cycles!
		:param qubit_index:
		:param res_index:
		:param flux_index:
		:param pi_amp_rel:
		:param n_avg:
		:param cd_time:
		:param tPath:
		:param f_str_datetime:
		:param simulate_flag:
		:param simulation_len:
		:param plot_flag:
		:param machine: None (default), will read from quam_state.json
		Return:
			machine
			rabi_duration_sweep: in ns!
			sig_amp
		"""
		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if min(rabi_duration_sweep) < 4:
			print("some rabi lengths shorter than 4 clock cycles, removed from run")
			rabi_duration_sweep = rabi_duration_sweep[rabi_duration_sweep>3]

		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)
		rabi_duration_sweep = rabi_duration_sweep.astype(int)

		with program() as time_rabi:
			[I, Q, n, I_st, Q_st, n_st] = declare_vars()
			t = declare(int)

			with for_(n, 0, n < n_avg, n + 1):
				with for_(*from_array(t, rabi_duration_sweep)):
					wait(5, machine.qubits[qubit_index].name)
					play("pi" * amp(pi_amp_rel), machine.qubits[qubit_index].name, duration=t)
					wait(5, machine.qubits[qubit_index].name)
					align(machine.qubits[qubit_index].name, machine.resonators[res_index].name)
					readout_avg_macro(machine.resonators[res_index].name,I,Q)
					save(I, I_st)
					save(Q, Q_st)
					wait(cd_time * u.ns, machine.resonators[qubit_index].name)
				save(n, n_st)

			with stream_processing():
				I_st.buffer(len(rabi_duration_sweep)).average().save("I")
				Q_st.buffer(len(rabi_duration_sweep)).average().save("Q")
				n_st.save("iteration")

		#  Open Communication with the QOP  #
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config, log_level = "ERROR")

		if simulate_flag:
			simulation_config = SimulationConfig(duration=simulation_len)  # in clock cycles
			job = qmm.simulate(config, time_rabi, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			qm = qmm.open_qm(config)
			job = qm.execute(time_rabi)
			results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")

			# Live plotting
			if plot_flag == True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [8, 4]
				interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

			while results.is_processing():
				# Fetch results
				I, Q, iteration = results.fetch_all()
				I = u.demod2volts(I, machine.resonators[qubit_index].readout_pulse_length)
				Q = u.demod2volts(Q, machine.resonators[qubit_index].readout_pulse_length)
				sig_amp = np.sqrt(I ** 2 + Q ** 2)
				sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))
				# Progress bar
				progress_counter(iteration, n_avg, start_time=results.get_start_time())
				if plot_flag == True:
					plt.cla()
					plt.title("Time Rabi")
					plt.plot(rabi_duration_sweep * 4, sig_amp, "b.")
					plt.xlabel("tau [ns]")
					plt.ylabel(r"$\sqrt{I^2 + Q^2}$ [V]")
					plt.pause(0.01)

			# fetch all data after live-updating
			I, Q, iteration = results.fetch_all()
			# Convert I & Q to Volts
			I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
			Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
			sig_amp = np.sqrt(I ** 2 + Q ** 2)
			sig_phase = np.angle(I + 1j * Q)

			# save data
			exp_name = 'time_rabi'
			qubit_name = 'Q' + str(qubit_index + 1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name),
					{"Q_rabi_duration": rabi_duration_sweep * 4, "sig_amp": sig_amp, "sig_phase": sig_phase})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, rabi_duration_sweep * 4, sig_amp

	def rabi_amp(self, rabi_amp_sweep_rel, qubit_index, res_index, flux_index, n_avg = 1E3, cd_time = 10E3, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
		qubit rabi experiment in 1D (sweeps amplitude of rabi pulse)
		note that the input argument is in relative amplitude, the return argument is in absolute amplitude
		:param rabi_amp_sweep: relative amplitude, based on pi_amp[0]
		:param qubit_index:
		:param res_index:
		:param flux_index:
		:param n_avg:
		:param cd_time:
		:param tPath:
		:param f_str_datetime:
		:param simulate_flag:
		:param simulation_len:
		:param plot_flag:
		:param machine: None (default), will read from quam_state.json
		Return:
			machine
			rabi_amp_sweep_abs
			sig_amp
		"""
		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)

		qubit_if = machine.qubits[qubit_index].f_01 - machine.qubits[qubit_index].lo
		#if max(abs(rabi_amp_sweep_rel)) > 2:
		#	print("some relative amps > 2, removed from experiment run")
		#	rabi_amp_sweep_rel = rabi_amp_sweep_rel[abs(rabi_amp_sweep_rel) < 2]
		rabi_amp_sweep_abs = rabi_amp_sweep_rel * machine.qubits[qubit_index].pi_amp[0] # actual rabi amplitude

		with program() as power_rabi:
			[I, Q, n, I_st, Q_st, n_st] = declare_vars()
			a = declare(fixed)

			with for_(n, 0, n < n_avg, n + 1):
				with for_(*from_array(a, rabi_amp_sweep_rel)):
					update_frequency(machine.qubits[qubit_index].name, qubit_if)
					wait(5, machine.qubits[qubit_index].name)
					play("pi" * amp(a), machine.qubits[qubit_index].name)
					wait(5, machine.qubits[qubit_index].name)
					align(machine.qubits[qubit_index].name, machine.resonators[res_index].name)
					readout_avg_macro(machine.resonators[res_index].name,I,Q)
					save(I, I_st)
					save(Q, Q_st)
					wait(cd_time * u.ns, machine.resonators[qubit_index].name)
				save(n, n_st)

			with stream_processing():
				I_st.buffer(len(rabi_amp_sweep_rel)).average().save("I")
				Q_st.buffer(len(rabi_amp_sweep_rel)).average().save("Q")
				n_st.save("iteration")

		#  Open Communication with the QOP  #
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config, log_level = "ERROR")

		if simulate_flag:
			simulation_config = SimulationConfig(duration=1000)  # in clock cycles
			job = qmm.simulate(config, power_rabi, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			qm = qmm.open_qm(config)
			job = qm.execute(power_rabi)
			results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")

			# Live plotting
			if plot_flag == True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [8, 4]
				interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

			while results.is_processing():
				# Fetch results
				I, Q, iteration = results.fetch_all()
				I = u.demod2volts(I, machine.resonators[qubit_index].readout_pulse_length)
				Q = u.demod2volts(Q, machine.resonators[qubit_index].readout_pulse_length)
				sig_amp = np.sqrt(I ** 2 + Q ** 2)
				sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))
				# Progress bar
				progress_counter(iteration, n_avg, start_time=results.get_start_time())
				if plot_flag == True:
					plt.cla()
					plt.title("Power Rabi")
					plt.plot(rabi_amp_sweep_abs, sig_amp, "b.")
					plt.xlabel("rabi amplitude [V]")
					plt.ylabel(r"$\sqrt{I^2 + Q^2}$ [V]")
					plt.pause(0.01)

			# fetch all data after live-updating
			I, Q, iteration = results.fetch_all()
			# Convert I & Q to Volts
			I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
			Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
			sig_amp = np.sqrt(I ** 2 + Q ** 2)
			sig_phase = np.angle(I + 1j * Q)

			# save data
			exp_name = 'power_rabi'
			qubit_name = 'Q' + str(qubit_index + 1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name),
					{"Q_rabi_amplitude": rabi_amp_sweep_abs, "sig_amp": sig_amp, "sig_phase": sig_phase})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, rabi_amp_sweep_abs, sig_amp

	def qubit_switch_delay(self, qubit_switch_delay_sweep, qubit_index, res_index, flux_index, n_avg, cd_time, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
		1D experiment to calibrate switch delay for the qubit.

		Args:
			qubit_switch_delay_sweep (): in ns
			qubit_index ():
			res_index ():
			flux_index ():
			n_avg ():
			cd_time ():
			tPath ():
			f_str_datetime ():
			simulate_flag ():
			simulation_len ():
			plot_flag ():
			machine ():

		Returns:
			machine
			qubit_switch_delay_sweep
			sig_amp
		"""
		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)
		qubit_lo = machine.qubits[qubit_index].lo
		qubit_if = machine.qubits[qubit_index].f_01 - qubit_lo

		if abs(qubit_if) > 400E6: # check if parameters are within hardware limit
			print("qubit if > 400MHz")
			return None

		with program() as qubit_switch_delay_prog:
			[I,Q,n,I_st,Q_st,n_st] = declare_vars()

			with for_(n, 0, n < n_avg, n+1):
				update_frequency(machine.qubits[qubit_index].name, qubit_if)
				play('pi2', machine.qubits[qubit_index].name)
				align()
				readout_avg_macro(machine.resonators[res_index].name,I,Q)
				wait(cd_time * u.ns, machine.resonators[res_index].name)
				save(I, I_st)
				save(Q, Q_st)
			with stream_processing():
				I_st.average().save("I")
				Q_st.average().save("Q")

		#####################################
		#  Open Communication with the QOP  #
		#####################################
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config, log_level = "ERROR")
		# Simulate or execute #
		if simulate_flag: # simulation is useful to see the sequence, especially the timing (clock cycle vs ns)
			simulation_config = SimulationConfig(duration=simulation_len)
			job = qmm.simulate(config, qubit_switch_delay_prog, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			start_time = time.time()
			I_tot = []
			Q_tot = []
			if plot_flag == True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [8, 4]

			for delay_index, delay_value in enumerate(qubit_switch_delay_sweep):
				machine.qubits[qubit_index].digital_marker.delay = int(delay_value)
				config = build_config(machine)

				qm = qmm.open_qm(config)
				job = qm.execute(qubit_switch_delay_prog)
				# Get results from QUA program
				results = fetching_tool(job, data_list=["I", "Q"], mode = "live")

				if plot_flag:
					interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
				while results.is_processing():
					# Fetch results
					time.sleep(0.1)

				I, Q = results.fetch_all()
				I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
				Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
				I_tot.append(I)
				Q_tot.append(Q)

				# progress bar
				progress_counter(delay_index, len(qubit_switch_delay_sweep), start_time=start_time)

			I_tot = np.array(I_tot)
			Q_tot = np.array(Q_tot)
			sigs_qubit = I_tot + 1j * Q_tot
			sig_amp = np.abs(sigs_qubit)  # Amplitude
			sig_phase = np.angle(sigs_qubit)  # Phase

			if plot_flag == True:
				plt.cla()
				plt.title("qubit switch delay")
				plt.plot(qubit_switch_delay_sweep, sig_amp, ".")
				plt.xlabel("switch delay [ns]")
				plt.ylabel("Signal [V]")

			# save data
			exp_name = 'qubit_switch_delay'
			qubit_name = 'Q' + str(res_index+1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name), {"qubit_delay": qubit_switch_delay_sweep, "sig_amp": sig_amp, "sig_phase": sig_phase})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, qubit_switch_delay_sweep, sig_amp

	def qubit_switch_buffer(self, qubit_switch_buffer_sweep, qubit_index, res_index, flux_index, n_avg, cd_time, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
		1D experiment to calibrate switch buffer for the qubit.

		Args:
			qubit_switch_buffer_sweep (): in ns, this will be added to both sides of the switch (x2), to account for the rise and fall
			qubit_index ():
			res_index ():
			flux_index ():
			n_avg ():
			cd_time ():
			tPath ():
			f_str_datetime ():
			simulate_flag ():
			simulation_len ():
			plot_flag ():
			machine ():

		Returns:
			machine
			qubit_switch_buffer_sweep
			sig_amp
		"""
		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)
		qubit_lo = machine.qubits[qubit_index].lo
		qubit_if = machine.qubits[qubit_index].f_01 - qubit_lo

		if abs(qubit_if) > 400E6: # check if parameters are within hardware limit
			print("qubit if > 400MHz")
			return None

		with program() as qubit_switch_buffer_prog:
			[I,Q,n,I_st,Q_st,n_st] = declare_vars()

			with for_(n, 0, n < n_avg, n+1):
				update_frequency(machine.qubits[qubit_index].name, qubit_if)
				play('pi2', machine.qubits[qubit_index].name)
				align()
				readout_avg_macro(machine.resonators[res_index].name,I,Q)
				wait(cd_time * u.ns, machine.resonators[res_index].name)
				save(I, I_st)
				save(Q, Q_st)
			with stream_processing():
				I_st.average().save("I")
				Q_st.average().save("Q")

		#####################################
		#  Open Communication with the QOP  #
		#####################################
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config, log_level = "ERROR")
		# Simulate or execute #
		if simulate_flag: # simulation is useful to see the sequence, especially the timing (clock cycle vs ns)
			simulation_config = SimulationConfig(duration=simulation_len)
			job = qmm.simulate(config, qubit_switch_buffer_prog, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			start_time = time.time()
			I_tot = []
			Q_tot = []
			if plot_flag == True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [8, 4]

			for buffer_index, buffer_value in enumerate(qubit_switch_buffer_sweep):
				machine.qubits[qubit_index].digital_marker.buffer = int(buffer_value)
				config = build_config(machine)

				qm = qmm.open_qm(config)
				job = qm.execute(qubit_switch_buffer_prog)
				# Get results from QUA program
				results = fetching_tool(job, data_list=["I", "Q"], mode = "live")

				if plot_flag:
					interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
				while results.is_processing():
					# Fetch results
					time.sleep(0.1)

				I, Q = results.fetch_all()
				I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
				Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
				I_tot.append(I)
				Q_tot.append(Q)

				# progress bar
				progress_counter(buffer_index, len(qubit_switch_buffer_sweep), start_time=start_time)

			I_tot = np.array(I_tot)
			Q_tot = np.array(Q_tot)
			sigs_qubit = I_tot + 1j * Q_tot
			sig_amp = np.abs(sigs_qubit)  # Amplitude
			sig_phase = np.angle(sigs_qubit)  # Phase

			if plot_flag == True:
				plt.cla()
				plt.title("qubit switch buffer")
				plt.plot(qubit_switch_buffer_sweep, sig_amp, ".")
				plt.xlabel("switch buffer [ns]")
				plt.ylabel("Signal [V]")

			# save data
			exp_name = 'qubit_switch_buffer'
			qubit_name = 'Q' + str(res_index+1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name), {"qubit_buffer": qubit_switch_buffer_sweep, "sig_amp": sig_amp, "sig_phase": sig_phase})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, qubit_switch_buffer_sweep, sig_amp

	def TLS_freq(self, TLS_freq_sweep, qubit_index, res_index, flux_index, TLS_index = 0, pi_amp_rel = 1.0, n_avg = 1E3, cd_time_qubit = 10E3, cd_time_TLS = None, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
		1D experiment of TLS spectroscopy
		a strong MW pulse - SWAP - readout

		uses the iswap defined in machine.flux_lines[flux_index].iswap.length/level[TLS_index]
		the TLS driving pulse is a square wave, with duration = machine.qubits[qubit_index].pi_length_tls[TLS_index],
		 amplitude = machine.qubits[qubit_index].pi_amp_tls[TLS_index]

		Args:
			TLS_freq_sweep ():
			qubit_index ():
			res_index ():
			flux_index ():
			TLS_index ():
			pi_amp_rel ():
			n_avg ():
			cd_time ():
			tPath ():
			f_str_datetime ():
			simulate_flag ():
			simulation_len ():
			plot_flag ():
			machine ():

		Returns:
			machine
			TLS_freq_sweep
			sig_amp
		"""
		calibrate_octave = False # flat for calibrating octave. So that I can move this to the real run, avoiding it for simulation

		if cd_time_TLS is None:
			cd_time_TLS = cd_time_qubit

		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)
		qubit_lo = machine.qubits[qubit_index].lo
		TLS_if_sweep = TLS_freq_sweep - qubit_lo
		TLS_if_sweep = np.round(TLS_if_sweep)

		# fLux pulse baking for SWAP
		swap_length = machine.flux_lines[flux_index].iswap.length[TLS_index]
		swap_amp = machine.flux_lines[flux_index].iswap.level[TLS_index]
		flux_waveform = np.array([swap_amp] * swap_length)
		def baked_swap_waveform(waveform):
			pulse_segments = []  # Stores the baking objects
			# Create the different baked sequences, each one corresponding to a different truncated duration
			with baking(config, padding_method="right") as b:
				b.add_op("flux_pulse", machine.flux_lines[flux_index].name, waveform.tolist())
				b.play("flux_pulse", machine.flux_lines[flux_index].name)
				pulse_segments.append(b)
			return pulse_segments

		square_TLS_swap = baked_swap_waveform(flux_waveform)

		if np.max(abs(TLS_if_sweep)) > 350E6: # check if parameters are within hardware limit
			print("TLS if range > 350MHz, changing LO...")
			qubit_lo = np.mean(TLS_freq_sweep) - 200E6
			qubit_lo = int(qubit_lo.tolist())
			machine.qubits[qubit_index].f_01 = qubit_lo + 200E6
			machine.qubits[qubit_index].lo = qubit_lo + 0E6
			calibrate_octave = True
			# reassign values
			TLS_if_sweep = TLS_freq_sweep - qubit_lo
			TLS_if_sweep = np.round(TLS_if_sweep)
			if np.max(abs(TLS_if_sweep)) > 350E6:  # check if parameters are within hardware limit
				print("TLS freq sweep range too large, abort...")
				return None

		with program() as TLS_freq_prog:
			[I,Q,n,I_st,Q_st,n_st] = declare_vars()
			df = declare(int)

			with for_(n, 0, n < n_avg, n+1):
				with for_(*from_array(df,TLS_if_sweep)):
					update_frequency(machine.qubits[qubit_index].name, df)
					if pi_amp_rel==1.0:
						play('pi_tls', machine.qubits[qubit_index].name)
					else:
						play('pi_tls' * amp(pi_amp_rel), machine.qubits[qubit_index].name)
					align()
					square_TLS_swap[0].run()
					align()
					readout_rotated_macro(machine.resonators[res_index].name,I,Q)
					align()
					save(I, I_st)
					save(Q, Q_st)
					# eliminate charge accumulation, also initialize TLS
					wait(cd_time_qubit * u.ns, machine.resonators[res_index].name)
					align()
					square_TLS_swap[0].run(amp_array=[(machine.flux_lines[flux_index].name, -1)])
					wait(cd_time_TLS * u.ns, machine.resonators[res_index].name)
				save(n, n_st)
			with stream_processing():
				n_st.save('iteration')
				I_st.buffer(len(TLS_if_sweep)).average().save("I")
				Q_st.buffer(len(TLS_if_sweep)).average().save("Q")

		#####################################
		#  Open Communication with the QOP  #
		#####################################
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config, log_level = "ERROR")
		# Simulate or execute #
		if simulate_flag: # simulation is useful to see the sequence, especially the timing (clock cycle vs ns)
			simulation_config = SimulationConfig(duration=simulation_len)
			job = qmm.simulate(config, TLS_freq_prog, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			if calibrate_octave:
				self.octave_calibration(qubit_index, res_index, flux_index, machine=machine)

			qm = qmm.open_qm(config)
			job = qm.execute(TLS_freq_prog)
			# Get results from QUA program
			results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
			# Live plotting
		    #%matplotlib qt
			if plot_flag == True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [8, 4]
				interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
			while results.is_processing():
				# Fetch results
				I, Q, iteration = results.fetch_all()
				I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
				Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
				# progress bar
				progress_counter(iteration, n_avg, start_time=results.get_start_time())

				if plot_flag:
					plt.cla()
					plt.title("TLS spectroscopy")
					plt.plot((TLS_freq_sweep) / u.MHz, np.sqrt(I**2 +  Q**2), ".")
					plt.xlabel("Frequency [MHz]")
					plt.ylabel(r"$\sqrt{I^2 + Q^2}$ [V]")

			# fetch all data after live-updating
			I, Q, iteration = results.fetch_all()
			# Convert I & Q to Volts
			I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
			Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
			sig_amp = np.sqrt(I**2 + Q**2)
			sig_phase = np.angle(I + 1j * Q)

			# save data
			exp_name = 'freq'
			qubit_name = 'Q' + str(qubit_index + 1) + 'TLS' + str(TLS_index+1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name), {"TLS_freq": TLS_freq_sweep, "sig_amp": sig_amp, "sig_phase": sig_phase})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, TLS_freq_sweep, sig_amp

	def TLS_rabi_length(self, rabi_duration_sweep, qubit_index, res_index, flux_index, TLS_index = 0, pi_amp_rel = 1.0, n_avg = 1E3, cd_time_qubit = 20E3, cd_time_TLS = None, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
		1D experiment that runs time rabi of TLS

		uses the iswap defined in machine.flux_lines[flux_index].iswap.length/level[TLS_index]
		the TLS driving pulse is a square wave, with amplitude = machine.qubits[qubit_index].pi_amp_tls[TLS_index] * 0.25 V

		Args:
			rabi_duration_sweep (): in clock cycles! Must be integers!
			qubit_index ():
			res_index ():
			flux_index ():
			TLS_index ():
			pi_amp_rel ():
			n_avg ():
			cd_time_qubit ():
			cd_time_TLS ():
			tPath ():
			f_str_datetime ():
			simulate_flag ():
			simulation_len ():
			plot_flag ():
			machine ():

		Returns:
			machine
			rabi_duration_sweep * 4
			sig_I # temporary, 12/21/2023 by Mo Chen, because I am using the rotated readout
		"""
		if cd_time_TLS is None:
			cd_time_TLS = cd_time_qubit

		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)

		if min(rabi_duration_sweep) < 4:
			print("some rabi lengths shorter than 4 clock cycles, removed from run")
			rabi_duration_sweep = rabi_duration_sweep[rabi_duration_sweep>3]
		rabi_duration_sweep = rabi_duration_sweep.astype(int)

		# fLux pulse baking for SWAP
		swap_length = machine.flux_lines[flux_index].iswap.length[TLS_index]
		swap_amp = machine.flux_lines[flux_index].iswap.level[TLS_index]
		flux_waveform = np.array([swap_amp] * swap_length)
		def baked_swap_waveform(waveform):
			pulse_segments = []  # Stores the baking objects
			# Create the different baked sequences, each one corresponding to a different truncated duration
			with baking(config, padding_method="right") as b:
				b.add_op("flux_pulse", machine.flux_lines[flux_index].name, waveform.tolist())
				b.play("flux_pulse", machine.flux_lines[flux_index].name)
				pulse_segments.append(b)
			return pulse_segments

		square_TLS_swap = baked_swap_waveform(flux_waveform)

		with program() as TLS_rabi_prog:
			[I,Q,n,I_st,Q_st,n_st] = declare_vars()
			t = declare(int)

			with for_(n, 0, n < n_avg, n+1):
				with for_(*from_array(t,rabi_duration_sweep)):
					if pi_amp_rel==1.0:
						play('pi_tls', machine.qubits[qubit_index].name, duration = t) # clock cycles
					else:
						play('pi_tls' * amp(pi_amp_rel), machine.qubits[qubit_index].name, duration = t) # clock cycles
					align()
					square_TLS_swap[0].run()
					align()
					#readout_avg_macro(machine.resonators[res_index].name,I,Q)
					readout_rotated_macro(machine.resonators[res_index].name, I, Q)
					align()
					save(I, I_st)
					save(Q, Q_st)
					# eliminate charge accumulation, also initialize TLS
					wait(cd_time_qubit * u.ns, machine.resonators[res_index].name)
					align()
					square_TLS_swap[0].run(amp_array=[(machine.flux_lines[flux_index].name, -1)])
					wait(cd_time_TLS * u.ns, machine.resonators[res_index].name)
				save(n, n_st)
			with stream_processing():
				n_st.save('iteration')
				I_st.buffer(len(rabi_duration_sweep)).average().save("I")
				Q_st.buffer(len(rabi_duration_sweep)).average().save("Q")

		#####################################
		#  Open Communication with the QOP  #
		#####################################
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config, log_level = "ERROR")
		# Simulate or execute #
		if simulate_flag: # simulation is useful to see the sequence, especially the timing (clock cycle vs ns)
			simulation_config = SimulationConfig(duration=simulation_len)
			job = qmm.simulate(config, TLS_rabi_prog, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			qm = qmm.open_qm(config)
			job = qm.execute(TLS_rabi_prog)
			# Get results from QUA program
			results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
			# Live plotting
		    #%matplotlib qt
			if plot_flag == True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [8, 4]
				interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
			while results.is_processing():
				# Fetch results
				I, Q, iteration = results.fetch_all()
				I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
				Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
				# progress bar
				progress_counter(iteration, n_avg, start_time=results.get_start_time())

				if plot_flag:
					plt.cla()
					plt.title("TLS time rabi")
					#plt.plot(rabi_duration_sweep * 4, np.sqrt(I**2 +  Q**2), ".")
					plt.plot(rabi_duration_sweep * 4, I, ".")
					plt.xlabel("tau [ns]")
					#plt.ylabel(r"$\sqrt{I^2 + Q^2}$ [V]")
					plt.ylabel(r"$I$ [V]")

			# fetch all data after live-updating
			I, Q, iteration = results.fetch_all()
			# Convert I & Q to Volts
			I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
			Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
			sig_amp = np.sqrt(I**2 + Q**2)
			sig_phase = np.angle(I + 1j * Q)

			# save data
			exp_name = 'TLS_time_rabi'
			qubit_name = 'Q' + str(qubit_index + 1) + 'TLS' + str(TLS_index+1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name), {"TLS_rabi_duration": rabi_duration_sweep * 4, "sig_amp": sig_amp, "sig_phase": sig_phase})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, rabi_duration_sweep * 4, I

	def TLS_rabi_amp(self, rabi_amp_sweep_rel, qubit_index, res_index, flux_index, TLS_index = 0, n_avg = 1E3, cd_time_qubit = 20E3, cd_time_TLS = None, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""

		1D experiment that runs power rabi of TLS

		uses the iswap defined in machine.flux_lines[flux_index].iswap.length/level[TLS_index]
		the TLS driving pulse is a square wave, with amplitude = machine.qubits[qubit_index].pi_amp_tls[TLS_index] * 0.25 V

		note that the input argument is in relative amplitude, the return argument is in absolute amplitude
		:param rabi_amp_sweep: relative amplitude, based on pi_amp[0]
		:param qubit_index:
		:param res_index:
		:param flux_index:
		:param n_avg:
		:param cd_time:
		:param tPath:
		:param f_str_datetime:
		:param simulate_flag:
		:param simulation_len:
		:param plot_flag:
		:param machine: None (default), will read from quam_state.json
		Return:
			machine
			rabi_amp_sweep_abs
			sig_amp
		"""
		if cd_time_TLS is None:
			cd_time_TLS = cd_time_qubit
		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)

		qubit_if = machine.qubits[qubit_index].f_01 - machine.qubits[qubit_index].lo
		if max(abs(rabi_amp_sweep_rel)) > 2:
			print("some relative amps > 2, removed from experiment run")
			rabi_amp_sweep_rel = rabi_amp_sweep_rel[abs(rabi_amp_sweep_rel) < 2]
		rabi_amp_sweep_abs = rabi_amp_sweep_rel * machine.qubits[qubit_index].pi_amp_tls[TLS_index] # actual rabi amplitude
		if max(abs(rabi_amp_sweep_abs)) > 0.5:
			print("some abs amps > 0.5, removed from experiment run")
			rabi_amp_sweep_rel = rabi_amp_sweep_rel[abs(rabi_amp_sweep_abs) < 0.5]
			rabi_amp_sweep_abs = rabi_amp_sweep_abs[abs(rabi_amp_sweep_abs) < 0.5]

		# fLux pulse baking for SWAP
		swap_length = machine.flux_lines[flux_index].iswap.length[TLS_index]
		swap_amp = machine.flux_lines[flux_index].iswap.level[TLS_index]
		flux_waveform = np.array([swap_amp] * swap_length)

		def baked_swap_waveform(waveform):
			pulse_segments = []  # Stores the baking objects
			# Create the different baked sequences, each one corresponding to a different truncated duration
			with baking(config, padding_method="right") as b:
				b.add_op("flux_pulse", machine.flux_lines[flux_index].name, waveform.tolist())
				b.play("flux_pulse", machine.flux_lines[flux_index].name)
				pulse_segments.append(b)
			return pulse_segments

		square_TLS_swap = baked_swap_waveform(flux_waveform)

		with program() as tls_power_rabi:
			[I, Q, n, I_st, Q_st, n_st] = declare_vars()
			a = declare(fixed)

			with for_(n, 0, n < n_avg, n + 1):
				with for_(*from_array(a, rabi_amp_sweep_rel)):
					update_frequency(machine.qubits[qubit_index].name, qubit_if)
					play("pi_tls" * amp(a), machine.qubits[qubit_index].name)
					align()
					square_TLS_swap[0].run()
					align()
					readout_rotated_macro(machine.resonators[res_index].name, I, Q)
					align()
					save(I, I_st)
					save(Q, Q_st)
					# eliminate charge accumulation, also initialize TLS
					wait(cd_time_qubit * u.ns, machine.resonators[res_index].name)
					align()
					square_TLS_swap[0].run(amp_array=[(machine.flux_lines[flux_index].name, -1)])
					wait(cd_time_TLS * u.ns, machine.resonators[res_index].name)
				save(n, n_st)

			with stream_processing():
				I_st.buffer(len(rabi_amp_sweep_rel)).average().save("I")
				Q_st.buffer(len(rabi_amp_sweep_rel)).average().save("Q")
				n_st.save("iteration")

		#  Open Communication with the QOP  #
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config, log_level = "ERROR")

		if simulate_flag:
			simulation_config = SimulationConfig(duration=1000)  # in clock cycles
			job = qmm.simulate(config, tls_power_rabi, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			qm = qmm.open_qm(config)
			job = qm.execute(tls_power_rabi)
			results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")

			# Live plotting
			if plot_flag == True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [8, 4]
				interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

			while results.is_processing():
				# Fetch results
				I, Q, iteration = results.fetch_all()
				I = u.demod2volts(I, machine.resonators[qubit_index].readout_pulse_length)
				Q = u.demod2volts(Q, machine.resonators[qubit_index].readout_pulse_length)
				sig_amp = np.sqrt(I ** 2 + Q ** 2)
				sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))
				# Progress bar
				progress_counter(iteration, n_avg, start_time=results.get_start_time())
				if plot_flag == True:
					plt.cla()
					plt.title("TLS power rabi")
					plt.plot(rabi_amp_sweep_abs, sig_amp, "b.")
					plt.xlabel("rabi amplitude [V]")
					plt.ylabel(r"$\sqrt{I^2 + Q^2}$ [V]")
					plt.pause(0.01)

			# fetch all data after live-updating
			I, Q, iteration = results.fetch_all()
			# Convert I & Q to Volts
			I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
			Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
			sig_amp = np.sqrt(I ** 2 + Q ** 2)
			sig_phase = np.angle(I + 1j * Q)

			# save data
			exp_name = 'TLS_power_rabi'
			qubit_name = 'Q' + str(qubit_index + 1) + 'TLS' + str(TLS_index+1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name),
					{"TLS_rabi_amplitude": rabi_amp_sweep_abs, "sig_amp": sig_amp, "sig_phase": sig_phase})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, rabi_amp_sweep_abs, sig_amp

	def ef_freq(self, ef_freq_sweep, qubit_index, res_index, flux_index, pi_amp_rel = 1.0, pi_amp_rel_ef = 1.0, n_avg = 1E3, cd_time = 10E3, readout_state = 'g', tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
		ef spectroscopy experiment in 1D

		Args:
		:param ef_freq_sweep: 1D array of qubit ef transition frequency sweep
		:param qubit_index:
		:param res_index:
		:param flux_index:
		:param pi_amp_rel:
		:param pi_amp_rel_ef: 1.0 (default). relative amplitude of pi pulse for ef transition
		:param n_avg: repetition of the experiments
		:param cd_time: cooldown time between subsequent experiments
		:param readout_state: state used for readout. If 'g' (default), ground state will be used, so a pi pulse to bring population back to g is employed. If 'e', then no additional pi pulse for readout is sent
		:param ff_amp: fast flux amplitude the overlaps with the Rabi pulse. The ff pulse is 40ns longer than Rabi pulse, and share the same center time.
		:param tPath: target path/folder for saving the data. Default is today.
		:param f_str_datetime: datetime string for saving the data. Default is now.
		:param simulate_flag: True-run simulation; False (default)-run experiment.
		:param simulation_len: Length of the sequence to simulate. In clock cycles (4ns).
		:param plot_flag: True (default) plot the experiment. False, do not plot.
		:param machine: None (default), will read from quam_state.json
		Return:
			machine
			ef_freq_sweep
			sig_amp
		"""
		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)
		qubit_lo = machine.qubits[qubit_index].lo
		qubit_if = machine.qubits[qubit_index].f_01 - machine.qubits[qubit_index].lo
		ef_if_sweep = ef_freq_sweep - qubit_lo
		ef_if_sweep = np.round(ef_if_sweep)

		if abs(qubit_if) > 350E6:
			print("qubit if > 350MHz")
			return None
		if abs(qubit_if) < 20E6:
			print("qubit if < 20MHz")
			return None
		if np.max(abs(ef_if_sweep)) > 350E6: # check if parameters are within hardware limit
			print("ef if range > 350MHz")
			return None
		if np.min(abs(ef_if_sweep)) < 20E6: # check if parameters are within hardware limit
			print("ef if range < 20MHz")
			return None

		with program() as ef_freq_prog:
			[I,Q,n,I_st,Q_st,n_st] = declare_vars()
			df = declare(int)
			with for_(n, 0, n < n_avg, n+1):
				with for_(*from_array(df,ef_if_sweep)):
					update_frequency(machine.qubits[qubit_index].name, qubit_if)
					play('pi'*amp(pi_amp_rel), machine.qubits[qubit_index].name)
					align(machine.qubits[qubit_index].name, machine.flux_lines[flux_index].name,
						  machine.resonators[res_index].name)
					update_frequency(machine.qubits[qubit_index].name, df)
					play('pi_ef' * amp(pi_amp_rel_ef), machine.qubits[qubit_index].name)
					if readout_state == 'g':
						update_frequency(machine.qubits[qubit_index].name, qubit_if)
						play('pi'*amp(pi_amp_rel), machine.qubits[qubit_index].name)
					elif readout_state == 'e':
						pass
					else:
						print('Readout state does not exist')
						return None
					align()
					readout_avg_macro(machine.resonators[res_index].name,I,Q)
					wait(cd_time * u.ns, machine.resonators[res_index].name)
					save(I, I_st)
					save(Q, Q_st)
				save(n, n_st)
			with stream_processing():
				n_st.save('iteration')
				I_st.buffer(len(ef_if_sweep)).average().save("I")
				Q_st.buffer(len(ef_if_sweep)).average().save("Q")

		#####################################
		#  Open Communication with the QOP  #
		#####################################
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config, log_level = "ERROR")
		# Simulate or execute #
		if simulate_flag: # simulation is useful to see the sequence, especially the timing (clock cycle vs ns)
			simulation_config = SimulationConfig(duration=simulation_len)
			job = qmm.simulate(config, ef_freq_prog, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			qm = qmm.open_qm(config)
			job = qm.execute(ef_freq_prog)
			# Get results from QUA program
			results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
			# Live plotting
		    #%matplotlib qt
			if plot_flag == True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [8, 4]
				interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
			while results.is_processing():
				# Fetch results
				I, Q, iteration = results.fetch_all()
				I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
				Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
				# progress bar
				progress_counter(iteration, n_avg, start_time=results.get_start_time())

				if plot_flag == True:
					plt.cla()
					plt.title("ef spectroscopy")
					plt.plot((ef_freq_sweep) / u.MHz, np.sqrt(I**2 +  Q**2), ".")
					plt.xlabel("Frequency [MHz]")
					plt.ylabel(r"$\sqrt{I^2 + Q^2}$ [V]")

			# fetch all data after live-updating
			I, Q, iteration = results.fetch_all()
			# Convert I & Q to Volts
			I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
			Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
			sig_amp = np.sqrt(I**2 + Q**2)
			sig_phase = np.angle(I + 1j * Q)

			# save data
			exp_name = 'ef_freq'
			qubit_name = 'Q' + str(qubit_index + 1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name), {"ef_freq": ef_freq_sweep, "sig_amp": sig_amp, "sig_phase": sig_phase, "readout_state": readout_state})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, ef_freq_sweep, sig_amp

	def ef_rabi_length(self, rabi_duration_sweep, qubit_index, res_index, flux_index, pi_amp_rel = 1.0, pi_amp_rel_ef = 1.0, n_avg = 1E3, cd_time = 10E3, readout_state = 'g', tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
		qubit ef rabi experiment in 1D (sweeps length of rabi pulse)

		:param rabi_duration_sweep: in clock cycles!
		:param qubit_index:
		:param res_index:
		:param flux_index:
		:param pi_amp_rel:
		:param pi_amp_rel_ef: 1.0 (default). relative amplitude of pi pulse for ef transition
		:param n_avg:
		:param cd_time:
		:param readout_state: state used for readout. 'g' (default), a g-e pi pulse before readout. If 'e', then no additional pi pulse for readout.
		:param tPath:
		:param f_str_datetime:
		:param simulate_flag:
		:param simulation_len:
		:param plot_flag:
		:param machine: None (default), will read from quam_state.json
		Return:
			machine
			rabi_duration_sweep: in ns!
			sig_amp
		"""
		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if min(rabi_duration_sweep) < 4:
			print("some rabi lengths shorter than 4 clock cycles, removed from run")
			rabi_duration_sweep = rabi_duration_sweep[rabi_duration_sweep>3]

		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)
		rabi_duration_sweep = rabi_duration_sweep.astype(int)
		qubit_if = machine.qubits[qubit_index].f_01 - machine.qubits[qubit_index].lo
		ef_if = machine.qubits[qubit_index].f_01 - machine.qubits[qubit_index].anharmonicity - machine.qubits[qubit_index].lo

		if abs(qubit_if) > 350E6:
			print("qubit if > 350MHz")
			return None
		if abs(qubit_if) < 20E6:
			print("qubit if < 20MHz")
			return None
		if abs(ef_if) > 350E6:
			print("ef if > 350MHz")
			return None
		if abs(ef_if) < 20E6:
			print("ef if < 20MHz")
			return None

		with program() as time_rabi_ef:
			[I, Q, n, I_st, Q_st, n_st] = declare_vars()
			t = declare(int)

			with for_(n, 0, n < n_avg, n + 1):
				with for_(*from_array(t, rabi_duration_sweep)):
					update_frequency(machine.qubits[qubit_index].name, qubit_if)
					play('pi'*amp(pi_amp_rel), machine.qubits[qubit_index].name)
					align(machine.qubits[qubit_index].name, machine.flux_lines[flux_index].name,
						  machine.resonators[res_index].name)
					update_frequency(machine.qubits[qubit_index].name, ef_if)
					play('pi_ef' * amp(pi_amp_rel_ef), machine.qubits[qubit_index].name, duration=t) # clock cycle
					if readout_state == 'g':
						update_frequency(machine.qubits[qubit_index].name, qubit_if)
						play('pi'*amp(pi_amp_rel), machine.qubits[qubit_index].name)
					elif readout_state == 'e':
						pass
					else:
						print('Readout state does not exist')
						return None, None, None
					align()
					readout_avg_macro(machine.resonators[res_index].name,I,Q)
					save(I, I_st)
					save(Q, Q_st)
					wait(cd_time * u.ns, machine.resonators[res_index].name)
				save(n, n_st)
			with stream_processing():
				I_st.buffer(len(rabi_duration_sweep)).average().save("I")
				Q_st.buffer(len(rabi_duration_sweep)).average().save("Q")
				n_st.save("iteration")

		#  Open Communication with the QOP  #
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config, log_level = "ERROR")

		if simulate_flag:
			simulation_config = SimulationConfig(duration=simulation_len)  # in clock cycles
			job = qmm.simulate(config, time_rabi_ef, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			qm = qmm.open_qm(config)
			job = qm.execute(time_rabi_ef)
			results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")

			# Live plotting
			if plot_flag == True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [8, 4]
				interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

			while results.is_processing():
				# Fetch results
				I, Q, iteration = results.fetch_all()
				I = u.demod2volts(I, machine.resonators[qubit_index].readout_pulse_length)
				Q = u.demod2volts(Q, machine.resonators[qubit_index].readout_pulse_length)
				sig_amp = np.sqrt(I ** 2 + Q ** 2)
				sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))
				# Progress bar
				progress_counter(iteration, n_avg, start_time=results.get_start_time())
				if plot_flag == True:
					plt.cla()
					plt.title("ef time Rabi")
					plt.plot(rabi_duration_sweep * 4, sig_amp, "b.")
					plt.xlabel("tau [ns]")
					plt.ylabel(r"$\sqrt{I^2 + Q^2}$ [V]")
					plt.pause(0.01)

			# fetch all data after live-updating
			I, Q, iteration = results.fetch_all()
			# Convert I & Q to Volts
			I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
			Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
			sig_amp = np.sqrt(I ** 2 + Q ** 2)
			sig_phase = np.angle(I + 1j * Q)

			# save data
			exp_name = 'ef_time_rabi'
			qubit_name = 'Q' + str(qubit_index + 1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name),
					{"Q_rabi_duration": rabi_duration_sweep * 4, "sig_amp": sig_amp, "sig_phase": sig_phase, "readout_state": readout_state})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, rabi_duration_sweep * 4, sig_amp

	def ef_rabi_amp(self, rabi_amp_sweep_rel, qubit_index, res_index, flux_index, pi_amp_rel = 1.0, n_avg = 1E3, cd_time = 10E3, readout_state = 'g', tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
		qubit ef rabi experiment in 1D (sweeps amplitude of rabi pulse)
		note that the input argument is in relative amplitude, the return argument is in absolute amplitude

		:param rabi_amp_sweep_rel: relative amplitude, based on pi_amp[1]
		:param qubit_index:
		:param res_index:
		:param flux_index:
		:param pi_amp_rel: for the ge pulse
		:param n_avg:
		:param cd_time:
		:param readout_state: state used for readout. 'g' (default), a g-e pi pulse before readout. If 'e', then no additional pi pulse for readout.
		:param tPath:
		:param f_str_datetime:
		:param simulate_flag:
		:param simulation_len:
		:param plot_flag:
		:param machine: None (default), will read from quam_state.json
		Return:
			machine
			rabi_amp_sweep_abs
			sig_amp
		"""
		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)

		qubit_if = machine.qubits[qubit_index].f_01 - machine.qubits[qubit_index].lo
		rabi_amp_sweep_abs = rabi_amp_sweep_rel * machine.qubits[qubit_index].pi_amp[1] # actual rabi amplitude
		ef_if = machine.qubits[qubit_index].f_01 - machine.qubits[qubit_index].anharmonicity - machine.qubits[qubit_index].lo

		if abs(qubit_if) > 350E6:
			print("qubit if > 350MHz")
			return None
		if abs(qubit_if) < 20E6:
			print("qubit if < 20MHz")
			return None
		if abs(ef_if) > 350E6:
			print("ef if > 350MHz")
			return None
		if abs(ef_if) < 20E6:
			print("ef if < 20MHz")
			return None

		with program() as power_rabi_ef:
			[I, Q, n, I_st, Q_st, n_st] = declare_vars()
			a = declare(fixed)

			with for_(n, 0, n < n_avg, n + 1):
				with for_(*from_array(a, rabi_amp_sweep_rel)):
					update_frequency(machine.qubits[qubit_index].name, qubit_if)
					play('pi' * amp(pi_amp_rel), machine.qubits[qubit_index].name)
					align(machine.qubits[qubit_index].name, machine.flux_lines[flux_index].name,
						  machine.resonators[res_index].name)
					update_frequency(machine.qubits[qubit_index].name, ef_if)
					play('pi_ef' * amp(a), machine.qubits[qubit_index].name)
					if readout_state == 'g':
						update_frequency(machine.qubits[qubit_index].name, qubit_if)
						play('pi' * amp(pi_amp_rel), machine.qubits[qubit_index].name)
					elif readout_state == 'e':
						pass
					else:
						print('Readout state does not exist')
						return None, None, None
					align()
					readout_avg_macro(machine.resonators[res_index].name, I, Q)
					save(I, I_st)
					save(Q, Q_st)
					wait(cd_time * u.ns, machine.resonators[res_index].name)
				save(n, n_st)

			with stream_processing():
				I_st.buffer(len(rabi_amp_sweep_rel)).average().save("I")
				Q_st.buffer(len(rabi_amp_sweep_rel)).average().save("Q")
				n_st.save("iteration")

		#  Open Communication with the QOP  #
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config, log_level = "ERROR")

		if simulate_flag:
			simulation_config = SimulationConfig(duration=1000)  # in clock cycles
			job = qmm.simulate(config, power_rabi_ef, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			qm = qmm.open_qm(config)
			job = qm.execute(power_rabi_ef)
			results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")

			# Live plotting
			if plot_flag == True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [8, 4]
				interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

			while results.is_processing():
				# Fetch results
				I, Q, iteration = results.fetch_all()
				I = u.demod2volts(I, machine.resonators[qubit_index].readout_pulse_length)
				Q = u.demod2volts(Q, machine.resonators[qubit_index].readout_pulse_length)
				sig_amp = np.sqrt(I ** 2 + Q ** 2)
				sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))
				# Progress bar
				progress_counter(iteration, n_avg, start_time=results.get_start_time())
				if plot_flag == True:
					plt.cla()
					plt.title("ef power Rabi")
					plt.plot(rabi_amp_sweep_abs, sig_amp, "b.")
					plt.xlabel("rabi amplitude [V]")
					plt.ylabel(r"$\sqrt{I^2 + Q^2}$ [V]")
					plt.pause(0.01)

			# fetch all data after live-updating
			I, Q, iteration = results.fetch_all()
			# Convert I & Q to Volts
			I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
			Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
			sig_amp = np.sqrt(I ** 2 + Q ** 2)
			sig_phase = np.angle(I + 1j * Q)

			# save data
			exp_name = 'ef_power_rabi'
			qubit_name = 'Q' + str(qubit_index + 1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name),
					{"Q_rabi_amplitude": rabi_amp_sweep_abs, "sig_amp": sig_amp, "sig_phase": sig_phase, "readout_state": readout_state})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, rabi_amp_sweep_abs, sig_amp

	def ef_rabi_length_thermal(self, rabi_duration_sweep, qubit_index, res_index, flux_index, pi_amp_rel = 1.0, pi_amp_rel_ef = 1.0, n_avg = 1E3, cd_time = 10E3, readout_state = 'e', tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
		qubit ef rabi experiment with no first ge pi pulse
		This is to measure the oscillation of residual |e> state, A_sig in https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.114.240501

		:param rabi_duration_sweep: in clock cycles!
		:param qubit_index:
		:param res_index:
		:param flux_index:
		:param pi_amp_rel:
		:param pi_amp_rel_ef: relative amplitude of pi pulse for ef transition, based on pi_amp[1]
		:param n_avg:
		:param cd_time:
		:param readout_state: state used for readout. 'e' (default). If 'g', then a g-e pi pulse before readout.
		:param tPath:
		:param f_str_datetime:
		:param simulate_flag:
		:param simulation_len:
		:param plot_flag:
		:param machine: None (default), will read from quam_state.json
		Return:
			machine
			rabi_duration_sweep: in ns!
			sig_amp
		"""
		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if min(rabi_duration_sweep) < 4:
			print("some rabi lengths shorter than 4 clock cycles, removed from run")
			rabi_duration_sweep = rabi_duration_sweep[rabi_duration_sweep>3]

		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)
		rabi_duration_sweep = rabi_duration_sweep.astype(int)
		qubit_if = machine.qubits[qubit_index].f_01 - machine.qubits[qubit_index].lo
		ef_if = machine.qubits[qubit_index].f_01 - machine.qubits[qubit_index].anharmonicity - machine.qubits[qubit_index].lo

		if abs(qubit_if) > 350E6:
			print("qubit if > 350MHz")
			return None
		if abs(qubit_if) < 20E6:
			print("qubit if < 20MHz")
			return None
		if abs(ef_if) > 350E6:
			print("ef if > 350MHz")
			return None
		if abs(ef_if) < 20E6:
			print("ef if < 20MHz")
			return None

		with program() as time_rabi_ef_thermal:
			[I, Q, n, I_st, Q_st, n_st] = declare_vars()
			t = declare(int)

			with for_(n, 0, n < n_avg, n + 1):
				with for_(*from_array(t, rabi_duration_sweep)):
					update_frequency(machine.qubits[qubit_index].name, ef_if)
					play('pi_ef' * amp(pi_amp_rel_ef), machine.qubits[qubit_index].name, duration=t)
					if readout_state == 'g':
						update_frequency(machine.qubits[qubit_index].name, qubit_if)
						play('pi'*amp(pi_amp_rel), machine.qubits[qubit_index].name)
					elif readout_state == 'e':
						pass
					else:
						print('Readout state does not exist')
						return None
					align()
					readout_avg_macro(machine.resonators[res_index].name,I,Q)
					save(I, I_st)
					save(Q, Q_st)
					wait(cd_time * u.ns, machine.resonators[res_index].name)
				save(n, n_st)
			with stream_processing():
				I_st.buffer(len(rabi_duration_sweep)).average().save("I")
				Q_st.buffer(len(rabi_duration_sweep)).average().save("Q")
				n_st.save("iteration")

		#  Open Communication with the QOP  #
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config, log_level = "ERROR")

		if simulate_flag:
			simulation_config = SimulationConfig(duration=simulation_len)  # in clock cycles
			job = qmm.simulate(config, time_rabi_ef_thermal, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			qm = qmm.open_qm(config)
			job = qm.execute(time_rabi_ef_thermal)
			results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")

			# Live plotting
			if plot_flag == True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [8, 4]
				interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

			while results.is_processing():
				# Fetch results
				I, Q, iteration = results.fetch_all()
				I = u.demod2volts(I, machine.resonators[qubit_index].readout_pulse_length)
				Q = u.demod2volts(Q, machine.resonators[qubit_index].readout_pulse_length)
				sig_amp = np.sqrt(I ** 2 + Q ** 2)
				sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))
				# Progress bar
				progress_counter(iteration, n_avg, start_time=results.get_start_time())
				if plot_flag == True:
					plt.cla()
					plt.title("residual e state time rabi")
					plt.plot(rabi_duration_sweep * 4, sig_amp, "b.")
					plt.xlabel("tau [ns]")
					plt.ylabel(r"$\sqrt{I^2 + Q^2}$ [V]")
					plt.pause(0.01)

			# fetch all data after live-updating
			I, Q, iteration = results.fetch_all()
			# Convert I & Q to Volts
			I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
			Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
			sig_amp = np.sqrt(I ** 2 + Q ** 2)
			sig_phase = np.angle(I + 1j * Q)

			# save data
			exp_name = 'time_rabi_ef_thermal'
			qubit_name = 'Q' + str(qubit_index + 1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name),
					{"Q_rabi_duration": rabi_duration_sweep * 4, "sig_amp": sig_amp, "sig_phase": sig_phase, "readout_state": readout_state})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, rabi_duration_sweep * 4, sig_amp

class EH_T1:
	def __init__(self, ref_to_update_tPath, ref_to_update_str_datetime):
		self.update_tPath = ref_to_update_tPath
		self.update_str_datetime = ref_to_update_str_datetime

	def qubit_T1(self, tau_sweep_abs, qubit_index, res_index, flux_index, TLS_index=0, n_avg = 1E3, cd_time = 10E3, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
		runs qubit T1. Designed to be at fixed 0 fast flux.

		Args:
			tau_sweep_abs (): in ns. Will be regulated to integer clock cycles
			qubit_index ():
			res_index ():
			flux_index ():
			n_avg ():
			cd_time ():
			tPath ():
			f_str_datetime ():
			simulate_flag ():
			simulation_len ():
			plot_flag ():
			machine (): None (default), will read from quam_state.json

		Returns:
			machine
			tau_sweep_abs
			sig_amp

		"""
		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)

		tau_sweep_cc = tau_sweep_abs//4 # in clock cycles
		tau_sweep_cc = np.unique(tau_sweep_cc)
		tau_sweep = tau_sweep_cc.astype(int) # clock cycles
		tau_sweep_abs = tau_sweep * 4 # time in ns

		with program() as t1_prog:
			[I, Q, n, I_st, Q_st, n_st] = declare_vars()
			tau = declare(int)

			with for_(n, 0, n < n_avg, n + 1):
				with for_(*from_array(tau, tau_sweep)):
					play("pi", machine.qubits[qubit_index].name)
					wait(tau, machine.qubits[qubit_index].name)
					align(machine.qubits[qubit_index].name, machine.resonators[qubit_index].name)
					readout_avg_macro(machine.resonators[res_index].name,I,Q)
					save(I, I_st)
					save(Q, Q_st)
					wait(cd_time * u.ns, machine.resonators[res_index].name)
				save(n, n_st)
			with stream_processing():
				I_st.buffer(len(tau_sweep)).average().save("I")
				Q_st.buffer(len(tau_sweep)).average().save("Q")
				n_st.save("iteration")

		#  Open Communication with the QOP  #
		qmm = QuantumMachinesManager(machine.network.qop_ip, port='9510', octave=octave_config, log_level = "ERROR")

		# Simulate or execute #
		if simulate_flag:
			simulation_config = SimulationConfig(duration=simulation_len)
			job = qmm.simulate(config, t1_prog, simulation_config)
			job.get_simulated_samples().con1.plot()

			return None
		else:
			qm = qmm.open_qm(config)
			job = qm.execute(t1_prog)
			# Get results from QUA program
			results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
			# Live plotting
			if plot_flag is True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [12, 8]
				interrupt_on_close(fig, job)  # Interrupts the job when closing the figure    while results.is_processing():
			while results.is_processing():
				# Fetch results
				I, Q, iteration = results.fetch_all()
				I = u.demod2volts(I, machine.resonators[qubit_index].readout_pulse_length)
				Q = u.demod2volts(Q, machine.resonators[qubit_index].readout_pulse_length)
				sig_amp = np.sqrt(I ** 2 + Q ** 2)
				sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))
				# Progress bar
				progress_counter(iteration, n_avg, start_time=results.get_start_time())
				if plot_flag == True:
					plt.cla()
					plt.title("T1")
					plt.plot(tau_sweep_abs, sig_amp, "b.")
					plt.xlabel("tau [ns]")
					plt.ylabel(r"$\sqrt{I^2 + Q^2}$ [V]")
					plt.pause(0.01)

		# save data
		exp_name = 'T1'
		qubit_name = 'Q' + str(qubit_index + 1)
		f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
		file_name = f_str + '.mat'
		json_name = f_str + '_state.json'
		savemat(os.path.join(tPath, file_name),
				{"Q_tau": tau_sweep_abs, "sig_amp": sig_amp, "sig_phase": sig_phase})
		machine._save(os.path.join(tPath, json_name), flat_data=False)

		return machine, tau_sweep_abs, sig_amp

	def TLS_T1(self, tau_sweep_abs, qubit_index, res_index, flux_index, TLS_index=0, n_avg = 1E3, cd_time_qubit = 10E3, cd_time_TLS = None, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
		TLS T1 using SWAP only
		sequence is qubit pi - SWAP - wait - SWAP - qubit readout

		:param tau_sweep_abs: in ns!
		:param qubit_index:
		:param res_index:
		:param flux_index:
		:param TLS_index:
		:param n_avg:
		:param cd_time:
		:param cd_time_TLS:
		:param tPath:
		:param f_str_datetime:
		:param simulate_flag:
		:param simulation_len:
		:param plot_flag:
		:param machine:
		:return:
			machine
			tau_sweep_abs
			sig_amp
		"""
		if cd_time_TLS is None:
			cd_time_TLS = cd_time_qubit

		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)

		swap_length = machine.flux_lines[flux_index].iswap.length[TLS_index]
		swap_amp = machine.flux_lines[flux_index].iswap.level[TLS_index]
		tau_sweep_cc = tau_sweep_abs//4 # in clock cycles
		tau_sweep_cc = np.unique(tau_sweep_cc)
		tau_sweep = tau_sweep_cc.astype(int) # clock cycles
		tau_sweep_abs = tau_sweep * 4 # time in ns

		# fLux pulse baking for SWAP
		flux_waveform = np.array([swap_amp] * swap_length)
		def baked_swap_waveform(waveform):
			pulse_segments = []  # Stores the baking objects
			# Create the different baked sequences, each one corresponding to a different truncated duration
			with baking(config, padding_method="right") as b:
				b.add_op("flux_pulse", machine.flux_lines[flux_index].name, waveform.tolist())
				b.play("flux_pulse", machine.flux_lines[flux_index].name)
				pulse_segments.append(b)
			return pulse_segments
		square_TLS_swap = baked_swap_waveform(flux_waveform)

		with program() as t1_prog:
			[I, Q, n, I_st, Q_st, n_st] = declare_vars()
			tau = declare(int)

			with for_(n, 0, n < n_avg, n + 1):
				with for_(*from_array(tau, tau_sweep)):
					play("pi", machine.qubits[qubit_index].name)
					align()
					square_TLS_swap[0].run()
					wait(tau, machine.flux_lines[flux_index].name)
					square_TLS_swap[0].run()
					align()
					readout_rotated_macro(machine.resonators[res_index].name,I,Q)
					save(I, I_st)
					save(Q, Q_st)
					align()
					wait(cd_time_qubit * u.ns)
					square_TLS_swap[0].run(amp_array=[(machine.flux_lines[flux_index].name, -1)])
					wait(cd_time_qubit * u.ns)
					square_TLS_swap[0].run(amp_array=[(machine.flux_lines[flux_index].name, -1)])
					wait(cd_time_TLS * u.ns)
				save(n, n_st)
			with stream_processing():
				I_st.buffer(len(tau_sweep)).average().save("I")
				Q_st.buffer(len(tau_sweep)).average().save("Q")
				n_st.save("iteration")

		#  Open Communication with the QOP  #
		qmm = QuantumMachinesManager(machine.network.qop_ip, port='9510', octave=octave_config, log_level = "ERROR")

		# Simulate or execute #
		if simulate_flag:
			simulation_config = SimulationConfig(duration=simulation_len)
			job = qmm.simulate(config, t1_prog, simulation_config)
			job.get_simulated_samples().con1.plot()

			return None
		else:
			qm = qmm.open_qm(config)
			job = qm.execute(t1_prog)
			# Get results from QUA program
			results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
			# Live plotting
			if plot_flag is True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [12, 8]
				interrupt_on_close(fig, job)  # Interrupts the job when closing the figure    while results.is_processing():
			while results.is_processing():
				# Fetch results
				I, Q, iteration = results.fetch_all()
				I = u.demod2volts(I, machine.resonators[qubit_index].readout_pulse_length)
				Q = u.demod2volts(Q, machine.resonators[qubit_index].readout_pulse_length)
				sig_amp = np.sqrt(I ** 2 + Q ** 2)
				sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))
				# Progress bar
				progress_counter(iteration, n_avg, start_time=results.get_start_time())
				if plot_flag == True:
					plt.cla()
					plt.title("TLS T1")
					plt.plot(tau_sweep_abs, I, "b.")
					plt.xlabel("tau [ns]")
					plt.ylabel(r"$I$ [V]")
					plt.pause(0.01)

		# save data
		exp_name = 'T1'
		qubit_name = 'Q' + str(qubit_index + 1) + "_TLS" + str(TLS_index + 1)
		f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
		file_name = f_str + '.mat'
		json_name = f_str + '_state.json'
		savemat(os.path.join(tPath, file_name),
				{"TLS_tau": tau_sweep_abs, "sig_amp": sig_amp, "sig_phase": sig_phase})
		machine._save(os.path.join(tPath, json_name), flat_data=False)

		return machine, tau_sweep_abs, I

	def TLS_T1_driving(self, tau_sweep_abs, qubit_index, res_index, flux_index, TLS_index=0, n_avg = 1E3, cd_time_qubit = 10E3, cd_time_TLS = None, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
		TLS T1 using direct TLS driving
		sequence is TLS pi - wait - SWAP - qubit readout

		:param tau_sweep_abs:
		:param qubit_index:
		:param res_index:
		:param flux_index:
		:param TLS_index:
		:param n_avg:
		:param cd_time_qubit:
		:param cd_time_TLS:
		:param tPath:
		:param f_str_datetime:
		:param simulate_flag:
		:param simulation_len:
		:param plot_flag:
		:param machine:
		:return:
			machine
			tau_sweep_abs
			I
		"""
		if cd_time_TLS is None:
			cd_time_TLS = cd_time_qubit

		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)

		swap_length = machine.flux_lines[flux_index].iswap.length[TLS_index]
		swap_amp = machine.flux_lines[flux_index].iswap.level[TLS_index]
		tau_sweep_cc = tau_sweep_abs//4 # in clock cycles
		tau_sweep_cc = np.unique(tau_sweep_cc)
		tau_sweep = tau_sweep_cc.astype(int) # clock cycles
		tau_sweep_abs = tau_sweep * 4 # time in ns

		# fLux pulse baking for SWAP
		flux_waveform = np.array([swap_amp] * swap_length)
		def baked_swap_waveform(waveform):
			pulse_segments = []  # Stores the baking objects
			# Create the different baked sequences, each one corresponding to a different truncated duration
			with baking(config, padding_method="right") as b:
				b.add_op("flux_pulse", machine.flux_lines[flux_index].name, waveform.tolist())
				b.play("flux_pulse", machine.flux_lines[flux_index].name)
				pulse_segments.append(b)
			return pulse_segments
		square_TLS_swap = baked_swap_waveform(flux_waveform)

		with program() as t1_prog:
			[I, Q, n, I_st, Q_st, n_st] = declare_vars()
			tau = declare(int)

			with for_(n, 0, n < n_avg, n + 1):
				with for_(*from_array(tau, tau_sweep)):
					play("pi_tls", machine.qubits[qubit_index].name)
					wait(tau, machine.qubits[qubit_index].name)
					align()
					square_TLS_swap[0].run()
					align()
					readout_rotated_macro(machine.resonators[res_index].name,I,Q)
					save(I, I_st)
					save(Q, Q_st)
					align()
					wait(cd_time_qubit * u.ns)
					square_TLS_swap[0].run(amp_array=[(machine.flux_lines[flux_index].name, -1)])
					wait(cd_time_TLS * u.ns)
				save(n, n_st)
			with stream_processing():
				I_st.buffer(len(tau_sweep)).average().save("I")
				Q_st.buffer(len(tau_sweep)).average().save("Q")
				n_st.save("iteration")

		#  Open Communication with the QOP  #
		qmm = QuantumMachinesManager(machine.network.qop_ip, port='9510', octave=octave_config, log_level = "ERROR")

		# Simulate or execute #
		if simulate_flag:
			simulation_config = SimulationConfig(duration=simulation_len)
			job = qmm.simulate(config, t1_prog, simulation_config)
			job.get_simulated_samples().con1.plot()

			return None
		else:
			qm = qmm.open_qm(config)
			job = qm.execute(t1_prog)
			# Get results from QUA program
			results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
			# Live plotting
			if plot_flag is True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [12, 8]
				interrupt_on_close(fig, job)  # Interrupts the job when closing the figure    while results.is_processing():
			while results.is_processing():
				# Fetch results
				I, Q, iteration = results.fetch_all()
				I = u.demod2volts(I, machine.resonators[qubit_index].readout_pulse_length)
				Q = u.demod2volts(Q, machine.resonators[qubit_index].readout_pulse_length)
				sig_amp = np.sqrt(I ** 2 + Q ** 2)
				sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))
				# Progress bar
				progress_counter(iteration, n_avg, start_time=results.get_start_time())
				if plot_flag == True:
					plt.cla()
					plt.title("TLS T1 (driving)")
					plt.plot(tau_sweep_abs, I, "b.")
					plt.xlabel("tau [ns]")
					plt.ylabel(r"$I$ [V]")
					plt.pause(0.01)

		# save data
		exp_name = 'T1_driving'
		qubit_name = 'Q' + str(qubit_index + 1) + "_TLS" + str(TLS_index + 1)
		f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
		file_name = f_str + '.mat'
		json_name = f_str + '_state.json'
		savemat(os.path.join(tPath, file_name),
				{"TLS_tau": tau_sweep_abs, "sig_amp": sig_amp, "sig_phase": sig_phase})
		machine._save(os.path.join(tPath, json_name), flat_data=False)

		return machine, tau_sweep_abs, I

class EH_SWAP:
	"""
	class in ExperimentHandle, for SWAP sequence related 1D experiments
	Methods:
		update_tPath
		update_str_datetime
		qubit_freq(self, qubit_freq_sweep, qubit_index, res_index, flux_index, n_avg, cd_time, ff_amp = 1.0, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000)
	"""

	def __init__(self, ref_to_update_tPath, ref_to_update_str_datetime, ref_to_octave_calibration):
		self.update_tPath = ref_to_update_tPath
		self.update_str_datetime = ref_to_update_str_datetime
		self.octave_calibration = ref_to_octave_calibration

	def rabi_SWAP(self, rabi_duration_sweep, qubit_index, res_index, flux_index, TLS_index, pi_amp_rel = 1.0, n_avg = 1E3, cd_time = 10E3, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
		1D experiment: qubit rabi (length sweep) - SWAP - measure
		qubit rabi duration in clock cycle

		Args:
			rabi_duration_sweep (): in clock cycle!
			qubit_index ():
			res_index ():
			flux_index ():
			TLS_index ():
			pi_amp_rel ():
			n_avg ():
			cd_time ():
			tPath ():
			f_str_datetime ():
			simulate_flag ():
			simulation_len ():
			plot_flag ():
			machine ():

		Returns:
			machine
			rabi_duration_sweep * 4: in ns
			sig_amp
		"""
		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if min(rabi_duration_sweep) < 4:
			print("some rabi lengths shorter than 4 clock cycles, removed from run")
			rabi_duration_sweep = rabi_duration_sweep[rabi_duration_sweep>3]

		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)
		rabi_duration_sweep = rabi_duration_sweep.astype(int)

		# fLux pulse baking for SWAP
		swap_length = machine.flux_lines[flux_index].iswap.length[TLS_index]
		swap_amp = machine.flux_lines[flux_index].iswap.level[TLS_index]
		flux_waveform = np.array([swap_amp] * swap_length)

		def baked_swap_waveform(waveform):
			pulse_segments = []  # Stores the baking objects
			# Create the different baked sequences, each one corresponding to a different truncated duration
			with baking(config, padding_method="right") as b:
				b.add_op("flux_pulse", machine.flux_lines[flux_index].name, waveform.tolist())
				b.play("flux_pulse", machine.flux_lines[flux_index].name)
				pulse_segments.append(b)
			return pulse_segments
		square_TLS_swap = baked_swap_waveform(flux_waveform)

		with program() as time_rabi:
			[I, Q, n, I_st, Q_st, n_st] = declare_vars()
			t = declare(int)

			with for_(n, 0, n < n_avg, n + 1):
				with for_(*from_array(t, rabi_duration_sweep)):
					wait(5, machine.qubits[qubit_index].name)
					play("pi" * amp(pi_amp_rel), machine.qubits[qubit_index].name, duration=t)
					wait(5, machine.qubits[qubit_index].name)
					align()
					square_TLS_swap[0].run()
					align()
					readout_avg_macro(machine.resonators[res_index].name,I,Q)
					save(I, I_st)
					save(Q, Q_st)
					wait(cd_time * u.ns, machine.resonators[qubit_index].name)
					align()
					square_TLS_swap[0].run(amp_array=[(machine.flux_lines[flux_index].name, -1)])
					align()
					wait(cd_time * u.ns, machine.resonators[qubit_index].name)
				save(n, n_st)

			with stream_processing():
				I_st.buffer(len(rabi_duration_sweep)).average().save("I")
				Q_st.buffer(len(rabi_duration_sweep)).average().save("Q")
				n_st.save("iteration")

		#  Open Communication with the QOP  #
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config, log_level = "ERROR")

		if simulate_flag:
			simulation_config = SimulationConfig(duration=simulation_len)  # in clock cycles
			job = qmm.simulate(config, time_rabi, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			qm = qmm.open_qm(config)
			job = qm.execute(time_rabi)
			results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")

			# Live plotting
			if plot_flag == True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [8, 4]
				interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

			while results.is_processing():
				# Fetch results
				I, Q, iteration = results.fetch_all()
				I = u.demod2volts(I, machine.resonators[qubit_index].readout_pulse_length)
				Q = u.demod2volts(Q, machine.resonators[qubit_index].readout_pulse_length)
				sig_amp = np.sqrt(I ** 2 + Q ** 2)
				sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))
				# Progress bar
				progress_counter(iteration, n_avg, start_time=results.get_start_time())
				if plot_flag == True:
					plt.cla()
					plt.title("Time Rabi")
					plt.plot(rabi_duration_sweep * 4, sig_amp, "b.")
					plt.xlabel("tau [ns]")
					plt.ylabel(r"$\sqrt{I^2 + Q^2}$ [V]")
					plt.pause(0.01)

			# fetch all data after live-updating
			I, Q, iteration = results.fetch_all()
			# Convert I & Q to Volts
			I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
			Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
			sig_amp = np.sqrt(I ** 2 + Q ** 2)
			sig_phase = np.angle(I + 1j * Q)

			# save data
			exp_name = 'time_rabi'
			qubit_name = 'Q' + str(qubit_index + 1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name),
					{"Q_rabi_duration": rabi_duration_sweep * 4, "sig_amp": sig_amp, "sig_phase": sig_phase})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, rabi_duration_sweep * 4, sig_amp

	def swap_coarse(self,tau_sweep_abs, qubit_index, res_index, flux_index, TLS_index, n_avg, cd_time, tPath=None,
					f_str_datetime=None, simulate_flag=False, simulation_len=1000, plot_flag=True, machine = None):
		"""
		1D SWAP spectroscopy. qubit pi - SWAP (sweep Z duration) - measure
		tau_sweep in ns, only takes multiples of 4ns

		Args:
			tau_sweep_abs ():
			qubit_index ():
			res_index ():
			flux_index ():
			TLS_index ():
			n_avg ():
			cd_time ():
			tPath ():
			f_str_datetime ():
			simulate_flag ():
			simulation_len ():
			plot_flag ():
			machine ():

		Returns:
			machine
			tau_sweep_abs
			sig_amp
		"""

		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		tau_sweep_cc = tau_sweep_abs // 4  # in clock cycles
		tau_sweep_cc = np.unique(tau_sweep_cc)
		tau_sweep = tau_sweep_cc.astype(int)  # clock cycles
		tau_sweep_abs = tau_sweep * 4  # time in ns

		# set up variables
		if machine is None:
			machine = QuAM("quam_state.json") # this "machine" object is going to be changed by a lot, do not rely on it too much
		config = build_config(machine)

		with program() as iswap:
			[I, Q, n, I_st, Q_st, n_st] = declare_vars()
			t = declare(int)
			da = declare(fixed)

			with for_(n, 0, n < n_avg, n + 1):
				with for_(*from_array(t, tau_sweep)):
					play("pi", machine.qubits[qubit_index].name)
					align()
					play("iswap", machine.flux_lines[flux_index].name, duration=t)
					align()
					readout_avg_macro(machine.resonators[res_index].name,I,Q)
					align()
					wait(50)
					play("iswap" * amp(-1), machine.flux_lines[flux_index].name, duration=t)
					save(I, I_st)
					save(Q, Q_st)
					wait(cd_time * u.ns, machine.resonators[res_index].name)
				save(n, n_st)

			with stream_processing():
				# for the progress counter
				n_st.save("iteration")
				I_st.buffer(len(tau_sweep)).average().save("I")
				Q_st.buffer(len(tau_sweep)).average().save("Q")

		#####################################
		#  Open Communication with the QOP  #
		#####################################
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config, log_level = "ERROR")

		if simulate_flag:
			simulation_config = SimulationConfig(duration=simulation_len)
			job = qmm.simulate(config, iswap, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			qm = qmm.open_qm(config)
			job = qm.execute(iswap)
			results = fetching_tool(job, ["I", "Q", "iteration"], mode="live")

			if plot_flag:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [8,4]
				interrupt_on_close(fig, job)

			while results.is_processing():
				I, Q, iteration = results.fetch_all()
				progress_counter(iteration, n_avg, start_time=results.get_start_time())
				time.sleep(0.1)

			I, Q, _ = results.fetch_all()
			I = u.demod2volts(I, machine.resonators[qubit_index].readout_pulse_length)
			Q = u.demod2volts(Q, machine.resonators[qubit_index].readout_pulse_length)
			sig_amp = np.sqrt(I ** 2 + Q ** 2)
			sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))

			# save data
			exp_name = 'SWAP1D'
			qubit_name = 'Q' + str(qubit_index + 1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name),
					{"ff_amp": machine.flux_lines[flux_index].iswap.level[TLS_index], "sig_amp": sig_amp, "sig_phase": sig_phase,
					 "tau_sweep": tau_sweep_abs})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			if plot_flag:
				plt.cla()
				plt.plot(tau_sweep_abs, sig_amp)
				plt.ylabel("signal (V)")
				plt.xlabel("interaction time (ns)")

		return machine, tau_sweep_abs, sig_amp

	def SWAP_rabi(self, rabi_duration_sweep, qubit_index, res_index, flux_index, TLS_index, pi_amp_rel = 1.0, n_avg = 1E3, cd_time = 10E3, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
		1D experiment for debug: SWAP - qubit rabi (sweep duration) - measure

		Args:
			rabi_duration_sweep (): in clock cycle
			qubit_index ():
			res_index ():
			flux_index ():
			TLS_index ():
			pi_amp_rel ():
			n_avg ():
			cd_time ():
			tPath ():
			f_str_datetime ():
			simulate_flag ():
			simulation_len ():
			plot_flag ():
			machine ():

		Returns:
			machine
			rabi_duration_sweep * 4
			sig_amp
		"""

		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if min(rabi_duration_sweep) < 4:
			print("some rabi lengths shorter than 4 clock cycles, removed from run")
			rabi_duration_sweep = rabi_duration_sweep[rabi_duration_sweep>3]

		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)
		rabi_duration_sweep = rabi_duration_sweep.astype(int)

		# fLux pulse baking for SWAP
		swap_length = machine.flux_lines[flux_index].iswap.length[TLS_index]
		swap_amp = machine.flux_lines[flux_index].iswap.level[TLS_index]
		flux_waveform = np.array([swap_amp] * swap_length)

		def baked_swap_waveform(waveform):
			pulse_segments = []  # Stores the baking objects
			# Create the different baked sequences, each one corresponding to a different truncated duration
			with baking(config, padding_method="right") as b:
				b.add_op("flux_pulse", machine.flux_lines[flux_index].name, waveform.tolist())
				b.play("flux_pulse", machine.flux_lines[flux_index].name)
				pulse_segments.append(b)
			return pulse_segments
		square_TLS_swap = baked_swap_waveform(flux_waveform)

		with program() as time_rabi:
			[I, Q, n, I_st, Q_st, n_st] = declare_vars()
			t = declare(int)

			with for_(n, 0, n < n_avg, n + 1):
				with for_(*from_array(t, rabi_duration_sweep)):
					square_TLS_swap[0].run()
					align()
					wait(5, machine.qubits[qubit_index].name)
					play("pi" * amp(pi_amp_rel), machine.qubits[qubit_index].name, duration=t)
					wait(5, machine.qubits[qubit_index].name)
					align()
					readout_avg_macro(machine.resonators[res_index].name,I,Q)
					save(I, I_st)
					save(Q, Q_st)
					wait(cd_time * u.ns, machine.resonators[qubit_index].name)
					align()
					square_TLS_swap[0].run(amp_array=[(machine.flux_lines[flux_index].name, -1)])
					align()
					wait(cd_time * u.ns, machine.resonators[qubit_index].name)
				save(n, n_st)

			with stream_processing():
				I_st.buffer(len(rabi_duration_sweep)).average().save("I")
				Q_st.buffer(len(rabi_duration_sweep)).average().save("Q")
				n_st.save("iteration")

		#  Open Communication with the QOP  #
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config, log_level = "ERROR")

		if simulate_flag:
			simulation_config = SimulationConfig(duration=simulation_len)  # in clock cycles
			job = qmm.simulate(config, time_rabi, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			qm = qmm.open_qm(config)
			job = qm.execute(time_rabi)
			results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")

			# Live plotting
			if plot_flag == True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [8, 4]
				interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

			while results.is_processing():
				# Fetch results
				I, Q, iteration = results.fetch_all()
				I = u.demod2volts(I, machine.resonators[qubit_index].readout_pulse_length)
				Q = u.demod2volts(Q, machine.resonators[qubit_index].readout_pulse_length)
				sig_amp = np.sqrt(I ** 2 + Q ** 2)
				sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))
				# Progress bar
				progress_counter(iteration, n_avg, start_time=results.get_start_time())
				if plot_flag == True:
					plt.cla()
					plt.title("Time Rabi")
					plt.plot(rabi_duration_sweep * 4, sig_amp, "b.")
					plt.xlabel("tau [ns]")
					plt.ylabel(r"$\sqrt{I^2 + Q^2}$ [V]")
					plt.pause(0.01)

			# fetch all data after live-updating
			I, Q, iteration = results.fetch_all()
			# Convert I & Q to Volts
			I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
			Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
			sig_amp = np.sqrt(I ** 2 + Q ** 2)
			sig_phase = np.angle(I + 1j * Q)

			# save data
			exp_name = 'time_rabi'
			qubit_name = 'Q' + str(qubit_index + 1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name),
					{"Q_rabi_duration": rabi_duration_sweep * 4, "sig_amp": sig_amp, "sig_phase": sig_phase})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, rabi_duration_sweep * 4, sig_amp

	def rabi_SWAP2(self, rabi_duration_sweep, qubit_index, res_index, flux_index, TLS_index, pi_amp_rel = 1.0, n_avg = 1E3, cd_time = 10E3, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
		1D experiment: qubit rabi (sweep duration) - SWAP - SWAP, to see if the state comes back

		Args:
			rabi_duration_sweep (): in clock cycle
			qubit_index ():
			res_index ():
			flux_index ():
			TLS_index ():
			pi_amp_rel ():
			n_avg ():
			cd_time ():
			tPath ():
			f_str_datetime ():
			simulate_flag ():
			simulation_len ():
			plot_flag ():
			machine ():

		Returns:
			machine
			rabi_duration_sweep * 4
			sig_amp
		"""
		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if min(rabi_duration_sweep) < 4:
			print("some rabi lengths shorter than 4 clock cycles, removed from run")
			rabi_duration_sweep = rabi_duration_sweep[rabi_duration_sweep>3]

		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)
		rabi_duration_sweep = rabi_duration_sweep.astype(int)

		# fLux pulse baking for SWAP
		swap_length = machine.flux_lines[flux_index].iswap.length[TLS_index]
		swap_amp = machine.flux_lines[flux_index].iswap.level[TLS_index]
		flux_waveform = np.array([swap_amp] * swap_length)

		def baked_swap_waveform(waveform):
			pulse_segments = []  # Stores the baking objects
			# Create the different baked sequences, each one corresponding to a different truncated duration
			with baking(config, padding_method="right") as b:
				b.add_op("flux_pulse", machine.flux_lines[flux_index].name, waveform.tolist())
				b.play("flux_pulse", machine.flux_lines[flux_index].name)
				pulse_segments.append(b)
			return pulse_segments
		square_TLS_swap = baked_swap_waveform(flux_waveform)

		with program() as time_rabi:
			[I, Q, n, I_st, Q_st, n_st] = declare_vars()
			t = declare(int)

			with for_(n, 0, n < n_avg, n + 1):
				with for_(*from_array(t, rabi_duration_sweep)):
					wait(5, machine.qubits[qubit_index].name)
					play("pi" * amp(pi_amp_rel), machine.qubits[qubit_index].name, duration=t)
					wait(5, machine.qubits[qubit_index].name)
					align()
					square_TLS_swap[0].run()
					wait(5)
					square_TLS_swap[0].run()
					align()
					readout_avg_macro(machine.resonators[res_index].name,I,Q)
					save(I, I_st)
					save(Q, Q_st)
					wait(cd_time * u.ns, machine.resonators[qubit_index].name)
					align()
					square_TLS_swap[0].run(amp_array=[(machine.flux_lines[flux_index].name, -1)])
					wait(5)
					square_TLS_swap[0].run(amp_array=[(machine.flux_lines[flux_index].name, -1)])
					align()
					wait(cd_time * u.ns, machine.resonators[qubit_index].name)
				save(n, n_st)

			with stream_processing():
				I_st.buffer(len(rabi_duration_sweep)).average().save("I")
				Q_st.buffer(len(rabi_duration_sweep)).average().save("Q")
				n_st.save("iteration")

		#  Open Communication with the QOP  #
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config, log_level = "ERROR")

		if simulate_flag:
			simulation_config = SimulationConfig(duration=simulation_len)  # in clock cycles
			job = qmm.simulate(config, time_rabi, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			qm = qmm.open_qm(config)
			job = qm.execute(time_rabi)
			results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")

			# Live plotting
			if plot_flag == True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [8, 4]
				interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

			while results.is_processing():
				# Fetch results
				I, Q, iteration = results.fetch_all()
				I = u.demod2volts(I, machine.resonators[qubit_index].readout_pulse_length)
				Q = u.demod2volts(Q, machine.resonators[qubit_index].readout_pulse_length)
				sig_amp = np.sqrt(I ** 2 + Q ** 2)
				sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))
				# Progress bar
				progress_counter(iteration, n_avg, start_time=results.get_start_time())
				if plot_flag == True:
					plt.cla()
					plt.title("Time Rabi")
					plt.plot(rabi_duration_sweep * 4, sig_amp, "b.")
					plt.xlabel("tau [ns]")
					plt.ylabel(r"$\sqrt{I^2 + Q^2}$ [V]")
					plt.pause(0.01)

			# fetch all data after live-updating
			I, Q, iteration = results.fetch_all()
			# Convert I & Q to Volts
			I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
			Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
			sig_amp = np.sqrt(I ** 2 + Q ** 2)
			sig_phase = np.angle(I + 1j * Q)

			# save data
			exp_name = 'time_rabi'
			qubit_name = 'Q' + str(qubit_index + 1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name),
					{"Q_rabi_duration": rabi_duration_sweep * 4, "sig_amp": sig_amp, "sig_phase": sig_phase})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, rabi_duration_sweep * 4, sig_amp

class EH_Ramsey:
	def __init__(self, ref_to_update_tPath, ref_to_update_str_datetime):
		self.update_tPath = ref_to_update_tPath
		self.update_str_datetime = ref_to_update_str_datetime

	def ramsey(self, ramsey_duration_sweep, qubit_index, res_index, flux_index, pi_amp_rel = 1.0, n_avg = 1E3, detuning = 1E6, cd_time = 10E3, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
		qubit Ramsey in 1D. Detuning realized by tuning the phase of second pi/2 pulse
		sequence given by pi/2 - wait - pi/2 for various wait times
		the frame of the last pi/2 pulse is rotated rather than using qubit detuning

		:param ramsey_duration_sweep: in clock cycles!
		:param qubit_index:
		:param res_index:
		:param flux_index:
		:param pi_amp_rel:
		:param n_avg:
		:param detuning: effective detuning, in unit of Hz!
		:param cd_time:
		:param tPath:
		:param f_str_datetime:
		:param simulate_flag:
		:param simulation_len:
		:param plot_flag:
		:param machine: None (default), will read from quam_state.json
		Return:
			machine
			rabi_duration_sweep: in ns!
			sig_amp
		"""
		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if min(ramsey_duration_sweep) < 4:
			print("some ramsey lengths shorter than 4 clock cycles, removed from run")
			ramsey_duration_sweep = ramsey_duration_sweep[ramsey_duration_sweep>3]

		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)
		ramsey_duration_sweep = ramsey_duration_sweep.astype(int)
		phi_sweep = (detuning * 1E-9 * ramsey_duration_sweep * 4) % 1 # in units of 2*pi

		with program() as ramsey_vr:
			[I, Q, n, I_st, Q_st, n_st] = declare_vars()
			t = declare(int)
			phi = declare(fixed) # for virtual z rotation

			with for_(n, 0, n < n_avg, n + 1):
				with for_each_((t, phi), (ramsey_duration_sweep, phi_sweep)):
					with strict_timing_():
						play("pi2" * amp(pi_amp_rel), machine.qubits[qubit_index].name)
						wait(t, machine.qubits[qubit_index].name)
						frame_rotation_2pi(phi, machine.qubits[qubit_index].name)
						play("pi2" * amp(pi_amp_rel), machine.qubits[qubit_index].name)
					align(machine.qubits[qubit_index].name, machine.resonators[res_index].name)
					readout_avg_macro(machine.resonators[res_index].name,I,Q)
					save(I, I_st)
					save(Q, Q_st)
					wait(cd_time * u.ns, machine.resonators[qubit_index].name)
					reset_frame(machine.qubits[qubit_index].name) # to avoid phase accumulation
				save(n, n_st)

			with stream_processing():
				I_st.buffer(len(ramsey_duration_sweep)).average().save("I")
				Q_st.buffer(len(ramsey_duration_sweep)).average().save("Q")
				n_st.save("iteration")

		#  Open Communication with the QOP  #
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config, log_level = "ERROR")

		if simulate_flag:
			simulation_config = SimulationConfig(duration=simulation_len)  # in clock cycles
			job = qmm.simulate(config, ramsey_vr, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			qm = qmm.open_qm(config)
			job = qm.execute(ramsey_vr)
			results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")

			# Live plotting
			if plot_flag == True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [8, 4]
				interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

			while results.is_processing():
				# Fetch results
				I, Q, iteration = results.fetch_all()
				I = u.demod2volts(I, machine.resonators[qubit_index].readout_pulse_length)
				Q = u.demod2volts(Q, machine.resonators[qubit_index].readout_pulse_length)
				sig_amp = np.sqrt(I ** 2 + Q ** 2)
				sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))
				# Progress bar
				progress_counter(iteration, n_avg, start_time=results.get_start_time())
				if plot_flag == True:
					plt.cla()
					plt.title("Ramsey with detuning = %i MHz" % (detuning/1E6))
					plt.plot(ramsey_duration_sweep * 4, sig_amp, "b.")
					plt.xlabel("tau [ns]")
					plt.ylabel(r"$\sqrt{I^2 + Q^2}$ [V]")
					plt.pause(0.01)

			# fetch all data after live-updating
			I, Q, iteration = results.fetch_all()
			# Convert I & Q to Volts
			I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
			Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
			sig_amp = np.sqrt(I ** 2 + Q ** 2)
			sig_phase = np.angle(I + 1j * Q)

			# save data
			exp_name = 'ramsey'
			qubit_name = 'Q' + str(qubit_index + 1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name),
					{"Q_ramsey_duration": ramsey_duration_sweep * 4, "sig_amp": sig_amp, "sig_phase": sig_phase})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, ramsey_duration_sweep * 4, sig_amp

	def TLS_ramsey(self, ramsey_duration_sweep, qubit_index, res_index, flux_index, TLS_index = 0, pi_amp_rel = 1.0, n_avg = 1E3, detuning = 1E6, cd_time_qubit = 20E3, cd_time_TLS = None, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
		TLS Ramsey in 1D. Detuning realized by tuning the phase of second pi/2 pulse
		sequence given by pi/2 - wait - pi/2 for various wait times
		the frame of the last pi/2 pulse is rotated rather than using actual driving freq. detuning

		:param ramsey_duration_sweep: in clock cycles!
		:param qubit_index:
		:param res_index:
		:param flux_index:
		:param TLS_index:
		:param pi_amp_rel:
		:param n_avg:
		:param detuning:
		:param cd_time_qubit:
		:param cd_time_TLS:
		:param tPath:
		:param f_str_datetime:
		:param simulate_flag:
		:param simulation_len:
		:param plot_flag:
		:param machine:
		:return:
			machine
			ramsey_duration_sweep * 4: in ns!
			I: using rotated readout, assuming it's calibrated
		"""
		if cd_time_TLS is None:
			cd_time_TLS = cd_time_qubit

		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if min(ramsey_duration_sweep) < 4:
			print("some ramsey lengths shorter than 4 clock cycles, removed from run")
			ramsey_duration_sweep = ramsey_duration_sweep[ramsey_duration_sweep>3]

		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)
		ramsey_duration_sweep = ramsey_duration_sweep.astype(int)
		phi_sweep = (detuning * 1E-9 * ramsey_duration_sweep * 4) % 1 # in units of 2*pi

		# fLux pulse baking for SWAP
		swap_length = machine.flux_lines[flux_index].iswap.length[TLS_index]
		swap_amp = machine.flux_lines[flux_index].iswap.level[TLS_index]
		flux_waveform = np.array([swap_amp] * swap_length)

		def baked_swap_waveform(waveform):
			pulse_segments = []  # Stores the baking objects
			# Create the different baked sequences, each one corresponding to a different truncated duration
			with baking(config, padding_method="right") as b:
				b.add_op("flux_pulse", machine.flux_lines[flux_index].name, waveform.tolist())
				b.play("flux_pulse", machine.flux_lines[flux_index].name)
				pulse_segments.append(b)
			return pulse_segments

		square_TLS_swap = baked_swap_waveform(flux_waveform)

		with program() as tls_ramsey:
			[I, Q, n, I_st, Q_st, n_st] = declare_vars()
			t = declare(int)
			phi = declare(fixed) # for virtual z rotation

			with for_(n, 0, n < n_avg, n + 1):
				with for_each_((t, phi), (ramsey_duration_sweep, phi_sweep)):
					with strict_timing_():
						play("pi2_tls" * amp(pi_amp_rel), machine.qubits[qubit_index].name)
						wait(t, machine.qubits[qubit_index].name)
						frame_rotation_2pi(phi, machine.qubits[qubit_index].name)
						play("pi2_tls" * amp(pi_amp_rel), machine.qubits[qubit_index].name)
					align()
					square_TLS_swap[0].run()
					readout_rotated_macro(machine.resonators[res_index].name,I,Q)
					save(I, I_st)
					save(Q, Q_st)
					align()
					wait(cd_time_qubit * u.ns, machine.resonators[qubit_index].name)
					align()
					square_TLS_swap[0].run(amp_array=[(machine.flux_lines[flux_index].name, -1)])
					wait(cd_time_TLS * u.ns, machine.resonators[qubit_index].name)
					reset_frame(machine.qubits[qubit_index].name) # to avoid phase accumulation
				save(n, n_st)

			with stream_processing():
				I_st.buffer(len(ramsey_duration_sweep)).average().save("I")
				Q_st.buffer(len(ramsey_duration_sweep)).average().save("Q")
				n_st.save("iteration")

		#  Open Communication with the QOP  #
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config, log_level = "ERROR")

		if simulate_flag:
			simulation_config = SimulationConfig(duration=simulation_len)  # in clock cycles
			job = qmm.simulate(config, tls_ramsey, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			qm = qmm.open_qm(config)
			job = qm.execute(tls_ramsey)
			results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")

			# Live plotting
			if plot_flag == True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [8, 4]
				interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

			while results.is_processing():
				# Fetch results
				I, Q, iteration = results.fetch_all()
				I = u.demod2volts(I, machine.resonators[qubit_index].readout_pulse_length)
				Q = u.demod2volts(Q, machine.resonators[qubit_index].readout_pulse_length)
				sig_amp = np.sqrt(I ** 2 + Q ** 2)
				sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))
				# Progress bar
				progress_counter(iteration, n_avg, start_time=results.get_start_time())
				if plot_flag == True:
					plt.cla()
					plt.title("Ramsey with detuning = %i MHz" % (detuning/1E6))
					#plt.plot(ramsey_duration_sweep * 4, sig_amp, "b.")
					plt.plot(ramsey_duration_sweep * 4, I, "b.")
					plt.xlabel("tau [ns]")
					#plt.ylabel(r"$\sqrt{I^2 + Q^2}$ [V]")
					plt.ylabel(r"$I$ [V]")
					plt.pause(0.01)

			# fetch all data after live-updating
			I, Q, iteration = results.fetch_all()
			# Convert I & Q to Volts
			I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
			Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
			sig_amp = np.sqrt(I ** 2 + Q ** 2)
			sig_phase = np.angle(I + 1j * Q)

			# save data
			exp_name = 'ramsey'
			qubit_name = 'Q' + str(qubit_index + 1) + 'TLS' + str(TLS_index+1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name),
					{"TLS_ramsey_duration": ramsey_duration_sweep * 4, "sig_amp": sig_amp, "sig_phase": sig_phase})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, ramsey_duration_sweep * 4, I

class EH_DD:
	def __init__(self, ref_to_update_tPath, ref_to_update_str_datetime):
		self.update_tPath = ref_to_update_tPath
		self.update_str_datetime = ref_to_update_str_datetime

	def TLS_echo(self, tau_sweep, qubit_index, res_index, flux_index, TLS_index = 0, if_x_pi2 = False, n_avg = 1E3, cd_time_qubit = 20E3, cd_time_TLS = None, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
		TLS echo in 1D.
		pi/2_y - tau - pi_x - tau - pi/2_y

		:param tau_sweep: in clock cycle!
		:param qubit_index:
		:param res_index:
		:param flux_index:
		:param if_x_pi2: False (default), apply pi/2 along y; True, apply pi/2 along x, used for sanity check
		:param TLS_index:
		:param n_avg:
		:param cd_time_qubit:
		:param cd_time_TLS:
		:param tPath:
		:param f_str_datetime:
		:param simulate_flag:
		:param simulation_len:
		:param plot_flag:
		:param machine:
		:return:
			machine
			tau_sweep_abs: in ns. Note this is the spacing between pi pulses
			I
		"""
		if cd_time_TLS is None:
			cd_time_TLS = cd_time_qubit

		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if min(tau_sweep) < 4:
			print("some tau lengths shorter than 4 clock cycles, removed from run")
			tau_sweep = tau_sweep[tau_sweep>3]

		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)
		tau_sweep = tau_sweep.astype(int)

		# fLux pulse baking for SWAP
		swap_length = machine.flux_lines[flux_index].iswap.length[TLS_index]
		swap_amp = machine.flux_lines[flux_index].iswap.level[TLS_index]
		flux_waveform = np.array([swap_amp] * swap_length)

		def baked_swap_waveform(waveform):
			pulse_segments = []  # Stores the baking objects
			# Create the different baked sequences, each one corresponding to a different truncated duration
			with baking(config, padding_method="right") as b:
				b.add_op("flux_pulse", machine.flux_lines[flux_index].name, waveform.tolist())
				b.play("flux_pulse", machine.flux_lines[flux_index].name)
				pulse_segments.append(b)
			return pulse_segments

		square_TLS_swap = baked_swap_waveform(flux_waveform)

		with program() as tls_echo:
			[I, Q, n, I_st, Q_st, n_st] = declare_vars()
			t = declare(int)

			with for_(n, 0, n < n_avg, n + 1):
				with for_(*from_array(t, tau_sweep)):
					with strict_timing_():
						if if_x_pi2==True:
							play("pi2_tls", machine.qubits[qubit_index].name)
						else:
							play("pi2y_tls", machine.qubits[qubit_index].name)
						wait(t, machine.qubits[qubit_index].name)
						play("pi_tls", machine.qubits[qubit_index].name)
						wait(t, machine.qubits[qubit_index].name)
						if if_x_pi2 == True:
							play("pi2_tls", machine.qubits[qubit_index].name)
						else:
							play("pi2y_tls", machine.qubits[qubit_index].name)
					align()
					square_TLS_swap[0].run()
					readout_rotated_macro(machine.resonators[res_index].name,I,Q)
					save(I, I_st)
					save(Q, Q_st)
					align()
					wait(cd_time_qubit * u.ns, machine.resonators[qubit_index].name)
					align()
					square_TLS_swap[0].run(amp_array=[(machine.flux_lines[flux_index].name, -1)])
					wait(cd_time_TLS * u.ns, machine.resonators[qubit_index].name)
					reset_frame(machine.qubits[qubit_index].name) # to avoid phase accumulation
				save(n, n_st)

			with stream_processing():
				I_st.buffer(len(tau_sweep)).average().save("I")
				Q_st.buffer(len(tau_sweep)).average().save("Q")
				n_st.save("iteration")

		#  Open Communication with the QOP  #
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config, log_level = "ERROR")

		if simulate_flag:
			simulation_config = SimulationConfig(duration=simulation_len)  # in clock cycles
			job = qmm.simulate(config, tls_echo, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			qm = qmm.open_qm(config)
			job = qm.execute(tls_echo)
			results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")

			# Live plotting
			if plot_flag == True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [8, 4]
				interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

			while results.is_processing():
				# Fetch results
				I, Q, iteration = results.fetch_all()
				I = u.demod2volts(I, machine.resonators[qubit_index].readout_pulse_length)
				Q = u.demod2volts(Q, machine.resonators[qubit_index].readout_pulse_length)
				sig_amp = np.sqrt(I ** 2 + Q ** 2)
				sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))
				# Progress bar
				progress_counter(iteration, n_avg, start_time=results.get_start_time())
				if plot_flag == True:
					plt.cla()
					plt.title("TLS echo")
					#plt.plot(tau_sweep * 4, sig_amp, "b.")
					plt.plot(tau_sweep * 4, I, "b.")
					plt.xlabel("tau (pulse spacing) [ns]")
					#plt.ylabel(r"$\sqrt{I^2 + Q^2}$ [V]")
					plt.ylabel(r"$I$ [V]")
					plt.pause(0.01)

			# fetch all data after live-updating
			I, Q, iteration = results.fetch_all()
			# Convert I & Q to Volts
			I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
			Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
			sig_amp = np.sqrt(I ** 2 + Q ** 2)
			sig_phase = np.angle(I + 1j * Q)

			# save data
			exp_name = 'echo'
			qubit_name = 'Q' + str(qubit_index + 1) + 'TLS' + str(TLS_index+1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name),
					{"TLS_echo_tau": tau_sweep * 4, "sig_amp": sig_amp, "sig_phase": sig_phase})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, tau_sweep * 4, I

	def TLS_CPMG(self, tau_sweep, qubit_index, res_index, flux_index, TLS_index = 0, if_x_pi2 = False, N_CPMG = 8, n_avg = 1E3, cd_time_qubit = 20E3, cd_time_TLS = None, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
		TLS CPMG8 in 1D.
		pi/2_y - (tau - pi_x - 2tau - pi_x - tau)^4 - pi/2_y

		:param tau_sweep: in clock cycle!
		:param qubit_index:
		:param res_index:
		:param flux_index:
		:param if_x_pi2: False (default), apply pi/2 along y; True, apply pi/2 along x, used for sanity check
		:param TLS_index:
		:param N_CPMG: number of pi pulses
		:param n_avg:
		:param cd_time_qubit:
		:param cd_time_TLS:
		:param tPath:
		:param f_str_datetime:
		:param simulate_flag:
		:param simulation_len:
		:param plot_flag:
		:param machine:
		:return:
			machine
			tau_sweep_abs: in ns. Note this is the spacing between pi pulses
			I
		"""
		if cd_time_TLS is None:
			cd_time_TLS = cd_time_qubit

		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if min(tau_sweep) < 4:
			print("some tau lengths shorter than 4 clock cycles, removed from run")
			tau_sweep = tau_sweep[tau_sweep>3]

		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)
		tau_sweep = tau_sweep.astype(int)

		# fLux pulse baking for SWAP
		swap_length = machine.flux_lines[flux_index].iswap.length[TLS_index]
		swap_amp = machine.flux_lines[flux_index].iswap.level[TLS_index]
		flux_waveform = np.array([swap_amp] * swap_length)

		def baked_swap_waveform(waveform):
			pulse_segments = []  # Stores the baking objects
			# Create the different baked sequences, each one corresponding to a different truncated duration
			with baking(config, padding_method="right") as b:
				b.add_op("flux_pulse", machine.flux_lines[flux_index].name, waveform.tolist())
				b.play("flux_pulse", machine.flux_lines[flux_index].name)
				pulse_segments.append(b)
			return pulse_segments

		square_TLS_swap = baked_swap_waveform(flux_waveform)

		with program() as tls_echo:
			[I, Q, n, I_st, Q_st, n_st] = declare_vars()
			t = declare(int)

			with for_(n, 0, n < n_avg, n + 1):
				with for_(*from_array(t, tau_sweep)):
					with strict_timing_():
						if if_x_pi2 == True:
							play("pi2_tls", machine.qubits[qubit_index].name)
						else:
							play("pi2y_tls", machine.qubits[qubit_index].name)
						wait(t, machine.qubits[qubit_index].name)
						for i in range(N_CPMG - 1):
							play("pi_tls", machine.qubits[qubit_index].name)
							wait(t * 2, machine.qubits[qubit_index].name)
						play("pi_tls", machine.qubits[qubit_index].name)
						wait(t, machine.qubits[qubit_index].name)
						if if_x_pi2 == True:
							play("pi2_tls", machine.qubits[qubit_index].name)
						else:
							play("pi2y_tls", machine.qubits[qubit_index].name)
					align()
					square_TLS_swap[0].run()
					readout_rotated_macro(machine.resonators[res_index].name,I,Q)
					save(I, I_st)
					save(Q, Q_st)
					align()
					wait(cd_time_qubit * u.ns, machine.resonators[qubit_index].name)
					align()
					square_TLS_swap[0].run(amp_array=[(machine.flux_lines[flux_index].name, -1)])
					wait(cd_time_TLS * u.ns, machine.resonators[qubit_index].name)
					reset_frame(machine.qubits[qubit_index].name) # to avoid phase accumulation
				save(n, n_st)

			with stream_processing():
				I_st.buffer(len(tau_sweep)).average().save("I")
				Q_st.buffer(len(tau_sweep)).average().save("Q")
				n_st.save("iteration")

		#  Open Communication with the QOP  #
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config, log_level = "ERROR")

		if simulate_flag:
			simulation_config = SimulationConfig(duration=simulation_len)  # in clock cycles
			job = qmm.simulate(config, tls_echo, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			qm = qmm.open_qm(config)
			job = qm.execute(tls_echo)
			results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")

			# Live plotting
			if plot_flag == True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [8, 4]
				interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

			while results.is_processing():
				# Fetch results
				I, Q, iteration = results.fetch_all()
				I = u.demod2volts(I, machine.resonators[qubit_index].readout_pulse_length)
				Q = u.demod2volts(Q, machine.resonators[qubit_index].readout_pulse_length)
				sig_amp = np.sqrt(I ** 2 + Q ** 2)
				sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))
				# Progress bar
				progress_counter(iteration, n_avg, start_time=results.get_start_time())
				if plot_flag == True:
					plt.cla()
					plt.title(f"TLS CPMG{N_CPMG}")
					#plt.plot(tau_sweep * 4, sig_amp, "b.")
					plt.plot(tau_sweep * 4, I, "b.")
					plt.xlabel("tau (half pulse spacing) [ns]")
					#plt.ylabel(r"$\sqrt{I^2 + Q^2}$ [V]")
					plt.ylabel(r"$I$ [V]")
					plt.pause(0.01)

			# fetch all data after live-updating
			I, Q, iteration = results.fetch_all()
			# Convert I & Q to Volts
			I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
			Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
			sig_amp = np.sqrt(I ** 2 + Q ** 2)
			sig_phase = np.angle(I + 1j * Q)

			# save data
			exp_name = f"CPMG{N_CPMG}"
			qubit_name = 'Q' + str(qubit_index + 1) + 'TLS' + str(TLS_index+1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name),
					{"TLS_CPMG_tau": tau_sweep * 4, "sig_amp": sig_amp, "sig_phase": sig_phase})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, tau_sweep * 4, I

class EH_exp1D:
	"""
	Class for running 1D experiments
	Attributes:

	Methods (useful ones):
		update_tPath: reference to Experiment.update_tPath
		update_str_datetime: reference to Experiment.update_str_datetime
		RR: a class for running readout resonator related experiments
		Rabi: a class for running Rabi sequence based experiments
		T1: a class for running T1 sequence based experiments
		SWAP: a class for running SWAP sequence based experiments
		Ramsey: a class for running Ramsey sequence based experiments
		DD: a class for running Dynamical Decoupling sequence based experiments
	"""
	def __init__(self,ref_to_update_tPath, ref_to_update_str_datetime, ref_to_octave_calibration):
		self.update_tPath = ref_to_update_tPath
		self.update_str_datetime = ref_to_update_str_datetime
		self.RR = EH_RR(ref_to_update_tPath,ref_to_update_str_datetime)
		self.Rabi = EH_Rabi(ref_to_update_tPath,ref_to_update_str_datetime,ref_to_octave_calibration)
		self.SWAP = EH_SWAP(ref_to_update_tPath, ref_to_update_str_datetime, ref_to_octave_calibration)
		self.DD = EH_DD(ref_to_update_tPath,ref_to_update_str_datetime)
		self.T1 = EH_T1(ref_to_update_tPath,ref_to_update_str_datetime)
		self.Ramsey = EH_Ramsey(ref_to_update_tPath, ref_to_update_str_datetime)

