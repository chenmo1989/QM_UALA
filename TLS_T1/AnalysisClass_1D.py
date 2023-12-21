"""
This file contains useful python functions meant to simplify the Jupyter notebook.
AnalysisHandle
written by Mo Chen in Oct. 2023
"""
from qm.qua import *
from qm import SimulationConfig, LoopbackInterface, generate_qua_script,QuantumMachinesManager
from qm.octave import *
from qm.octave.octave_manager import ClockMode
from configuration import *
from scipy import signal
from qualang_tools.bakery import baking
from qualang_tools.units import unit
from qm.octave import QmOctaveConfig
from set_octave import ElementsSettings, octave_settings
from quam import QuAM
from scipy.io import savemat
from scipy.io import loadmat
from scipy.optimize import curve_fit, minimize
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
import math

class AH_exp1D:
	"""
	Class for analysis of 1D experiments
	Attributes:

	Methods (useful ones):
		time_of_flight(self, adc1, adc2, adc1_single_run, adc2_single_run)
		rr_freq(self, res_freq_sweep, sig_amp)
	"""

	def __init__(self):
		pass

	def time_of_flight(self, adc1, adc2, adc1_single_run, adc2_single_run):
		"""
		analysis of time of flight experiment
		plot the experiment result, both single run, to check if signal level falls within +-0.5V, the range for ADC
		does some rudimentary analysis, the dc offsets are more useful. TOF is subject to scrutiny.
		Args:
			adc1: average adc voltage value from I channel
			adc2: average adc voltage value from Q channel
			adc1_single_run: adc voltage value from I channel, single run
			adc2_single_run: adc voltage value from Q channel, single run
		Return:
			dc_offset_i: to add to machine.global_parameters.con1_downconversion_offset_I
			dc_offset_q: to add to machine.global_parameters.con1_downconversion_offset_Q
			delay: to add to machine.global_parameters.time_of_flight
		"""
		adc1_mean = np.mean(adc1)
		adc2_mean = np.mean(adc2)
		adc1_unbiased = adc1 - np.mean(adc1)
		adc2_unbiased = adc2 - np.mean(adc2)
		signal = savgol_filter(np.abs(adc1_unbiased + 1j * adc2_unbiased), 11, 3)
		# detect arrival of readout signal
		th = (np.mean(signal[:100]) + np.mean(signal[:-100])) / 2
		delay = np.where(signal > th)[0][0]
		delay = np.round(delay / 4) * 4
		dc_offset_i = -adc1_mean
		dc_offset_q = -adc2_mean

		# Update the config
		print(f"DC offset to add to I: {dc_offset_i:.6f} V")
		print(f"DC offset to add to Q: {dc_offset_q:.6f} V")
		print(f"TOF to add: {delay} ns")

		# Plot data
		fig = plt.figure(figsize=[14, 6])
		plt.subplot(121)
		plt.title("Single run")
		plt.plot(adc1_single_run, "b", label="I")
		plt.plot(adc2_single_run, "r", label="Q")
		plt.axhline(y=0.5)
		plt.axhline(y=-0.5)
		xl = plt.xlim()
		yl = plt.ylim()
		plt.plot(xl, adc1_mean * np.ones(2), "k--")
		plt.plot(xl, adc2_mean * np.ones(2), "k--")
		plt.plot(delay * np.ones(2), yl, "k--")
		plt.xlabel("Time [ns]")
		plt.ylabel("Signal amplitude [V]")
		plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
				   fancybox=True, shadow=True, ncol=5)

		plt.subplot(122)
		plt.title("Averaged run")
		plt.plot(adc1, "b", label="I")
		plt.plot(adc2, "r", label="Q")
		plt.xlabel("Time [ns]")
		plt.ylabel("Signal amplitude [V]")
		xl = plt.xlim()
		yl = plt.ylim()
		plt.plot(xl, adc1_mean * np.ones(2), "k--")
		plt.plot(xl, adc2_mean * np.ones(2), "k--")
		plt.plot(delay * np.ones(2), yl, "k--")
		plt.xlabel("Time [ns]")
		plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
				   fancybox=True, shadow=True, ncol=5)
		plt.grid("all")
		plt.tight_layout(pad=2)
		plt.show()

		return dc_offset_i, dc_offset_q, delay

	def rr_freq(self, res_freq_sweep, sig_amp):
		"""
		analysis for the 1D resonator spectroscopy experiment, and find the resonance frequency by looking for the minima
		Args:
			res_freq_sweep: resonator frequency array
			sig_amp: corresponding signal amplitude array
		Return:
			 res_freq_sweep[idx]: the resonance frequency
		"""

		idx = np.argmin(sig_amp)  # find minimum
		print(f"resonator frequency: {res_freq_sweep[idx] / u.MHz:.3f} MHz")

		plt.close('all')
		# 1D spectroscopy plot
		plt.figure(figsize=[6, 3])
		plt.title("Resonator spectroscopy")
		plt.plot((res_freq_sweep) / u.MHz, sig_amp, ".")
		plt.xlabel("Frequency [MHz]")
		plt.ylabel(r"$\sqrt{I^2 + Q^2}$ [V]")
		plt.axvline(x=(res_freq_sweep[idx]) / u.MHz)
		plt.show()

		return res_freq_sweep[idx]

	def peak_fit(self, x, y, method = "sinc", plot_flag = True):
		"""
		this function fits a single peak to sinc, lorentzian, or gaussian functions
		Args:
		:param x: x data
		:param y: y data
		:param method: "sinc" (default), "lorentz", "gaussian"
		Return:
		the x value (usually frequency) that gives the peak
		"""
		if method == "sinc":
			def __fit_fun(x,c0,c1,c2,c3):
				return c3 + c0 * np.sinc((x - c1) / c2)**2
		elif method == "lorentz":
			def __fit_fun(x,c0,c1,c2,c3):
				return c3 + c0 / (1 + ((x-c1)/c2)**2)
		else:
			def __fit_fun(x,c0,c1,c2,c3):
				return c3 + c0 * np.exp(-(x-c1)**2/2/c2**2)
		gamma = abs(x[-1] - x[0]) / 40
		cont = max(y) - min(y)
		f_index = np.argmax(y)
		f = x[f_index]
		init_guess = [cont, f, gamma, y[0] - __fit_fun(x[0], cont, f, gamma, 0)]

		LB = [0, min(x), gamma / 1e2, -10]
		UB = [cont*10, max(x), gamma * 1e2, 10]

		popt, _ = curve_fit(lambda x, *guess: __fit_fun(x, *guess),
							xdata=x, ydata=y, p0=init_guess, check_finite="true", bounds=(LB, UB))

		if plot_flag == True:
			fig = plt.figure()
			plt.rcParams['figure.figsize'] = [6, 3]
			plt.cla()
			plt.plot(x/u.MHz,y,'.')
			plt.plot(x/u.MHz,__fit_fun(x,popt[0],popt[1],popt[2],popt[3]),'r')

			plt.title("qubit spectroscopy")
			plt.xlabel("Frequency [MHz]")
			plt.ylabel("Signal [V]")
			print(f"resonant frequency: {popt[1] / u.MHz:.3f} MHz")

		return popt[1]

	def rabi_length(self, x, y, method = "time_rabi", plot_flag = True):
		"""
		this function fits a single oscillatory curve to a cosine, typically used for a rabi oscillation
		note x is in units of ns. The translation from clock cycle is already done in the output of ExperimentClass
		:param x: x data--for time_rabi, it is ns not clock cycle!
		:param y: y data
		:param method: "time_rabi" (default), finds the pi pulse lengths, in ns; "power_rabi", finds the amp for pi pulse; "decaying_time_rabi", "decaying_power_rabi" will have an additional exp decay term
		:param plot_flag:
		Return:
			fitted pi pulse length
		"""
		if method[0:5] == "decay":
			def __fit_fun(x, c0, c1, c2, c3, c4):
				return c2 + c1 * np.cos(x * 2 * np.pi * c0 + c3) * np.exp(-x/c4)
		else:
			def __fit_fun(x, c0, c1, c2, c3):
				return c2+ c1*np.cos(x*2*np.pi*c0+c3)

		delta = abs(x[0] - x[1])
		Fs = 1 / delta  # Sampling frequency
		L = np.size(x)
		NFFT = int(2 * 2 ** self.next_power_of_2(L))
		Freq = Fs / 2 * np.linspace(0, 1, NFFT // 2 + 1, endpoint=True)
		Y = np.fft.fft(y - np.mean(y), NFFT) / L
		DataY = abs(Y[0:(NFFT // 2)]) ** 2
		index = np.argmax(DataY)
		amp = abs(max(y) - min(y)) / 2
		rabi = Freq[index]
		init_guess = [rabi, amp, (max(y) + min(y))/2, -np.pi]
		LB = [0.5 * rabi, 0.0, -1, -6]
		UB = [2 * rabi, 5*amp, 1, 6]

		if method[0:5] == "decay":
			init_guess.append(x[-1])
			LB.append(x[-1]/1E3)
			UB.append(x[-1]*1E3)

		popt, _ = curve_fit(lambda x, *guess: __fit_fun(x, *guess),
							xdata=x, ydata=y, p0=init_guess, check_finite="true", bounds=(LB, UB))

		if plot_flag == True:
			fig = plt.figure()
			plt.rcParams['figure.figsize'] = [6, 3]
			plt.cla()

			if method == "time_rabi":
				plt.plot(x, y,'.') # in ns
				plt.plot(x, __fit_fun(x,popt[0],popt[1],popt[2],popt[3]),'r')
				plt.title("qubit rabi")
				plt.xlabel("tau [ns]")
				plt.ylabel("Signal [V]")
			elif method == "power_rabi":
				plt.plot(x, y, '.')  # in V
				plt.plot(x, __fit_fun(x, popt[0], popt[1], popt[2], popt[3]), 'r')
				plt.title("qubit rabi")
				plt.xlabel("rabi amplitude [V]")
				plt.ylabel("Signal [V]")
			elif method == "decaying_time_rabi":
				plt.plot(x, y, '.')  # in ns
				plt.plot(x, __fit_fun(x, popt[0], popt[1], popt[2], popt[3], popt[4]), 'r')
				plt.title("decaying qubit rabi")
				plt.xlabel("tau [ns]")
				plt.ylabel("Signal [V]")
				print(f"T2rabi: {(popt[4]):.1f} ns")
			elif method == "decaying_power_rabi":
				plt.plot(x, y, '.')  # in V
				plt.plot(x, __fit_fun(x, popt[0], popt[1], popt[2], popt[3], popt[4]), 'r')
				plt.title("decaying qubit rabi")
				plt.xlabel("rabi amplitude [V]")
				plt.ylabel("Signal [V]")

		if method[-9:] == "time_rabi":
			print(f"rabi_pi_pulse: {(-popt[3]) / popt[0] / 2 / np.pi:.1f} ns")
			print(f"half period: {1 / 2 / popt[0]:.2f} ns")
			return np.round((-popt[3]) / popt[0] / 2 / np.pi)
		elif method[-9:] == "ower_rabi":
			print(f"rabi_pi_pulse_amp: {(-popt[3]) / popt[0] / 2 / np.pi:.5f} V")
			print(f"half period: {1 / 2 / popt[0]:.7f} V")
			return np.round((-popt[3]) / popt[0] / 2 / np.pi, decimals = 7)

	def T1(self, tau_sweep, sig_amp, method = "exp", plot_flag = True):
		if method == "exp":
			def __fit_fun(t, A, T1, c):
				return A * np.exp(-t / T1) + c

		sig = min(sig_amp) + (max(sig_amp) - min(sig_amp)) / np.exp(1)
		for i, v in enumerate(sig_amp):
			if sig < v:
				T1_y = v
			else:
				pass
		T1_g = tau_sweep[np.where(sig_amp == T1_y)][0]

		param, _ = curve_fit(__fit_fun, tau_sweep, sig_amp, p0=[max(sig_amp) - min(sig_amp), T1_g, min(sig_amp)])

		if plot_flag == True:
			fig = plt.figure()
			plt.rcParams['figure.figsize'] = [6, 3]
			plt.cla()
			plt.plot(tau_sweep / u.us, sig_amp,'.')
			plt.plot(tau_sweep / u.us, __fit_fun(tau_sweep,param[0],param[1],param[2]),'r')

			plt.xlabel("tau [us]")
			plt.ylabel("Signal [V]")
			print('Qubit T1 [us]:', param[1] / u.us)

		return param[1]

	def ramsey(self, x, y, method = "ramsey", plot_flag = True):
		"""
		this function fits the resulting data to a cosine multiplied by an exponential decay (to a power) function
		note x is in units of ns. The translation from clock cycle is already done in the output of ExperimentClass
		:param x: x data--for ramsey, it is ns not clock cycle!
		:param y: y data
		:param method: "ramsey"
		:param plot_flag:
		Return:
			T2*
		"""
		if method == "ramsey":
			def __fit_fun(t, A, T2star, n, det, phi, c, offset):
				return A * np.exp(-(t / T2star) ** n) * (np.cos(t * 2 * np.pi * det + phi) + c) + offset

		delta = abs(x[0] - x[1])
		Fs = 1 / delta  # Sampling frequency
		L = np.size(x)
		NFFT = int(2 * 2 ** self.next_power_of_2(L))
		Freq = Fs / 2 * np.linspace(0, 1, NFFT // 2 + 1, endpoint=True)
		Y = np.fft.fft(y - np.mean(y), NFFT) / L
		DataY = abs(Y[0:(NFFT // 2)]) ** 2
		index = np.argmax(DataY)
		det = Freq[index]
		amp = abs(max(y) - min(y)) / 2
		init_guess = [amp, 500, 1, det, 0, 0, min(y)]

		popt, _ = curve_fit(lambda x, *guess: __fit_fun(x, *guess),
							xdata=x, ydata=y, p0=init_guess, check_finite="true")

		if plot_flag == True:
			fig = plt.figure()
			plt.rcParams['figure.figsize'] = [6, 3]
			plt.cla()
			plt.plot(x, y, '.')
			plt.plot(x, __fit_fun(x, popt[0], popt[1], popt[2], popt[3], popt[4], popt[5], popt[6]), 'r')
			plt.title("qubit Ramsey")
			plt.xlabel("tau [ns]")
			plt.ylabel("Signal [V]")
			print('Qubit T2* [ns]:', popt[1])
			print('Detuning [MHz]:', popt[3] * 1E3)
			print('Exponent n:', popt[2])
		return popt[1]

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

	def next_power_of_2(self,x):
		return 0 if x == 0 else math.ceil(math.log2(x))