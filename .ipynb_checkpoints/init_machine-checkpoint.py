from quam import QuAM

machine = QuAM("quam_bootstrap_state.json", flat_data=False)

qubits_name = ["q" + str(i) for i in range(1, 2)]
qubits_connectivity = [(5, 6, "con1")]
qubits_mixers_names = ["octave_octave1_3"]  # need to changed to reflect real connectivity
qubits_frequencies = [(6.386e9, 6.100e9)]
resonators_name = ["rr" + str(i) for i in range(1, 4)]
resonators_connectivity = [(1, 2, "con1")]
resonators_frequencies = [(7.256e9, 7.1e9), (6.999e9, 7.1e9), (6.875e9, 7.1e9)]
flux_lines_name = ["flux" + str(i) for i in range(1, 2)]
flux_lines_connectivity = [(8, "con1")]

for i in range(1):
    machine.qubits.append(
        {
            "name": qubits_name[i],
            "f_01": qubits_frequencies[i][0],
            "lo": qubits_frequencies[i][1],
            "rf_gain": 0,
            "rf_switch_mode": "on",
            "mixer_name": qubits_mixers_names[i],
            "anharmonicity": 250e6,
            "drag_coefficient": 0.0,
            "ac_stark_detuning": 0.0,
            "pi_length": 40,
            "pi_amp": 0.124,
            "wiring": {
                "controller": qubits_connectivity[i][2],
                "I": qubits_connectivity[i][0],
                "Q": qubits_connectivity[i][1],
            },
            "T1": 1230,
            "T2": 123,
        }
    )

    machine.flux_lines.append(
        {
            "name": flux_lines_name[i],
            "flux_pulse_length": 16,
            "flux_pulse_amp": 0.175,
            "max_frequency_point": 0.0,
            "iswap": {
                "length": 16,
                "level": 0.075,
            },
            "wiring": {
                "controller": flux_lines_connectivity[0][1],
                "port": flux_lines_connectivity[0][0],
                "filter": {"iir_taps": [], "fir_taps": []},
            },
        },
    )
for i in range(3):
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
            "readout_pulse_amp": 0.05,
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