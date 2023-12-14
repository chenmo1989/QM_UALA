"""
This file contains useful python functions meant to simplify the Jupyter notebook.
ExperimentHandle
written by Mo Chen in Oct. 2023
"""
# these are just for octave_calibration
from set_octave import ElementsSettings, octave_settings
from qm.QuantumMachinesManager import QuantumMachinesManager
from configuration import *
from quam import QuAM
from qm.octave.octave_manager import ClockMode # for setting external clock
import json
import datetime
import os
import Labber

from ExperimentClass_1D import EH_exp1D
from ExperimentClass_2D import EH_exp2D

class EH_expsave:
	def __init__(self):
		pass

class ExperimentHandle:
	def __init__(self):
		self.exp1D = EH_exp1D(self.update_tPath,self.update_str_datetime,self.octave_calibration)
		self.exp2D = EH_exp2D(self.update_tPath,self.update_str_datetime,self.octave_calibration)
		#self.expsave = EH_expsave()

		now = datetime.datetime.now()
		year = now.strftime("%Y")
		month = now.strftime("%m")
		day = now.strftime("%d")
		tPath = os.path.join(r'Z:\LabberData_DF5\QM_Data_DF5',year,month,'Data_'+month+day)
		if not os.path.exists(tPath):
			os.makedirs(tPath)
		self.tPath = tPath

	def update_tPath(self):
		now = datetime.datetime.now()
		year = now.strftime("%Y")
		month = now.strftime("%m")
		day = now.strftime("%d")
		tPath = os.path.join(r'Z:\LabberData_DF5\QM_Data_DF5',year,month,'Data_'+month+day)
		if not os.path.exists(tPath):
			os.makedirs(tPath)
		self.tPath = tPath
		return tPath

	def update_str_datetime(self):
		now = datetime.datetime.now()
		month = now.strftime("%m")
		day = now.strftime("%d")
		hour = now.strftime("%H")
		minute = now.strftime("%M")
		f_str_datetime = month + day + '-' + hour + minute
		return f_str_datetime

	def set_Labber(self, machine, qubit_index, res_index, flux_index):
		"""
		function to set Labber controlled hardware, according to object "machine"
		1. set QDAC to 0 V
		2. set QDAC CH (flux_index+1) to the saved sweet spot value saved in "machine"
		3. set Vaunix digital attenuators to ROI, ROO values saved in "machine"
		4. set TWPA pumping frequency and power to values saved in "machine"

		Args:
			machine: initially from quam_state.json
			qubit_index:
			res_index:
			flux_index:
		Return:

		"""
		# connect to server
		client = Labber.connectToServer('localhost')  # get list of instruments

		# reset all QDevil channels to 0 V
		QDevil = client.connectToInstrument('QDevil QDAC', dict(interface='Serial', address='3'))
		for n in range(24):
			if n + 1 < 10:
				QDevil.setValue("CH0" + str(n + 1) + " Voltage", 0.0)
			else:
				QDevil.setValue("CH" + str(n + 1) + " Voltage", 0.0)
		# Set qubits to desired dc value
		for flux_index_tmp in range(6):
			QDevil.setValue("CH0" + str(flux_index_tmp + 1) + " Voltage", machine.flux_lines[flux_index_tmp].dc_voltage)

		# digital attenuators
		Vaunix1 = client.connectToInstrument('Painter Vaunix Lab Brick Digital Attenuator',
											 dict(interface='USB', address='25606'))
		Vaunix2 = client.connectToInstrument('Painter Vaunix Lab Brick Digital Attenuator',
											 dict(interface='USB', address='25607'))
		Vaunix1.setValue("Attenuation", machine.resonators[res_index].RO_attenuation[0])
		Vaunix2.setValue("Attenuation", machine.resonators[res_index].RO_attenuation[1])

		# TWPA pump
		SG = client.connectToInstrument('Rohde&Schwarz RF Source', dict(interface='TCPIP', address='192.168.88.2'))
		SG.setValue('Frequency', machine.resonators[res_index].TWPA[0])
		SG.setValue('Power', machine.resonators[res_index].TWPA[1])
		SG.setValue('Output', True)

		client.close()

	def set_QDAC(self,qubit_index,res_index,flux_index,dc_value,machine = None):
		if machine is None:
			machine = QuAM("quam_state.json")

		machine.flux_lines[flux_index].dc_voltage = dc_value + 0E1
		# connect to server
		client = Labber.connectToServer('localhost')  # get list of instruments
		QDevil = client.connectToInstrument('QDevil QDAC', dict(interface='Serial', address='3'))
		QDevil.setValue("CH0" + str(flux_index + 1) + " Voltage", dc_value)
		client.close()
		return machine

	def octave_calibration(self,qubit_index,res_index,flux_index,machine = None,log_flag = True,qubit_only = False,calibration_flag = True):
		"""
		calibrates octave, using parameters saved in machine
		:param qubit_index:
		:param res_index:
		:param flux_index:
		:param machine: if not given, takes value saved in quam_state.json
		:param log_flag: True (default), have warnings from QM; False: error log only
		:param qubit_only: False (default). If true, only calibrate qubit, skip the resonator.
		:param calibration_flag: True (default). If false, will still update octave configuration, but not run calibration
		:return:
		"""
		if machine is None:
			machine = QuAM('quam_state.json')

		# Configure the Octave parameters for each element
		resonator = ElementsSettings("r" + str(res_index), gain=machine.resonators[res_index].rf_gain, rf_in_port=["octave1", 1], down_convert_LO_source="Internal",
									 switch_mode = machine.resonators[res_index].rf_switch_mode)
		# resonator_aux = ElementsSettings("resonator_aux", gain=0, rf_in_port=["octave1", 1], down_convert_LO_source="Internal")
		qubit = ElementsSettings("q" + str(qubit_index), gain=machine.qubits[qubit_index].rf_gain, switch_mode = machine.qubits[qubit_index].rf_switch_mode)
		# Add the "octave" elements
		if qubit_only:
			elements_settings = [qubit]
		else:
			elements_settings = [resonator, qubit]

		#machine._save("quam_state.json", flat_data=False)

		# Configure the Octave according to the elements settings and calibrate
		if log_flag:
			qmm = QuantumMachinesManager(host = machine.network.qop_ip, port='9510', octave=octave_config)
			config = build_config(machine)
		else:
			qmm = QuantumMachinesManager(host=machine.network.qop_ip, port='9510', octave=octave_config, log_level = "ERROR")
			config = build_config(machine)
			print("Octave calibration starts...")
			print(f"------------------------------------- Calibrates r{res_index:.0f} for (LO, IF) = ({machine.resonators[res_index].lo/1E9:.3f} GHz, {(machine.resonators[res_index].f_readout - machine.resonators[res_index].lo)/1E6: .3f} MHz)")
			print(f"------------------------------------- Calibrates q{qubit_index:.0f} for (LO, IF) = ({machine.qubits[qubit_index].lo/1E9:.3f} GHz, {(machine.qubits[qubit_index].f_01 - machine.qubits[qubit_index].lo)/1E6: .3f} MHz)")
			print("Octave calibration finished.")

		octave_settings(
			qmm=qmm,
			config=config,
			octaves=octaves,
			elements_settings=elements_settings,
			calibration=calibration_flag,
		)

		qm = qmm.open_qm(config)

		if calibration_flag:
			calibration_parameters = json.load(open("calibration_db.json"))["_default"]
			# for the qubit tone
			IF = machine.qubits[qubit_index].f_01 - machine.qubits[qubit_index].lo
			for i in calibration_parameters.keys():
				if calibration_parameters[i]["lo_frequency"] == machine.qubits[qubit_index].lo:
					if calibration_parameters[i]["if_frequency"] == IF:
						I_off = calibration_parameters[i]["i_offset"]
						Q_off = calibration_parameters[i]["q_offset"]
						C_mat = calibration_parameters[i]["correction"]
						qm = qmm.open_qm(config)
						qm.set_output_dc_offset_by_element(machine.qubits[qubit_index].name, ('I', 'Q'), (I_off, Q_off))
					else:
						pass
				else:
					pass
			# for the resonator tone
			IF = machine.resonators[res_index].f_readout - machine.resonators[res_index].lo
			for i in calibration_parameters.keys():
				if calibration_parameters[i]["lo_frequency"] == machine.resonators[qubit_index].lo:
					if calibration_parameters[i]["if_frequency"] == IF:
						I_off = calibration_parameters[i]["i_offset"]
						Q_off = calibration_parameters[i]["q_offset"]
						C_mat = calibration_parameters[i]["correction"]
						qm = qmm.open_qm(config)
						qm.set_output_dc_offset_by_element(machine.resonators[res_index].name, ('I', 'Q'), (I_off, Q_off))
					else:
						pass
				else:
					pass

		qmm.close()
		return

	def set_external_clock(self):
		"""
		should set the octave clock to external 10MHz. Not working properly at the moment!!
		:return:
		"""
		machine._save("quam_state.json", flat_data=False)
		# set to external clock #
		###########################
		qmm = QuantumMachinesManager(host=machine.network.qop_ip, port='9510', octave=octave_config)
		config = build_config(machine)
		qm = qmm.open_qm(config)
		qm.octave.set_clock("octave1", clock_mode=ClockMode.External_10MHz)
		qmm.close()
		return
