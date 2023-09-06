from quam import QuAM

machine = QuAM('quam_state.json')

for i in range(7):
    machine.resonators[i].readout_pulse_amp = 0.3
   
machine._save('quam_state.json', flat_data=False)
