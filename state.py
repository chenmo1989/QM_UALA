import quam_sdk.constructor

# The system state is a high level abstraction of the experiment written in the language of physicists
# The structure is almost completely free
state = {
    "network": {"qop_ip": "192.168.88.254", "octave1_ip": "192.168.88.179", "qop_port": 80, "octave_port": 80, "cluster_name": 'DF5', "save_dir": ""},
    "qubits": [
        {
            "name": "q0",
            "f_01": 6341135416.0, 
            "lo": 6382000000.0,
            "rf_gain": 0,
            "rf_switch_mode": "on",
            "mixer_name": "octave_octave1_2",
            "anharmonicity": 250e6,
            "drag_coefficient": 0.0,
            "ac_stark_detuning": 0.0,
            "x180_length": 40,
            "x180_amp": 0.25,
            "pi_length": 40,
            "pi_amp": 0.25,
            "wiring": {
                "controller": "con1",
                "I": 3,
                "Q": 4,
            },
            "T1": 1230,
            "T2": 123,
        },
    ],
    "flux_lines": [
        {
            "name": "flux0",
            "flux_pulse_length": 16,
            "flux_pulse_amp": 0.125,
            "max_frequency_point": 0.0,
            "Z_delay": 19,
            "iswap": {
                "length": 16,
                "level": 0.075,
            },
            "wiring": {
                "controller": "con1",
                "port": 7,
                "filter": {"iir_taps": [], "fir_taps": []},
            },
        },
    ],
    "resonators": [
        {
            "name": "r0",
            "f_readout": 7.256e9,
            "lo": 7.206e9,
            "rf_gain": 0,
            "rf_switch_mode": "on",
            "depletion_time": 10_000,
            "readout_pulse_length": 500,
            "optimal_pulse_length": 2_000,
            "readout_pulse_amp": 0.125,
            "rotation_angle": 0.0,
            "ge_threshold": 0.0,
            "wiring": {
                "controller": "con1",
                "I": 1,
                "Q": 2,
            },
        },
    ],
    "global_parameters": {
        "time_of_flight": 304,
        "saturation_amp": 0.1,
        "saturation_len": 14000,
        "con1_downconversion_offset_I": 0.0,
        "con1_downconversion_offset_Q": 0.0,
        "con1_downconversion_gain": 0,
        "con2_downconversion_offset_I": 0.0,
        "con2_downconversion_offset_Q": 0.0,
        "con2_downconversion_gain": 0,
    },
}

# Now we use QuAM SDK to construct the Python class out of the state
quam_sdk.constructor.quamConstructor(state, flat_data=False)