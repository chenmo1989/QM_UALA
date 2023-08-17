# qdacExample.py
# Copyright QDevil ApS, 2018, 2019
VERSION = "1.21"

import qdac
import random
import math

with qdac.qdac('COM3') as q:
    print("QDAC Serial number: %s" % q.getSerialNumber())
    print("Number of channels: %d" % q.getNumberOfChannels())

    print("-----------------------------------------------")
    print("Setting Channel 1 voltage range to 10 V")
    result = q.setVoltageRange(channel=1, theRange=10)
    print("Result: %s" % result)
    print("Setting Channel 1 DC voltage to 1.23456 V")
    result = q.setDCVoltage(channel=1, volts=0)
    print("Result: %s" % result)
    voltage1 = q.getDCVoltage(1)
    print("Voltage output on channel 1 is %f V" % voltage1)

