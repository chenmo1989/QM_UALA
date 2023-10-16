"""
This file contains useful python functions meant to simplify the Jupyter notebook.
We have three categories

"""

from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np
##############
class QM_data_processing:
    def __init__(self):
        self.xdata = []
        self.ydata = []
        self.zdata = []


