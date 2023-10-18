"""
This file contains useful python functions meant to simplify the Jupyter notebook.
ExperimentHandle

"""
import datetime
import os

from ExperimentClass_1D import EH_exp1D
#from ExperimentClass_2D import EH_exp2D

class EH_expsave:
	def __init__(self):
		pass

class ExperimentHandle:
	def __init__(self):
		self.exp1D = EH_exp1D()
		#self.exp2D = EH_exp2D()
		self.expsave = EH_expsave()

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

	def update_str_datetime(self):
		now = datetime.datetime.now()
		month = now.strftime("%m")
		day = now.strftime("%d")
		hour = now.strftime("%H")
		minute = now.strftime("%M")
		f_str_datetime = month + day + '-' + hour + minute
		return f_str_datetime