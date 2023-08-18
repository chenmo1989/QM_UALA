from quam import QuAM

machine = QuAM('quam_state.json')

machine.qubits[6].pi_length = 80

machine._save('quam_state.json', flat_data=False)