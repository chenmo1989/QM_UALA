from quam import QuAM

machine = QuAM('quam_state.json')

machine.qubits[1].f_01 = 6214425658
machine.qubits[1].lo = 6110E6
#machine.qubits[1].pi_length = 80

machine._save('quam_state.json', flat_data=False)