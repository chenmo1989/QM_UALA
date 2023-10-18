"""
This file contains useful python functions meant to simplify the Jupyter notebook.
ExperimentHandle.exp2D

"""
class EH_RR: # subclass in ExperimentHandle, for Readout Resonator (RR) related experiments
	def __init__(self):
		pass

	def RR_vs_dc_flux(self, res_freq_sweep, qubit_index, res_index, n_avg, cd_time, tPath, f_str_datetime, simulate_flag = False, simulation_len = 1000):
		# 2D scan, RR frequency vs DC flux
		machine = QuAM("quam_state.json")
		config = build_config(machine)
		res_lo = machine.resonators[res_index].lo
		res_if_sweep = res_freq_sweep - res_lo
		res_if_sweep = res_if_sweep.astype(int)

		


class EH_exp2D:
	def __init__(self):
		self.RR = EH_RR()
		self.Rabi = EH_Rabi()
		self.Echo = EH_Echo()
		self.CPMG = EH_CPMG()