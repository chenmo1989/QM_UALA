"""
This file is used to configure the Octave ports (gain, switch_mode, down-conversion) and calibrate the up-conversion mixers.
You need to run this file in order to update the Octaves with the new parameters.
"""
from set_octave import ElementsSettings, octave_settings
from qm.QuantumMachinesManager import QuantumMachinesManager
from configuration import *
from quam import QuAM
from qm.octave.octave_manager import ClockMode # for setting external clock
# import time

machine = QuAM('quam_state.json')
# Configure the Octave parameters for each element
resonator = ElementsSettings("r0", gain=0, rf_in_port=["octave1", 1], down_convert_LO_source="Internal")
# resonator_aux = ElementsSettings("resonator_aux", gain=0, rf_in_port=["octave1", 1], down_convert_LO_source="Internal")
qubit = ElementsSettings("q0", gain=0)
# Add the "octave" elements
elements_settings = [resonator, qubit]


machine._save("quam_state.json", flat_data=False)
###################
# Octave settings #
###################
# Configure the Octave according to the elements settings and calibrate
qmm = QuantumMachinesManager(host=machine.network.qop_ip, port = '9510', octave=octave_config, log_level="ERROR")
config = build_config(machine)
# set to external clock #
###########################
#qm = qmm.open_qm(config)
#qm.octave.set_clock("octave1", clock_mode=ClockMode.External_10MHz)
# qm.octave.set_clock("octave1", ClockType.External_10MHz)

octave_settings(
    qmm=qmm,
    config=config,
    octaves=octaves,
    elements_settings=elements_settings,
    calibration=True,
)

qmm.close()

