from quam import QuAM

machine = QuAM('quam_state.json')

for i in range(7):
    machine.qubits[i].rf_switch_mode = "trig_normal"
    machine.resonators[i].rf_switch_mode = "on"
    #machine.resonators[i].rf_switch_mode = "trig_normal"
    #machine.resonators[i].readout_pulse_amp = 0.3
    #machine.resonators[i].digital_marker.delay = 85
    #machine.resonators[i].digital_marker.buffer = 20
    machine.qubits[i].digital_marker.delay = 87
    machine.qubits[i].digital_marker.buffer = 18
   
machine._save('quam_state.json')
