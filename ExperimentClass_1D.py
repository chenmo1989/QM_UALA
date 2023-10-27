"""
This file contains useful python functions meant to simplify the Jupyter notebook.
ExperimentHandle.exp1D
written by Mo Chen in Oct. 2023
"""
from qm.qua import *
from qm.QuantumMachinesManager import QuantumMachinesManager
from qm import SimulationConfig, LoopbackInterface
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

	def time_of_flight(self, qubit_index, res_index, flux_index, n_avg, cd_time, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000):
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

	def rr_freq(self, res_freq_sweep, qubit_index, res_index, flux_index, n_avg, cd_time, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True):
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
		:param tPath: target path/folder for saving the data. Default is today.
		:param f_str_datetime: datetime string for saving the data. Default is now.
		:param simulate_flag: True-run simulation; False (default)-run experiment.
		:param simulation_len: Length of the sequence to simulate. In clock cycles (4ns).
		:param plot_flag: True (default) plot the experiment. False, do not plot.
		Return:
			machine
			res_freq_sweep
			sig_amp
		"""

		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

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
			savemat(os.path.join(tPath, file_name), {"RR_freq": res_freq_sweep, "sig_amp": sig_amp, "sig_phase": sig_phase})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, res_freq_sweep, sig_amp

class EH_Rabi:
	"""
	class in ExperimentHandle, for Rabi sequence related 1D experiments
	Methods:
		update_tPath
		update_str_datetime
		qubit_freq(self, qubit_freq_sweep, qubit_index, res_index, flux_index, n_avg, cd_time, ff_amp = 1.0, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000)
	"""
	def __init__(self, ref_to_update_tPath, ref_to_update_str_datetime):
		self.update_tPath = ref_to_update_tPath
		self.update_str_datetime = ref_to_update_str_datetime

	def qubit_freq(self, qubit_freq_sweep, qubit_index, res_index, flux_index, pi_amp_rel = 1.0, ff_amp = 0.0, n_avg = 1E3, cd_time = 10E3, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True):
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
		Return:
			machine
			qubit_freq_sweep
			sig_amp
		"""
		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

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
			exp_name = 'Q_freq'
			qubit_name = 'Q' + str(qubit_index + 1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name), {"Q_freq": qubit_freq_sweep, "sig_amp": sig_amp, "sig_phase": sig_phase})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, qubit_freq_sweep, sig_amp

	def rabi_length(self, rabi_duration_sweep, qubit_index, res_index, flux_index, pi_amp_rel = 1.0, n_avg = 1E3, cd_time = 10E3, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True):
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
		Return:
			machine
			rabi_duration_sweep
			sig_amp
		"""
		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if min(rabi_duration_sweep) < 4:
			print("some rabi lengths shorter than 4 clock cycles, removed from run")
			rabi_duration_sweep = rabi_duration_sweep[rabi_duration_sweep>3]

		machine = QuAM("quam_state.json")
		config = build_config(machine)
		rabi_duration_sweep = rabi_duration_sweep.astype(int)

		with program() as time_rabi:
			[I, Q, n, I_st, Q_st, n_st] = declare_vars()
			t = declare(int)

			with for_(n, 0, n < n_avg, n + 1):
				with for_(*from_array(t, rabi_duration_sweep)):
					play("pi" * amp(pi_amp_rel), machine.qubits[qubit_index].name, duration=t)
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
			simulation_config = SimulationConfig(duration=1000)  # in clock cycles
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
			exp_name = 'Q_time_rabi'
			qubit_name = 'Q' + str(qubit_index + 1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name),
					{"Q_rabi_duration": rabi_duration_sweep, "sig_amp": sig_amp, "sig_phase": sig_phase})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, rabi_duration_sweep, sig_amp

	def rabi_amp(self, rabi_amp_sweep_rel, qubit_index, res_index, flux_index, n_avg = 1E3, cd_time = 10E3, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True):
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
		Return:
			machine
			rabi_amp_sweep_abs
			sig_amp
		"""
		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		machine = QuAM("quam_state.json")
		config = build_config(machine)

		if max(abs(rabi_amp_sweep_rel)) > 2:
			print("some relative amps > 2, removed from experiment run")
			rabi_amp_sweep_rel = rabi_amp_sweep_rel[abs(rabi_amp_sweep_rel) < 2]
		rabi_amp_sweep_abs = rabi_amp_sweep_rel * machine.qubits[qubit_index].pi_amp[0] # actual rabi amplitude

		with program() as power_rabi:
			[I, Q, n, I_st, Q_st, n_st] = declare_vars()
			a = declare(fixed)

			with for_(n, 0, n < n_avg, n + 1):
				with for_(*from_array(a, rabi_amp_sweep_rel)):
					play("pi" * amp(a), machine.qubits[qubit_index].name)
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
			exp_name = 'Q_power_rabi'
			qubit_name = 'Q' + str(qubit_index + 1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name),
					{"Q_rabi_amplitude": rabi_amp_sweep_abs, "sig_amp": sig_amp, "sig_phase": sig_phase})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return machine, rabi_amp_sweep_abs, sig_amp


	def rabi_amplitude(self):
		pass

class EH_Ramsey:
	def __init__(self, ref_to_update_tPath, ref_to_update_str_datetime):
		self.update_tPath = ref_to_update_tPath
		self.update_str_datetime = ref_to_update_str_datetime

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
	def __init__(self,ref_to_update_tPath, ref_to_update_str_datetime):
		self.update_tPath = ref_to_update_tPath
		self.update_str_datetime = ref_to_update_str_datetime
		self.RR = EH_RR(ref_to_update_tPath,ref_to_update_str_datetime)
		self.Rabi = EH_Rabi(ref_to_update_tPath,ref_to_update_str_datetime)
		self.Echo = EH_Echo(ref_to_update_tPath,ref_to_update_str_datetime)
		self.CPMG = EH_CPMG(ref_to_update_tPath,ref_to_update_str_datetime)

