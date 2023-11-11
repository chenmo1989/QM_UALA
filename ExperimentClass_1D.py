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
from qm import SimulationConfig
from qualang_tools.bakery import baking
from qualang_tools.units import unit
from qm import generate_qua_script
from qm.octave import QmOctaveConfig
from set_octave import ElementsSettings, octave_settings
from quam import QuAM
from scipy.io import savemat
from scipy.io import loadmat
from scipy.optimize import curve_fit
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

	def time_of_flight(self, qubit_index, res_index, flux_index, n_avg, cd_time, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, machine = None):
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

	def rr_freq(self, res_freq_sweep, qubit_index, res_index, flux_index, n_avg, cd_time, readout_state = 'g', tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
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
			# detrend removes the linear increase of phase
			sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))

			# save data
			exp_name = 'RR_freq'
			qubit_name = 'Q' + str(res_index+1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name), {"RR_freq": res_freq_sweep, "sig_amp": sig_amp, "sig_phase": sig_phase, "readout_state": readout_state})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, res_freq_sweep, sig_amp

	def rr_switch_delay(self, rr_switch_delay_sweep, qubit_index, res_index, flux_index, n_avg, cd_time, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
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

	def rr_switch_buffer(self, rr_switch_buffer_sweep, qubit_index, res_index, flux_index, n_avg, cd_time, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
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
					plt.xlabel("Frequency [MHz]")
					plt.ylabel(r"$\sqrt{I^2 + Q^2}$ [V]")

			# fetch all data after live-updating
			I, Q, iteration = results.fetch_all()
			# Convert I & Q to Volts
			I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
			Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
			sig_amp = np.sqrt(I**2 + Q**2)
			# detrend removes the linear increase of phase
			sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))

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
			# detrend removes the linear increase of phase
			sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))

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
			# detrend removes the linear increase of phase
			sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))

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
		 amplitude = machine.qubits[qubit_index].pi_amp_tls[TLS_index] * 0.25 V

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

		# TLS pi pulse
		TLS_pi_length = machine.qubits[qubit_index].pi_length_tls[TLS_index]
		TLS_pi_amp = machine.qubits[qubit_index].pi_amp_tls[TLS_index] # note this is relative amp!
		TLS_pi_rel = TLS_pi_amp * pi_amp_rel
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
					play('cw' * amp(TLS_pi_rel), machine.qubits[qubit_index].name, duration = TLS_pi_length * u.ns)
					align()
					square_TLS_swap[0].run()
					align()
					readout_avg_macro(machine.resonators[res_index].name,I,Q)
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
			# detrend removes the linear increase of phase
			sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))

			# save data
			exp_name = 'freq'
			qubit_name = 'Q' + str(qubit_index + 1) + 'TLS' + str(TLS_index+1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name), {"TLS_freq": TLS_freq_sweep, "sig_amp": sig_amp, "sig_phase": sig_phase})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, TLS_freq_sweep, sig_amp

	def TLS_rabi_length(self, rabi_duration_sweep, qubit_index, res_index, flux_index, TLS_index = 0, pi_amp_rel = 1.0, n_avg = 1E3, cd_time_qubit = 10E3, cd_time_TLS = None, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
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

		if min(rabi_duration_sweep) < 4:
			print("some rabi lengths shorter than 4 clock cycles, removed from run")
			rabi_duration_sweep = rabi_duration_sweep[rabi_duration_sweep>3]
		rabi_duration_sweep = rabi_duration_sweep.astype(int)

		# TLS pi pulse
		TLS_pi_amp = machine.qubits[qubit_index].pi_amp_tls[TLS_index] # note this is relative amp!
		TLS_pi_rel = TLS_pi_amp * pi_amp_rel
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
					play('cw' * amp(TLS_pi_rel), machine.qubits[qubit_index].name, duration = t) # clock cycles
					align()
					square_TLS_swap[0].run()
					align()
					readout_avg_macro(machine.resonators[res_index].name,I,Q)
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
					plt.plot(rabi_duration_sweep * 4, np.sqrt(I**2 +  Q**2), ".")
					plt.xlabel("tau [ns]")
					plt.ylabel(r"$\sqrt{I^2 + Q^2}$ [V]")

			# fetch all data after live-updating
			I, Q, iteration = results.fetch_all()
			# Convert I & Q to Volts
			I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
			Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
			sig_amp = np.sqrt(I**2 + Q**2)
			# detrend removes the linear increase of phase
			sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))

			# save data
			exp_name = 'TLS_time_rabi'
			qubit_name = 'Q' + str(qubit_index + 1) + 'TLS' + str(TLS_index+1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name), {"TLS_rabi_duration": rabi_duration_sweep * 4, "sig_amp": sig_amp, "sig_phase": sig_phase})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, rabi_duration_sweep * 4, sig_amp

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

		if len(machine.qubits[qubit_index].pi_length) > 1:
			ef_pi_length = machine.qubits[qubit_index].pi_length[1]
		if len(machine.qubits[qubit_index].pi_amp) > 1:
			pi_amp_rel_ef = machine.qubits[qubit_index].pi_amp[1]/machine.qubits[qubit_index].pi_amp[0] * pi_amp_rel_ef

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
					play('pi'*amp(pi_amp_rel_ef), machine.qubits[qubit_index].name, duration = ef_pi_length * u.ns)
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
			# detrend removes the linear increase of phase
			sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))

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

		if len(machine.qubits[qubit_index].pi_amp) > 1:
			pi_amp_rel_ef = machine.qubits[qubit_index].pi_amp[1]/machine.qubits[qubit_index].pi_amp[0] * pi_amp_rel_ef

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
					play('pi'*amp(pi_amp_rel_ef), machine.qubits[qubit_index].name, duration=t)
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
			# detrend removes the linear increase of phase
			sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))

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
		rabi_amp_sweep_rel = rabi_amp_sweep_abs / machine.qubits[qubit_index].pi_amp[0]
		ef_if = machine.qubits[qubit_index].f_01 - machine.qubits[qubit_index].anharmonicity - machine.qubits[qubit_index].lo
		if len(machine.qubits[qubit_index].pi_length) > 1:
			ef_pi_length = machine.qubits[qubit_index].pi_length[1]

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
					play('pi' * amp(a), machine.qubits[qubit_index].name, duration = ef_pi_length * u.ns)
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
			# detrend removes the linear increase of phase
			sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))

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

		if len(machine.qubits[qubit_index].pi_amp) > 1:
			pi_amp_rel_ef = machine.qubits[qubit_index].pi_amp[1] / machine.qubits[qubit_index].pi_amp[0] * pi_amp_rel_ef

		with program() as time_rabi_ef_thermal:
			[I, Q, n, I_st, Q_st, n_st] = declare_vars()
			t = declare(int)

			with for_(n, 0, n < n_avg, n + 1):
				with for_(*from_array(t, rabi_duration_sweep)):
					update_frequency(machine.qubits[qubit_index].name, ef_if)
					play('pi'*amp(pi_amp_rel_ef), machine.qubits[qubit_index].name, duration=t)
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
			# detrend removes the linear increase of phase
			sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))

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

	def TLS_T1(self, tau_sweep_abs, qubit_index, res_index, flux_index, TLS_index=0, n_avg = 1E3, cd_time = 10E3, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):

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
					readout_avg_macro(machine.resonators[res_index].name,I,Q)
					save(I, I_st)
					save(Q, Q_st)
					align()
					wait(50)
					square_TLS_swap[0].run(amp_array=[(machine.flux_lines[flux_index].name, -1)])
					wait(50)
					square_TLS_swap[0].run(amp_array=[(machine.flux_lines[flux_index].name, -1)])
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
					plt.title("TLS T1")
					plt.plot(tau_sweep_abs, sig_amp, "b.")
					plt.xlabel("tau [ns]")
					plt.ylabel(r"$\sqrt{I^2 + Q^2}$ [V]")
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

		return machine, tau_sweep_abs, sig_amp

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
			# detrend removes the linear increase of phase
			sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))

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

		ff_amp_rel = machine.flux_lines[flux_index].iswap.level[TLS_index] / machine.flux_lines[flux_index].flux_pulse_amp

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
					play("const" * amp(ff_amp_rel), machine.flux_lines[flux_index].name, duration=t)
					align()
					readout_avg_macro(machine.resonators[res_index].name,I,Q)
					align()
					wait(50)
					play("const" * amp(-ff_amp_rel), machine.flux_lines[flux_index].name, duration=t)
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
			# detrend removes the linear increase of phase
			sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))

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
			# detrend removes the linear increase of phase
			sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))

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

	def ramsey_virtual_rotation(self, ramsey_duration_sweep, qubit_index, res_index, flux_index, pi_amp_rel = 1.0, n_avg = 1E3, detuning = 1E6, cd_time = 10E3, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
		qubit Ramsey in 1D with virtual Z rotation
		sequence given by pi/2 - wait - pi/2 fro various wait times
		the frame of the last pi/2 pulse is rotated rather than using qubit detuning


		:param ramsey_duration_sweep: in clock cycles!
		:param qubit_index:
		:param res_index:
		:param flux_index:
		:param pi_amp_rel:
		:param n_avg:
		:param detuning: effective detuning that is transformed into a virtual z rotation
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

		with program() as ramsey_vr:
			[I, Q, n, I_st, Q_st, n_st] = declare_vars()
			t = declare(int)
			phi = declare(fixed) # for virtual z rotation

			with for_(n, 0, n < n_avg, n + 1):
				with for_(*from_array(t, ramsey_duration_sweep)):
					assign(phi, Cast.mul_fixed_by_int(detuning * 1e-9, 4 * t))
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
					plt.title("Ramsey with detuning = %i Hz" %detuning)
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
			# detrend removes the linear increase of phase
			sig_phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))

			# save data
			exp_name = 'ramsey_vr'
			qubit_name = 'Q' + str(qubit_index + 1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name),
					{"Q_ramsey_duration": ramsey_duration_sweep * 4, "sig_amp": sig_amp, "sig_phase": sig_phase})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, ramsey_duration_sweep * 4, sig_amp

class EH_Echo:
	def __init__(self, ref_to_update_tPath, ref_to_update_str_datetime):
		self.update_tPath = ref_to_update_tPath
		self.update_str_datetime = ref_to_update_str_datetime

class EH_CPMG:
	def __init__(self, ref_to_update_tPath, ref_to_update_str_datetime):
		self.update_tPath = ref_to_update_tPath
		self.update_str_datetime = ref_to_update_str_datetime


class EH_exp1D:
	"""
	Class for running 1D experiments
	Attributes:

	Methods (useful ones):
		update_tPath: reference to Experiment.update_tPath
		update_str_datetime: reference to Experiment.update_str_datetime
		RR: a class for running readout resonator related experiments
		Rabi: a class for running Rabi sequence based experiments
		Echo: a class for running Echo sequence based experiments
		CPMG: a class for running CPMG sequence based experiments
	"""
	def __init__(self,ref_to_update_tPath, ref_to_update_str_datetime, ref_to_octave_calibration):
		self.update_tPath = ref_to_update_tPath
		self.update_str_datetime = ref_to_update_str_datetime
		self.RR = EH_RR(ref_to_update_tPath,ref_to_update_str_datetime)
		self.Rabi = EH_Rabi(ref_to_update_tPath,ref_to_update_str_datetime,ref_to_octave_calibration)
		self.SWAP = EH_SWAP(ref_to_update_tPath, ref_to_update_str_datetime, ref_to_octave_calibration)
		self.Echo = EH_Echo(ref_to_update_tPath,ref_to_update_str_datetime)
		self.CPMG = EH_CPMG(ref_to_update_tPath,ref_to_update_str_datetime)
		self.T1 = EH_T1(ref_to_update_tPath,ref_to_update_str_datetime)
		self.Ramsey = EH_Ramsey(ref_to_update_tPath, ref_to_update_str_datetime)

