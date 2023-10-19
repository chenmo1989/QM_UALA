"""
This file contains useful python functions meant to simplify the Jupyter notebook.
ExperimentHandle.exp1D

"""

import os
from qm.qua import *
from qm.QuantumMachinesManager import QuantumMachinesManager
from qm import SimulationConfig, LoopbackInterface
from qm.octave import *
from qm.octave.octave_manager import ClockMode
from configuration import *
import matplotlib.pyplot as plt
from scipy import signal
from qm import SimulationConfig
from qualang_tools.bakery import baking
from qualang_tools.units import unit
import warnings
from qm import generate_qua_script
from qm.octave import QmOctaveConfig
from qm.octave.octave_manager import ClockMode
from typing import Union
import json
from set_octave import ElementsSettings, octave_settings
from quam import QuAM
from macros import *

warnings.filterwarnings("ignore")

class EH_RR: # subclass in ExperimentHandle, for Readout Resonator (RR) related experiments
	def __init__(self):
		pass

	def time_of_flight(self, qubit_index, res_index, n_avg, cd_time, tPath, f_str_datetime, simulate_flag = False, simulation_len = 1000):
		machine = QuAM("quam_state.json")
		config = build_config(machine)

		with program() as raw_trace_prog:
			n = declare(int)
			adc_st = declare_stream(adc_trace=True)

			with for_(n, 0, n < n_avg, n + 1):
				reset_phase(machine.resonators[res_index].name)
				measure("readout", machine.resonators[res_index].name, adc_st)
				wait(cd_time * u.ns, machine.resonators[res_index].name)

			with stream_processing():
				# Will save average:
				adc_st.input1().average().save("adc1")
				adc_st.input2().average().save("adc2")
				# # Will save only last run:
				adc_st.input1().save("adc1_single_run")
				adc_st.input2().save("adc2_single_run")

		#####################################
		#  Open Communication with the QOP  #
		#####################################
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config)

		if simulate_flag:
			simulation_config = SimulationConfig(duration=simulation_len)
			job = qmm.simulate(config, resonator_spec, simulation_config)
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
			qubit_name = 'Q' + res_index
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name), {"adc1": adc1, "adc2": adc2, "adc1_single_run": adc1_single_run, "adc2_single_run": adc2_single_run})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return adc1,adc2,adc1_single_run,adc2_single_run

	def rr_freq(self, res_freq_sweep, qubit_index, res_index, flux_index, n_avg, cd_time, tPath, f_str_datetime, simulate_flag = False, simulation_len = 1000):
		machine = QuAM("quam_state.json")
		config = build_config(machine)
		res_lo = machine.resonators[res_index].lo
		res_if_sweep = res_freq_sweep - res_lo
		res_if_sweep = res_if_sweep.astype(int)

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
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config)
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
			fig = plt.figure()
			plt.rcParams['figure.figsize'] = [12, 8]
			interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
			while results.is_processing():
				# Fetch results
				I, Q, iteration = results.fetch_all()
				I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
				Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
				# progress bar
				progress_counter(iteration, n_avg, start_time=results.get_start_time())
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
			qubit_name = 'Q' + res_index
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name), {"RR_freq": res_freq_sweep, "sig_amp": sig_amp, "sig_phase": sig_phase})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return res_freq_sweep, sig_amp


class EH_Rabi:
	def __init__(self):
		pass

	def qubit_freq(self, qubit_freq_sweep, qubit_index, res_index, flux_index, n_avg, cd_time, ff_amp, tPath, f_str_datetime, simulate_flag = False, simulation_len = 1000):
		machine = QuAM("quam_state.json")
		config = build_config(machine)
		qubit_lo = machine.qubits[qubit_index].lo
		qubit_if_sweep = qubit_freq_sweep - qubit_lo
		qubit_if_sweep = qubit_if_sweep.astype(int)
		ff_duration = machine.qubits[qubit_index].pi_length + 40

		with program() as qubit_freq_prog:
			[I,Q,n,I_st,Q_st,n_st] = declare_vars()
			df = declare(int)

			with for_(n, 0, n < n_avg, n+1):
				with for_(*from_array(df,qubit_if_sweep)):
					update_frequency(machine.qubits[qubit_index].name, df)
					play("const" * amp(ff_amp), machine.flux_lines[flux_index].name, duration=ff_duration * u.ns)
					wait(5, machine.qubits[qubit_index].name)
					play('pi', machine.qubits[qubit_index].name)
					align(machine.qubits[qubit_index].name, machine.flux_lines[flux_index].name,
						  machine.resonators[res_index].name)
					readout_avg_macro(machine.resonators[res_index].name,I,Q)
					align()
					wait(50)
					# eliminate charge accumulation
					play("const" * amp((-1) * ff_amp), machine.flux_lines[flux_index].name, duration=ff_duration * u.ns)
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
		qmm = QuantumMachinesManager(machine.network.qop_ip, port = '9510', octave=octave_config)
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
			fig = plt.figure()
			plt.rcParams['figure.figsize'] = [12, 8]
			interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
			while results.is_processing():
				# Fetch results
				I, Q, iteration = results.fetch_all()
				I = u.demod2volts(I, machine.resonators[res_index].readout_pulse_length)
				Q = u.demod2volts(Q, machine.resonators[res_index].readout_pulse_length)
				# progress bar
				progress_counter(iteration, n_avg, start_time=results.get_start_time())
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
			qubit_name = 'Q' + qubit_index
			f_str = qubit_name + '-' + exp_name + '-' + f_str_datetime
			file_name = f_str + '.mat'
			json_name = f_str + '_state.json'
			savemat(os.path.join(tPath, file_name), {"Q_freq": qubit_freq_sweep, "sig_amp": sig_amp, "sig_phase": sig_phase})
			machine._save(os.path.join(tPath, json_name), flat_data=False)

			return qubit_freq_sweep, sig_amp


class EH_Ramsey:
	def __init__(self):
		pass

class EH_Echo:
	def __init__(self):
		pass

class EH_CPMG:
	def __init__(self):
		pass


class EH_exp1D:
	def __init__(self):
		self.RR = EH_RR()
		self.Rabi = EH_Rabi()
		self.Echo = EH_Echo()
		self.CPMG = EH_CPMG()
