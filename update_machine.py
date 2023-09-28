from quam import QuAM

machine = QuAM('quam_state.json')

# for i in range(7):
#     machine.flux_lines[i].flux_pulse_amp = 0.25
machine.qubits[0].lo= 6340432000
   
machine._save('quam_state.json', flat_data=False)
