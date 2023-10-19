"""
This file contains useful python functions meant to simplify the Jupyter notebook.
AnalysisHandle

"""
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
from configuration import *
import json
import numpy as np

class AH_RR: # subclass in AnalysisHandle, for Readout Resonator (RR) related data analysis
	def __init__(self):
		pass

	def time_of_flight(self, adc1,adc2,adc1_single_run,adc2_single_run):
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

	def rr_freq(self, res_freq_sweep, sig_amp):
		%matplotlib qt
		idx = np.argmin(sig_amp) # find minimum
		print(f"IF offset to add to IF: {res_freq_sweep[idx] / u.MHz:.6f} MHz")

		plt.close('all')
		%matplotlib inline
		# 1D spectroscopy plot
		fig = plt.figure(figsize=[8, 4])
		plt.title("Resonator spectroscopy")
		plt.plot((res_freq_sweep) / u.MHz, sig_amp, ".")
		plt.xlabel("Frequency [MHz]")
		plt.ylabel(r"$\sqrt{I^2 + Q^2}$ [V]")
		plt.axvline(x = (res_freq_sweep[idx]) / u.MHz)

class AH_exp1D:
	def __init__(self):
		self.RR = AH_RR()
		self.Rabi = AH_Rabi()
		self.Echo = AH_Echo()
		self.CPMG = AH_CPMG()

class AH_exp2D:
	def __init__(self):
		pass

class AnalysisHandle:
	def __init__(self)
		self.exp1D = AH_exp1D()
		self.exp2D = AH_exp2D() 
		self.expsave = AH_expsave()
