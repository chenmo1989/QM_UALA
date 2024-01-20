"""
This file contains useful python functions meant to simplify the Jupyter notebook.
AnalysisHandle
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
import datetime
import os
import time
import warnings
import json
import matplotlib.pyplot as plt
import numpy as np

from AnalysisClass_1D import AH_exp1D
from AnalysisClass_2D import AH_exp2D

class AnalysisHandle:
	def __init__(self):
		self.exp1D = AH_exp1D()
		self.exp2D = AH_exp2D()
		# for updated values
		self.ham_param = []
		self.poly_param = []

	def get_machine(self):
		machine = QuAM("quam_state.json")
		config = build_config(machine)
		return machine

	def set_machine(self,machine):
		machine._save("quam_state.json")
		return machine

	def update_machine_qubit_frequency(self,machine,qubit_index,new_freq):
		machine.qubits[qubit_index].f_01 = new_freq
		return machine

	def update_machine_qubit_frequency_rel(self,machine,qubit_index,new_freq):
		machine.qubits[qubit_index].f_01 += new_freq
		return machine

	def update_machine_res_frequency(self,machine,qubit_index,new_freq):
		machine.resonators[qubit_index].f_readout = new_freq
		return machine

	def update_machine_res_frequency_rel(self,machine,qubit_index,new_freq):
		machine.resonators[qubit_index].f_readout += new_freq
		return machine

	def update_analysis_tuning_curve(self,qubit_index,res_index,flux_index,ham_param = None, poly_param = None,is_DC_curve = False):
		if ham_param is None:
			self.ham_param = self.get_machine().resonators[res_index].tuning_curve
		if poly_param is None:
			if is_DC_curve:
				self.poly_param = self.get_machine().qubits[qubit_index].DC_tuning_curve
			else:
				self.poly_param = self.get_machine().qubits[qubit_index].AC_tuning_curve
		return

	def get_sweept_spot(self,poly_param = None):
		if poly_param is None:
			poly_param = self.poly_param
		if np.size(poly_param) > 3:
			print("polynomial order > 2")
			return None
		else:
			return -poly_param[1]/2/poly_param[0]



