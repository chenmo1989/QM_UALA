"""
This file contains useful python functions meant to simplify the Jupyter notebook.
ExperimentHandle.exp2D
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

	def rr_vs_dc_flux(self, res_freq_sweep, dc_flux_sweep, qubit_index, res_index, flux_index, n_avg, cd_time, tPath = None, f_str_datetime = None, simulate_flag = False, simulation_len = 1000):
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
		machine = QuAM("quam_state.json")
		config = build_config(machine)
		res_lo = machine.resonators[res_index].lo
		res_if_sweep = res_freq_sweep - res_lo
		res_if_sweep = res_if_sweep.astype(int)

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
			fig = plt.figure()
			plt.rcParams['figure.figsize'] = [8, 4]
			interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

			for m in range(len(dc_flux_sweep)):
				# set QDAC voltage
				dc_flux = dc_flux_sweep[m]
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

class EH_exp2D:
	"""
	Class for running 2D experiments
	Attributes:

	Methods (useful ones):
		update_tPath: reference to Experiment.update_tPath
		update_str_datetime: reference to Experiment.update_str_datetime
		RR: a class for running readout resonator related experiments
	"""
	def __init__(self,ref_to_update_tPath, ref_to_update_str_datetime):
		self.update_tPath = ref_to_update_tPath
		self.update_str_datetime = ref_to_update_str_datetime
		self.RR = EH_RR(ref_to_update_tPath,ref_to_update_str_datetime)
		#self.Rabi = EH_Rabi(ref_to_update_tPath,ref_to_update_str_datetime)
		#self.Echo = EH_Echo(ref_to_update_tPath,ref_to_update_str_datetime)
		#self.CPMG = EH_CPMG(ref_to_update_tPath,ref_to_update_str_datetime)