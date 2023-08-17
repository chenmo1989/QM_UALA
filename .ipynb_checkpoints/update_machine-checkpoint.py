from quam import QuAM

machine = QuAM('quam_state.json', flat_data=False)

machine.qubits[0].f_01 = 5.567E9
machine.qubits[0].lo = 5.467E9
machine.resonators[0].f_readout = 6.112E9
machine.resonators[0].lo = 6.062E9

machine._save('quam_state.json', flat_data=False)