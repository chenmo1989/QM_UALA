from quam import QuAM

machine = QuAM('quam_state.json')

machine.qubits[0].f_01 += 915E6
machine.qubits[0].lo = 6382E6
#machine.qubits[1].pi_length = 80

machine.resonators[0].f_readout += 1144E6
machine.resonators[0].lo = 7206E6

machine._save('quam_state.json', flat_data=False)
