"""
This file contains useful python functions meant to simplify the Jupyter notebook.
ExperimentHandle.exp2D
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

class EH_1D:
	"""
	class for some 1D experiments used for 2D scans
	"""
	def res_freq(self, res_freq_sweep, qubit_index, res_index, flux_index, n_avg, cd_time, machine = None, simulate_flag = False, simulation_len = 1000, fig = None):
		"""
		resonator spectroscopy experiment
		this experiment find the resonance frequency by localizing the minima in pulsed transmission signal.
		this 1D experiment is not automatically saved
		Args:
		:param res_freq_sweep: 1D array for resonator frequency sweep
		:param qubit_index:
		:param res_index:
		:param flux_index:
		:param n_avg: repetition of expeirment
		:param cd_time: cooldown time between subsequent experiments
		:param machine:
		:param simulate_flag: True-run simulation; False (default)-run experiment.
		:param simulation_len: Length of the sequence to simulate. In clock cycles (4ns).
		:param fig: None (default). Fig reference, mainly to have the ability to interupt the experiment.
		Return:
			machine
			I
			Q
		"""
		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)

		res_lo = machine.resonators[res_index].lo
		if res_lo < 2E9:
			print("LO < 2GHz, abort")
			return None
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
			if fig is not None:
				interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

			while results.is_processing():
				# Fetch results
				I, Q, iteration = results.fetch_all()
				I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
				Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
				# progress bar
				#progress_counter(iteration, n_avg, start_time=results.get_start_time())

			# fetch all data after live-updating
			I, Q, iteration = results.fetch_all()
			# Convert I & Q to Volts
			I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
			Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)

			return machine, I, Q

	def qubit_freq(self, qubit_freq_sweep, qubit_index, res_index, flux_index, pi_amp_rel = 1.0, ff_amp = 0.0, n_avg = 1E3, cd_time = 10E3, machine = None, simulate_flag = False, simulation_len = 1000, fig = None):
		"""
		qubit spectroscopy experiment in 1D (equivalent of ESR for spin qubit)
		this 1D experiment is not automatically saved
		Args:
		:param qubit_freq_sweep: 1D array of qubit frequency sweep
		:param qubit_index:
		:param res_index:
		:param flux_index:
		:param n_avg: repetition of the experiments
		:param cd_time: cooldown time between subsequent experiments
		:param ff_amp: fast flux amplitude the overlaps with the Rabi pulse. The ff pulse is 40ns longer than Rabi pulse, and share the same center time.
		:param machine:
		:param simulate_flag: True-run simulation; False (default)-run experiment.
		:param simulation_len: Length of the sequence to simulate. In clock cycles (4ns).
		:param fig: None (default). Fig reference, mainly to have the ability to interupt the experiment.
		Return:
			machine
			I
			Q
		"""
		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)

		qubit_lo = machine.qubits[qubit_index].lo
		if qubit_lo < 2E9:
			print("LO < 2GHz, abort")
			return None

		qubit_if_sweep = qubit_freq_sweep - qubit_lo
		qubit_if_sweep = np.round(qubit_if_sweep)
		ff_duration = machine.qubits[qubit_index].pi_length[0] + 40

		if np.max(abs(qubit_if_sweep)) > 350E6: # check if parameters are within hardware limit
			print("qubit if range > 350MHz")
			return None

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
			if fig is not None:
				interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
			while results.is_processing():
				time.sleep(0.1)
				# Fetch results
				# I, Q, iteration = results.fetch_all()
				# I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
				# Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
				# progress bar
				# progress_counter(iteration, n_avg, start_time=results.get_start_time())

			# fetch all data after live-updating
			I, Q, iteration = results.fetch_all()
			# Convert I & Q to Volts
			I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
			Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)

			return machine, I, Q

	def res_freq_analysis(self,res_freq_sweep, I, Q):
		"""
		analysis for the 1D resonator spectroscopy experiment, and find the resonance frequency by looking for the minima
		Args:
			res_freq_sweep: resonator frequency array
			I: corresponding signal I array
			Q: corresponding signal Q array
		Return:
			 res_freq_sweep[idx]: the resonance frequency
		"""
		sig_amp = np.sqrt(I ** 2 + Q ** 2)
		idx = np.argmin(sig_amp)  # find minimum
		return res_freq_sweep[idx]

class EH_RR:
	"""
	class in ExperimentHandle, for Readout Resonator (RR) related 2D experiments
	Methods:
		update_tPath
		update_str_datetime
		rr_vs_dc_flux(self, res_freq_sweep, dc_flux_sweep, qubit_index, res_index, flux_index, n_avg, cd_time, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000)
	"""
	def __init__(self, ref_to_update_tPath,ref_to_update_str_datetime):
		self.update_tPath = ref_to_update_tPath
		self.update_str_datetime = ref_to_update_str_datetime

	def rr_vs_dc_flux(self, res_freq_sweep, dc_flux_sweep, qubit_index, res_index, flux_index, n_avg, cd_time, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000, plot_flag = True, machine = None):
		"""
		resonator spectroscopy vs dc flux 2D experiment
		this is supposed to be some of the first qubit characterization experiment. Purpose is to get an initial estimate
		of the qubit-resonator system parameters. I choose to use a Jaynes-Cummings model for this.

		This 2D sweep is assumed to be square--same frequency sweep range for all dc flux values.

		Args:
		:param res_freq_sweep: 1D array for the resonator frequency sweep
		:param dc_flux_sweep: 1D array for the dc flux sweep
		:param qubit_index:
		:param res_index:
		:param flux_index:
		:param n_avg: repetition of the experiments
		:param cd_time: cooldown time between subsequent experiments
		:param tPath: target path/folder for saving the data. Default is today.
		:param f_str_datetime: datetime string for saving the data. Default is now.
		:param simulate_flag: True-run simulation; False (default)-run experiment.
		:param simulation_len: Length of the sequence to simulate. In clock cycles (4ns).
		:param plot_flag: True (default) plot the experiment. False, do not plot.
		:param machine: None (default), will read from quam_state.json
		Return:
			machine
			res_freq_sweep
			dc_flux_sweep
			sig_amp
		"""
		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		# 2D scan, RR frequency vs DC flux
		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)
		res_lo = machine.resonators[res_index].lo
		res_if_sweep = res_freq_sweep - res_lo
		res_if_sweep = np.round(res_if_sweep)

		if np.max(abs(res_if_sweep)) > 400E6: # check if parameters are within hardware limit
			print("res if range > 400MHz")
			return None, None, None

		# QDAC communication through Labber
		client = Labber.connectToServer('localhost')  # get list of instruments
		QDevil = client.connectToInstrument('QDevil QDAC', dict(interface='Serial', address='3'))

		with program() as resonator_spec_2D:
			[I, Q, n, I_st, Q_st, n_st] = declare_vars()
			m = declare(int)  # DC sweep index
			df = declare(int)  # Resonator frequency

			with for_(m, 0, m < len(dc_flux_sweep) + 1, m + 1):
				# The QUA program #
				pause()
				with for_(n, 0, n < n_avg, n + 1):
					with for_(*from_array(df, res_if_sweep)):
						# Update the resonator frequency
						update_frequency(machine.resonators[res_index].name, df)
						# Measure the resonator
						readout_avg_macro(machine.resonators[res_index].name,I,Q)
						# Wait for the resonator to cooldown
						wait(cd_time * u.ns, machine.resonators[res_index].name)
						# Save data to the stream processing
						save(I, I_st)
						save(Q, Q_st)
				save(m, n_st)

			with stream_processing():
				I_st.buffer(len(res_freq_sweep)).buffer(n_avg).map(FUNCTIONS.average()).save_all("I")
				Q_st.buffer(len(res_freq_sweep)).buffer(n_avg).map(FUNCTIONS.average()).save_all("Q")
				n_st.save_all("iteration")

		#####################################
		#  Open Communication with the QOP  #
		#####################################
		qmm = QuantumMachinesManager(machine.network.qop_ip, port='9510', octave=octave_config, log_level = "ERROR")

		if simulate_flag: # simulation is useful to see the sequence, especially the timing (clock cycle vs ns)
			simulation_config = SimulationConfig(duration=simulation_len)
			job = qmm.simulate(config, resonator_spec_2D, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			qm = qmm.open_qm(config)
			job = qm.execute(resonator_spec_2D)
			# Creates results handles to fetch the data
			res_handles = job.result_handles
			I_handle = res_handles.get("I")
			Q_handle = res_handles.get("Q")
			n_handle = res_handles.get("iteration")

			# Initialize empty vectors to store the global 'I' & 'Q' results
			I_tot = []
			Q_tot = []
			# Live plotting
			if plot_flag == True:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [8, 4]
				interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

			for m in range(len(dc_flux_sweep)):
				# set QDAC voltage
				dc_flux = dc_flux_sweep[m].tolist()
				QDevil.setValue("CH0" + str(flux_index+1) + " Voltage", dc_flux)
				machine.flux_lines[flux_index].dc_voltage = dc_flux

				# Resume the QUA program
				job.resume()
				# Wait until the program reaches the 'pause' statement again, indicating that the QUA program is done
				wait_until_job_is_paused(job)

				# Wait until the data of this run is processed by the stream processing
				I_handle.wait_for_values(m + 1)
				Q_handle.wait_for_values(m + 1)
				n_handle.wait_for_values(m + 1)

				# Fetch the data from the last OPX run corresponding to the current LO frequency
				I = np.concatenate(I_handle.fetch(m)["value"])
				Q = np.concatenate(Q_handle.fetch(m)["value"])
				iteration = n_handle.fetch(m)["value"][0]
				# Update the list of global results
				I_tot.append(I)
				Q_tot.append(Q)
				# Progress bar
				progress_counter(iteration, len(dc_flux_sweep))

				# Convert results into Volts
				sigs = u.demod2volts(I + 1j * Q, machine.resonators[res_index].readout_pulse_length)
				sig_amp = np.abs(sigs)  # Amplitude
				sig_phase = np.angle(sigs)  # Phase
				# Plot results
				if plot_flag == True:
					plt.suptitle("RR spectroscopy")
					plt.title("Resonator spectroscopy")
					plt.plot((res_freq_sweep) / u.MHz, sig_amp, ".")
					plt.xlabel("Frequency [MHz]")
					plt.ylabel(r"$\sqrt{I^2 + Q^2}$ [V]")

			# Interrupt the FPGA program
			job.halt()

			I = np.concatenate(I_tot)
			Q = np.concatenate(Q_tot)
			sigs = u.demod2volts(I + 1j * Q, machine.resonators[res_index].readout_pulse_length)
			sig_amp = np.abs(sigs)  # Amplitude
			sig_phase = np.angle(sigs)  # Phase

			# save data
			exp_name = 'res_vs_dc_flux'
			qubit_name = 'Q' + str(qubit_index+1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name),
					{"RR_freq": res_freq_sweep, "sig_amp": sig_amp, "sig_phase": sig_phase, "dc_flux_sweep": dc_flux_sweep})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

		client.close()
		return machine, res_freq_sweep, dc_flux_sweep, sig_amp

	def rr_pulse_optimize(self, res_duration_sweep_abs, res_amp_sweep, qubit_index, res_index, flux_index, n_avg=1E3, cd_time=20E3, tPath=None,
							f_str_datetime=None, simulate_flag=False, simulation_len=1000, plot_flag=True, machine=None):
		"""
		characterize QND during readout pulse, find the optimal readout amp and duration
		pi pulse -- variable readout pulse -- readout
		Args:
			res_duration_sweep_abs ():
			res_amp_sweep ():
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
			res_amp_sweep: 1D
			res_duration_sweep_abs: 1D
			sig_amp: 2D
		"""
		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		if machine is None:
			machine = QuAM("quam_state.json")

		res_amp_sweep_rel = res_amp_sweep / 0.25 # 0.25 is the amplitude of "cw" pulse/"const_wf"
		res_duration_sweep_cc = res_duration_sweep_abs // 4  # in clock cycles
		res_duration_sweep_cc = np.unique(res_duration_sweep_cc)
		res_duration_sweep = res_duration_sweep_cc.astype(int)  # clock cycles
		res_duration_sweep_abs = res_duration_sweep * 4  # time in ns

		config = build_config(machine)

		with program() as rr_pulse_optimize:
			[I,Q,n,I_st,Q_st,n_st] = declare_vars()
			t = declare(int)
			da = declare(fixed)

			with for_(n, 0, n < n_avg, n + 1):
				with for_(*from_array(t, res_duration_sweep)):
					with for_(*from_array(da, res_amp_sweep_rel)):
						play("pi", machine.qubits[qubit_index].name)
						align()
						play("cw" * amp(da), machine.resonators[res_index].name, duration=t)
						align()
						readout_avg_macro(machine.resonators[res_index].name, I, Q)
						save(I, I_st)
						save(Q, Q_st)
						wait(cd_time * u.ns, machine.resonators[res_index].name)
				save(n, n_st)

			with stream_processing():
				# for the progress counter
				n_st.save("iteration")
				I_st.buffer(len(res_amp_sweep_rel)).buffer(len(res_duration_sweep)).average().save("I")
				Q_st.buffer(len(res_amp_sweep_rel)).buffer(len(res_duration_sweep)).average().save("Q")

		#####################################
		#  Open Communication with the QOP  #
		#####################################
		qmm = QuantumMachinesManager(machine.network.qop_ip, port='9510', octave=octave_config, log_level="ERROR")

		if simulate_flag:
			simulation_config = SimulationConfig(duration=simulation_len)
			job = qmm.simulate(config, rr_pulse_optimize, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			qm = qmm.open_qm(config)
			job = qm.execute(rr_pulse_optimize)
			results = fetching_tool(job, ["I", "Q", "iteration"], mode="live")

			if plot_flag:
				fig = plt.figure()
				plt.rcParams['figure.figsize'] = [8, 4]
				interrupt_on_close(fig, job)

			while results.is_processing():
				I, Q, iteration = results.fetch_all()
				progress_counter(iteration, n_avg, start_time=results.get_start_time())
				time.sleep(0.1)

			I, Q, _ = results.fetch_all()
			I = u.demod2volts(I, machine.resonators[qubit_index].readout_pulse_length)
			Q = u.demod2volts(Q, machine.resonators[qubit_index].readout_pulse_length)
			sig_amp = np.sqrt(I ** 2 + Q ** 2)
			sig_phase = np.angle(I + 1j * Q)

			# save data
			exp_name = 'res_pulse_optimize'
			qubit_name = 'Q' + str(qubit_index + 1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name),
					{"res_amp_sweep": res_amp_sweep, "sig_amp": sig_amp, "sig_phase": sig_phase,
					 "res_duration_sweep": res_duration_sweep_abs})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			if plot_flag:
				plt.cla()
				plt.pcolor(res_amp_sweep, res_duration_sweep_abs, sig_amp, cmap="seismic")
				plt.colorbar()
				plt.xlabel("res amp (V)")
				plt.ylabel("res pulse duration (ns)")

			return machine, res_amp_sweep, res_duration_sweep_abs, sig_amp

class EH_Rabi:
	"""
	class in ExperimentHandle, for qubit Rabi related 2D experiments
	Methods:
		update_tPath
		update_str_datetime
		qubit_freq_vs_dc_flux(self, poly_param, ham_param, dc_flux_sweep, qubit_index, res_index, flux_index, n_avg, cd_time, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000)
	"""

	def __init__(self, ref_to_update_tPath, ref_to_update_str_datetime,ref_to_local_exp1D,ref_to_octave_calibration):
		self.update_tPath = ref_to_update_tPath
		self.update_str_datetime = ref_to_update_str_datetime
		self.exp1D = ref_to_local_exp1D
		self.octave_calibration = ref_to_octave_calibration

	def qubit_freq_vs_dc_flux(self, dc_flux_sweep, qubit_index, res_index, flux_index, n_avg, cd_time, pi_amp_rel = 1.0, ham_param = None,
					  poly_param = None, tPath=None, f_str_datetime=None, simulate_flag=False, simulation_len=1000, plot_flag=True, machine = None):
		"""
		qubit spectroscopy vs dc flux 2D experiment
		go back and forth between 1D resonator spectroscopy and 1D qubit spectroscopy.
		end result should be two 2D experiments, one for RR, one for qubit.
		Requires the ham_param for RR, and poly_param for qubit
		This sweep is not squared!!

		Args:
		:param poly_param: for qubit polynomial fit
		:param ham_param: fot resonator hamiltonian fit
		:param dc_flux_sweep: 1D array for the dc flux sweep
		:param qubit_index:
		:param res_index:
		:param flux_index:
		:param n_avg: repetition of the experiments
		:param cd_time: cooldown time between subsequent experiments
		:param tPath: target path/folder for saving the data. Default is today.
		:param f_str_datetime: datetime string for saving the data. Default is now.
		:param simulate_flag: True-run simulation; False (default)-run experiment.
		:param simulation_len: Length of the sequence to simulate. In clock cycles (4ns).
		:param plot_flag: True (default) plot the experiment. False, do not plot.
		:param machine: None (default), will read from quam_state.json
		Return:
			machine
			qubit_freq_sweep
			dc_flux_sweep
			sig_amp_qubit
		"""
		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		# set up variables
		if machine is None:
			machine = QuAM("quam_state.json") # this "machine" object is going to be changed by a lot, do not rely on it too much
		config = build_config(machine)

		if poly_param is None:
			poly_param = machine.qubits[qubit_index].DC_tuning_curve
		if ham_param is None:
			ham_param = machine.resonators[res_index].tuning_curve

		qubit_freq_est = np.polyval(poly_param, dc_flux_sweep) * 1E6  # in Hz
		qubit_lo = machine.qubits[qubit_index].lo
		if qubit_lo < 2E9:
			print("LO < 2GHz, abort")
			return None

		qubit_if_sweep = qubit_freq_est - qubit_lo
		qubit_if_sweep = np.round(qubit_if_sweep)
		if np.max(abs(qubit_if_sweep)) > 350E6:  # check if parameters are within hardware limit
			print("qubit if for est. freq > 350MHz")
			return None
		if np.min(abs(qubit_if_sweep)) < 20E6:  # check if parameters are within hardware limit
			print("qubit if for est. freq < 20MHz")
			return None

		# Initialize empty vectors to store the global 'I' & 'Q' results
		I_qubit_tot = []
		Q_qubit_tot = []
		qubit_freq_sweep_tot = []
		I_res_tot = []
		Q_res_tot = []
		res_freq_sweep_tot = []
		res_freq_tot = []

		# QDAC communication through Labber
		client = Labber.connectToServer('localhost')  # get list of instruments
		QDevil = client.connectToInstrument('QDevil QDAC', dict(interface='Serial', address='3'))

		if plot_flag == True:
			fig = plt.figure()
			plt.rcParams['figure.figsize'] = [8, 4]

		start_time = time.time()

		# 2D scan, RR frequency vs DC flux
		for dc_index, dc_value in enumerate(dc_flux_sweep): # sweep over all dc fluxes
			# Set dc flux value
			QDevil.setValue("CH0" + str(flux_index + 1) + " Voltage", dc_value)
			# 1D RR experiment
			res_freq_est = ham([dc_value.tolist()], ham_param[0], ham_param[1], ham_param[2], ham_param[3], ham_param[4], ham_param[5], output_flag = 1) * 1E6 # to Hz
			res_freq_sweep = int(res_freq_est[0]) + np.arange(-5E6, 5E6 + 1, 0.05E6)

			if plot_flag == True:
				machine, I_tmp, Q_tmp = self.exp1D.res_freq(res_freq_sweep, qubit_index, res_index, flux_index, n_avg, cd_time, machine=machine,
						simulate_flag=simulate_flag, simulation_len=simulation_len, fig = fig)
			else:
				machine, I_tmp, Q_tmp = self.exp1D.res_freq(res_freq_sweep, qubit_index, res_index, flux_index, n_avg, cd_time, machine=machine,
						simulate_flag=simulate_flag, simulation_len=simulation_len)

			res_freq_tmp = self.exp1D.res_freq_analysis(res_freq_sweep, I_tmp, Q_tmp)
			# save 1D RR data
			I_res_tot.append(I_tmp)
			Q_res_tot.append(Q_tmp)
			res_freq_tot.append(res_freq_tmp)
			res_freq_sweep_tot.append(res_freq_sweep)
			# set resonator freq for qubit spectroscopy
			machine.resonators[res_index].f_readout = int(res_freq_tmp.tolist()) + 0E6

			# 1D qubit experiment
			progress_counter(dc_index, len(dc_flux_sweep), start_time=start_time)
			qubit_freq_est = np.polyval(poly_param,dc_value) * 1E6 # in Hz
			qubit_freq_sweep = int(qubit_freq_est) + np.arange(-125E6, 125E6 + 1, 2E6)
			machine, I_tmp, Q_tmp = self.exp1D.qubit_freq(qubit_freq_sweep, qubit_index, res_index, flux_index, pi_amp_rel=pi_amp_rel, ff_amp=0.0,
					   n_avg=n_avg, cd_time=cd_time, machine=machine, simulate_flag=simulate_flag, simulation_len=simulation_len, fig = fig)
			I_qubit_tot.append(I_tmp)
			Q_qubit_tot.append(Q_tmp)
			qubit_freq_sweep_tot.append(qubit_freq_sweep)

		# save
		I_qubit = np.concatenate(I_qubit_tot)
		Q_qubit = np.concatenate(Q_qubit_tot)
		qubit_freq_sweep = np.concatenate(qubit_freq_sweep_tot)
		I_res = np.concatenate(I_res_tot)
		Q_res = np.concatenate(Q_res_tot)
		#res_freq = np.concatenate(res_freq_tot)

		sigs_qubit = u.demod2volts(I_qubit + 1j * Q_qubit, machine.resonators[res_index].readout_pulse_length)
		sig_amp_qubit = np.abs(sigs_qubit)  # Amplitude
		sig_phase_qubit = np.angle(sigs_qubit)  # Phase
		sigs_res = u.demod2volts(I_res + 1j * Q_res, machine.resonators[res_index].readout_pulse_length)
		sig_amp_res = np.abs(sigs_res)  # Amplitude
		sig_phase_res = np.angle(sigs_res)  # Phase
		# save data
		exp_name = 'qubit_freq_vs_dc_flux'
		qubit_name = 'Q' + str(qubit_index + 1)
		f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
		file_name = f_str + '.mat'
		json_name = f_str + '_state.json'
		savemat(os.path.join(tPath, file_name),
				{"RR_freq": res_freq_sweep, "sig_amp_res": sig_amp_res, "sig_phase_res": sig_phase_res, "dc_flux_sweep": dc_flux_sweep,
				 "Q_freq": qubit_freq_sweep, "sig_amp_qubit": sig_amp_qubit, "sig_phase_qubit": sig_phase_qubit})
		machine._save(os.path.join(tPath, json_name), flat_data=False)

		# plot
		qubit_freq_sweep_plt = qubit_freq_sweep.reshape(np.size(dc_flux_sweep),
													np.size(qubit_freq_sweep) // np.size(dc_flux_sweep))
		sig_amp_qubit_plt = sig_amp_qubit.reshape(np.size(dc_flux_sweep),
												  np.size(sig_amp_qubit) // np.size(dc_flux_sweep))
		_, dc_flux_sweep_plt = np.meshgrid(qubit_freq_sweep_plt[0, :], dc_flux_sweep)
		plt.pcolormesh(dc_flux_sweep_plt, qubit_freq_sweep_plt / u.MHz, sig_amp_qubit_plt, cmap="seismic")
		plt.title("Qubit tuning curve")
		plt.xlabel("DC flux level [V]")
		plt.ylabel("Frequency [MHz]")
		plt.colorbar()

		return machine, qubit_freq_sweep, dc_flux_sweep, sig_amp_qubit

	def qubit_freq_vs_fast_flux_slow(self, ff_sweep_abs, qubit_if_sweep, qubit_index, res_index, flux_index, n_avg, cd_time, pi_amp_rel = 1.0, ff_to_dc_ratio = None,
					  poly_param = None, tPath=None, f_str_datetime=None, simulate_flag=False, simulation_len=1000, plot_flag=True, machine = None):
		"""
		2D qubit spectroscopy experiment vs fast flux
		use this to sweep by fast flux. This should be a coarse sweep only!
		this is an assembly of 1D qubit spectroscopy (from subroutines). Each 1D scan is called in a python loop, therefore slow.

		Args:
		:param ff_sweep_abs: absolute voltage value of fast flux sweep. [-0.5V, 0.5V]
		:param qubit_if_sweep: sweep range around the estimated qubit frequency
		:param qubit_index:
		:param res_index:
		:param flux_index:
		:param n_avg:
		:param cd_time:
		:param pi_amp_rel: 1.0 (default). Relative knob to tune the pi pulse amplitude
		:param ff_to_dc_ratio: None (default). If not None, then tuning curve comes from dc flux tuning curve. find qubit freq est around the sweet spot, using this dc/ff ratio.
		:param poly_param:
		:param tPath:
		:param f_str_datetime:
		:param simulate_flag:
		:param simulation_len:
		:param plot_flag:
		:param machine: None (default), will read from quam_state.json.
		Return:
			machine
			qubit_freq_sweep
			ff_sweep_abs
			sig_amp_qubit
		"""
		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		# set up variables
		if machine is None:
			machine = QuAM("quam_state.json") # this "machine" object is going to be changed by a lot, do not rely on it too much
		config = build_config(machine)

		ff_sweep = ff_sweep_abs / machine.flux_lines[flux_index].flux_pulse_amp
		if ff_to_dc_ratio is None:
			if poly_param is None:
				poly_param = machine.qubits[qubit_index].AC_tuning_curve
			qubit_freq_est_sweep = np.polyval(poly_param, ff_sweep_abs) * 1E6 # Hz
		else:
			if poly_param is None:
				poly_param = machine.qubits[qubit_index].DC_tuning_curve
			qubit_freq_est_sweep = np.polyval(poly_param, (ff_to_dc_ratio * ff_sweep_abs) + machine.flux_lines[flux_index].max_frequency_point) * 1E6 # Hz
		qubit_freq_est_sweep = np.round(qubit_freq_est_sweep)

		qubit_lo = machine.qubits[qubit_index].lo

		# Initialize empty vectors to store the global 'I' & 'Q' results
		I_qubit_tot = []
		Q_qubit_tot = []
		qubit_freq_sweep_tot = []

		if plot_flag == True:
			fig = plt.figure()
			plt.rcParams['figure.figsize'] = [8, 4]

		start_time = time.time()
		# 2D scan, RR frequency vs fast flux (ff)
		for ff_index, ff_value in enumerate(ff_sweep):  # sweep over all fast fluxes
			progress_counter(ff_index, len(ff_sweep), start_time=start_time)
			qubit_freq_est = qubit_freq_est_sweep[ff_index]

			if qubit_lo - (qubit_freq_est - max(qubit_if_sweep)) > -50E6: # need to decrease LO
				qubit_lo = qubit_freq_est + max(qubit_if_sweep) - 350E6
				machine.qubits[qubit_index].lo = int(qubit_lo.tolist()) + 0E6
				machine.qubits[qubit_index].f_01 = int(qubit_freq_est.tolist()) + 0E6
				self.octave_calibration(qubit_index,res_index,flux_index,machine = machine, qubit_only = True)

			if qubit_lo - (qubit_freq_est + max(qubit_if_sweep)) < -350E6: # need to increase LO
				qubit_lo = qubit_freq_est + max(qubit_if_sweep) - 350E6
				machine.qubits[qubit_index].lo = int(qubit_lo.tolist()) + 0E6
				machine.qubits[qubit_index].f_01 = int(qubit_freq_est.tolist()) + 0E6
				self.octave_calibration(qubit_index,res_index,flux_index,machine = machine, qubit_only = True)
			qubit_freq_sweep = qubit_freq_est + qubit_if_sweep

			if plot_flag == True:
				machine, I_tmp, Q_tmp = self.exp1D.qubit_freq(qubit_freq_sweep, qubit_index, res_index, flux_index,
															  pi_amp_rel=pi_amp_rel, ff_amp=ff_value,
															  n_avg=n_avg, cd_time=cd_time, machine=machine,
															  simulate_flag=simulate_flag, simulation_len=simulation_len,
															  fig=fig)
			else:
				machine, I_tmp, Q_tmp = self.exp1D.qubit_freq(qubit_freq_sweep, qubit_index, res_index, flux_index,
															  pi_amp_rel=pi_amp_rel, ff_amp=ff_value,
															  n_avg=n_avg, cd_time=cd_time, machine=machine,
															  simulate_flag=simulate_flag,
															  simulation_len=simulation_len)
			I_qubit_tot.append(I_tmp)
			Q_qubit_tot.append(Q_tmp)
			qubit_freq_sweep_tot.append(qubit_freq_sweep)

		# save
		I_qubit = np.concatenate(I_qubit_tot)
		Q_qubit = np.concatenate(Q_qubit_tot)
		qubit_freq_sweep = np.concatenate(qubit_freq_sweep_tot)
		sigs_qubit = I_qubit + 1j * Q_qubit
		sig_amp_qubit = np.abs(sigs_qubit)  # Amplitude
		sig_phase_qubit = np.angle(sigs_qubit)  # Phase
		# save data
		exp_name = 'qubit_freq_vs_fast_flux'
		qubit_name = 'Q' + str(qubit_index + 1)
		f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
		file_name = f_str + '.mat'
		json_name = f_str + '_state.json'
		savemat(os.path.join(tPath, file_name),
				{"fast_flux_sweep": ff_sweep_abs,
				 "Q_freq": qubit_freq_sweep, "sig_amp_qubit": sig_amp_qubit, "sig_phase_qubit": sig_phase_qubit})
		machine._save(os.path.join(tPath, json_name), flat_data=False)

		# plot
		qubit_freq_sweep_plt = qubit_freq_sweep.reshape(np.size(ff_sweep),
														np.size(qubit_freq_sweep) // np.size(ff_sweep))
		sig_amp_qubit_plt = sig_amp_qubit.reshape(np.size(ff_sweep),
												  np.size(sig_amp_qubit) // np.size(ff_sweep))
		_, ff_sweep_plt = np.meshgrid(qubit_freq_sweep_plt[0, :], ff_sweep_abs)
		plt.pcolormesh(ff_sweep_plt, qubit_freq_sweep_plt / u.MHz, sig_amp_qubit_plt, cmap="seismic")
		plt.title("Qubit tuning curve")
		plt.xlabel("fast flux level [V]")
		plt.ylabel("Frequency [MHz]")
		plt.colorbar()

		return machine, qubit_freq_sweep, ff_sweep_abs, sig_amp_qubit

	def qubit_freq_fast_flux_subroutine(self, ff_sweep_rel, qubit_freq_est_sweep, qubit_if_sweep, qubit_index, res_index, flux_index,
										pi_amp_rel = 1.0, n_avg = 1E3, cd_time = 10E3, machine = None, simulate_flag = False, simulation_len = 1000, fig = None):
		"""
		subroutine for 2D qubit freq spectroscopy vs fast flux
		input should have been checked: no need to change LO.
		Args:
			ff_sweep_rel (): relative voltage value of fast flux sweep. absolute value is ff_sweep_rel * machine.flux_lines[flux_index].flux_pulse_amp
			qubit_freq_est_sweep (): estimated qubit frequencies to be swept. Each freq correspond to a fast flux value above.
			qubit_if_sweep (): sweep range around the estimated qubit frequency
			qubit_index ():
			res_index ():
			flux_index ():
			pi_amp_rel (): 1.0 (default). Relative knob to tune the pi pulse amplitude
			n_avg ():
			cd_time ():
			machine ():
			simulate_flag ():
			simulation_len ():
			fig (): None (default). If a fig is given, it gives us the ability to interrupt the experimental run.

		Returns:
			machine
			qubit_freq_sweep_tot
			I_tot
			Q_tot
			ff_sweep_rel * machine.flux_lines[flux_index].flux_pulse_amp
		"""
		if machine is None:
			machine = QuAM("quam_state.json")
		config = build_config(machine)

		qubit_lo = machine.qubits[qubit_index].lo
		qubit_if_est_sweep = np.round(qubit_freq_est_sweep - qubit_lo)
		qubit_if_est_sweep = qubit_if_est_sweep.astype(int)

		if max(abs(qubit_if_est_sweep)) + max(qubit_if_sweep) > 400E6:
			print("max IF freq > 400 MHz, abort. Check the input!")
			return None

		ff_duration = machine.qubits[qubit_index].pi_length[0] + 40

		# construct qubit freq_sweep_tot
		qubit_freq_sweep_tot = []
		for qubit_freq_i in qubit_freq_est_sweep:
			qubit_freq_sweep_tot.append(qubit_freq_i + qubit_if_sweep)

		with program() as qubit_freq_2D_prog:
			[I,Q,n,I_st,Q_st,n_st] = declare_vars()
			df = declare(int)
			q_freq_est = declare(int) # estimated qubit freq
			da = declare(fixed) # fast flux amplitude

			with for_(n, 0, n < n_avg, n+1):
				with for_each_((da, q_freq_est), (ff_sweep_rel, qubit_if_est_sweep)):
					with for_(*from_array(df,qubit_if_sweep)):
						update_frequency(machine.qubits[qubit_index].name, df + q_freq_est)
						play("const" * amp(da), machine.flux_lines[flux_index].name, duration=ff_duration * u.ns)
						wait(5, machine.qubits[qubit_index].name)
						play('pi'*amp(pi_amp_rel), machine.qubits[qubit_index].name)
						align(machine.qubits[qubit_index].name, machine.flux_lines[flux_index].name,
							  machine.resonators[res_index].name)
						#wait(4)  # avoid overlap between Z and RO
						readout_avg_macro(machine.resonators[res_index].name,I,Q)
						align()
						wait(50)
						# eliminate charge accumulation
						play("const" * amp(-1 * da), machine.flux_lines[flux_index].name, duration=ff_duration * u.ns)
						wait(cd_time * u.ns, machine.resonators[res_index].name)
						save(I, I_st)
						save(Q, Q_st)
				save(n, n_st)
			with stream_processing():
				I_st.buffer(len(qubit_if_sweep)).buffer(len(ff_sweep_rel)).average().save("I")
				Q_st.buffer(len(qubit_if_sweep)).buffer(len(ff_sweep_rel)).average().save("Q")
				n_st.save("iteration")

		#####################################
		#  Open Communication with the QOP  #
		#####################################
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config, log_level = "ERROR")
		# Simulate or execute #
		if simulate_flag: # simulation is useful to see the sequence, especially the timing (clock cycle vs ns)
			simulation_config = SimulationConfig(duration=simulation_len)
			job = qmm.simulate(config, qubit_freq_2D_prog, simulation_config)
			job.get_simulated_samples().con1.plot()
		else:
			qm = qmm.open_qm(config)
			job = qm.execute(qubit_freq_2D_prog)
			# Get results from QUA program
			results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
			# Live plotting
		    #%matplotlib qt
			if fig is not None:
				interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
			while results.is_processing():
				time.sleep(0.1)
				# Fetch results
				I, Q, iteration = results.fetch_all()
				# I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
				# Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
				# progress bar
				progress_counter(iteration, n_avg, start_time=results.get_start_time())

			# fetch all data after live-updating
			I, Q, iteration = results.fetch_all()
			# Convert I & Q to Volts
			I_tot = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
			Q_tot = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)

			return machine, qubit_freq_sweep_tot, I_tot, Q_tot, ff_sweep_rel * machine.flux_lines[flux_index].flux_pulse_amp

	def qubit_freq_vs_fast_flux(self, qubit_freq_sweep, qubit_if_sweep, qubit_index, res_index, flux_index, n_avg, cd_time, pi_amp_rel = 1.0,
					  poly_param = None, tPath=None, f_str_datetime=None, simulate_flag=False, simulation_len=1000, plot_flag=True, machine = None):
		"""
		2D qubit spectroscopy experiment vs fast flux
		with a good tuning curve, this method is used to run fine scans of the qubit spectroscopy, for identification of avoided crossings
		consists of block-wise 2D scans using the qubit_freq_fast_flux_subroutine. Each block consists of 4 calls to the subroutine, with 2 LO frequencies.

		Args:
			qubit_freq_sweep (): desired qubit frequency sweep range for the 2D scan. The corresponding fast flux value will be calculated based on a 4th order polynomial tuning curve.
			qubit_if_sweep (): sweep range around the estimated qubit frequency
			qubit_index ():
			res_index ():
			flux_index ():
			n_avg ():
			cd_time ():
			pi_amp_rel (): 1.0 (default). Relative knob to tune the pi pulse amplitude
			poly_param (): None (default). qubit freq. tuning curve. Must be 4th order polynomial!
			tPath ():
			f_str_datetime ():
			simulate_flag ():
			simulation_len ():
			plot_flag ():
			machine (): None (default), will read from quam_state.json

		Returns:
			machine
			qubit_freq_sweep
			ff_sweep_abs
			sig_amp_qubit
		"""
		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		# set up variables
		if machine is None:
			machine = QuAM("quam_state.json") # this "machine" object is going to be changed by a lot, do not rely on it too much
		config = build_config(machine)

		if poly_param is None:
			poly_param = np.array(machine.qubits[qubit_index].AC_tuning_curve[:])

		# sort qubit_freq_sweep from small to large, for later use of searchsorted
		qubit_freq_sweep = np.sort(np.floor(qubit_freq_sweep)) # floor, to avoid larger than max freq situation

		# find the corresponding fast flux values for qubit_freq_sweep
		ff_sweep_abs = []
		for freq_tmp in qubit_freq_sweep:
			sol_tmp = np.roots(poly_param - np.array([0, 0, 0, 0, freq_tmp/1E6]))
			if np.sum(np.isreal(sol_tmp))==4: # four real solutions, take the smaller positive one
				sol_tmp = min(np.real(sol_tmp[sol_tmp>0]))
			else: # two real and two complex solutions, take the positive real value
				sol_tmp = max(np.real(sol_tmp[np.isreal(sol_tmp)]))
			ff_sweep_abs.append(sol_tmp)
		ff_sweep_abs = np.array(ff_sweep_abs)
		if max(abs(ff_sweep_abs)) > 0.5:
			print("-------------------------------------some fast flux > 0.5V, removed from experiment run")
			qubit_freq_sweep = qubit_freq_sweep[abs(ff_sweep_abs) < 0.5]
			ff_sweep_abs = ff_sweep_abs[abs(ff_sweep_abs) < 0.5]

		ff_sweep_rel = ff_sweep_abs / machine.flux_lines[flux_index].flux_pulse_amp

		if plot_flag == True:
			fig = plt.figure()
			plt.rcParams['figure.figsize'] = [8, 4]

		# Initialize empty vectors to store the global 'I' & 'Q' results
		I_tot = []
		Q_tot = []
		qubit_freq_sweep_tot = []
		ff_sweep_tot = []

		start_time = time.time()

		# divide and conquer!
		# use +- (100 - 300) MHz IF freq range
		# each period is 800 MHz, with two LOs, separated by 200 MHz
		qubit_freq_sweep_head = max(qubit_freq_sweep) # the start of the current analysis
		while qubit_freq_sweep_head + 1 > min(qubit_freq_sweep): # full period (with 2x LOs).
			# find the index of frequencies in qubit_freq_sweep for this sweep, with IF freq > 0
			# LO1
			freq_seg_index_pos_IF_LO1 = [np.searchsorted(qubit_freq_sweep, qubit_freq_sweep_head - 200E6, side='right'),
										 np.searchsorted(
											 qubit_freq_sweep, qubit_freq_sweep_head,
											 side='right')]  # -1 s.t. head will be included. sweep range is IF = (100, 300] MHz
			freq_seg_index_neg_IF_LO1 = [np.searchsorted(qubit_freq_sweep, qubit_freq_sweep_head - 600E6, side='right'),
										 np.searchsorted(
											 qubit_freq_sweep, qubit_freq_sweep_head - 400E6,
											 side='right')]  # -1 s.t. head will be included. sweep range is IF = (-300, -100] MHz
			# LO2
			freq_seg_index_pos_IF_LO2 = [np.searchsorted(qubit_freq_sweep, qubit_freq_sweep_head - 400E6, side='right'),
										 np.searchsorted(
											 qubit_freq_sweep, qubit_freq_sweep_head - 200E6,
											 side='right')]  # -1 s.t. head will be included. sweep range is IF = (100, 300] MHz
			freq_seg_index_neg_IF_LO2 = [np.searchsorted(qubit_freq_sweep, qubit_freq_sweep_head - 800E6, side='right'),
										 np.searchsorted(
											 qubit_freq_sweep, qubit_freq_sweep_head - 600E6,
											 side='right')]  # -1 s.t. head will be included. sweep range is IF = (-300, -100] MHz

			# LO1
			qubit_lo = qubit_freq_sweep_head - 300E6
			machine.qubits[qubit_index].lo = int(qubit_lo.tolist()) + 0E6
			machine.qubits[qubit_index].f_01 = int(qubit_lo.tolist()) + 200E6  # calibrate in the center of the +ive sweep range
			self.octave_calibration(qubit_index, res_index, flux_index, machine=machine, qubit_only = True)
			# qubit freq vs fast flux, sweep over +ive and -ive IF freq
			for freq_seg_index in [freq_seg_index_pos_IF_LO1,freq_seg_index_neg_IF_LO1]:
				ff_sweep_rel_seg = ff_sweep_rel[freq_seg_index[0]:freq_seg_index[1]]
				qubit_freq_sweep_seg = qubit_freq_sweep[freq_seg_index[0]:freq_seg_index[1]]

				if len(ff_sweep_rel_seg) > 0: # still need to sweep
					if plot_flag == True:
						machine, qubit_freq_sweep_tmp, I_tmp, Q_tmp, ff_sweep_tmp = self.qubit_freq_fast_flux_subroutine(
							ff_sweep_rel_seg, qubit_freq_sweep_seg, qubit_if_sweep,
							qubit_index, res_index, flux_index, pi_amp_rel=pi_amp_rel, n_avg=n_avg, cd_time=cd_time, machine=machine,
							fig=fig)
					else:
						machine, qubit_freq_sweep_tmp, I_tmp, Q_tmp, ff_sweep_tmp = self.qubit_freq_fast_flux_subroutine(
							ff_sweep_rel_seg, qubit_freq_sweep_seg, qubit_if_sweep,
							qubit_index, res_index, flux_index, pi_amp_rel=pi_amp_rel, n_avg=n_avg, cd_time=cd_time, machine=machine)

					I_tot.append(I_tmp)
					Q_tot.append(Q_tmp)
					qubit_freq_sweep_tot.append(qubit_freq_sweep_tmp)
					ff_sweep_tot.append(ff_sweep_tmp)
				else: # no need to scan. For the last period
					pass

			# LO2
			qubit_lo = qubit_freq_sweep_head - 500E6
			machine.qubits[qubit_index].lo = int(qubit_lo.tolist()) + 0E6
			machine.qubits[qubit_index].f_01 = machine.qubits[
												   qubit_index].lo + 200E6  # calibrate in the center of the +ive sweep range
			self.octave_calibration(qubit_index, res_index, flux_index, machine=machine, qubit_only = True)
			# qubit freq vs fast flux, sweep over +ive and -ive IF freq
			for freq_seg_index in [freq_seg_index_pos_IF_LO2, freq_seg_index_neg_IF_LO2]:
				ff_sweep_rel_seg = ff_sweep_rel[freq_seg_index[0]:freq_seg_index[1]]
				qubit_freq_sweep_seg = qubit_freq_sweep[freq_seg_index[0]:freq_seg_index[1]]

				if len(ff_sweep_rel_seg) > 0:  # still need to sweep
					if plot_flag == True:
						machine, qubit_freq_sweep_tmp, I_tmp, Q_tmp, ff_sweep_tmp = self.qubit_freq_fast_flux_subroutine(
							ff_sweep_rel_seg, qubit_freq_sweep_seg, qubit_if_sweep,
							qubit_index, res_index, flux_index, pi_amp_rel=pi_amp_rel, n_avg=n_avg, cd_time=cd_time,
							machine=machine,
							fig=fig)
					else:
						machine, qubit_freq_sweep_tmp, I_tmp, Q_tmp, ff_sweep_tmp = self.qubit_freq_fast_flux_subroutine(
							ff_sweep_rel_seg, qubit_freq_sweep_seg, qubit_if_sweep,
							qubit_index, res_index, flux_index, pi_amp_rel=pi_amp_rel, n_avg=n_avg, cd_time=cd_time,
							machine=machine)

					I_tot.append(I_tmp)
					Q_tot.append(Q_tmp)
					qubit_freq_sweep_tot.append(qubit_freq_sweep_tmp)
					ff_sweep_tot.append(ff_sweep_tmp)
				else: # no need to scan. For the last period
					pass

			qubit_freq_sweep_head -= 800E6 # move to the next full period

		# save
		I_qubit = np.concatenate(I_tot)
		Q_qubit = np.concatenate(Q_tot)
		qubit_freq_sweep = np.concatenate(qubit_freq_sweep_tot)
		ff_sweep_abs = np.concatenate(ff_sweep_tot)
		sigs_qubit = I_qubit + 1j * Q_qubit
		sig_amp_qubit = np.abs(sigs_qubit)  # Amplitude
		sig_phase_qubit = np.angle(sigs_qubit)  # Phase

		# sort according to fast flux sweep
		qubit_freq_sweep = qubit_freq_sweep.reshape(np.size(ff_sweep_abs),
														np.size(qubit_freq_sweep) // np.size(ff_sweep_abs))
		sig_amp_qubit = sig_amp_qubit.reshape(np.size(ff_sweep_abs),
												  np.size(sig_amp_qubit) // np.size(ff_sweep_abs))

		sort_index = np.argsort(ff_sweep_abs)
		qubit_freq_sweep = qubit_freq_sweep[sort_index,:]
		sig_amp_qubit = sig_amp_qubit[sort_index,:]
		ff_sweep_abs = ff_sweep_abs[sort_index]
		_, ff_sweep_plt = np.meshgrid(qubit_freq_sweep[0, :], ff_sweep_abs)

		# plot
		if plot_flag == True:
			plt.pcolormesh(ff_sweep_plt, qubit_freq_sweep / u.MHz, sig_amp_qubit, cmap="seismic")
			plt.title("Qubit tuning curve")
			plt.xlabel("fast flux level [V]")
			plt.ylabel("Frequency [MHz]")
			plt.colorbar()

		# save data
		exp_name = 'qubit_freq_vs_fast_flux'
		qubit_name = 'Q' + str(qubit_index + 1)
		f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
		file_name = f_str + '.mat'
		json_name = f_str + '_state.json'
		savemat(os.path.join(tPath, file_name),
				{"fast_flux_sweep": ff_sweep_abs,
				 "Q_freq": qubit_freq_sweep, "sig_amp_qubit": sig_amp_qubit, "sig_phase_qubit": sig_phase_qubit})
		machine._save(os.path.join(tPath, json_name), flat_data=False)

		return machine, qubit_freq_sweep, ff_sweep_abs, sig_amp_qubit

	def qubit_freq_vs_fast_flux_obsolete(self, ff_sweep_abs, qubit_if_sweep, qubit_index, res_index, flux_index, n_avg, cd_time,
								pi_amp_rel=1.0, ff_to_dc_ratio=None,
								poly_param=None, tPath=None, f_str_datetime=None, simulate_flag=False,
								simulation_len=1000, plot_flag=True):
		"""
		working, but not working well. For temporary storage, before I make sure "qubit_freq_vs_fast_flux" is fully functional
		"""

		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		# set up variables
		machine = QuAM(
			"quam_state.json")  # this "machine" object is going to be changed by a lot, do not rely on it too much
		config = build_config(machine)

		if poly_param is None:
			poly_param = machine.qubits[qubit_index].AC_tuning_curve

		ff_sweep = ff_sweep_abs / machine.flux_lines[flux_index].flux_pulse_amp
		if ff_to_dc_ratio is None:
			qubit_freq_est_sweep = np.polyval(poly_param, ff_sweep_abs) * 1E6  # Hz
		else:
			qubit_freq_est_sweep = np.polyval(poly_param, (ff_to_dc_ratio * ff_sweep_abs) + machine.flux_lines[
				flux_index].max_frequency_point) * 1E6  # Hz
		qubit_freq_est_sweep = np.round(qubit_freq_est_sweep)

		# divide and conquer!
		freq_est_seg_index = [0]
		for freq_est_index, freq_est_value in enumerate(qubit_freq_est_sweep):
			if freq_est_value < qubit_freq_est_sweep[freq_est_seg_index[-1]] - 500E6:
				freq_est_seg_index.append(freq_est_index)
		freq_est_seg_index.append(len(qubit_freq_est_sweep))

		if plot_flag == True:
			fig = plt.figure()
			plt.rcParams['figure.figsize'] = [8, 4]

		# Initialize empty vectors to store the global 'I' & 'Q' results
		I_tot = []
		Q_tot = []
		qubit_freq_sweep_tot = []
		ff_sweep_tot = []

		start_time = time.time()

		for freq_seg_index, freq_est_value in enumerate(freq_est_seg_index[1:]):
			print(f"seg {freq_est_seg_index[freq_seg_index]:.0f} / {freq_est_seg_index[-1]:.0f} ...")
			index_seg_lower = freq_est_seg_index[freq_seg_index]
			index_seg_upper = freq_est_value

			ff_sweep_rel_seg = ff_sweep[index_seg_lower:index_seg_upper]
			qubit_freq_est_sweep_seg = qubit_freq_est_sweep[index_seg_lower:index_seg_upper]

			qubit_lo = max(qubit_freq_est_sweep_seg) + max(qubit_if_sweep) - 350E6
			machine.qubits[qubit_index].lo = int(qubit_lo.tolist()) + 0E6
			machine.qubits[qubit_index].f_01 = int(max(qubit_freq_est_sweep_seg).tolist()) + 0E6
			self.octave_calibration(qubit_index, res_index, flux_index, machine=machine)

			if plot_flag == True:
				machine, qubit_freq_sweep_tmp, I_tmp, Q_tmp, ff_sweep_tmp = self.qubit_freq_fast_flux_subroutine(
					ff_sweep_rel_seg, qubit_freq_est_sweep_seg, qubit_if_sweep,
					qubit_index, res_index, flux_index, pi_amp_rel=pi_amp_rel, n_avg=n_avg, cd_time=cd_time, machine=machine,
					fig=fig)
			else:
				machine, qubit_freq_sweep_tmp, I_tmp, Q_tmp, ff_sweep_tmp = self.qubit_freq_fast_flux_subroutine(
					ff_sweep_rel_seg, qubit_freq_est_sweep_seg, qubit_if_sweep,
					qubit_index, res_index, flux_index, pi_amp_rel=pi_amp_rel, n_avg=n_avg, cd_time=cd_time, machine=machine)

			I_tot.append(I_tmp)
			Q_tot.append(Q_tmp)
			qubit_freq_sweep_tot.append(qubit_freq_sweep_tmp)
			ff_sweep_tot.append(ff_sweep_tmp)

		# save
		I_qubit = np.concatenate(I_tot)
		Q_qubit = np.concatenate(Q_tot)
		qubit_freq_sweep = np.concatenate(qubit_freq_sweep_tot)
		ff_sweep_abs = np.concatenate(ff_sweep_tot)
		sigs_qubit = I_qubit + 1j * Q_qubit
		sig_amp_qubit = np.abs(sigs_qubit)  # Amplitude
		sig_phase_qubit = np.angle(sigs_qubit)  # Phase
		# save data
		exp_name = 'qubit_freq_vs_fast_flux'
		qubit_name = 'Q' + str(qubit_index + 1)
		f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
		file_name = f_str + '.mat'
		json_name = f_str + '_state.json'
		savemat(os.path.join(tPath, file_name),
				{"fast_flux_sweep": ff_sweep_abs,
				 "Q_freq": qubit_freq_sweep, "sig_amp_qubit": sig_amp_qubit, "sig_phase_qubit": sig_phase_qubit})
		machine._save(os.path.join(tPath, json_name), flat_data=False)

		# plot
		qubit_freq_sweep_plt = qubit_freq_sweep.reshape(np.size(ff_sweep_abs),
														np.size(qubit_freq_sweep) // np.size(ff_sweep_abs))
		sig_amp_qubit_plt = sig_amp_qubit.reshape(np.size(ff_sweep_abs),
												  np.size(sig_amp_qubit) // np.size(ff_sweep_abs))
		_, ff_sweep_plt = np.meshgrid(qubit_freq_sweep_plt[0, :], ff_sweep_abs)
		plt.pcolormesh(ff_sweep_plt, qubit_freq_sweep_plt / u.MHz, sig_amp_qubit_plt, cmap="seismic")
		plt.title("Qubit tuning curve")
		plt.xlabel("fast flux level [V]")
		plt.ylabel("Frequency [MHz]")
		plt.colorbar()

		return machine, qubit_freq_sweep, ff_sweep_abs, sig_amp_qubit

class EH_SWAP:
	"""
	class in ExperimentHandle, for SWAP related 2D experiments
	Methods:
		update_tPath
		update_str_datetime
	"""

	def __init__(self, ref_to_update_tPath, ref_to_update_str_datetime):
		self.update_tPath = ref_to_update_tPath
		self.update_str_datetime = ref_to_update_str_datetime

	def swap_coarse(self,tau_sweep_abs, ff_sweep_abs, qubit_index, res_index, flux_index, n_avg, cd_time, tPath=None,
					f_str_datetime=None, simulate_flag=False, simulation_len=1000, plot_flag=True, machine = None):
		"""
		runs 2D SWAP spectroscopy experiment
		Note time resolution is 4ns!

		Args:
			tau_sweep_abs (): interaction time sweep, in ns. Will be regulated to multiples of 4ns, starting from 16ns
			ff_sweep_abs (): fast flux sweep, in V
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

		ff_sweep_rel = ff_sweep_abs / machine.flux_lines[flux_index].flux_pulse_amp

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
					with for_(*from_array(da, ff_sweep_rel)):
						play("pi", machine.qubits[qubit_index].name)
						align()
						play("const" * amp(da), machine.flux_lines[flux_index].name, duration=t)
						align()
						readout_avg_macro(machine.resonators[res_index].name,I,Q)
						align()
						wait(50)
						play("const" * amp(-da), machine.flux_lines[flux_index].name, duration=t)
						save(I, I_st)
						save(Q, Q_st)
						wait(cd_time * u.ns, machine.resonators[res_index].name)
				save(n, n_st)

			with stream_processing():
				# for the progress counter
				n_st.save("iteration")
				I_st.buffer(len(ff_sweep_rel)).buffer(len(tau_sweep)).average().save("I")
				Q_st.buffer(len(ff_sweep_rel)).buffer(len(tau_sweep)).average().save("Q")

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
			sig_phase = np.angle(I + 1j * Q)

			# save data
			exp_name = 'SWAP'
			qubit_name = 'Q' + str(qubit_index + 1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name),
					{"ff_sweep": ff_sweep_abs, "sig_amp": sig_amp, "sig_phase": sig_phase,
					 "tau_sweep": tau_sweep_abs})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			if plot_flag:
				plt.cla()
				plt.pcolor(ff_sweep_abs, tau_sweep_abs, sig_amp, cmap="seismic")
				plt.colorbar()
				plt.xlabel("fast flux amp (V)")
				plt.ylabel("interaction time (ns)")

		return machine, ff_sweep_abs, tau_sweep_abs, sig_amp

	def swap_fine(self,tau_sweep_abs, ff_sweep_abs, qubit_index, res_index, flux_index, n_avg, cd_time, tPath=None,
					f_str_datetime=None, simulate_flag=False, simulation_len=1000, plot_flag=True, machine = None):
		"""
		runs 2D SWAP spectroscopy
		allows 1ns time resolution, and start at t < 16ns
		Args:
			tau_sweep_abs (): interaction time sweep, in ns.
			ff_sweep_abs (): fast flux sweep in V
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
			ff_sweep_abs: 1D array of fast flux amplitude in V
			tau_sweep_abs: 1D array of tau in ns
			sig_amp.T: such that x is flux, y is time

		"""
		if tPath is None:
			tPath = self.update_tPath()
		if f_str_datetime is None:
			f_str_datetime = self.update_str_datetime()

		ff_sweep_rel = ff_sweep_abs / machine.flux_lines[flux_index].flux_pulse_amp
		tau_sweep = tau_sweep_abs.astype(int)  # clock cycles

		# set up variables
		if machine is None:
			machine = QuAM("quam_state.json") # this "machine" object is going to be changed by a lot, do not rely on it too much
		config = build_config(machine)

		max_pulse_duration = max(tau_sweep_abs)
		max_pulse_duration = int(max_pulse_duration)
		min_pulse_duration = min(tau_sweep_abs)
		min_pulse_duration = int(min_pulse_duration)
		dt_pulse_duration = tau_sweep_abs[2] - tau_sweep_abs[1]
		dt_pulse_duration = int(dt_pulse_duration)

		# fLux pulse waveform generation, 250 ns/points
		flux_waveform = np.array([machine.flux_lines[flux_index].flux_pulse_amp] * max_pulse_duration)

		def baked_ff_waveform(waveform, pulse_duration):
			pulse_segments = []  # Stores the baking objects
			# Create the different baked sequences, each one corresponding to a different truncated duration
			for i in range(0, pulse_duration + 1):
				with baking(config, padding_method="right") as b:
					if i == 0:  # Otherwise, the baking will be empty and will not be created
						wf = [0.0] * 16
					else:
						wf = waveform[:i].tolist()
					b.add_op("flux_pulse", machine.flux_lines[flux_index].name, wf)
					b.play("flux_pulse", machine.flux_lines[flux_index].name)
				# Append the baking object in the list to call it from the QUA program
				pulse_segments.append(b)
			return pulse_segments

		# Baked flux pulse segments
		square_pulse_segments = baked_ff_waveform(flux_waveform, max_pulse_duration)

		with program() as iswap:
			[I, Q, n, I_st, Q_st, n_st] = declare_vars()
			t = declare(int)
			da = declare(fixed)
			segment = declare(int)  # Flux pulse segment

			with for_(n, 0, n < n_avg, n + 1):
				with for_(*from_array(da, ff_sweep_rel)):
					with for_(segment, min_pulse_duration, segment <= max_pulse_duration, segment + dt_pulse_duration):
						play("pi", machine.qubits[qubit_index].name)
						align()
						with switch_(segment):
							for j in range(min_pulse_duration,max_pulse_duration+1,dt_pulse_duration):
								with case_(j):
									square_pulse_segments[j].run(amp_array=[(machine.flux_lines[flux_index].name, da)])
						align()
						readout_avg_macro(machine.resonators[res_index].name,I,Q)
						save(I, I_st)
						save(Q, Q_st)
						align()
						wait(cd_time * u.ns, machine.resonators[res_index].name)
						align()
						with switch_(segment):
							for j in range(min_pulse_duration,max_pulse_duration+1,dt_pulse_duration):
								with case_(j):
									square_pulse_segments[j].run(amp_array=[(machine.flux_lines[flux_index].name, -da)])
						wait(cd_time * u.ns, machine.resonators[res_index].name)
				save(n, n_st)

			with stream_processing():
				# for the progress counter
				n_st.save("iteration")
				I_st.buffer(len(tau_sweep)).buffer(len(ff_sweep_rel)).average().save("I")
				Q_st.buffer(len(tau_sweep)).buffer(len(ff_sweep_rel)).average().save("Q")

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
			sig_phase = np.angle(I + 1j * Q)

			# save data
			exp_name = 'SWAP'
			qubit_name = 'Q' + str(qubit_index + 1)
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name),
					{"ff_sweep": ff_sweep_abs, "sig_amp": sig_amp.T, "sig_phase": sig_phase.T,
					 "tau_sweep": tau_sweep_abs})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			if plot_flag:
				plt.cla()
				plt.pcolor(ff_sweep_abs, tau_sweep_abs, sig_amp.T, cmap="seismic")
				plt.colorbar()
				plt.xlabel("fast flux amp (V)")
				plt.ylabel("interaction time (ns)")

		return machine, ff_sweep_abs, tau_sweep_abs, sig_amp.T


class EH_exp2D:
	"""
	Class for running 2D experiments
	Attributes:

	Methods (useful ones):
		update_tPath: reference to Experiment.update_tPath
		update_str_datetime: reference to Experiment.update_str_datetime
		RR: a class for running readout resonator related experiments
	"""
	def __init__(self,ref_to_update_tPath, ref_to_update_str_datetime, ref_to_octave_calibration):
		self.update_tPath = ref_to_update_tPath
		self.update_str_datetime = ref_to_update_str_datetime
		self.octave_calibration = ref_to_octave_calibration
		self.RR = EH_RR(ref_to_update_tPath,ref_to_update_str_datetime)
		self.exp1D = EH_1D()
		self.Rabi = EH_Rabi(ref_to_update_tPath,ref_to_update_str_datetime,self.exp1D,self.octave_calibration)
		self.SWAP = EH_SWAP(ref_to_update_tPath,ref_to_update_str_datetime)
		#self.CPMG = EH_CPMG(ref_to_update_tPath,ref_to_update_str_datetime)