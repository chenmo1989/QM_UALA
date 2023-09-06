from quam import QuAM

machine = QuAM('quam_state.json')

for i in range(7):
    machine.qubits[i].x180_length = machine.qubits[i].pi_length
    machine.qubits[i].x180_amp = machine.qubits[i].pi_amp
    machine.flux_lines[i].Z_delay = 19.0
   
machine._save('quam_state.json', flat_data=False)
