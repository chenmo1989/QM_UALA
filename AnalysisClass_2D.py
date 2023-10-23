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

class AH_exp2D:
	"""
	Class for analysis of 2D experiments
	Attributes:
		ham_param: parameters for the Jaynes-Cummings Hamiltonian. Temporary storage.
		poly_param: parameters for the polynomial qubit tuning curve. Temporary storage.
	Methods (useful ones):
		rr_vs_dc_flux(self, res_freq_sweep, dc_flux_sweep, sig_amp, init_guess = None)
		qubit_vs_dc_flux_guess(self, ham_param = None)
		ham(self, dc_flux, wr, Ec, Ej, c, phi0, g, output_flag)
	"""

	def __init__(self):
		# only for temporary storage
		self.ham_param = []
		self.poly_param = []

	def rr_vs_dc_flux(self, res_freq_sweep, dc_flux_sweep, sig_amp, init_guess = None):
		"""
		Use the Jaynes-Cummings model to fit to the resonator vs dc_flux tuning curve
		Args:
			res_freq_sweep: 1D array, assumes the same frequency sweep for all the dc flux values
			dc_flux_sweep: 1D array of the dc flux swept values
			sig_amp: amplitude of the I, Q signal
			init_guess: [wr, Ec, Ej, c, phi0, g] for fitting to the Hamiltonian
		Return:
			popt: the fitted parameters of the Jaynes-Cummings Hamiltonian. Temporarily saved in AH_exp2D.ham_param.
				should save to Analysis.ham_param, and machine.resonators[res_index].tuning_curve for long-term storage.
		"""

		# define init_guess for the fitting
		if init_guess is None:
			wr = np.min(res_freq_sweep) / u.MHz  # Resonator frequency
			Ec = 170.0  # Capacitive energy
			Ej = 30.0E3  # Inductive energy
			c = 0.05  # Period in cosine function for flux
			phi0 = 0.4  # Offset in cosine function for flux
			g = 70.0  # RR-qubit coupling
		else:
			wr = init_guess[0]
			Ec = init_guess[1]
			Ej = init_guess[2]
			c = init_guess[3]
			phi0 = init_guess[4]
			g = init_guess[5]

		init_guess = [wr, Ec, Ej, c, phi0, g]

		# plot part
		sig = np.reshape(sig_amp,
						 (np.size(dc_flux_sweep), np.size(res_freq_sweep)))
		fig = plt.figure()
		plt.rcParams['figure.figsize'] = [8, 4]
		plt.cla()

		# 2D spectroscopy plot
		plt.title("Resonator spectroscopy tuning curve")
		plt.pcolormesh(np.linspace(np.min(dc_flux_sweep), np.max(dc_flux_sweep), np.size(dc_flux_sweep)),
					   np.linspace(np.min(res_freq_sweep),
								   np.max(res_freq_sweep),
								   np.size(res_freq_sweep)) / 1e6,
					   sig.T, shading="nearest", cmap="seismic")
		plt.xlabel("DC flux level [V]")
		plt.ylabel("Frequency [MHz]")
		plt.colorbar()

		# find minima of signal as resonator frequency for fitting
		res_freq = []
		for i in range(np.size(dc_flux_sweep)):
			res_freq.append(res_freq_sweep[np.argmin(sig[i])])
		res_freq = np.array(res_freq)

		# Fit data from res_freq to Hamiltonian function
		popt, _ = curve_fit(lambda dc_flux_sweep, *guess: self.ham(dc_flux_sweep, *guess, 1),
							xdata=dc_flux_sweep, ydata=res_freq/u.MHz, p0=init_guess, check_finite="true", bounds=(
			(wr - 200, Ec - 50, Ej - 10000, 0.0001, -6, g - 50), (wr + 200, Ec + 100, Ej + 10000, 4, 6, g + 50)))

		## plot data and fitting
		plt.scatter(dc_flux_sweep.T, res_freq / u.MHz)
		plt.plot(dc_flux_sweep.T, self.ham(dc_flux_sweep, *popt, 1))
		self.ham_param = popt

		return popt

	def qubit_vs_dc_flux_guess(self, ham_param = None):
		"""
		Use 2nd order polynomial to fit to the (simulated) qubit tuning curve around +-2V of the sweep spot dc flux.
		Simulation is based on the Jaynes-Cummings model, and parameters extracted from rr_vs_dc_flux experiment.
		Args:
			ham_param: default is the value saved in AH_exp2D.ham_param, if we ran rr_vs_dc_flux. This is supposed to
			be a temporary storage place. Better use Analysis.ham_param, or even better, machine.resonators[res_index].tuning_curve.
		Return:
			poly_param: 2nd order polynomial coefficient for the qubit tuning curve. Temporarily saved in AH_exp2D.poly_param.
				should save to Analysis.poly_param, and machine.qubits[qubit_index].tuning_curve for long-term storage.
		"""
		if ham_param is None:
			ham_param = self.ham_param

		c = ham_param[3]
		phi0 = ham_param[4]
		dc_ss = -phi0 / (2 * np.pi * c)
		dc_flux_fit = dc_ss + np.linspace(start=-2, stop=2, num=40, endpoint=True)
		qubit_freq_est = self.ham(dc_flux_fit,*ham_param,output_flag=2)
		poly_param = np.polyfit(dc_flux_fit, qubit_freq_est, deg = 2)
		self.poly_param = poly_param
		fig = plt.figure()
		plt.rcParams['figure.figsize'] = [8, 4]
		plt.plot(dc_flux_fit, qubit_freq_est, 'o')
		plt.plot(dc_flux_fit, np.polyval(poly_param,dc_flux_fit))

		return poly_param

	def ham(self, dc_flux, wr, Ec, Ej, c, phi0, g, output_flag = 1):
		"""
		The Jaynes-Cummings Hamiltonian, all in units of MHz
		Args:
			dc_flux: dc flux voltage values
			wr: bare resonator frequency
			Ec: capacitive energy of qubit
			Ej: Josephson energy of qubit
			c, phi0: linear coefficient for the mapping between dc voltage and flux, following
				magnetic flux = 2 * np.pi * c * dc_flux + phi0
			output_flag: 1-rr, 2-qubit, otherwise-pass
		Return:
			freq_sys: frequency of the system, with the system being either resonator or qubit
		"""

		N = 4  # 0-3 photons
		a = tensor(destroy(N), qeye(N))  # cavity mode
		b = tensor(qeye(N), destroy(N))  # qubit
		freq_sys = []

		# Hamiltonian as a function of flux
		for k in range(np.size(dc_flux)):
			H = wr * a.dag() * a + (np.sqrt(8 * Ec * Ej * np.abs(
				np.cos(self.phi_flux_rr(dc_flux[k], c, phi0)))) - Ec) * b.dag() * b - Ec / 2 * b.dag() * b.dag() * b * b + g * (
							a * b.dag() + a.dag() * b)
			w, v = np.linalg.eig(H)

			for n_1 in range(v.shape[1]):
				v[:, n_1] = v[:, n_1] / np.inner(v[:, n_1], v[:, n_1])

				idx_00 = np.argmax(np.abs(v[0, :]))  # |0,0>
				idx_01 = np.argmax(np.abs(v[N, :]))  # |1,0> photon
				idx_02 = np.argmax(np.abs(v[1, :]))  # |0,1> qubit
			if output_flag == 1:
				freq_sys.append(np.abs(np.maximum(w[idx_01], w[idx_02]) - w[idx_00]))
			elif output_flag == 2:
				freq_sys.append(np.abs(np.minimum(w[idx_01], w[idx_02]) - w[idx_00]))
			else:
				pass
		freq_sys = np.array(freq_sys)
		return freq_sys

	def phi_flux_rr(self,dc_flux, c, phi0):
		"""
		linear mapping function from dc flux voltage to dc magnetic flux
		magnetic flux = 2 * np.pi * c * dc_flux + phi0
		Args:
			dc_flux: the voltage we apply in experiment (QDAC)
			c: slope
			phi0: offset
		Return:
			the magnetic flux
		"""
		return 2 * np.pi * c * dc_flux + phi0