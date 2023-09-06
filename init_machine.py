from quam import QuAM

machine = QuAM("quam_bootstrap_state.json", flat_data = False)

qubits_name = ["q" + str(i) for i in range(1, 7)]
qubits_connectivity = [(3, 4, "con1")]
qubits_mixers_names = ["octave_octave1_2"]
qubits_frequencies = [(6.289e9, 6.189e9),(6.107e9, 6.007e9),(5.982e9,5.882e9),(5.768e9,5.668e9),(5.567e9,5.467e9),(5.442e9,5.342e9)]
resonators_name = ["r" + str(i) for i in range(1, 7)]
resonators_connectivity = [(1, 2, "con1")]
resonators_frequencies = [(7.130e9, 7.080e9), (6.999e9, 6.949e9), (6.875e9, 6.825e9),(6.217e9,6.167e9),(6.112e9,6.062e9),(6.018e9,5.968e9)]
flux_lines_name = ["flux" + str(i) for i in range(1, 7)]
flux_lines_connectivity = [(8, "con1"),(9, "con1"),(10, "con1"),(7, "con1"),(8, "con1"),(9, "con1")]

for i in range(6):
    machine.qubits.append(
        {
            "name": qubits_name[i],
            "f_01": qubits_frequencies[i][0],
            "lo": qubits_frequencies[i][1],
            "rf_gain": 0,
            "rf_switch_mode": "on",
            "mixer_name": qubits_mixers_names[0],
            "anharmonicity": 250e6,
            "drag_coefficient": 0.0,
            "ac_stark_detuning": 0.0,
            "x180_length": 40,
            "x180_amp": 0.25,
            "pi_length": 40,
            "pi_amp": 0.25,
            "wiring": {
                "controller": qubits_connectivity[0][2],
                "I": qubits_connectivity[0][0],
                "Q": qubits_connectivity[0][1],
            },
            "T1": 1230,
            "T2": 123,
        }
    )

    machine.flux_lines.append(
        {
            "name": flux_lines_name[i],
            "flux_pulse_length": 16,
            "flux_pulse_amp": 0.125,
            "max_frequency_point": 0.0,
            "Z_delay": 19,
            "iswap": {
                "length": 16,
                "level": 0.075,
            },
            "wiring": {
                "controller": flux_lines_connectivity[i][1],
                "port": flux_lines_connectivity[i][0],
                "filter": {"iir_taps": [], "fir_taps": []},
            },
        },
    )
for i in range(6):
        machine.resonators.append(
        {
            "name": resonators_name[i],
            "f_readout": resonators_frequencies[i][0],
            "lo": resonators_frequencies[i][1],
            "rf_gain": 0,
            "rf_switch_mode": "on",
            "depletion_time": 10_000,
            "readout_pulse_length": 500,
            "optimal_pulse_length": 2_000,
            "readout_pulse_amp": 0.125,
            "rotation_angle": 0.0,
            "ge_threshold": 0.0,
            "wiring": {
                "controller": resonators_connectivity[0][2],
                "I": resonators_connectivity[0][0],
                "Q": resonators_connectivity[0][1],
            },
        }
    )
machine._save("quam_state.json", flat_data=False)