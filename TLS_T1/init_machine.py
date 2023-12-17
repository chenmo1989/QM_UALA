from quam import QuAM

machine = QuAM("quam_bootstrap_state.json", flat_data = False)

qubits_name = ["q" + str(i) for i in range(1, 7)]
qubits_connectivity = [(3, 4, 3, "con1")]
qubits_mixers_names = ["octave_octave1_2"]
qubits_frequencies = [(6.289e9, 6.389e9),(6.107e9, 6.207e9),(5.982e9,6.082e9),(5.768e9,5.868e9),(5.567e9,5.667e9),(5.442e9,5.542e9)]
resonators_name = ["r" + str(i) for i in range(1, 7)]
resonators_connectivity = [(1, 2, 1, "con1")]
resonators_frequencies = [(7.130e9, 7.180e9), (6.999e9, 7.049e9), (6.875e9, 6.925e9),(6.217e9,6.267e9),(6.112e9,6.162e9),(6.018e9,6.068e9)]
flux_lines_name = ["flux" + str(i) for i in range(1, 7)]
flux_lines_connectivity = [(8, "con1"),(9, "con1"),(10, "con1"),(7, "con1"),(8, "con1"),(9, "con1")]
ROI = [38.0,38.0,36.0,40.0,42.0,40.0]
TWPA_freq = [6324E6,6324E6,6324E6,6730.6E6,6730.6E6,6730.6E6]
TWPA_pwr = [-10.0,-10.0,-10.0,-11.3,-11.3,-11.3]

for i in range(6):
    machine.qubits.append(
        {
            "name": qubits_name[i],
            "f_01": qubits_frequencies[i][0],
            "f_tls": [],
            "lo": qubits_frequencies[i][1],
            "rf_gain": 0,
            "rf_switch_mode": "on",
            "mixer_name": qubits_mixers_names[0],
            "anharmonicity": 250e6,
            "drag_coefficient": 0.0,
            "ac_stark_detuning": 0.0,
            "x180_length": 40,
            "x180_amp": 0.1,
            "pi_length": [40,80],
            "pi_amp": [0.05,0.02],
            "pi_length_tls": [200],
            "pi_amp_tls": [0.2],
            "T1": 1230,
            "T2": 123,
            "DC_tuning_curve": [0.0,0.0,0.0],
            "AC_tuning_curve": [0.0,0.0,0.0],
            "digital_marker": {
                "delay": 87,
                "buffer": 15,
            },
            "wiring": {
                "controller": qubits_connectivity[0][3],
                "I": qubits_connectivity[0][0],
                "Q": qubits_connectivity[0][1],
                "digital_marker": qubits_connectivity[0][2],
            },
        }
    )

    machine.flux_lines.append(
        {
            "name": flux_lines_name[i],
            "flux_pulse_length": 16,
            "flux_pulse_amp": 0.25,
            "max_frequency_point": 0.0,
            "Z_delay": 19,
            "dc_voltage": 0.0,
            "iswap": {
                "length": [16],
                "level": [0.2],
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
            "readout_pulse_amp": 0.5,
            "rotation_angle": 0.0,
            "ge_threshold": 0.0,
            "RO_attenuation": [ROI[i], 10],
            "TWPA": [TWPA_freq[i], TWPA_pwr[i]],
            "tuning_curve": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            "digital_marker": {
                "delay": 87,
                "buffer": 15,
            },
            "wiring": {
                "controller": resonators_connectivity[0][3],
                "I": resonators_connectivity[0][0],
                "Q": resonators_connectivity[0][1],
                "digital_marker": resonators_connectivity[0][2],
            },
        }
    )
machine._save("quam_state.json", flat_data=False)