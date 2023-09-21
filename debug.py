
# Single QUA script generated at 2023-09-19 15:02:59.333445
# QUA library version: 1.1.3

from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(int, )
    v3 = declare(int, )
    v4 = declare(fixed, )
    v5 = declare(fixed, )
    v6 = declare(fixed, )
    v7 = declare(int, )
    a1 = declare(fixed, value=[-0.5, -0.4, -0.30000000000000004, -0.20000000000000007, -0.10000000000000009, -1.1102230246251565e-16, 0.09999999999999987, 0.19999999999999984, 0.2999999999999998, 0.3999999999999998, 0.4999999999999998])
    a2 = declare(int, value=[6174864, 6256100, 6319511, 6365095, 6392853, 6402785, 6394891, 6369171, 6325625, 6264253, 6185055])
    with for_(v1,0,(v1<1000),(v1+1)):
        with for_each_((v4,v3),(a1,a2)):
            assign(v7, ((v3*1000)-6452785000.0))
            with for_(v2,-100000000,(v2<=90000000),(v2+10000000)):
                update_frequency("q0", (v7+v2), "Hz", False)
                play("const"*amp(v4), "flux0", duration=26)
                wait(5, "q0")
                play("pi", "q0")
                align("q0", "flux0", "r0")
                measure("readout", "r0", None, dual_demod.full("cos", "out1", "sin", "out2", v5), dual_demod.full("minus_sin", "out1", "cos", "out2", v6))
                align()
                play("const"*amp((-1*v4)), "flux0", duration=26)
                wait(2500, "r0")
                r1 = declare_stream()
                save(v5, r1)
                r2 = declare_stream()
                save(v6, r2)
        r3 = declare_stream()
        save(v1, r3)
    with stream_processing():
        r1.buffer(20).buffer(11).average().save("I")
        r2.buffer(20).buffer(11).average().save("Q")
        r3.save("iteration")


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                "1": {
                    "offset": -0.0067901611328125,
                },
                "2": {
                    "offset": -0.011688232421875,
                },
                "3": {
                    "offset": 0.01972198486328125,
                },
                "4": {
                    "offset": 0.053253173828125,
                },
                "5": {
                    "offset": 0.0,
                },
                "6": {
                    "offset": 0.0,
                },
                "7": {
                    "offset": 0.0,
                    "delay": 19,
                },
                "8": {
                    "offset": 0.0,
                    "delay": 19,
                },
                "9": {
                    "offset": 0.0,
                    "delay": 19,
                },
                "10": {
                    "offset": 0.0,
                    "delay": 19,
                },
            },
            "digital_outputs": {
                "1": {},
                "2": {},
                "3": {},
                "4": {},
                "5": {},
                "6": {},
                "7": {},
                "8": {},
                "9": {},
                "10": {},
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.009985,
                    "gain_db": 0,
                },
                "2": {
                    "offset": 0.013658,
                    "gain_db": 0,
                },
            },
        },
    },
    "elements": {
        "r0": {
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "lo_frequency": 7206000000.0,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": 56520000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q0",
            },
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 304,
            "smearing": 0,
        },
        "r1": {
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "lo_frequency": 7080000000.0,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": 50000000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q1",
            },
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 304,
            "smearing": 0,
        },
        "r2": {
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "lo_frequency": 6949000000.0,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": 50000000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q2",
            },
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 304,
            "smearing": 0,
        },
        "r3": {
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "lo_frequency": 6825000000.0,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": 50000000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q3",
            },
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 304,
            "smearing": 0,
        },
        "r4": {
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "lo_frequency": 6167000000.0,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": 50000000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q4",
            },
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 304,
            "smearing": 0,
        },
        "r5": {
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "lo_frequency": 6062000000.0,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": 50000000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q5",
            },
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 304,
            "smearing": 0,
        },
        "r6": {
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "lo_frequency": 5968000000.0,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": 50000000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q6",
            },
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 304,
            "smearing": 0,
        },
        "r0aux": {
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "lo_frequency": 7206000000.0,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": 56520000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q0",
            },
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 304,
            "smearing": 0,
        },
        "r1aux": {
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "lo_frequency": 7080000000.0,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": 50000000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q1",
            },
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 304,
            "smearing": 0,
        },
        "r2aux": {
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "lo_frequency": 6949000000.0,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": 50000000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q2",
            },
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 304,
            "smearing": 0,
        },
        "r3aux": {
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "lo_frequency": 6825000000.0,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": 50000000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q3",
            },
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 304,
            "smearing": 0,
        },
        "r4aux": {
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "lo_frequency": 6167000000.0,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": 50000000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q4",
            },
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 304,
            "smearing": 0,
        },
        "r5aux": {
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "lo_frequency": 6062000000.0,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": 50000000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q5",
            },
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 304,
            "smearing": 0,
        },
        "r6aux": {
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "lo_frequency": 5968000000.0,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": 50000000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q6",
            },
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 304,
            "smearing": 0,
        },
        "q0": {
            "mixInputs": {
                "I": ('con1', 3),
                "Q": ('con1', 4),
                "lo_frequency": 6452785000.0,
                "mixer": "octave_octave1_2",
            },
            "intermediate_frequency": -110924023.0,
            "operations": {
                "cw": "const_pulse",
                "pi": "pi_pulse0",
                "pi2": "pi_over_two_pulse0",
                "x180": "x180_pulse0",
                "x90": "x90_pulse0",
                "-x90": "-x90_pulse0",
                "y90": "y90_pulse0",
                "y180": "y180_pulse0",
                "-y90": "-y90_pulse0",
            },
        },
        "q1": {
            "mixInputs": {
                "I": ('con1', 3),
                "Q": ('con1', 4),
                "lo_frequency": 6189000000.0,
                "mixer": "octave_octave1_2",
            },
            "intermediate_frequency": 100000000.0,
            "operations": {
                "cw": "const_pulse",
                "pi": "pi_pulse1",
                "pi2": "pi_over_two_pulse1",
                "x180": "x180_pulse1",
                "x90": "x90_pulse1",
                "-x90": "-x90_pulse1",
                "y90": "y90_pulse1",
                "y180": "y180_pulse1",
                "-y90": "-y90_pulse1",
            },
        },
        "q2": {
            "mixInputs": {
                "I": ('con1', 3),
                "Q": ('con1', 4),
                "lo_frequency": 6007000000.0,
                "mixer": "octave_octave1_2",
            },
            "intermediate_frequency": 100000000.0,
            "operations": {
                "cw": "const_pulse",
                "pi": "pi_pulse2",
                "pi2": "pi_over_two_pulse2",
                "x180": "x180_pulse2",
                "x90": "x90_pulse2",
                "-x90": "-x90_pulse2",
                "y90": "y90_pulse2",
                "y180": "y180_pulse2",
                "-y90": "-y90_pulse2",
            },
        },
        "q3": {
            "mixInputs": {
                "I": ('con1', 3),
                "Q": ('con1', 4),
                "lo_frequency": 5882000000.0,
                "mixer": "octave_octave1_2",
            },
            "intermediate_frequency": 100000000.0,
            "operations": {
                "cw": "const_pulse",
                "pi": "pi_pulse3",
                "pi2": "pi_over_two_pulse3",
                "x180": "x180_pulse3",
                "x90": "x90_pulse3",
                "-x90": "-x90_pulse3",
                "y90": "y90_pulse3",
                "y180": "y180_pulse3",
                "-y90": "-y90_pulse3",
            },
        },
        "q4": {
            "mixInputs": {
                "I": ('con1', 3),
                "Q": ('con1', 4),
                "lo_frequency": 5668000000.0,
                "mixer": "octave_octave1_2",
            },
            "intermediate_frequency": 100000000.0,
            "operations": {
                "cw": "const_pulse",
                "pi": "pi_pulse4",
                "pi2": "pi_over_two_pulse4",
                "x180": "x180_pulse4",
                "x90": "x90_pulse4",
                "-x90": "-x90_pulse4",
                "y90": "y90_pulse4",
                "y180": "y180_pulse4",
                "-y90": "-y90_pulse4",
            },
        },
        "q5": {
            "mixInputs": {
                "I": ('con1', 3),
                "Q": ('con1', 4),
                "lo_frequency": 5467000000.0,
                "mixer": "octave_octave1_2",
            },
            "intermediate_frequency": 100000000.0,
            "operations": {
                "cw": "const_pulse",
                "pi": "pi_pulse5",
                "pi2": "pi_over_two_pulse5",
                "x180": "x180_pulse5",
                "x90": "x90_pulse5",
                "-x90": "-x90_pulse5",
                "y90": "y90_pulse5",
                "y180": "y180_pulse5",
                "-y90": "-y90_pulse5",
            },
        },
        "q6": {
            "mixInputs": {
                "I": ('con1', 3),
                "Q": ('con1', 4),
                "lo_frequency": 5342000000.0,
                "mixer": "octave_octave1_2",
            },
            "intermediate_frequency": 100000000.0,
            "operations": {
                "cw": "const_pulse",
                "pi": "pi_pulse6",
                "pi2": "pi_over_two_pulse6",
                "x180": "x180_pulse6",
                "x90": "x90_pulse6",
                "-x90": "-x90_pulse6",
                "y90": "y90_pulse6",
                "y180": "y180_pulse6",
                "-y90": "-y90_pulse6",
            },
        },
        "flux0": {
            "singleInput": {
                "port": ('con1', 7),
            },
            "operations": {
                "const": "const_flux_pulse0",
            },
        },
        "flux1": {
            "singleInput": {
                "port": ('con1', 8),
            },
            "operations": {
                "const": "const_flux_pulse1",
            },
        },
        "flux2": {
            "singleInput": {
                "port": ('con1', 9),
            },
            "operations": {
                "const": "const_flux_pulse2",
            },
        },
        "flux3": {
            "singleInput": {
                "port": ('con1', 10),
            },
            "operations": {
                "const": "const_flux_pulse3",
            },
        },
        "flux4": {
            "singleInput": {
                "port": ('con1', 7),
            },
            "operations": {
                "const": "const_flux_pulse4",
            },
        },
        "flux5": {
            "singleInput": {
                "port": ('con1', 8),
            },
            "operations": {
                "const": "const_flux_pulse5",
            },
        },
        "flux6": {
            "singleInput": {
                "port": ('con1', 9),
            },
            "operations": {
                "const": "const_flux_pulse6",
            },
        },
    },
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "const_flux_pulse0": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "const_flux0_wf",
            },
        },
        "const_flux_pulse1": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "const_flux1_wf",
            },
        },
        "const_flux_pulse2": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "const_flux2_wf",
            },
        },
        "const_flux_pulse3": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "const_flux3_wf",
            },
        },
        "const_flux_pulse4": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "const_flux4_wf",
            },
        },
        "const_flux_pulse5": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "const_flux5_wf",
            },
        },
        "const_flux_pulse6": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "const_flux6_wf",
            },
        },
        "readout_pulse_q0": {
            "operation": "measurement",
            "length": 500,
            "waveforms": {
                "I": "readout0_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights0",
                "sin": "sine_weights0",
                "minus_sin": "minus_sine_weights0",
                "rotated_cos": "rotated_cosine_weights0",
                "rotated_sin": "rotated_sine_weights0",
                "rotated_minus_sin": "rotated_minus_sine_weights0",
                "opt_cos": "opt_cosine_weights0",
                "opt_sin": "opt_sine_weights0",
                "opt_minus_sin": "opt_minus_sine_weights0",
            },
            "digital_marker": "ON",
        },
        "readout_pulse_q1": {
            "operation": "measurement",
            "length": 500,
            "waveforms": {
                "I": "readout1_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights1",
                "sin": "sine_weights1",
                "minus_sin": "minus_sine_weights1",
                "rotated_cos": "rotated_cosine_weights1",
                "rotated_sin": "rotated_sine_weights1",
                "rotated_minus_sin": "rotated_minus_sine_weights1",
                "opt_cos": "opt_cosine_weights1",
                "opt_sin": "opt_sine_weights1",
                "opt_minus_sin": "opt_minus_sine_weights1",
            },
            "digital_marker": "ON",
        },
        "readout_pulse_q2": {
            "operation": "measurement",
            "length": 500,
            "waveforms": {
                "I": "readout2_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights2",
                "sin": "sine_weights2",
                "minus_sin": "minus_sine_weights2",
                "rotated_cos": "rotated_cosine_weights2",
                "rotated_sin": "rotated_sine_weights2",
                "rotated_minus_sin": "rotated_minus_sine_weights2",
                "opt_cos": "opt_cosine_weights2",
                "opt_sin": "opt_sine_weights2",
                "opt_minus_sin": "opt_minus_sine_weights2",
            },
            "digital_marker": "ON",
        },
        "readout_pulse_q3": {
            "operation": "measurement",
            "length": 500,
            "waveforms": {
                "I": "readout3_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights3",
                "sin": "sine_weights3",
                "minus_sin": "minus_sine_weights3",
                "rotated_cos": "rotated_cosine_weights3",
                "rotated_sin": "rotated_sine_weights3",
                "rotated_minus_sin": "rotated_minus_sine_weights3",
                "opt_cos": "opt_cosine_weights3",
                "opt_sin": "opt_sine_weights3",
                "opt_minus_sin": "opt_minus_sine_weights3",
            },
            "digital_marker": "ON",
        },
        "readout_pulse_q4": {
            "operation": "measurement",
            "length": 500,
            "waveforms": {
                "I": "readout4_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights4",
                "sin": "sine_weights4",
                "minus_sin": "minus_sine_weights4",
                "rotated_cos": "rotated_cosine_weights4",
                "rotated_sin": "rotated_sine_weights4",
                "rotated_minus_sin": "rotated_minus_sine_weights4",
                "opt_cos": "opt_cosine_weights4",
                "opt_sin": "opt_sine_weights4",
                "opt_minus_sin": "opt_minus_sine_weights4",
            },
            "digital_marker": "ON",
        },
        "readout_pulse_q5": {
            "operation": "measurement",
            "length": 500,
            "waveforms": {
                "I": "readout5_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights5",
                "sin": "sine_weights5",
                "minus_sin": "minus_sine_weights5",
                "rotated_cos": "rotated_cosine_weights5",
                "rotated_sin": "rotated_sine_weights5",
                "rotated_minus_sin": "rotated_minus_sine_weights5",
                "opt_cos": "opt_cosine_weights5",
                "opt_sin": "opt_sine_weights5",
                "opt_minus_sin": "opt_minus_sine_weights5",
            },
            "digital_marker": "ON",
        },
        "readout_pulse_q6": {
            "operation": "measurement",
            "length": 500,
            "waveforms": {
                "I": "readout6_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights6",
                "sin": "sine_weights6",
                "minus_sin": "minus_sine_weights6",
                "rotated_cos": "rotated_cosine_weights6",
                "rotated_sin": "rotated_sine_weights6",
                "rotated_minus_sin": "rotated_minus_sine_weights6",
                "opt_cos": "opt_cosine_weights6",
                "opt_sin": "opt_sine_weights6",
                "opt_minus_sin": "opt_minus_sine_weights6",
            },
            "digital_marker": "ON",
        },
        "pi_pulse0": {
            "operation": "control",
            "length": 64,
            "waveforms": {
                "I": "pi_wf0",
                "Q": "zero_wf",
            },
        },
        "pi_pulse1": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "pi_wf1",
                "Q": "zero_wf",
            },
        },
        "pi_pulse2": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "pi_wf2",
                "Q": "zero_wf",
            },
        },
        "pi_pulse3": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "pi_wf3",
                "Q": "zero_wf",
            },
        },
        "pi_pulse4": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "pi_wf4",
                "Q": "zero_wf",
            },
        },
        "pi_pulse5": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "pi_wf5",
                "Q": "zero_wf",
            },
        },
        "pi_pulse6": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "pi_wf6",
                "Q": "zero_wf",
            },
        },
        "pi_over_two_pulse0": {
            "operation": "control",
            "length": 64,
            "waveforms": {
                "I": "pi_over_two_wf0",
                "Q": "zero_wf",
            },
        },
        "pi_over_two_pulse1": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "pi_over_two_wf1",
                "Q": "zero_wf",
            },
        },
        "pi_over_two_pulse2": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "pi_over_two_wf2",
                "Q": "zero_wf",
            },
        },
        "pi_over_two_pulse3": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "pi_over_two_wf3",
                "Q": "zero_wf",
            },
        },
        "pi_over_two_pulse4": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "pi_over_two_wf4",
                "Q": "zero_wf",
            },
        },
        "pi_over_two_pulse5": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "pi_over_two_wf5",
                "Q": "zero_wf",
            },
        },
        "pi_over_two_pulse6": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "pi_over_two_wf6",
                "Q": "zero_wf",
            },
        },
        "x90_pulse0": {
            "operation": "control",
            "length": 180,
            "waveforms": {
                "I": "x90_I_wf0",
                "Q": "x90_Q_wf0",
            },
        },
        "x90_pulse1": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "x90_I_wf1",
                "Q": "x90_Q_wf1",
            },
        },
        "x90_pulse2": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "x90_I_wf2",
                "Q": "x90_Q_wf2",
            },
        },
        "x90_pulse3": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "x90_I_wf3",
                "Q": "x90_Q_wf3",
            },
        },
        "x90_pulse4": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "x90_I_wf4",
                "Q": "x90_Q_wf4",
            },
        },
        "x90_pulse5": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "x90_I_wf5",
                "Q": "x90_Q_wf5",
            },
        },
        "x90_pulse6": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "x90_I_wf6",
                "Q": "x90_Q_wf6",
            },
        },
        "x180_pulse0": {
            "operation": "control",
            "length": 180,
            "waveforms": {
                "I": "x180_I_wf0",
                "Q": "x180_Q_wf0",
            },
        },
        "x180_pulse1": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "x180_I_wf1",
                "Q": "x180_Q_wf1",
            },
        },
        "x180_pulse2": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "x180_I_wf2",
                "Q": "x180_Q_wf2",
            },
        },
        "x180_pulse3": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "x180_I_wf3",
                "Q": "x180_Q_wf3",
            },
        },
        "x180_pulse4": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "x180_I_wf4",
                "Q": "x180_Q_wf4",
            },
        },
        "x180_pulse5": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "x180_I_wf5",
                "Q": "x180_Q_wf5",
            },
        },
        "x180_pulse6": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "x180_I_wf6",
                "Q": "x180_Q_wf6",
            },
        },
        "-x90_pulse0": {
            "operation": "control",
            "length": 180,
            "waveforms": {
                "I": "minus_x90_I_wf0",
                "Q": "minus_x90_Q_wf0",
            },
        },
        "-x90_pulse1": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "minus_x90_I_wf1",
                "Q": "minus_x90_Q_wf1",
            },
        },
        "-x90_pulse2": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "minus_x90_I_wf2",
                "Q": "minus_x90_Q_wf2",
            },
        },
        "-x90_pulse3": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "minus_x90_I_wf3",
                "Q": "minus_x90_Q_wf3",
            },
        },
        "-x90_pulse4": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "minus_x90_I_wf4",
                "Q": "minus_x90_Q_wf4",
            },
        },
        "-x90_pulse5": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "minus_x90_I_wf5",
                "Q": "minus_x90_Q_wf5",
            },
        },
        "-x90_pulse6": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "minus_x90_I_wf6",
                "Q": "minus_x90_Q_wf6",
            },
        },
        "y90_pulse0": {
            "operation": "control",
            "length": 180,
            "waveforms": {
                "I": "y90_I_wf0",
                "Q": "y90_Q_wf0",
            },
        },
        "y90_pulse1": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "y90_I_wf1",
                "Q": "y90_Q_wf1",
            },
        },
        "y90_pulse2": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "y90_I_wf2",
                "Q": "y90_Q_wf2",
            },
        },
        "y90_pulse3": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "y90_I_wf3",
                "Q": "y90_Q_wf3",
            },
        },
        "y90_pulse4": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "y90_I_wf4",
                "Q": "y90_Q_wf4",
            },
        },
        "y90_pulse5": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "y90_I_wf5",
                "Q": "y90_Q_wf5",
            },
        },
        "y90_pulse6": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "y90_I_wf6",
                "Q": "y90_Q_wf6",
            },
        },
        "y180_pulse0": {
            "operation": "control",
            "length": 180,
            "waveforms": {
                "I": "y180_I_wf0",
                "Q": "y180_Q_wf0",
            },
        },
        "y180_pulse1": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "y180_I_wf1",
                "Q": "y180_Q_wf1",
            },
        },
        "y180_pulse2": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "y180_I_wf2",
                "Q": "y180_Q_wf2",
            },
        },
        "y180_pulse3": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "y180_I_wf3",
                "Q": "y180_Q_wf3",
            },
        },
        "y180_pulse4": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "y180_I_wf4",
                "Q": "y180_Q_wf4",
            },
        },
        "y180_pulse5": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "y180_I_wf5",
                "Q": "y180_Q_wf5",
            },
        },
        "y180_pulse6": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "y180_I_wf6",
                "Q": "y180_Q_wf6",
            },
        },
        "-y90_pulse0": {
            "operation": "control",
            "length": 180,
            "waveforms": {
                "I": "minus_y90_I_wf0",
                "Q": "minus_y90_Q_wf0",
            },
        },
        "-y90_pulse1": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "minus_y90_I_wf1",
                "Q": "minus_y90_Q_wf1",
            },
        },
        "-y90_pulse2": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "minus_y90_I_wf2",
                "Q": "minus_y90_Q_wf2",
            },
        },
        "-y90_pulse3": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "minus_y90_I_wf3",
                "Q": "minus_y90_Q_wf3",
            },
        },
        "-y90_pulse4": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "minus_y90_I_wf4",
                "Q": "minus_y90_Q_wf4",
            },
        },
        "-y90_pulse5": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "minus_y90_I_wf5",
                "Q": "minus_y90_Q_wf5",
            },
        },
        "-y90_pulse6": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "minus_y90_I_wf6",
                "Q": "minus_y90_Q_wf6",
            },
        },
    },
    "waveforms": {
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "const_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "const_flux0_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "const_flux1_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "const_flux2_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "const_flux3_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "const_flux4_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "const_flux5_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "const_flux6_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "readout0_wf": {
            "type": "constant",
            "sample": 0.3,
        },
        "readout1_wf": {
            "type": "constant",
            "sample": 0.3,
        },
        "readout2_wf": {
            "type": "constant",
            "sample": 0.3,
        },
        "readout3_wf": {
            "type": "constant",
            "sample": 0.3,
        },
        "readout4_wf": {
            "type": "constant",
            "sample": 0.3,
        },
        "readout5_wf": {
            "type": "constant",
            "sample": 0.3,
        },
        "readout6_wf": {
            "type": "constant",
            "sample": 0.3,
        },
        "pi_wf0": {
            "type": "constant",
            "sample": 0.1092,
        },
        "pi_wf1": {
            "type": "constant",
            "sample": 0.25,
        },
        "pi_wf2": {
            "type": "constant",
            "sample": 0.25,
        },
        "pi_wf3": {
            "type": "constant",
            "sample": 0.25,
        },
        "pi_wf4": {
            "type": "constant",
            "sample": 0.25,
        },
        "pi_wf5": {
            "type": "constant",
            "sample": 0.25,
        },
        "pi_wf6": {
            "type": "constant",
            "sample": 0.25,
        },
        "pi_over_two_wf0": {
            "type": "constant",
            "sample": 0.0546,
        },
        "pi_over_two_wf1": {
            "type": "constant",
            "sample": 0.125,
        },
        "pi_over_two_wf2": {
            "type": "constant",
            "sample": 0.125,
        },
        "pi_over_two_wf3": {
            "type": "constant",
            "sample": 0.125,
        },
        "pi_over_two_wf4": {
            "type": "constant",
            "sample": 0.125,
        },
        "pi_over_two_wf5": {
            "type": "constant",
            "sample": 0.125,
        },
        "pi_over_two_wf6": {
            "type": "constant",
            "sample": 0.125,
        },
        "x90_I_wf0": {
            "type": "arbitrary",
            "samples": [0.0, 0.00040416620465755834, 0.0008320318708446434, 0.0012845788945819647, 0.001762798661865914, 0.002267689544406204, 0.002800254194721963, 0.0033614966397724627, 0.0039524191733662575, 0.004574019048730957, 0.005227284973831431, 0.005913193413293454, 0.0066327047021169545, 0.007386758977742835, 0.008176271938463344, 0.009002130437630656, 0.009865187924613631, 0.01076625974497014, 0.011706118313832137, 0.012685488178032564, 0.013705040984026638, 0.01476539037016362, 0.015867086803336754, 0.01701061238146674, 0.01819637562464483, 0.01942470627906296, 0.020695850159076677, 0.02200996405386956, 0.02336711072620154, 0.02476725403161595, 0.026210254187238206, 0.02769586321991057, 0.029223720623861513, 0.030793349258393096, 0.032404151516175934, 0.03405540579265952, 0.03574626328682754, 0.037475745163046886, 0.039242740103069274, 0.04104600227634162, 0.04288414975566317, 0.04475566340389212, 0.04665888625585296, 0.04859202341783009, 0.05055314250505774, 0.05254017463543585, 0.054550915995324765, 0.05658302999070759, 0.058634049994269, 0.060701382696035804, 0.06278231206217397, 0.06487400390335323, 0.06697351105079447, 0.06907777913472397, 0.07118365295649506, 0.07328788344212264, 0.07538713516143358, 0.07747799439348926, 0.07955697771541118, 0.08162054108826197, 0.08366508941022711, 0.085686986504034, 0.0876825655023604, 0.08964813959194799, 0.09158001307427546, 0.09347449269798133, 0.09532789921578447, 0.09713657911645074, 0.09889691648041778, 0.10060534490603643, 0.10225835945203246, 0.10385252854075183, 0.1053845057660392, 0.1068510415492232, 0.1082489945866514, 0.10957534303253762, 0.1108271953615586, 0.112001800856664, 0.1130965596689426, 0.11410903239811193, 0.11503694914426066, 0.11587821798386094, 0.11663093282577114, 0.11729338060594716, 0.11786404778285947, 0.1183416260991481, 0.11872501757881927, 0.11901333873326818, 0.11920592395357711] + [0.11930232807085857] * 2 + [0.11920592395357711, 0.11901333873326818, 0.11872501757881927, 0.1183416260991481, 0.11786404778285947, 0.11729338060594716, 0.11663093282577114, 0.11587821798386094, 0.11503694914426066, 0.11410903239811193, 0.1130965596689426, 0.112001800856664, 0.1108271953615586, 0.10957534303253762, 0.1082489945866514, 0.1068510415492232, 0.1053845057660392, 0.10385252854075183, 0.10225835945203246, 0.10060534490603643, 0.09889691648041778, 0.09713657911645074, 0.09532789921578447, 0.09347449269798133, 0.09158001307427546, 0.08964813959194799, 0.0876825655023604, 0.085686986504034, 0.08366508941022711, 0.08162054108826197, 0.07955697771541118, 0.07747799439348926, 0.07538713516143358, 0.07328788344212264, 0.07118365295649506, 0.06907777913472397, 0.06697351105079447, 0.06487400390335323, 0.06278231206217397, 0.060701382696035804, 0.058634049994269, 0.05658302999070759, 0.054550915995324765, 0.05254017463543585, 0.05055314250505774, 0.04859202341783009, 0.04665888625585296, 0.04475566340389212, 0.04288414975566317, 0.04104600227634162, 0.039242740103069274, 0.037475745163046886, 0.03574626328682754, 0.03405540579265952, 0.032404151516175934, 0.030793349258393096, 0.029223720623861513, 0.02769586321991057, 0.026210254187238206, 0.02476725403161595, 0.02336711072620154, 0.02200996405386956, 0.020695850159076677, 0.01942470627906296, 0.01819637562464483, 0.01701061238146674, 0.015867086803336754, 0.01476539037016362, 0.013705040984026638, 0.012685488178032564, 0.011706118313832137, 0.01076625974497014, 0.009865187924613631, 0.009002130437630656, 0.008176271938463344, 0.007386758977742835, 0.0066327047021169545, 0.005913193413293454, 0.005227284973831431, 0.004574019048730957, 0.0039524191733662575, 0.0033614966397724627, 0.002800254194721963, 0.002267689544406204, 0.001762798661865914, 0.0012845788945819647, 0.0008320318708446434, 0.00040416620465755834, 0.0],
        },
        "x90_I_wf1": {
            "type": "arbitrary",
            "samples": [0.0, 0.0022150469433227073, 0.005015813123173687, 0.008491584753998697, 0.012723560920712553, 0.017776666404548624, 0.023690402987698853, 0.030469425725473138, 0.03807475022143508, 0.04641664910656638, 0.05535034039512257, 0.06467547541850178, 0.0741401843068172, 0.08345003991731476, 0.09228178991126627, 0.10030113887181125, 0.10718331324880155, 0.11263469369056484, 0.11641352732340533] + [0.11834769134210223] * 2 + [0.11641352732340533, 0.11263469369056484, 0.10718331324880155, 0.10030113887181125, 0.09228178991126627, 0.08345003991731476, 0.0741401843068172, 0.06467547541850178, 0.05535034039512257, 0.04641664910656638, 0.03807475022143508, 0.030469425725473138, 0.023690402987698853, 0.017776666404548624, 0.012723560920712553, 0.008491584753998697, 0.005015813123173687, 0.0022150469433227073, 0.0],
        },
        "x90_I_wf2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0022150469433227073, 0.005015813123173687, 0.008491584753998697, 0.012723560920712553, 0.017776666404548624, 0.023690402987698853, 0.030469425725473138, 0.03807475022143508, 0.04641664910656638, 0.05535034039512257, 0.06467547541850178, 0.0741401843068172, 0.08345003991731476, 0.09228178991126627, 0.10030113887181125, 0.10718331324880155, 0.11263469369056484, 0.11641352732340533] + [0.11834769134210223] * 2 + [0.11641352732340533, 0.11263469369056484, 0.10718331324880155, 0.10030113887181125, 0.09228178991126627, 0.08345003991731476, 0.0741401843068172, 0.06467547541850178, 0.05535034039512257, 0.04641664910656638, 0.03807475022143508, 0.030469425725473138, 0.023690402987698853, 0.017776666404548624, 0.012723560920712553, 0.008491584753998697, 0.005015813123173687, 0.0022150469433227073, 0.0],
        },
        "x90_I_wf3": {
            "type": "arbitrary",
            "samples": [0.0, 0.0022150469433227073, 0.005015813123173687, 0.008491584753998697, 0.012723560920712553, 0.017776666404548624, 0.023690402987698853, 0.030469425725473138, 0.03807475022143508, 0.04641664910656638, 0.05535034039512257, 0.06467547541850178, 0.0741401843068172, 0.08345003991731476, 0.09228178991126627, 0.10030113887181125, 0.10718331324880155, 0.11263469369056484, 0.11641352732340533] + [0.11834769134210223] * 2 + [0.11641352732340533, 0.11263469369056484, 0.10718331324880155, 0.10030113887181125, 0.09228178991126627, 0.08345003991731476, 0.0741401843068172, 0.06467547541850178, 0.05535034039512257, 0.04641664910656638, 0.03807475022143508, 0.030469425725473138, 0.023690402987698853, 0.017776666404548624, 0.012723560920712553, 0.008491584753998697, 0.005015813123173687, 0.0022150469433227073, 0.0],
        },
        "x90_I_wf4": {
            "type": "arbitrary",
            "samples": [0.0, 0.0022150469433227073, 0.005015813123173687, 0.008491584753998697, 0.012723560920712553, 0.017776666404548624, 0.023690402987698853, 0.030469425725473138, 0.03807475022143508, 0.04641664910656638, 0.05535034039512257, 0.06467547541850178, 0.0741401843068172, 0.08345003991731476, 0.09228178991126627, 0.10030113887181125, 0.10718331324880155, 0.11263469369056484, 0.11641352732340533] + [0.11834769134210223] * 2 + [0.11641352732340533, 0.11263469369056484, 0.10718331324880155, 0.10030113887181125, 0.09228178991126627, 0.08345003991731476, 0.0741401843068172, 0.06467547541850178, 0.05535034039512257, 0.04641664910656638, 0.03807475022143508, 0.030469425725473138, 0.023690402987698853, 0.017776666404548624, 0.012723560920712553, 0.008491584753998697, 0.005015813123173687, 0.0022150469433227073, 0.0],
        },
        "x90_I_wf5": {
            "type": "arbitrary",
            "samples": [0.0, 0.0022150469433227073, 0.005015813123173687, 0.008491584753998697, 0.012723560920712553, 0.017776666404548624, 0.023690402987698853, 0.030469425725473138, 0.03807475022143508, 0.04641664910656638, 0.05535034039512257, 0.06467547541850178, 0.0741401843068172, 0.08345003991731476, 0.09228178991126627, 0.10030113887181125, 0.10718331324880155, 0.11263469369056484, 0.11641352732340533] + [0.11834769134210223] * 2 + [0.11641352732340533, 0.11263469369056484, 0.10718331324880155, 0.10030113887181125, 0.09228178991126627, 0.08345003991731476, 0.0741401843068172, 0.06467547541850178, 0.05535034039512257, 0.04641664910656638, 0.03807475022143508, 0.030469425725473138, 0.023690402987698853, 0.017776666404548624, 0.012723560920712553, 0.008491584753998697, 0.005015813123173687, 0.0022150469433227073, 0.0],
        },
        "x90_I_wf6": {
            "type": "arbitrary",
            "samples": [0.0, 0.0022150469433227073, 0.005015813123173687, 0.008491584753998697, 0.012723560920712553, 0.017776666404548624, 0.023690402987698853, 0.030469425725473138, 0.03807475022143508, 0.04641664910656638, 0.05535034039512257, 0.06467547541850178, 0.0741401843068172, 0.08345003991731476, 0.09228178991126627, 0.10030113887181125, 0.10718331324880155, 0.11263469369056484, 0.11641352732340533] + [0.11834769134210223] * 2 + [0.11641352732340533, 0.11263469369056484, 0.10718331324880155, 0.10030113887181125, 0.09228178991126627, 0.08345003991731476, 0.0741401843068172, 0.06467547541850178, 0.05535034039512257, 0.04641664910656638, 0.03807475022143508, 0.030469425725473138, 0.023690402987698853, 0.017776666404548624, 0.012723560920712553, 0.008491584753998697, 0.005015813123173687, 0.0022150469433227073, 0.0],
        },
        "x90_Q_wf0": {
            "type": "arbitrary",
            "samples": [0.0] * 180,
        },
        "x90_Q_wf1": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "x90_Q_wf2": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "x90_Q_wf3": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "x90_Q_wf4": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "x90_Q_wf5": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "x90_Q_wf6": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "x180_I_wf0": {
            "type": "arbitrary",
            "samples": [0.0, 0.0008083324093151167, 0.0016640637416892867, 0.0025691577891639294, 0.003525597323731828, 0.004535379088812408, 0.005600508389443926, 0.006722993279544925, 0.007904838346732515, 0.009148038097461914, 0.010454569947662862, 0.011826386826586908, 0.013265409404233909, 0.01477351795548567, 0.016352543876926688, 0.018004260875261312, 0.019730375849227263, 0.02153251948994028, 0.023412236627664274, 0.02537097635606513, 0.027410081968053276, 0.02953078074032724, 0.03173417360667351, 0.03402122476293348, 0.03639275124928966, 0.03884941255812592, 0.041391700318153354, 0.04401992810773912, 0.04673422145240308, 0.0495345080632319, 0.05242050837447641, 0.05539172643982114, 0.058447441247723025, 0.06158669851678619, 0.06480830303235187, 0.06811081158531904, 0.07149252657365508, 0.07495149032609377, 0.07848548020613855, 0.08209200455268324, 0.08576829951132633, 0.08951132680778424, 0.09331777251170592, 0.09718404683566018, 0.10110628501011548, 0.1050803492708717, 0.10910183199064953, 0.11316605998141518, 0.117268099988538, 0.12140276539207161, 0.12556462412434793, 0.12974800780670645, 0.13394702210158893, 0.13815555826944795, 0.14236730591299013, 0.14657576688424528, 0.15077427032286717, 0.15495598878697853, 0.15911395543082235, 0.16324108217652394, 0.16733017882045423, 0.171373973008068, 0.1753651310047208, 0.17929627918389598, 0.18316002614855093, 0.18694898539596266, 0.19065579843156893, 0.19427315823290148, 0.19779383296083555, 0.20121068981207285, 0.20451671890406492, 0.20770505708150366, 0.2107690115320784, 0.2137020830984464, 0.2164979891733028, 0.21915068606507523, 0.2216543907231172, 0.224003601713328, 0.2261931193378852, 0.22821806479622386, 0.23007389828852132, 0.23175643596772189, 0.23326186565154228, 0.2345867612118943, 0.23572809556571894, 0.2366832521982962, 0.23745003515763854, 0.23802667746653636, 0.23841184790715422] + [0.23860465614171714] * 2 + [0.23841184790715422, 0.23802667746653636, 0.23745003515763854, 0.2366832521982962, 0.23572809556571894, 0.2345867612118943, 0.23326186565154228, 0.23175643596772189, 0.23007389828852132, 0.22821806479622386, 0.2261931193378852, 0.224003601713328, 0.2216543907231172, 0.21915068606507523, 0.2164979891733028, 0.2137020830984464, 0.2107690115320784, 0.20770505708150366, 0.20451671890406492, 0.20121068981207285, 0.19779383296083555, 0.19427315823290148, 0.19065579843156893, 0.18694898539596266, 0.18316002614855093, 0.17929627918389598, 0.1753651310047208, 0.171373973008068, 0.16733017882045423, 0.16324108217652394, 0.15911395543082235, 0.15495598878697853, 0.15077427032286717, 0.14657576688424528, 0.14236730591299013, 0.13815555826944795, 0.13394702210158893, 0.12974800780670645, 0.12556462412434793, 0.12140276539207161, 0.117268099988538, 0.11316605998141518, 0.10910183199064953, 0.1050803492708717, 0.10110628501011548, 0.09718404683566018, 0.09331777251170592, 0.08951132680778424, 0.08576829951132633, 0.08209200455268324, 0.07848548020613855, 0.07495149032609377, 0.07149252657365508, 0.06811081158531904, 0.06480830303235187, 0.06158669851678619, 0.058447441247723025, 0.05539172643982114, 0.05242050837447641, 0.0495345080632319, 0.04673422145240308, 0.04401992810773912, 0.041391700318153354, 0.03884941255812592, 0.03639275124928966, 0.03402122476293348, 0.03173417360667351, 0.02953078074032724, 0.027410081968053276, 0.02537097635606513, 0.023412236627664274, 0.02153251948994028, 0.019730375849227263, 0.018004260875261312, 0.016352543876926688, 0.01477351795548567, 0.013265409404233909, 0.011826386826586908, 0.010454569947662862, 0.009148038097461914, 0.007904838346732515, 0.006722993279544925, 0.005600508389443926, 0.004535379088812408, 0.003525597323731828, 0.0025691577891639294, 0.0016640637416892867, 0.0008083324093151167, 0.0],
        },
        "x180_I_wf1": {
            "type": "arbitrary",
            "samples": [0.0, 0.004430093886645415, 0.010031626246347373, 0.016983169507997393, 0.025447121841425106, 0.03555333280909725, 0.047380805975397705, 0.060938851450946276, 0.07614950044287017, 0.09283329821313276, 0.11070068079024514, 0.12935095083700357, 0.1482803686136344, 0.1669000798346295, 0.18456357982253255, 0.2006022777436225, 0.2143666264976031, 0.22526938738112967, 0.23282705464681067] + [0.23669538268420445] * 2 + [0.23282705464681067, 0.22526938738112967, 0.2143666264976031, 0.2006022777436225, 0.18456357982253255, 0.1669000798346295, 0.1482803686136344, 0.12935095083700357, 0.11070068079024514, 0.09283329821313276, 0.07614950044287017, 0.060938851450946276, 0.047380805975397705, 0.03555333280909725, 0.025447121841425106, 0.016983169507997393, 0.010031626246347373, 0.004430093886645415, 0.0],
        },
        "x180_I_wf2": {
            "type": "arbitrary",
            "samples": [0.0, 0.004430093886645415, 0.010031626246347373, 0.016983169507997393, 0.025447121841425106, 0.03555333280909725, 0.047380805975397705, 0.060938851450946276, 0.07614950044287017, 0.09283329821313276, 0.11070068079024514, 0.12935095083700357, 0.1482803686136344, 0.1669000798346295, 0.18456357982253255, 0.2006022777436225, 0.2143666264976031, 0.22526938738112967, 0.23282705464681067] + [0.23669538268420445] * 2 + [0.23282705464681067, 0.22526938738112967, 0.2143666264976031, 0.2006022777436225, 0.18456357982253255, 0.1669000798346295, 0.1482803686136344, 0.12935095083700357, 0.11070068079024514, 0.09283329821313276, 0.07614950044287017, 0.060938851450946276, 0.047380805975397705, 0.03555333280909725, 0.025447121841425106, 0.016983169507997393, 0.010031626246347373, 0.004430093886645415, 0.0],
        },
        "x180_I_wf3": {
            "type": "arbitrary",
            "samples": [0.0, 0.004430093886645415, 0.010031626246347373, 0.016983169507997393, 0.025447121841425106, 0.03555333280909725, 0.047380805975397705, 0.060938851450946276, 0.07614950044287017, 0.09283329821313276, 0.11070068079024514, 0.12935095083700357, 0.1482803686136344, 0.1669000798346295, 0.18456357982253255, 0.2006022777436225, 0.2143666264976031, 0.22526938738112967, 0.23282705464681067] + [0.23669538268420445] * 2 + [0.23282705464681067, 0.22526938738112967, 0.2143666264976031, 0.2006022777436225, 0.18456357982253255, 0.1669000798346295, 0.1482803686136344, 0.12935095083700357, 0.11070068079024514, 0.09283329821313276, 0.07614950044287017, 0.060938851450946276, 0.047380805975397705, 0.03555333280909725, 0.025447121841425106, 0.016983169507997393, 0.010031626246347373, 0.004430093886645415, 0.0],
        },
        "x180_I_wf4": {
            "type": "arbitrary",
            "samples": [0.0, 0.004430093886645415, 0.010031626246347373, 0.016983169507997393, 0.025447121841425106, 0.03555333280909725, 0.047380805975397705, 0.060938851450946276, 0.07614950044287017, 0.09283329821313276, 0.11070068079024514, 0.12935095083700357, 0.1482803686136344, 0.1669000798346295, 0.18456357982253255, 0.2006022777436225, 0.2143666264976031, 0.22526938738112967, 0.23282705464681067] + [0.23669538268420445] * 2 + [0.23282705464681067, 0.22526938738112967, 0.2143666264976031, 0.2006022777436225, 0.18456357982253255, 0.1669000798346295, 0.1482803686136344, 0.12935095083700357, 0.11070068079024514, 0.09283329821313276, 0.07614950044287017, 0.060938851450946276, 0.047380805975397705, 0.03555333280909725, 0.025447121841425106, 0.016983169507997393, 0.010031626246347373, 0.004430093886645415, 0.0],
        },
        "x180_I_wf5": {
            "type": "arbitrary",
            "samples": [0.0, 0.004430093886645415, 0.010031626246347373, 0.016983169507997393, 0.025447121841425106, 0.03555333280909725, 0.047380805975397705, 0.060938851450946276, 0.07614950044287017, 0.09283329821313276, 0.11070068079024514, 0.12935095083700357, 0.1482803686136344, 0.1669000798346295, 0.18456357982253255, 0.2006022777436225, 0.2143666264976031, 0.22526938738112967, 0.23282705464681067] + [0.23669538268420445] * 2 + [0.23282705464681067, 0.22526938738112967, 0.2143666264976031, 0.2006022777436225, 0.18456357982253255, 0.1669000798346295, 0.1482803686136344, 0.12935095083700357, 0.11070068079024514, 0.09283329821313276, 0.07614950044287017, 0.060938851450946276, 0.047380805975397705, 0.03555333280909725, 0.025447121841425106, 0.016983169507997393, 0.010031626246347373, 0.004430093886645415, 0.0],
        },
        "x180_I_wf6": {
            "type": "arbitrary",
            "samples": [0.0, 0.004430093886645415, 0.010031626246347373, 0.016983169507997393, 0.025447121841425106, 0.03555333280909725, 0.047380805975397705, 0.060938851450946276, 0.07614950044287017, 0.09283329821313276, 0.11070068079024514, 0.12935095083700357, 0.1482803686136344, 0.1669000798346295, 0.18456357982253255, 0.2006022777436225, 0.2143666264976031, 0.22526938738112967, 0.23282705464681067] + [0.23669538268420445] * 2 + [0.23282705464681067, 0.22526938738112967, 0.2143666264976031, 0.2006022777436225, 0.18456357982253255, 0.1669000798346295, 0.1482803686136344, 0.12935095083700357, 0.11070068079024514, 0.09283329821313276, 0.07614950044287017, 0.060938851450946276, 0.047380805975397705, 0.03555333280909725, 0.025447121841425106, 0.016983169507997393, 0.010031626246347373, 0.004430093886645415, 0.0],
        },
        "x180_Q_wf0": {
            "type": "arbitrary",
            "samples": [0.0] * 180,
        },
        "x180_Q_wf1": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "x180_Q_wf2": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "x180_Q_wf3": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "x180_Q_wf4": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "x180_Q_wf5": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "x180_Q_wf6": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "minus_x90_I_wf0": {
            "type": "arbitrary",
            "samples": [0.0, -0.00040416620465755834, -0.0008320318708446434, -0.0012845788945819647, -0.001762798661865914, -0.002267689544406204, -0.002800254194721963, -0.0033614966397724627, -0.0039524191733662575, -0.004574019048730957, -0.005227284973831431, -0.005913193413293454, -0.0066327047021169545, -0.007386758977742835, -0.008176271938463344, -0.009002130437630656, -0.009865187924613631, -0.01076625974497014, -0.011706118313832137, -0.012685488178032564, -0.013705040984026638, -0.01476539037016362, -0.015867086803336754, -0.01701061238146674, -0.01819637562464483, -0.01942470627906296, -0.020695850159076677, -0.02200996405386956, -0.02336711072620154, -0.02476725403161595, -0.026210254187238206, -0.02769586321991057, -0.029223720623861513, -0.030793349258393096, -0.032404151516175934, -0.03405540579265952, -0.03574626328682754, -0.037475745163046886, -0.039242740103069274, -0.04104600227634162, -0.04288414975566317, -0.04475566340389212, -0.04665888625585296, -0.04859202341783009, -0.05055314250505774, -0.05254017463543585, -0.054550915995324765, -0.05658302999070759, -0.058634049994269, -0.060701382696035804, -0.06278231206217397, -0.06487400390335323, -0.06697351105079447, -0.06907777913472397, -0.07118365295649506, -0.07328788344212264, -0.07538713516143358, -0.07747799439348926, -0.07955697771541118, -0.08162054108826197, -0.08366508941022711, -0.085686986504034, -0.0876825655023604, -0.08964813959194799, -0.09158001307427546, -0.09347449269798133, -0.09532789921578447, -0.09713657911645074, -0.09889691648041778, -0.10060534490603643, -0.10225835945203246, -0.10385252854075183, -0.1053845057660392, -0.1068510415492232, -0.1082489945866514, -0.10957534303253762, -0.1108271953615586, -0.112001800856664, -0.1130965596689426, -0.11410903239811193, -0.11503694914426066, -0.11587821798386094, -0.11663093282577114, -0.11729338060594716, -0.11786404778285947, -0.1183416260991481, -0.11872501757881927, -0.11901333873326818, -0.11920592395357711] + [-0.11930232807085857] * 2 + [-0.11920592395357711, -0.11901333873326818, -0.11872501757881927, -0.1183416260991481, -0.11786404778285947, -0.11729338060594716, -0.11663093282577114, -0.11587821798386094, -0.11503694914426066, -0.11410903239811193, -0.1130965596689426, -0.112001800856664, -0.1108271953615586, -0.10957534303253762, -0.1082489945866514, -0.1068510415492232, -0.1053845057660392, -0.10385252854075183, -0.10225835945203246, -0.10060534490603643, -0.09889691648041778, -0.09713657911645074, -0.09532789921578447, -0.09347449269798133, -0.09158001307427546, -0.08964813959194799, -0.0876825655023604, -0.085686986504034, -0.08366508941022711, -0.08162054108826197, -0.07955697771541118, -0.07747799439348926, -0.07538713516143358, -0.07328788344212264, -0.07118365295649506, -0.06907777913472397, -0.06697351105079447, -0.06487400390335323, -0.06278231206217397, -0.060701382696035804, -0.058634049994269, -0.05658302999070759, -0.054550915995324765, -0.05254017463543585, -0.05055314250505774, -0.04859202341783009, -0.04665888625585296, -0.04475566340389212, -0.04288414975566317, -0.04104600227634162, -0.039242740103069274, -0.037475745163046886, -0.03574626328682754, -0.03405540579265952, -0.032404151516175934, -0.030793349258393096, -0.029223720623861513, -0.02769586321991057, -0.026210254187238206, -0.02476725403161595, -0.02336711072620154, -0.02200996405386956, -0.020695850159076677, -0.01942470627906296, -0.01819637562464483, -0.01701061238146674, -0.015867086803336754, -0.01476539037016362, -0.013705040984026638, -0.012685488178032564, -0.011706118313832137, -0.01076625974497014, -0.009865187924613631, -0.009002130437630656, -0.008176271938463344, -0.007386758977742835, -0.0066327047021169545, -0.005913193413293454, -0.005227284973831431, -0.004574019048730957, -0.0039524191733662575, -0.0033614966397724627, -0.002800254194721963, -0.002267689544406204, -0.001762798661865914, -0.0012845788945819647, -0.0008320318708446434, -0.00040416620465755834, 0.0],
        },
        "minus_x90_I_wf1": {
            "type": "arbitrary",
            "samples": [0.0, -0.0022150469433227073, -0.005015813123173687, -0.008491584753998697, -0.012723560920712553, -0.017776666404548624, -0.023690402987698853, -0.030469425725473138, -0.03807475022143508, -0.04641664910656638, -0.05535034039512257, -0.06467547541850178, -0.0741401843068172, -0.08345003991731476, -0.09228178991126627, -0.10030113887181125, -0.10718331324880155, -0.11263469369056484, -0.11641352732340533] + [-0.11834769134210223] * 2 + [-0.11641352732340533, -0.11263469369056484, -0.10718331324880155, -0.10030113887181125, -0.09228178991126627, -0.08345003991731476, -0.0741401843068172, -0.06467547541850178, -0.05535034039512257, -0.04641664910656638, -0.03807475022143508, -0.030469425725473138, -0.023690402987698853, -0.017776666404548624, -0.012723560920712553, -0.008491584753998697, -0.005015813123173687, -0.0022150469433227073, 0.0],
        },
        "minus_x90_I_wf2": {
            "type": "arbitrary",
            "samples": [0.0, -0.0022150469433227073, -0.005015813123173687, -0.008491584753998697, -0.012723560920712553, -0.017776666404548624, -0.023690402987698853, -0.030469425725473138, -0.03807475022143508, -0.04641664910656638, -0.05535034039512257, -0.06467547541850178, -0.0741401843068172, -0.08345003991731476, -0.09228178991126627, -0.10030113887181125, -0.10718331324880155, -0.11263469369056484, -0.11641352732340533] + [-0.11834769134210223] * 2 + [-0.11641352732340533, -0.11263469369056484, -0.10718331324880155, -0.10030113887181125, -0.09228178991126627, -0.08345003991731476, -0.0741401843068172, -0.06467547541850178, -0.05535034039512257, -0.04641664910656638, -0.03807475022143508, -0.030469425725473138, -0.023690402987698853, -0.017776666404548624, -0.012723560920712553, -0.008491584753998697, -0.005015813123173687, -0.0022150469433227073, 0.0],
        },
        "minus_x90_I_wf3": {
            "type": "arbitrary",
            "samples": [0.0, -0.0022150469433227073, -0.005015813123173687, -0.008491584753998697, -0.012723560920712553, -0.017776666404548624, -0.023690402987698853, -0.030469425725473138, -0.03807475022143508, -0.04641664910656638, -0.05535034039512257, -0.06467547541850178, -0.0741401843068172, -0.08345003991731476, -0.09228178991126627, -0.10030113887181125, -0.10718331324880155, -0.11263469369056484, -0.11641352732340533] + [-0.11834769134210223] * 2 + [-0.11641352732340533, -0.11263469369056484, -0.10718331324880155, -0.10030113887181125, -0.09228178991126627, -0.08345003991731476, -0.0741401843068172, -0.06467547541850178, -0.05535034039512257, -0.04641664910656638, -0.03807475022143508, -0.030469425725473138, -0.023690402987698853, -0.017776666404548624, -0.012723560920712553, -0.008491584753998697, -0.005015813123173687, -0.0022150469433227073, 0.0],
        },
        "minus_x90_I_wf4": {
            "type": "arbitrary",
            "samples": [0.0, -0.0022150469433227073, -0.005015813123173687, -0.008491584753998697, -0.012723560920712553, -0.017776666404548624, -0.023690402987698853, -0.030469425725473138, -0.03807475022143508, -0.04641664910656638, -0.05535034039512257, -0.06467547541850178, -0.0741401843068172, -0.08345003991731476, -0.09228178991126627, -0.10030113887181125, -0.10718331324880155, -0.11263469369056484, -0.11641352732340533] + [-0.11834769134210223] * 2 + [-0.11641352732340533, -0.11263469369056484, -0.10718331324880155, -0.10030113887181125, -0.09228178991126627, -0.08345003991731476, -0.0741401843068172, -0.06467547541850178, -0.05535034039512257, -0.04641664910656638, -0.03807475022143508, -0.030469425725473138, -0.023690402987698853, -0.017776666404548624, -0.012723560920712553, -0.008491584753998697, -0.005015813123173687, -0.0022150469433227073, 0.0],
        },
        "minus_x90_I_wf5": {
            "type": "arbitrary",
            "samples": [0.0, -0.0022150469433227073, -0.005015813123173687, -0.008491584753998697, -0.012723560920712553, -0.017776666404548624, -0.023690402987698853, -0.030469425725473138, -0.03807475022143508, -0.04641664910656638, -0.05535034039512257, -0.06467547541850178, -0.0741401843068172, -0.08345003991731476, -0.09228178991126627, -0.10030113887181125, -0.10718331324880155, -0.11263469369056484, -0.11641352732340533] + [-0.11834769134210223] * 2 + [-0.11641352732340533, -0.11263469369056484, -0.10718331324880155, -0.10030113887181125, -0.09228178991126627, -0.08345003991731476, -0.0741401843068172, -0.06467547541850178, -0.05535034039512257, -0.04641664910656638, -0.03807475022143508, -0.030469425725473138, -0.023690402987698853, -0.017776666404548624, -0.012723560920712553, -0.008491584753998697, -0.005015813123173687, -0.0022150469433227073, 0.0],
        },
        "minus_x90_I_wf6": {
            "type": "arbitrary",
            "samples": [0.0, -0.0022150469433227073, -0.005015813123173687, -0.008491584753998697, -0.012723560920712553, -0.017776666404548624, -0.023690402987698853, -0.030469425725473138, -0.03807475022143508, -0.04641664910656638, -0.05535034039512257, -0.06467547541850178, -0.0741401843068172, -0.08345003991731476, -0.09228178991126627, -0.10030113887181125, -0.10718331324880155, -0.11263469369056484, -0.11641352732340533] + [-0.11834769134210223] * 2 + [-0.11641352732340533, -0.11263469369056484, -0.10718331324880155, -0.10030113887181125, -0.09228178991126627, -0.08345003991731476, -0.0741401843068172, -0.06467547541850178, -0.05535034039512257, -0.04641664910656638, -0.03807475022143508, -0.030469425725473138, -0.023690402987698853, -0.017776666404548624, -0.012723560920712553, -0.008491584753998697, -0.005015813123173687, -0.0022150469433227073, 0.0],
        },
        "minus_x90_Q_wf0": {
            "type": "arbitrary",
            "samples": [0.0] * 180,
        },
        "minus_x90_Q_wf1": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "minus_x90_Q_wf2": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "minus_x90_Q_wf3": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "minus_x90_Q_wf4": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "minus_x90_Q_wf5": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "minus_x90_Q_wf6": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "y90_I_wf0": {
            "type": "arbitrary",
            "samples": [-0.0] * 180,
        },
        "y90_I_wf1": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
        },
        "y90_I_wf2": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
        },
        "y90_I_wf3": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
        },
        "y90_I_wf4": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
        },
        "y90_I_wf5": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
        },
        "y90_I_wf6": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
        },
        "y90_Q_wf0": {
            "type": "arbitrary",
            "samples": [0.0, 0.00040416620465755834, 0.0008320318708446434, 0.0012845788945819647, 0.001762798661865914, 0.002267689544406204, 0.002800254194721963, 0.0033614966397724627, 0.0039524191733662575, 0.004574019048730957, 0.005227284973831431, 0.005913193413293454, 0.0066327047021169545, 0.007386758977742835, 0.008176271938463344, 0.009002130437630656, 0.009865187924613631, 0.01076625974497014, 0.011706118313832137, 0.012685488178032564, 0.013705040984026638, 0.01476539037016362, 0.015867086803336754, 0.01701061238146674, 0.01819637562464483, 0.01942470627906296, 0.020695850159076677, 0.02200996405386956, 0.02336711072620154, 0.02476725403161595, 0.026210254187238206, 0.02769586321991057, 0.029223720623861513, 0.030793349258393096, 0.032404151516175934, 0.03405540579265952, 0.03574626328682754, 0.037475745163046886, 0.039242740103069274, 0.04104600227634162, 0.04288414975566317, 0.04475566340389212, 0.04665888625585296, 0.04859202341783009, 0.05055314250505774, 0.05254017463543585, 0.054550915995324765, 0.05658302999070759, 0.058634049994269, 0.060701382696035804, 0.06278231206217397, 0.06487400390335323, 0.06697351105079447, 0.06907777913472397, 0.07118365295649506, 0.07328788344212264, 0.07538713516143358, 0.07747799439348926, 0.07955697771541118, 0.08162054108826197, 0.08366508941022711, 0.085686986504034, 0.0876825655023604, 0.08964813959194799, 0.09158001307427546, 0.09347449269798133, 0.09532789921578447, 0.09713657911645074, 0.09889691648041778, 0.10060534490603643, 0.10225835945203246, 0.10385252854075183, 0.1053845057660392, 0.1068510415492232, 0.1082489945866514, 0.10957534303253762, 0.1108271953615586, 0.112001800856664, 0.1130965596689426, 0.11410903239811193, 0.11503694914426066, 0.11587821798386094, 0.11663093282577114, 0.11729338060594716, 0.11786404778285947, 0.1183416260991481, 0.11872501757881927, 0.11901333873326818, 0.11920592395357711] + [0.11930232807085857] * 2 + [0.11920592395357711, 0.11901333873326818, 0.11872501757881927, 0.1183416260991481, 0.11786404778285947, 0.11729338060594716, 0.11663093282577114, 0.11587821798386094, 0.11503694914426066, 0.11410903239811193, 0.1130965596689426, 0.112001800856664, 0.1108271953615586, 0.10957534303253762, 0.1082489945866514, 0.1068510415492232, 0.1053845057660392, 0.10385252854075183, 0.10225835945203246, 0.10060534490603643, 0.09889691648041778, 0.09713657911645074, 0.09532789921578447, 0.09347449269798133, 0.09158001307427546, 0.08964813959194799, 0.0876825655023604, 0.085686986504034, 0.08366508941022711, 0.08162054108826197, 0.07955697771541118, 0.07747799439348926, 0.07538713516143358, 0.07328788344212264, 0.07118365295649506, 0.06907777913472397, 0.06697351105079447, 0.06487400390335323, 0.06278231206217397, 0.060701382696035804, 0.058634049994269, 0.05658302999070759, 0.054550915995324765, 0.05254017463543585, 0.05055314250505774, 0.04859202341783009, 0.04665888625585296, 0.04475566340389212, 0.04288414975566317, 0.04104600227634162, 0.039242740103069274, 0.037475745163046886, 0.03574626328682754, 0.03405540579265952, 0.032404151516175934, 0.030793349258393096, 0.029223720623861513, 0.02769586321991057, 0.026210254187238206, 0.02476725403161595, 0.02336711072620154, 0.02200996405386956, 0.020695850159076677, 0.01942470627906296, 0.01819637562464483, 0.01701061238146674, 0.015867086803336754, 0.01476539037016362, 0.013705040984026638, 0.012685488178032564, 0.011706118313832137, 0.01076625974497014, 0.009865187924613631, 0.009002130437630656, 0.008176271938463344, 0.007386758977742835, 0.0066327047021169545, 0.005913193413293454, 0.005227284973831431, 0.004574019048730957, 0.0039524191733662575, 0.0033614966397724627, 0.002800254194721963, 0.002267689544406204, 0.001762798661865914, 0.0012845788945819647, 0.0008320318708446434, 0.00040416620465755834, 0.0],
        },
        "y90_Q_wf1": {
            "type": "arbitrary",
            "samples": [0.0, 0.0022150469433227073, 0.005015813123173687, 0.008491584753998697, 0.012723560920712553, 0.017776666404548624, 0.023690402987698853, 0.030469425725473138, 0.03807475022143508, 0.04641664910656638, 0.05535034039512257, 0.06467547541850178, 0.0741401843068172, 0.08345003991731476, 0.09228178991126627, 0.10030113887181125, 0.10718331324880155, 0.11263469369056484, 0.11641352732340533] + [0.11834769134210223] * 2 + [0.11641352732340533, 0.11263469369056484, 0.10718331324880155, 0.10030113887181125, 0.09228178991126627, 0.08345003991731476, 0.0741401843068172, 0.06467547541850178, 0.05535034039512257, 0.04641664910656638, 0.03807475022143508, 0.030469425725473138, 0.023690402987698853, 0.017776666404548624, 0.012723560920712553, 0.008491584753998697, 0.005015813123173687, 0.0022150469433227073, 0.0],
        },
        "y90_Q_wf2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0022150469433227073, 0.005015813123173687, 0.008491584753998697, 0.012723560920712553, 0.017776666404548624, 0.023690402987698853, 0.030469425725473138, 0.03807475022143508, 0.04641664910656638, 0.05535034039512257, 0.06467547541850178, 0.0741401843068172, 0.08345003991731476, 0.09228178991126627, 0.10030113887181125, 0.10718331324880155, 0.11263469369056484, 0.11641352732340533] + [0.11834769134210223] * 2 + [0.11641352732340533, 0.11263469369056484, 0.10718331324880155, 0.10030113887181125, 0.09228178991126627, 0.08345003991731476, 0.0741401843068172, 0.06467547541850178, 0.05535034039512257, 0.04641664910656638, 0.03807475022143508, 0.030469425725473138, 0.023690402987698853, 0.017776666404548624, 0.012723560920712553, 0.008491584753998697, 0.005015813123173687, 0.0022150469433227073, 0.0],
        },
        "y90_Q_wf3": {
            "type": "arbitrary",
            "samples": [0.0, 0.0022150469433227073, 0.005015813123173687, 0.008491584753998697, 0.012723560920712553, 0.017776666404548624, 0.023690402987698853, 0.030469425725473138, 0.03807475022143508, 0.04641664910656638, 0.05535034039512257, 0.06467547541850178, 0.0741401843068172, 0.08345003991731476, 0.09228178991126627, 0.10030113887181125, 0.10718331324880155, 0.11263469369056484, 0.11641352732340533] + [0.11834769134210223] * 2 + [0.11641352732340533, 0.11263469369056484, 0.10718331324880155, 0.10030113887181125, 0.09228178991126627, 0.08345003991731476, 0.0741401843068172, 0.06467547541850178, 0.05535034039512257, 0.04641664910656638, 0.03807475022143508, 0.030469425725473138, 0.023690402987698853, 0.017776666404548624, 0.012723560920712553, 0.008491584753998697, 0.005015813123173687, 0.0022150469433227073, 0.0],
        },
        "y90_Q_wf4": {
            "type": "arbitrary",
            "samples": [0.0, 0.0022150469433227073, 0.005015813123173687, 0.008491584753998697, 0.012723560920712553, 0.017776666404548624, 0.023690402987698853, 0.030469425725473138, 0.03807475022143508, 0.04641664910656638, 0.05535034039512257, 0.06467547541850178, 0.0741401843068172, 0.08345003991731476, 0.09228178991126627, 0.10030113887181125, 0.10718331324880155, 0.11263469369056484, 0.11641352732340533] + [0.11834769134210223] * 2 + [0.11641352732340533, 0.11263469369056484, 0.10718331324880155, 0.10030113887181125, 0.09228178991126627, 0.08345003991731476, 0.0741401843068172, 0.06467547541850178, 0.05535034039512257, 0.04641664910656638, 0.03807475022143508, 0.030469425725473138, 0.023690402987698853, 0.017776666404548624, 0.012723560920712553, 0.008491584753998697, 0.005015813123173687, 0.0022150469433227073, 0.0],
        },
        "y90_Q_wf5": {
            "type": "arbitrary",
            "samples": [0.0, 0.0022150469433227073, 0.005015813123173687, 0.008491584753998697, 0.012723560920712553, 0.017776666404548624, 0.023690402987698853, 0.030469425725473138, 0.03807475022143508, 0.04641664910656638, 0.05535034039512257, 0.06467547541850178, 0.0741401843068172, 0.08345003991731476, 0.09228178991126627, 0.10030113887181125, 0.10718331324880155, 0.11263469369056484, 0.11641352732340533] + [0.11834769134210223] * 2 + [0.11641352732340533, 0.11263469369056484, 0.10718331324880155, 0.10030113887181125, 0.09228178991126627, 0.08345003991731476, 0.0741401843068172, 0.06467547541850178, 0.05535034039512257, 0.04641664910656638, 0.03807475022143508, 0.030469425725473138, 0.023690402987698853, 0.017776666404548624, 0.012723560920712553, 0.008491584753998697, 0.005015813123173687, 0.0022150469433227073, 0.0],
        },
        "y90_Q_wf6": {
            "type": "arbitrary",
            "samples": [0.0, 0.0022150469433227073, 0.005015813123173687, 0.008491584753998697, 0.012723560920712553, 0.017776666404548624, 0.023690402987698853, 0.030469425725473138, 0.03807475022143508, 0.04641664910656638, 0.05535034039512257, 0.06467547541850178, 0.0741401843068172, 0.08345003991731476, 0.09228178991126627, 0.10030113887181125, 0.10718331324880155, 0.11263469369056484, 0.11641352732340533] + [0.11834769134210223] * 2 + [0.11641352732340533, 0.11263469369056484, 0.10718331324880155, 0.10030113887181125, 0.09228178991126627, 0.08345003991731476, 0.0741401843068172, 0.06467547541850178, 0.05535034039512257, 0.04641664910656638, 0.03807475022143508, 0.030469425725473138, 0.023690402987698853, 0.017776666404548624, 0.012723560920712553, 0.008491584753998697, 0.005015813123173687, 0.0022150469433227073, 0.0],
        },
        "y180_I_wf0": {
            "type": "arbitrary",
            "samples": [-0.0] * 180,
        },
        "y180_I_wf1": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
        },
        "y180_I_wf2": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
        },
        "y180_I_wf3": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
        },
        "y180_I_wf4": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
        },
        "y180_I_wf5": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
        },
        "y180_I_wf6": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
        },
        "y180_Q_wf0": {
            "type": "arbitrary",
            "samples": [0.0, 0.0008083324093151167, 0.0016640637416892867, 0.0025691577891639294, 0.003525597323731828, 0.004535379088812408, 0.005600508389443926, 0.006722993279544925, 0.007904838346732515, 0.009148038097461914, 0.010454569947662862, 0.011826386826586908, 0.013265409404233909, 0.01477351795548567, 0.016352543876926688, 0.018004260875261312, 0.019730375849227263, 0.02153251948994028, 0.023412236627664274, 0.02537097635606513, 0.027410081968053276, 0.02953078074032724, 0.03173417360667351, 0.03402122476293348, 0.03639275124928966, 0.03884941255812592, 0.041391700318153354, 0.04401992810773912, 0.04673422145240308, 0.0495345080632319, 0.05242050837447641, 0.05539172643982114, 0.058447441247723025, 0.06158669851678619, 0.06480830303235187, 0.06811081158531904, 0.07149252657365508, 0.07495149032609377, 0.07848548020613855, 0.08209200455268324, 0.08576829951132633, 0.08951132680778424, 0.09331777251170592, 0.09718404683566018, 0.10110628501011548, 0.1050803492708717, 0.10910183199064953, 0.11316605998141518, 0.117268099988538, 0.12140276539207161, 0.12556462412434793, 0.12974800780670645, 0.13394702210158893, 0.13815555826944795, 0.14236730591299013, 0.14657576688424528, 0.15077427032286717, 0.15495598878697853, 0.15911395543082235, 0.16324108217652394, 0.16733017882045423, 0.171373973008068, 0.1753651310047208, 0.17929627918389598, 0.18316002614855093, 0.18694898539596266, 0.19065579843156893, 0.19427315823290148, 0.19779383296083555, 0.20121068981207285, 0.20451671890406492, 0.20770505708150366, 0.2107690115320784, 0.2137020830984464, 0.2164979891733028, 0.21915068606507523, 0.2216543907231172, 0.224003601713328, 0.2261931193378852, 0.22821806479622386, 0.23007389828852132, 0.23175643596772189, 0.23326186565154228, 0.2345867612118943, 0.23572809556571894, 0.2366832521982962, 0.23745003515763854, 0.23802667746653636, 0.23841184790715422] + [0.23860465614171714] * 2 + [0.23841184790715422, 0.23802667746653636, 0.23745003515763854, 0.2366832521982962, 0.23572809556571894, 0.2345867612118943, 0.23326186565154228, 0.23175643596772189, 0.23007389828852132, 0.22821806479622386, 0.2261931193378852, 0.224003601713328, 0.2216543907231172, 0.21915068606507523, 0.2164979891733028, 0.2137020830984464, 0.2107690115320784, 0.20770505708150366, 0.20451671890406492, 0.20121068981207285, 0.19779383296083555, 0.19427315823290148, 0.19065579843156893, 0.18694898539596266, 0.18316002614855093, 0.17929627918389598, 0.1753651310047208, 0.171373973008068, 0.16733017882045423, 0.16324108217652394, 0.15911395543082235, 0.15495598878697853, 0.15077427032286717, 0.14657576688424528, 0.14236730591299013, 0.13815555826944795, 0.13394702210158893, 0.12974800780670645, 0.12556462412434793, 0.12140276539207161, 0.117268099988538, 0.11316605998141518, 0.10910183199064953, 0.1050803492708717, 0.10110628501011548, 0.09718404683566018, 0.09331777251170592, 0.08951132680778424, 0.08576829951132633, 0.08209200455268324, 0.07848548020613855, 0.07495149032609377, 0.07149252657365508, 0.06811081158531904, 0.06480830303235187, 0.06158669851678619, 0.058447441247723025, 0.05539172643982114, 0.05242050837447641, 0.0495345080632319, 0.04673422145240308, 0.04401992810773912, 0.041391700318153354, 0.03884941255812592, 0.03639275124928966, 0.03402122476293348, 0.03173417360667351, 0.02953078074032724, 0.027410081968053276, 0.02537097635606513, 0.023412236627664274, 0.02153251948994028, 0.019730375849227263, 0.018004260875261312, 0.016352543876926688, 0.01477351795548567, 0.013265409404233909, 0.011826386826586908, 0.010454569947662862, 0.009148038097461914, 0.007904838346732515, 0.006722993279544925, 0.005600508389443926, 0.004535379088812408, 0.003525597323731828, 0.0025691577891639294, 0.0016640637416892867, 0.0008083324093151167, 0.0],
        },
        "y180_Q_wf1": {
            "type": "arbitrary",
            "samples": [0.0, 0.004430093886645415, 0.010031626246347373, 0.016983169507997393, 0.025447121841425106, 0.03555333280909725, 0.047380805975397705, 0.060938851450946276, 0.07614950044287017, 0.09283329821313276, 0.11070068079024514, 0.12935095083700357, 0.1482803686136344, 0.1669000798346295, 0.18456357982253255, 0.2006022777436225, 0.2143666264976031, 0.22526938738112967, 0.23282705464681067] + [0.23669538268420445] * 2 + [0.23282705464681067, 0.22526938738112967, 0.2143666264976031, 0.2006022777436225, 0.18456357982253255, 0.1669000798346295, 0.1482803686136344, 0.12935095083700357, 0.11070068079024514, 0.09283329821313276, 0.07614950044287017, 0.060938851450946276, 0.047380805975397705, 0.03555333280909725, 0.025447121841425106, 0.016983169507997393, 0.010031626246347373, 0.004430093886645415, 0.0],
        },
        "y180_Q_wf2": {
            "type": "arbitrary",
            "samples": [0.0, 0.004430093886645415, 0.010031626246347373, 0.016983169507997393, 0.025447121841425106, 0.03555333280909725, 0.047380805975397705, 0.060938851450946276, 0.07614950044287017, 0.09283329821313276, 0.11070068079024514, 0.12935095083700357, 0.1482803686136344, 0.1669000798346295, 0.18456357982253255, 0.2006022777436225, 0.2143666264976031, 0.22526938738112967, 0.23282705464681067] + [0.23669538268420445] * 2 + [0.23282705464681067, 0.22526938738112967, 0.2143666264976031, 0.2006022777436225, 0.18456357982253255, 0.1669000798346295, 0.1482803686136344, 0.12935095083700357, 0.11070068079024514, 0.09283329821313276, 0.07614950044287017, 0.060938851450946276, 0.047380805975397705, 0.03555333280909725, 0.025447121841425106, 0.016983169507997393, 0.010031626246347373, 0.004430093886645415, 0.0],
        },
        "y180_Q_wf3": {
            "type": "arbitrary",
            "samples": [0.0, 0.004430093886645415, 0.010031626246347373, 0.016983169507997393, 0.025447121841425106, 0.03555333280909725, 0.047380805975397705, 0.060938851450946276, 0.07614950044287017, 0.09283329821313276, 0.11070068079024514, 0.12935095083700357, 0.1482803686136344, 0.1669000798346295, 0.18456357982253255, 0.2006022777436225, 0.2143666264976031, 0.22526938738112967, 0.23282705464681067] + [0.23669538268420445] * 2 + [0.23282705464681067, 0.22526938738112967, 0.2143666264976031, 0.2006022777436225, 0.18456357982253255, 0.1669000798346295, 0.1482803686136344, 0.12935095083700357, 0.11070068079024514, 0.09283329821313276, 0.07614950044287017, 0.060938851450946276, 0.047380805975397705, 0.03555333280909725, 0.025447121841425106, 0.016983169507997393, 0.010031626246347373, 0.004430093886645415, 0.0],
        },
        "y180_Q_wf4": {
            "type": "arbitrary",
            "samples": [0.0, 0.004430093886645415, 0.010031626246347373, 0.016983169507997393, 0.025447121841425106, 0.03555333280909725, 0.047380805975397705, 0.060938851450946276, 0.07614950044287017, 0.09283329821313276, 0.11070068079024514, 0.12935095083700357, 0.1482803686136344, 0.1669000798346295, 0.18456357982253255, 0.2006022777436225, 0.2143666264976031, 0.22526938738112967, 0.23282705464681067] + [0.23669538268420445] * 2 + [0.23282705464681067, 0.22526938738112967, 0.2143666264976031, 0.2006022777436225, 0.18456357982253255, 0.1669000798346295, 0.1482803686136344, 0.12935095083700357, 0.11070068079024514, 0.09283329821313276, 0.07614950044287017, 0.060938851450946276, 0.047380805975397705, 0.03555333280909725, 0.025447121841425106, 0.016983169507997393, 0.010031626246347373, 0.004430093886645415, 0.0],
        },
        "y180_Q_wf5": {
            "type": "arbitrary",
            "samples": [0.0, 0.004430093886645415, 0.010031626246347373, 0.016983169507997393, 0.025447121841425106, 0.03555333280909725, 0.047380805975397705, 0.060938851450946276, 0.07614950044287017, 0.09283329821313276, 0.11070068079024514, 0.12935095083700357, 0.1482803686136344, 0.1669000798346295, 0.18456357982253255, 0.2006022777436225, 0.2143666264976031, 0.22526938738112967, 0.23282705464681067] + [0.23669538268420445] * 2 + [0.23282705464681067, 0.22526938738112967, 0.2143666264976031, 0.2006022777436225, 0.18456357982253255, 0.1669000798346295, 0.1482803686136344, 0.12935095083700357, 0.11070068079024514, 0.09283329821313276, 0.07614950044287017, 0.060938851450946276, 0.047380805975397705, 0.03555333280909725, 0.025447121841425106, 0.016983169507997393, 0.010031626246347373, 0.004430093886645415, 0.0],
        },
        "y180_Q_wf6": {
            "type": "arbitrary",
            "samples": [0.0, 0.004430093886645415, 0.010031626246347373, 0.016983169507997393, 0.025447121841425106, 0.03555333280909725, 0.047380805975397705, 0.060938851450946276, 0.07614950044287017, 0.09283329821313276, 0.11070068079024514, 0.12935095083700357, 0.1482803686136344, 0.1669000798346295, 0.18456357982253255, 0.2006022777436225, 0.2143666264976031, 0.22526938738112967, 0.23282705464681067] + [0.23669538268420445] * 2 + [0.23282705464681067, 0.22526938738112967, 0.2143666264976031, 0.2006022777436225, 0.18456357982253255, 0.1669000798346295, 0.1482803686136344, 0.12935095083700357, 0.11070068079024514, 0.09283329821313276, 0.07614950044287017, 0.060938851450946276, 0.047380805975397705, 0.03555333280909725, 0.025447121841425106, 0.016983169507997393, 0.010031626246347373, 0.004430093886645415, 0.0],
        },
        "minus_y90_I_wf0": {
            "type": "arbitrary",
            "samples": [-0.0] * 180,
        },
        "minus_y90_I_wf1": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
        },
        "minus_y90_I_wf2": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
        },
        "minus_y90_I_wf3": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
        },
        "minus_y90_I_wf4": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
        },
        "minus_y90_I_wf5": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
        },
        "minus_y90_I_wf6": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
        },
        "minus_y90_Q_wf0": {
            "type": "arbitrary",
            "samples": [0.0, -0.00040416620465755834, -0.0008320318708446434, -0.0012845788945819647, -0.001762798661865914, -0.002267689544406204, -0.002800254194721963, -0.0033614966397724627, -0.0039524191733662575, -0.004574019048730957, -0.005227284973831431, -0.005913193413293454, -0.0066327047021169545, -0.007386758977742835, -0.008176271938463344, -0.009002130437630656, -0.009865187924613631, -0.01076625974497014, -0.011706118313832137, -0.012685488178032564, -0.013705040984026638, -0.01476539037016362, -0.015867086803336754, -0.01701061238146674, -0.01819637562464483, -0.01942470627906296, -0.020695850159076677, -0.02200996405386956, -0.02336711072620154, -0.02476725403161595, -0.026210254187238206, -0.02769586321991057, -0.029223720623861513, -0.030793349258393096, -0.032404151516175934, -0.03405540579265952, -0.03574626328682754, -0.037475745163046886, -0.039242740103069274, -0.04104600227634162, -0.04288414975566317, -0.04475566340389212, -0.04665888625585296, -0.04859202341783009, -0.05055314250505774, -0.05254017463543585, -0.054550915995324765, -0.05658302999070759, -0.058634049994269, -0.060701382696035804, -0.06278231206217397, -0.06487400390335323, -0.06697351105079447, -0.06907777913472397, -0.07118365295649506, -0.07328788344212264, -0.07538713516143358, -0.07747799439348926, -0.07955697771541118, -0.08162054108826197, -0.08366508941022711, -0.085686986504034, -0.0876825655023604, -0.08964813959194799, -0.09158001307427546, -0.09347449269798133, -0.09532789921578447, -0.09713657911645074, -0.09889691648041778, -0.10060534490603643, -0.10225835945203246, -0.10385252854075183, -0.1053845057660392, -0.1068510415492232, -0.1082489945866514, -0.10957534303253762, -0.1108271953615586, -0.112001800856664, -0.1130965596689426, -0.11410903239811193, -0.11503694914426066, -0.11587821798386094, -0.11663093282577114, -0.11729338060594716, -0.11786404778285947, -0.1183416260991481, -0.11872501757881927, -0.11901333873326818, -0.11920592395357711] + [-0.11930232807085857] * 2 + [-0.11920592395357711, -0.11901333873326818, -0.11872501757881927, -0.1183416260991481, -0.11786404778285947, -0.11729338060594716, -0.11663093282577114, -0.11587821798386094, -0.11503694914426066, -0.11410903239811193, -0.1130965596689426, -0.112001800856664, -0.1108271953615586, -0.10957534303253762, -0.1082489945866514, -0.1068510415492232, -0.1053845057660392, -0.10385252854075183, -0.10225835945203246, -0.10060534490603643, -0.09889691648041778, -0.09713657911645074, -0.09532789921578447, -0.09347449269798133, -0.09158001307427546, -0.08964813959194799, -0.0876825655023604, -0.085686986504034, -0.08366508941022711, -0.08162054108826197, -0.07955697771541118, -0.07747799439348926, -0.07538713516143358, -0.07328788344212264, -0.07118365295649506, -0.06907777913472397, -0.06697351105079447, -0.06487400390335323, -0.06278231206217397, -0.060701382696035804, -0.058634049994269, -0.05658302999070759, -0.054550915995324765, -0.05254017463543585, -0.05055314250505774, -0.04859202341783009, -0.04665888625585296, -0.04475566340389212, -0.04288414975566317, -0.04104600227634162, -0.039242740103069274, -0.037475745163046886, -0.03574626328682754, -0.03405540579265952, -0.032404151516175934, -0.030793349258393096, -0.029223720623861513, -0.02769586321991057, -0.026210254187238206, -0.02476725403161595, -0.02336711072620154, -0.02200996405386956, -0.020695850159076677, -0.01942470627906296, -0.01819637562464483, -0.01701061238146674, -0.015867086803336754, -0.01476539037016362, -0.013705040984026638, -0.012685488178032564, -0.011706118313832137, -0.01076625974497014, -0.009865187924613631, -0.009002130437630656, -0.008176271938463344, -0.007386758977742835, -0.0066327047021169545, -0.005913193413293454, -0.005227284973831431, -0.004574019048730957, -0.0039524191733662575, -0.0033614966397724627, -0.002800254194721963, -0.002267689544406204, -0.001762798661865914, -0.0012845788945819647, -0.0008320318708446434, -0.00040416620465755834, 0.0],
        },
        "minus_y90_Q_wf1": {
            "type": "arbitrary",
            "samples": [0.0, -0.0022150469433227073, -0.005015813123173687, -0.008491584753998697, -0.012723560920712553, -0.017776666404548624, -0.023690402987698853, -0.030469425725473138, -0.03807475022143508, -0.04641664910656638, -0.05535034039512257, -0.06467547541850178, -0.0741401843068172, -0.08345003991731476, -0.09228178991126627, -0.10030113887181125, -0.10718331324880155, -0.11263469369056484, -0.11641352732340533] + [-0.11834769134210223] * 2 + [-0.11641352732340533, -0.11263469369056484, -0.10718331324880155, -0.10030113887181125, -0.09228178991126627, -0.08345003991731476, -0.0741401843068172, -0.06467547541850178, -0.05535034039512257, -0.04641664910656638, -0.03807475022143508, -0.030469425725473138, -0.023690402987698853, -0.017776666404548624, -0.012723560920712553, -0.008491584753998697, -0.005015813123173687, -0.0022150469433227073, 0.0],
        },
        "minus_y90_Q_wf2": {
            "type": "arbitrary",
            "samples": [0.0, -0.0022150469433227073, -0.005015813123173687, -0.008491584753998697, -0.012723560920712553, -0.017776666404548624, -0.023690402987698853, -0.030469425725473138, -0.03807475022143508, -0.04641664910656638, -0.05535034039512257, -0.06467547541850178, -0.0741401843068172, -0.08345003991731476, -0.09228178991126627, -0.10030113887181125, -0.10718331324880155, -0.11263469369056484, -0.11641352732340533] + [-0.11834769134210223] * 2 + [-0.11641352732340533, -0.11263469369056484, -0.10718331324880155, -0.10030113887181125, -0.09228178991126627, -0.08345003991731476, -0.0741401843068172, -0.06467547541850178, -0.05535034039512257, -0.04641664910656638, -0.03807475022143508, -0.030469425725473138, -0.023690402987698853, -0.017776666404548624, -0.012723560920712553, -0.008491584753998697, -0.005015813123173687, -0.0022150469433227073, 0.0],
        },
        "minus_y90_Q_wf3": {
            "type": "arbitrary",
            "samples": [0.0, -0.0022150469433227073, -0.005015813123173687, -0.008491584753998697, -0.012723560920712553, -0.017776666404548624, -0.023690402987698853, -0.030469425725473138, -0.03807475022143508, -0.04641664910656638, -0.05535034039512257, -0.06467547541850178, -0.0741401843068172, -0.08345003991731476, -0.09228178991126627, -0.10030113887181125, -0.10718331324880155, -0.11263469369056484, -0.11641352732340533] + [-0.11834769134210223] * 2 + [-0.11641352732340533, -0.11263469369056484, -0.10718331324880155, -0.10030113887181125, -0.09228178991126627, -0.08345003991731476, -0.0741401843068172, -0.06467547541850178, -0.05535034039512257, -0.04641664910656638, -0.03807475022143508, -0.030469425725473138, -0.023690402987698853, -0.017776666404548624, -0.012723560920712553, -0.008491584753998697, -0.005015813123173687, -0.0022150469433227073, 0.0],
        },
        "minus_y90_Q_wf4": {
            "type": "arbitrary",
            "samples": [0.0, -0.0022150469433227073, -0.005015813123173687, -0.008491584753998697, -0.012723560920712553, -0.017776666404548624, -0.023690402987698853, -0.030469425725473138, -0.03807475022143508, -0.04641664910656638, -0.05535034039512257, -0.06467547541850178, -0.0741401843068172, -0.08345003991731476, -0.09228178991126627, -0.10030113887181125, -0.10718331324880155, -0.11263469369056484, -0.11641352732340533] + [-0.11834769134210223] * 2 + [-0.11641352732340533, -0.11263469369056484, -0.10718331324880155, -0.10030113887181125, -0.09228178991126627, -0.08345003991731476, -0.0741401843068172, -0.06467547541850178, -0.05535034039512257, -0.04641664910656638, -0.03807475022143508, -0.030469425725473138, -0.023690402987698853, -0.017776666404548624, -0.012723560920712553, -0.008491584753998697, -0.005015813123173687, -0.0022150469433227073, 0.0],
        },
        "minus_y90_Q_wf5": {
            "type": "arbitrary",
            "samples": [0.0, -0.0022150469433227073, -0.005015813123173687, -0.008491584753998697, -0.012723560920712553, -0.017776666404548624, -0.023690402987698853, -0.030469425725473138, -0.03807475022143508, -0.04641664910656638, -0.05535034039512257, -0.06467547541850178, -0.0741401843068172, -0.08345003991731476, -0.09228178991126627, -0.10030113887181125, -0.10718331324880155, -0.11263469369056484, -0.11641352732340533] + [-0.11834769134210223] * 2 + [-0.11641352732340533, -0.11263469369056484, -0.10718331324880155, -0.10030113887181125, -0.09228178991126627, -0.08345003991731476, -0.0741401843068172, -0.06467547541850178, -0.05535034039512257, -0.04641664910656638, -0.03807475022143508, -0.030469425725473138, -0.023690402987698853, -0.017776666404548624, -0.012723560920712553, -0.008491584753998697, -0.005015813123173687, -0.0022150469433227073, 0.0],
        },
        "minus_y90_Q_wf6": {
            "type": "arbitrary",
            "samples": [0.0, -0.0022150469433227073, -0.005015813123173687, -0.008491584753998697, -0.012723560920712553, -0.017776666404548624, -0.023690402987698853, -0.030469425725473138, -0.03807475022143508, -0.04641664910656638, -0.05535034039512257, -0.06467547541850178, -0.0741401843068172, -0.08345003991731476, -0.09228178991126627, -0.10030113887181125, -0.10718331324880155, -0.11263469369056484, -0.11641352732340533] + [-0.11834769134210223] * 2 + [-0.11641352732340533, -0.11263469369056484, -0.10718331324880155, -0.10030113887181125, -0.09228178991126627, -0.08345003991731476, -0.0741401843068172, -0.06467547541850178, -0.05535034039512257, -0.04641664910656638, -0.03807475022143508, -0.030469425725473138, -0.023690402987698853, -0.017776666404548624, -0.012723560920712553, -0.008491584753998697, -0.005015813123173687, -0.0022150469433227073, 0.0],
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights0": {
            "cosine": [(1.0, 500)],
            "sine": [(0.0, 500)],
        },
        "cosine_weights1": {
            "cosine": [(1.0, 500)],
            "sine": [(0.0, 500)],
        },
        "cosine_weights2": {
            "cosine": [(1.0, 500)],
            "sine": [(0.0, 500)],
        },
        "cosine_weights3": {
            "cosine": [(1.0, 500)],
            "sine": [(0.0, 500)],
        },
        "cosine_weights4": {
            "cosine": [(1.0, 500)],
            "sine": [(0.0, 500)],
        },
        "cosine_weights5": {
            "cosine": [(1.0, 500)],
            "sine": [(0.0, 500)],
        },
        "cosine_weights6": {
            "cosine": [(1.0, 500)],
            "sine": [(0.0, 500)],
        },
        "sine_weights0": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
        "sine_weights1": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
        "sine_weights2": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
        "sine_weights3": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
        "sine_weights4": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
        "sine_weights5": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
        "sine_weights6": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
        "minus_sine_weights0": {
            "cosine": [(0.0, 500)],
            "sine": [(-1.0, 500)],
        },
        "minus_sine_weights1": {
            "cosine": [(0.0, 500)],
            "sine": [(-1.0, 500)],
        },
        "minus_sine_weights2": {
            "cosine": [(0.0, 500)],
            "sine": [(-1.0, 500)],
        },
        "minus_sine_weights3": {
            "cosine": [(0.0, 500)],
            "sine": [(-1.0, 500)],
        },
        "minus_sine_weights4": {
            "cosine": [(0.0, 500)],
            "sine": [(-1.0, 500)],
        },
        "minus_sine_weights5": {
            "cosine": [(0.0, 500)],
            "sine": [(-1.0, 500)],
        },
        "minus_sine_weights6": {
            "cosine": [(0.0, 500)],
            "sine": [(-1.0, 500)],
        },
        "rotated_cosine_weights0": {
            "cosine": [(1.0, 500)],
            "sine": [(-0.0, 500)],
        },
        "rotated_cosine_weights1": {
            "cosine": [(1.0, 500)],
            "sine": [(-0.0, 500)],
        },
        "rotated_cosine_weights2": {
            "cosine": [(1.0, 500)],
            "sine": [(-0.0, 500)],
        },
        "rotated_cosine_weights3": {
            "cosine": [(1.0, 500)],
            "sine": [(-0.0, 500)],
        },
        "rotated_cosine_weights4": {
            "cosine": [(1.0, 500)],
            "sine": [(-0.0, 500)],
        },
        "rotated_cosine_weights5": {
            "cosine": [(1.0, 500)],
            "sine": [(-0.0, 500)],
        },
        "rotated_cosine_weights6": {
            "cosine": [(1.0, 500)],
            "sine": [(-0.0, 500)],
        },
        "rotated_sine_weights0": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
        "rotated_sine_weights1": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
        "rotated_sine_weights2": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
        "rotated_sine_weights3": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
        "rotated_sine_weights4": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
        "rotated_sine_weights5": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
        "rotated_sine_weights6": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
        "rotated_minus_sine_weights0": {
            "cosine": [(-0.0, 500)],
            "sine": [(-1.0, 500)],
        },
        "rotated_minus_sine_weights1": {
            "cosine": [(-0.0, 500)],
            "sine": [(-1.0, 500)],
        },
        "rotated_minus_sine_weights2": {
            "cosine": [(-0.0, 500)],
            "sine": [(-1.0, 500)],
        },
        "rotated_minus_sine_weights3": {
            "cosine": [(-0.0, 500)],
            "sine": [(-1.0, 500)],
        },
        "rotated_minus_sine_weights4": {
            "cosine": [(-0.0, 500)],
            "sine": [(-1.0, 500)],
        },
        "rotated_minus_sine_weights5": {
            "cosine": [(-0.0, 500)],
            "sine": [(-1.0, 500)],
        },
        "rotated_minus_sine_weights6": {
            "cosine": [(-0.0, 500)],
            "sine": [(-1.0, 500)],
        },
        "opt_cosine_weights0": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "opt_cosine_weights1": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "opt_cosine_weights2": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "opt_cosine_weights3": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "opt_cosine_weights4": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "opt_cosine_weights5": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "opt_cosine_weights6": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "opt_sine_weights0": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "opt_sine_weights1": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "opt_sine_weights2": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "opt_sine_weights3": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "opt_sine_weights4": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "opt_sine_weights5": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "opt_sine_weights6": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "opt_minus_sine_weights0": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
        "opt_minus_sine_weights1": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
        "opt_minus_sine_weights2": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
        "opt_minus_sine_weights3": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
        "opt_minus_sine_weights4": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
        "opt_minus_sine_weights5": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
        "opt_minus_sine_weights6": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
    },
    "mixers": {
        "octave_octave1_2": [
            {'intermediate_frequency': 184220000, 'lo_frequency': 6100000000, 'correction': [0.9843983836472034, 0.056579768657684326, 0.05430668592453003, 1.0256017595529556]},
            {'intermediate_frequency': 100000000, 'lo_frequency': 5467000000, 'correction': [1.008311040699482, 0.13667917624115944, 0.1319584883749485, 1.0443823970854282]},
            {'intermediate_frequency': 186000000, 'lo_frequency': 6100000000, 'correction': [0.9844945967197418, 0.057187315076589584, 0.054889824241399765, 1.025702003389597]},
            {'intermediate_frequency': 100000000, 'lo_frequency': 6382000000, 'correction': [0.9780302569270134, 0.01799078658223152, 0.017183978110551834, 1.0239499509334564]},
            {'intermediate_frequency': 100000000, 'lo_frequency': 5342000000, 'correction': [1.0420268923044205, 0.1728515625, 0.1728515625, 1.0420268923044205]},
            {'intermediate_frequency': 100000000, 'lo_frequency': 6189000000, 'correction': [0.9796239621937275, 0.021456871181726456, 0.020554695278406143, 1.0226210989058018]},
            {'intermediate_frequency': 179000000, 'lo_frequency': 6110000000, 'correction': [0.9841276444494724, 0.05483501777052879, 0.052632030099630356, 1.025319691747427]},
            {'intermediate_frequency': 169000000, 'lo_frequency': 6110000000, 'correction': [0.9832491092383862, 0.052119217813014984, 0.04997655004262924, 1.025404404848814]},
            {'intermediate_frequency': 172215300, 'lo_frequency': 6110000000, 'correction': [0.9834322556853294, 0.05336608737707138, 0.0511721596121788, 1.0255954004824162]},
            {'intermediate_frequency': 100000000, 'lo_frequency': 6007000000, 'correction': [0.9805241003632545, 0.04597645252943039, 0.04391460865736008, 1.0265608876943588]},
            {'intermediate_frequency': 100000000, 'lo_frequency': 5882000000, 'correction': [0.9815450236201286, 0.08165643364191055, 0.0771622434258461, 1.0387135222554207]},
            {'intermediate_frequency': -40864584, 'lo_frequency': 6382000000, 'correction': [0.9785669781267643, -0.02498408779501915, -0.023869480937719345, 1.0242620408535004]},
            {'intermediate_frequency': -10139023, 'lo_frequency': 6352000000, 'correction': [0.9787439368665218, -0.012496553361415863, -0.01195981353521347, 1.022668570280075]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6391860977, 'correction': [0.9792955070734024, -0.026965998113155365, -0.025794409215450287, 1.0237753726541996]},
            {'intermediate_frequency': -100000000, 'lo_frequency': 6441860977, 'correction': [0.9828890860080719, -0.052893687039613724, -0.05066971853375435, 1.026029534637928]},
            {'intermediate_frequency': -110924023, 'lo_frequency': 6452785000, 'correction': [0.9841265715658665, -0.057854827493429184, -0.055476363748311996, 1.0263194851577282]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 5668000000.0, 'correction': [1.0, 0.0, 0.0, 1.0]},
        ],
        "octave_octave1_1": [
            {'intermediate_frequency': 35322000, 'lo_frequency': 7100000000, 'correction': [0.9942276552319527, -0.09682570397853851, -0.09318546950817108, 1.033066563308239]},
            {'intermediate_frequency': 100000000, 'lo_frequency': 6012000000, 'correction': [0.9902525208890438, 0.030617237091064453, 0.029937267303466797, 1.0127442739903927]},
            {'intermediate_frequency': 34000000, 'lo_frequency': 7100000000, 'correction': [0.9941620528697968, -0.09657679498195648, -0.09294591844081879, 1.0329983979463577]},
            {'intermediate_frequency': 50000000, 'lo_frequency': 6062000000, 'correction': [0.9920627623796463, 0.03204335272312164, 0.03143896162509918, 1.0111344456672668]},
            {'intermediate_frequency': 57620000, 'lo_frequency': 6062000000, 'correction': [0.9917549826204777, 0.031311605125665665, 0.030706021934747696, 1.0113143399357796]},
            {'intermediate_frequency': 50000000, 'lo_frequency': 7206000000, 'correction': [0.9985018000006676, -0.10661306977272034, -0.10292454063892365, 1.0342853255569935]},
            {'intermediate_frequency': 56000000, 'lo_frequency': 6062000000, 'correction': [0.9918001294136047, 0.031804703176021576, 0.031189583241939545, 1.0113603807985783]},
            {'intermediate_frequency': 50000000, 'lo_frequency': 5968000000, 'correction': [0.9894565418362617, 0.045296911150217056, 0.04407525435090065, 1.0168818235397339]},
            {'intermediate_frequency': 59260000, 'lo_frequency': 6062000000, 'correction': [0.9918229691684246, 0.03205125033855438, 0.03143136203289032, 1.0113836713135242]},
            {'intermediate_frequency': 53900000, 'lo_frequency': 5968000000, 'correction': [0.989488635212183, 0.04554443806409836, 0.04431610554456711, 1.0169148072600365]},
            {'intermediate_frequency': 50000000, 'lo_frequency': 7080000000, 'correction': [0.9925949797034264, -0.09571203589439392, -0.09186682105064392, 1.0341414362192154]},
            {'intermediate_frequency': 54940000, 'lo_frequency': 7080000000, 'correction': [0.9928321950137615, -0.09568821638822556, -0.09188877791166306, 1.0338840521872044]},
            {'intermediate_frequency': 55100000, 'lo_frequency': 7080000000, 'correction': [0.9927028380334377, -0.09518983960151672, -0.09141018986701965, 1.0337493494153023]},
            {'intermediate_frequency': 56500000, 'lo_frequency': 7206000000, 'correction': [0.9980056993663311, -0.1069246344268322, -0.10310576483607292, 1.0349702052772045]},
            {'intermediate_frequency': 50000000, 'lo_frequency': 6949000000, 'correction': [0.9934355728328228, -0.0903998464345932, -0.08714990317821503, 1.030482191592455]},
            {'intermediate_frequency': 50000000, 'lo_frequency': 6825000000, 'correction': [0.9955396018922329, -0.0938892513513565, -0.09073497354984283, 1.0301481820642948]},
            {'intermediate_frequency': 56420000, 'lo_frequency': 7206000000, 'correction': [0.9981252439320087, -0.10691135376691818, -0.10311811417341232, 1.034841664135456]},
            {'intermediate_frequency': 54200000, 'lo_frequency': 7206000000, 'correction': [0.9981368966400623, -0.10652517899870872, -0.10277071222662926, 1.0346012897789478]},
            {'intermediate_frequency': 56520000, 'lo_frequency': 7206000000, 'correction': [0.9982746280729771, -0.10593293979763985, -0.10226170346140862, 1.0341130904853344]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6167000000.0, 'correction': [1.0, 0.0, 0.0, 1.0]},
        ],
    },
}

loaded_config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1",
            "analog_outputs": {
                "1": {
                    "offset": -0.0067901611328125,
                    "delay": 0,
                    "shareable": False,
                },
                "2": {
                    "offset": -0.011688232421875,
                    "delay": 0,
                    "shareable": False,
                },
                "3": {
                    "offset": 0.01972198486328125,
                    "delay": 0,
                    "shareable": False,
                },
                "4": {
                    "offset": 0.053253173828125,
                    "delay": 0,
                    "shareable": False,
                },
                "5": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                },
                "6": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                },
                "7": {
                    "offset": 0.0,
                    "delay": 19,
                    "shareable": False,
                },
                "8": {
                    "offset": 0.0,
                    "delay": 19,
                    "shareable": False,
                },
                "9": {
                    "offset": 0.0,
                    "delay": 19,
                    "shareable": False,
                },
                "10": {
                    "offset": 0.0,
                    "delay": 19,
                    "shareable": False,
                },
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.009985,
                    "gain_db": 0,
                    "shareable": False,
                },
                "2": {
                    "offset": 0.013658,
                    "gain_db": 0,
                    "shareable": False,
                },
            },
            "digital_outputs": {
                "1": {
                    "shareable": False,
                    "inverted": False,
                },
                "2": {
                    "shareable": False,
                    "inverted": False,
                },
                "3": {
                    "shareable": False,
                    "inverted": False,
                },
                "4": {
                    "shareable": False,
                    "inverted": False,
                },
                "5": {
                    "shareable": False,
                    "inverted": False,
                },
                "6": {
                    "shareable": False,
                    "inverted": False,
                },
                "7": {
                    "shareable": False,
                    "inverted": False,
                },
                "8": {
                    "shareable": False,
                    "inverted": False,
                },
                "9": {
                    "shareable": False,
                    "inverted": False,
                },
                "10": {
                    "shareable": False,
                    "inverted": False,
                },
            },
        },
    },
    "oscillators": {},
    "elements": {
        "r0": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 304,
            "smearing": 0,
            "intermediate_frequency": 56520000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q0",
            },
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "mixer": "octave_octave1_1",
                "lo_frequency": 7206000000.0,
            },
        },
        "r1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 304,
            "smearing": 0,
            "intermediate_frequency": 50000000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q1",
            },
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "mixer": "octave_octave1_1",
                "lo_frequency": 7080000000.0,
            },
        },
        "r2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 304,
            "smearing": 0,
            "intermediate_frequency": 50000000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q2",
            },
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "mixer": "octave_octave1_1",
                "lo_frequency": 6949000000.0,
            },
        },
        "r3": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 304,
            "smearing": 0,
            "intermediate_frequency": 50000000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q3",
            },
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "mixer": "octave_octave1_1",
                "lo_frequency": 6825000000.0,
            },
        },
        "r4": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 304,
            "smearing": 0,
            "intermediate_frequency": 50000000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q4",
            },
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "mixer": "octave_octave1_1",
                "lo_frequency": 6167000000.0,
            },
        },
        "r5": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 304,
            "smearing": 0,
            "intermediate_frequency": 50000000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q5",
            },
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "mixer": "octave_octave1_1",
                "lo_frequency": 6062000000.0,
            },
        },
        "r6": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 304,
            "smearing": 0,
            "intermediate_frequency": 50000000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q6",
            },
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "mixer": "octave_octave1_1",
                "lo_frequency": 5968000000.0,
            },
        },
        "r0aux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 304,
            "smearing": 0,
            "intermediate_frequency": 56520000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q0",
            },
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "mixer": "octave_octave1_1",
                "lo_frequency": 7206000000.0,
            },
        },
        "r1aux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 304,
            "smearing": 0,
            "intermediate_frequency": 50000000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q1",
            },
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "mixer": "octave_octave1_1",
                "lo_frequency": 7080000000.0,
            },
        },
        "r2aux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 304,
            "smearing": 0,
            "intermediate_frequency": 50000000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q2",
            },
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "mixer": "octave_octave1_1",
                "lo_frequency": 6949000000.0,
            },
        },
        "r3aux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 304,
            "smearing": 0,
            "intermediate_frequency": 50000000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q3",
            },
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "mixer": "octave_octave1_1",
                "lo_frequency": 6825000000.0,
            },
        },
        "r4aux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 304,
            "smearing": 0,
            "intermediate_frequency": 50000000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q4",
            },
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "mixer": "octave_octave1_1",
                "lo_frequency": 6167000000.0,
            },
        },
        "r5aux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 304,
            "smearing": 0,
            "intermediate_frequency": 50000000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q5",
            },
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "mixer": "octave_octave1_1",
                "lo_frequency": 6062000000.0,
            },
        },
        "r6aux": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 304,
            "smearing": 0,
            "intermediate_frequency": 50000000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q6",
            },
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "mixer": "octave_octave1_1",
                "lo_frequency": 5968000000.0,
            },
        },
        "q0": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 110924023.0,
            "operations": {
                "cw": "const_pulse",
                "pi": "pi_pulse0",
                "pi2": "pi_over_two_pulse0",
                "x180": "x180_pulse0",
                "x90": "x90_pulse0",
                "-x90": "-x90_pulse0",
                "y90": "y90_pulse0",
                "y180": "y180_pulse0",
                "-y90": "-y90_pulse0",
            },
            "mixInputs": {
                "I": ('con1', 3),
                "Q": ('con1', 4),
                "mixer": "octave_octave1_2",
                "lo_frequency": 6452785000.0,
            },
        },
        "q1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 100000000.0,
            "operations": {
                "cw": "const_pulse",
                "pi": "pi_pulse1",
                "pi2": "pi_over_two_pulse1",
                "x180": "x180_pulse1",
                "x90": "x90_pulse1",
                "-x90": "-x90_pulse1",
                "y90": "y90_pulse1",
                "y180": "y180_pulse1",
                "-y90": "-y90_pulse1",
            },
            "mixInputs": {
                "I": ('con1', 3),
                "Q": ('con1', 4),
                "mixer": "octave_octave1_2",
                "lo_frequency": 6189000000.0,
            },
        },
        "q2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 100000000.0,
            "operations": {
                "cw": "const_pulse",
                "pi": "pi_pulse2",
                "pi2": "pi_over_two_pulse2",
                "x180": "x180_pulse2",
                "x90": "x90_pulse2",
                "-x90": "-x90_pulse2",
                "y90": "y90_pulse2",
                "y180": "y180_pulse2",
                "-y90": "-y90_pulse2",
            },
            "mixInputs": {
                "I": ('con1', 3),
                "Q": ('con1', 4),
                "mixer": "octave_octave1_2",
                "lo_frequency": 6007000000.0,
            },
        },
        "q3": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 100000000.0,
            "operations": {
                "cw": "const_pulse",
                "pi": "pi_pulse3",
                "pi2": "pi_over_two_pulse3",
                "x180": "x180_pulse3",
                "x90": "x90_pulse3",
                "-x90": "-x90_pulse3",
                "y90": "y90_pulse3",
                "y180": "y180_pulse3",
                "-y90": "-y90_pulse3",
            },
            "mixInputs": {
                "I": ('con1', 3),
                "Q": ('con1', 4),
                "mixer": "octave_octave1_2",
                "lo_frequency": 5882000000.0,
            },
        },
        "q4": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 100000000.0,
            "operations": {
                "cw": "const_pulse",
                "pi": "pi_pulse4",
                "pi2": "pi_over_two_pulse4",
                "x180": "x180_pulse4",
                "x90": "x90_pulse4",
                "-x90": "-x90_pulse4",
                "y90": "y90_pulse4",
                "y180": "y180_pulse4",
                "-y90": "-y90_pulse4",
            },
            "mixInputs": {
                "I": ('con1', 3),
                "Q": ('con1', 4),
                "mixer": "octave_octave1_2",
                "lo_frequency": 5668000000.0,
            },
        },
        "q5": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 100000000.0,
            "operations": {
                "cw": "const_pulse",
                "pi": "pi_pulse5",
                "pi2": "pi_over_two_pulse5",
                "x180": "x180_pulse5",
                "x90": "x90_pulse5",
                "-x90": "-x90_pulse5",
                "y90": "y90_pulse5",
                "y180": "y180_pulse5",
                "-y90": "-y90_pulse5",
            },
            "mixInputs": {
                "I": ('con1', 3),
                "Q": ('con1', 4),
                "mixer": "octave_octave1_2",
                "lo_frequency": 5467000000.0,
            },
        },
        "q6": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 100000000.0,
            "operations": {
                "cw": "const_pulse",
                "pi": "pi_pulse6",
                "pi2": "pi_over_two_pulse6",
                "x180": "x180_pulse6",
                "x90": "x90_pulse6",
                "-x90": "-x90_pulse6",
                "y90": "y90_pulse6",
                "y180": "y180_pulse6",
                "-y90": "-y90_pulse6",
            },
            "mixInputs": {
                "I": ('con1', 3),
                "Q": ('con1', 4),
                "mixer": "octave_octave1_2",
                "lo_frequency": 5342000000.0,
            },
        },
        "flux0": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "operations": {
                "const": "const_flux_pulse0",
            },
            "singleInput": {
                "port": ('con1', 7),
            },
        },
        "flux1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "operations": {
                "const": "const_flux_pulse1",
            },
            "singleInput": {
                "port": ('con1', 8),
            },
        },
        "flux2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "operations": {
                "const": "const_flux_pulse2",
            },
            "singleInput": {
                "port": ('con1', 9),
            },
        },
        "flux3": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "operations": {
                "const": "const_flux_pulse3",
            },
            "singleInput": {
                "port": ('con1', 10),
            },
        },
        "flux4": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "operations": {
                "const": "const_flux_pulse4",
            },
            "singleInput": {
                "port": ('con1', 7),
            },
        },
        "flux5": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "operations": {
                "const": "const_flux_pulse5",
            },
            "singleInput": {
                "port": ('con1', 8),
            },
        },
        "flux6": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "operations": {
                "const": "const_flux_pulse6",
            },
            "singleInput": {
                "port": ('con1', 9),
            },
        },
    },
    "pulses": {
        "const_pulse": {
            "length": 1000,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
            "operation": "control",
        },
        "const_flux_pulse0": {
            "length": 16,
            "waveforms": {
                "single": "const_flux0_wf",
            },
            "operation": "control",
        },
        "const_flux_pulse1": {
            "length": 16,
            "waveforms": {
                "single": "const_flux1_wf",
            },
            "operation": "control",
        },
        "const_flux_pulse2": {
            "length": 16,
            "waveforms": {
                "single": "const_flux2_wf",
            },
            "operation": "control",
        },
        "const_flux_pulse3": {
            "length": 16,
            "waveforms": {
                "single": "const_flux3_wf",
            },
            "operation": "control",
        },
        "const_flux_pulse4": {
            "length": 16,
            "waveforms": {
                "single": "const_flux4_wf",
            },
            "operation": "control",
        },
        "const_flux_pulse5": {
            "length": 16,
            "waveforms": {
                "single": "const_flux5_wf",
            },
            "operation": "control",
        },
        "const_flux_pulse6": {
            "length": 16,
            "waveforms": {
                "single": "const_flux6_wf",
            },
            "operation": "control",
        },
        "readout_pulse_q0": {
            "length": 500,
            "waveforms": {
                "I": "readout0_wf",
                "Q": "zero_wf",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights0",
                "sin": "sine_weights0",
                "minus_sin": "minus_sine_weights0",
                "rotated_cos": "rotated_cosine_weights0",
                "rotated_sin": "rotated_sine_weights0",
                "rotated_minus_sin": "rotated_minus_sine_weights0",
                "opt_cos": "opt_cosine_weights0",
                "opt_sin": "opt_sine_weights0",
                "opt_minus_sin": "opt_minus_sine_weights0",
            },
            "operation": "measurement",
        },
        "readout_pulse_q1": {
            "length": 500,
            "waveforms": {
                "I": "readout1_wf",
                "Q": "zero_wf",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights1",
                "sin": "sine_weights1",
                "minus_sin": "minus_sine_weights1",
                "rotated_cos": "rotated_cosine_weights1",
                "rotated_sin": "rotated_sine_weights1",
                "rotated_minus_sin": "rotated_minus_sine_weights1",
                "opt_cos": "opt_cosine_weights1",
                "opt_sin": "opt_sine_weights1",
                "opt_minus_sin": "opt_minus_sine_weights1",
            },
            "operation": "measurement",
        },
        "readout_pulse_q2": {
            "length": 500,
            "waveforms": {
                "I": "readout2_wf",
                "Q": "zero_wf",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights2",
                "sin": "sine_weights2",
                "minus_sin": "minus_sine_weights2",
                "rotated_cos": "rotated_cosine_weights2",
                "rotated_sin": "rotated_sine_weights2",
                "rotated_minus_sin": "rotated_minus_sine_weights2",
                "opt_cos": "opt_cosine_weights2",
                "opt_sin": "opt_sine_weights2",
                "opt_minus_sin": "opt_minus_sine_weights2",
            },
            "operation": "measurement",
        },
        "readout_pulse_q3": {
            "length": 500,
            "waveforms": {
                "I": "readout3_wf",
                "Q": "zero_wf",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights3",
                "sin": "sine_weights3",
                "minus_sin": "minus_sine_weights3",
                "rotated_cos": "rotated_cosine_weights3",
                "rotated_sin": "rotated_sine_weights3",
                "rotated_minus_sin": "rotated_minus_sine_weights3",
                "opt_cos": "opt_cosine_weights3",
                "opt_sin": "opt_sine_weights3",
                "opt_minus_sin": "opt_minus_sine_weights3",
            },
            "operation": "measurement",
        },
        "readout_pulse_q4": {
            "length": 500,
            "waveforms": {
                "I": "readout4_wf",
                "Q": "zero_wf",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights4",
                "sin": "sine_weights4",
                "minus_sin": "minus_sine_weights4",
                "rotated_cos": "rotated_cosine_weights4",
                "rotated_sin": "rotated_sine_weights4",
                "rotated_minus_sin": "rotated_minus_sine_weights4",
                "opt_cos": "opt_cosine_weights4",
                "opt_sin": "opt_sine_weights4",
                "opt_minus_sin": "opt_minus_sine_weights4",
            },
            "operation": "measurement",
        },
        "readout_pulse_q5": {
            "length": 500,
            "waveforms": {
                "I": "readout5_wf",
                "Q": "zero_wf",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights5",
                "sin": "sine_weights5",
                "minus_sin": "minus_sine_weights5",
                "rotated_cos": "rotated_cosine_weights5",
                "rotated_sin": "rotated_sine_weights5",
                "rotated_minus_sin": "rotated_minus_sine_weights5",
                "opt_cos": "opt_cosine_weights5",
                "opt_sin": "opt_sine_weights5",
                "opt_minus_sin": "opt_minus_sine_weights5",
            },
            "operation": "measurement",
        },
        "readout_pulse_q6": {
            "length": 500,
            "waveforms": {
                "I": "readout6_wf",
                "Q": "zero_wf",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights6",
                "sin": "sine_weights6",
                "minus_sin": "minus_sine_weights6",
                "rotated_cos": "rotated_cosine_weights6",
                "rotated_sin": "rotated_sine_weights6",
                "rotated_minus_sin": "rotated_minus_sine_weights6",
                "opt_cos": "opt_cosine_weights6",
                "opt_sin": "opt_sine_weights6",
                "opt_minus_sin": "opt_minus_sine_weights6",
            },
            "operation": "measurement",
        },
        "pi_pulse0": {
            "length": 64,
            "waveforms": {
                "I": "pi_wf0",
                "Q": "zero_wf",
            },
            "operation": "control",
        },
        "pi_pulse1": {
            "length": 40,
            "waveforms": {
                "I": "pi_wf1",
                "Q": "zero_wf",
            },
            "operation": "control",
        },
        "pi_pulse2": {
            "length": 40,
            "waveforms": {
                "I": "pi_wf2",
                "Q": "zero_wf",
            },
            "operation": "control",
        },
        "pi_pulse3": {
            "length": 40,
            "waveforms": {
                "I": "pi_wf3",
                "Q": "zero_wf",
            },
            "operation": "control",
        },
        "pi_pulse4": {
            "length": 40,
            "waveforms": {
                "I": "pi_wf4",
                "Q": "zero_wf",
            },
            "operation": "control",
        },
        "pi_pulse5": {
            "length": 40,
            "waveforms": {
                "I": "pi_wf5",
                "Q": "zero_wf",
            },
            "operation": "control",
        },
        "pi_pulse6": {
            "length": 40,
            "waveforms": {
                "I": "pi_wf6",
                "Q": "zero_wf",
            },
            "operation": "control",
        },
        "pi_over_two_pulse0": {
            "length": 64,
            "waveforms": {
                "I": "pi_over_two_wf0",
                "Q": "zero_wf",
            },
            "operation": "control",
        },
        "pi_over_two_pulse1": {
            "length": 40,
            "waveforms": {
                "I": "pi_over_two_wf1",
                "Q": "zero_wf",
            },
            "operation": "control",
        },
        "pi_over_two_pulse2": {
            "length": 40,
            "waveforms": {
                "I": "pi_over_two_wf2",
                "Q": "zero_wf",
            },
            "operation": "control",
        },
        "pi_over_two_pulse3": {
            "length": 40,
            "waveforms": {
                "I": "pi_over_two_wf3",
                "Q": "zero_wf",
            },
            "operation": "control",
        },
        "pi_over_two_pulse4": {
            "length": 40,
            "waveforms": {
                "I": "pi_over_two_wf4",
                "Q": "zero_wf",
            },
            "operation": "control",
        },
        "pi_over_two_pulse5": {
            "length": 40,
            "waveforms": {
                "I": "pi_over_two_wf5",
                "Q": "zero_wf",
            },
            "operation": "control",
        },
        "pi_over_two_pulse6": {
            "length": 40,
            "waveforms": {
                "I": "pi_over_two_wf6",
                "Q": "zero_wf",
            },
            "operation": "control",
        },
        "x90_pulse0": {
            "length": 180,
            "waveforms": {
                "I": "x90_I_wf0",
                "Q": "x90_Q_wf0",
            },
            "operation": "control",
        },
        "x90_pulse1": {
            "length": 40,
            "waveforms": {
                "I": "x90_I_wf1",
                "Q": "x90_Q_wf1",
            },
            "operation": "control",
        },
        "x90_pulse2": {
            "length": 40,
            "waveforms": {
                "I": "x90_I_wf2",
                "Q": "x90_Q_wf2",
            },
            "operation": "control",
        },
        "x90_pulse3": {
            "length": 40,
            "waveforms": {
                "I": "x90_I_wf3",
                "Q": "x90_Q_wf3",
            },
            "operation": "control",
        },
        "x90_pulse4": {
            "length": 40,
            "waveforms": {
                "I": "x90_I_wf4",
                "Q": "x90_Q_wf4",
            },
            "operation": "control",
        },
        "x90_pulse5": {
            "length": 40,
            "waveforms": {
                "I": "x90_I_wf5",
                "Q": "x90_Q_wf5",
            },
            "operation": "control",
        },
        "x90_pulse6": {
            "length": 40,
            "waveforms": {
                "I": "x90_I_wf6",
                "Q": "x90_Q_wf6",
            },
            "operation": "control",
        },
        "x180_pulse0": {
            "length": 180,
            "waveforms": {
                "I": "x180_I_wf0",
                "Q": "x180_Q_wf0",
            },
            "operation": "control",
        },
        "x180_pulse1": {
            "length": 40,
            "waveforms": {
                "I": "x180_I_wf1",
                "Q": "x180_Q_wf1",
            },
            "operation": "control",
        },
        "x180_pulse2": {
            "length": 40,
            "waveforms": {
                "I": "x180_I_wf2",
                "Q": "x180_Q_wf2",
            },
            "operation": "control",
        },
        "x180_pulse3": {
            "length": 40,
            "waveforms": {
                "I": "x180_I_wf3",
                "Q": "x180_Q_wf3",
            },
            "operation": "control",
        },
        "x180_pulse4": {
            "length": 40,
            "waveforms": {
                "I": "x180_I_wf4",
                "Q": "x180_Q_wf4",
            },
            "operation": "control",
        },
        "x180_pulse5": {
            "length": 40,
            "waveforms": {
                "I": "x180_I_wf5",
                "Q": "x180_Q_wf5",
            },
            "operation": "control",
        },
        "x180_pulse6": {
            "length": 40,
            "waveforms": {
                "I": "x180_I_wf6",
                "Q": "x180_Q_wf6",
            },
            "operation": "control",
        },
        "-x90_pulse0": {
            "length": 180,
            "waveforms": {
                "I": "minus_x90_I_wf0",
                "Q": "minus_x90_Q_wf0",
            },
            "operation": "control",
        },
        "-x90_pulse1": {
            "length": 40,
            "waveforms": {
                "I": "minus_x90_I_wf1",
                "Q": "minus_x90_Q_wf1",
            },
            "operation": "control",
        },
        "-x90_pulse2": {
            "length": 40,
            "waveforms": {
                "I": "minus_x90_I_wf2",
                "Q": "minus_x90_Q_wf2",
            },
            "operation": "control",
        },
        "-x90_pulse3": {
            "length": 40,
            "waveforms": {
                "I": "minus_x90_I_wf3",
                "Q": "minus_x90_Q_wf3",
            },
            "operation": "control",
        },
        "-x90_pulse4": {
            "length": 40,
            "waveforms": {
                "I": "minus_x90_I_wf4",
                "Q": "minus_x90_Q_wf4",
            },
            "operation": "control",
        },
        "-x90_pulse5": {
            "length": 40,
            "waveforms": {
                "I": "minus_x90_I_wf5",
                "Q": "minus_x90_Q_wf5",
            },
            "operation": "control",
        },
        "-x90_pulse6": {
            "length": 40,
            "waveforms": {
                "I": "minus_x90_I_wf6",
                "Q": "minus_x90_Q_wf6",
            },
            "operation": "control",
        },
        "y90_pulse0": {
            "length": 180,
            "waveforms": {
                "I": "y90_I_wf0",
                "Q": "y90_Q_wf0",
            },
            "operation": "control",
        },
        "y90_pulse1": {
            "length": 40,
            "waveforms": {
                "I": "y90_I_wf1",
                "Q": "y90_Q_wf1",
            },
            "operation": "control",
        },
        "y90_pulse2": {
            "length": 40,
            "waveforms": {
                "I": "y90_I_wf2",
                "Q": "y90_Q_wf2",
            },
            "operation": "control",
        },
        "y90_pulse3": {
            "length": 40,
            "waveforms": {
                "I": "y90_I_wf3",
                "Q": "y90_Q_wf3",
            },
            "operation": "control",
        },
        "y90_pulse4": {
            "length": 40,
            "waveforms": {
                "I": "y90_I_wf4",
                "Q": "y90_Q_wf4",
            },
            "operation": "control",
        },
        "y90_pulse5": {
            "length": 40,
            "waveforms": {
                "I": "y90_I_wf5",
                "Q": "y90_Q_wf5",
            },
            "operation": "control",
        },
        "y90_pulse6": {
            "length": 40,
            "waveforms": {
                "I": "y90_I_wf6",
                "Q": "y90_Q_wf6",
            },
            "operation": "control",
        },
        "y180_pulse0": {
            "length": 180,
            "waveforms": {
                "I": "y180_I_wf0",
                "Q": "y180_Q_wf0",
            },
            "operation": "control",
        },
        "y180_pulse1": {
            "length": 40,
            "waveforms": {
                "I": "y180_I_wf1",
                "Q": "y180_Q_wf1",
            },
            "operation": "control",
        },
        "y180_pulse2": {
            "length": 40,
            "waveforms": {
                "I": "y180_I_wf2",
                "Q": "y180_Q_wf2",
            },
            "operation": "control",
        },
        "y180_pulse3": {
            "length": 40,
            "waveforms": {
                "I": "y180_I_wf3",
                "Q": "y180_Q_wf3",
            },
            "operation": "control",
        },
        "y180_pulse4": {
            "length": 40,
            "waveforms": {
                "I": "y180_I_wf4",
                "Q": "y180_Q_wf4",
            },
            "operation": "control",
        },
        "y180_pulse5": {
            "length": 40,
            "waveforms": {
                "I": "y180_I_wf5",
                "Q": "y180_Q_wf5",
            },
            "operation": "control",
        },
        "y180_pulse6": {
            "length": 40,
            "waveforms": {
                "I": "y180_I_wf6",
                "Q": "y180_Q_wf6",
            },
            "operation": "control",
        },
        "-y90_pulse0": {
            "length": 180,
            "waveforms": {
                "I": "minus_y90_I_wf0",
                "Q": "minus_y90_Q_wf0",
            },
            "operation": "control",
        },
        "-y90_pulse1": {
            "length": 40,
            "waveforms": {
                "I": "minus_y90_I_wf1",
                "Q": "minus_y90_Q_wf1",
            },
            "operation": "control",
        },
        "-y90_pulse2": {
            "length": 40,
            "waveforms": {
                "I": "minus_y90_I_wf2",
                "Q": "minus_y90_Q_wf2",
            },
            "operation": "control",
        },
        "-y90_pulse3": {
            "length": 40,
            "waveforms": {
                "I": "minus_y90_I_wf3",
                "Q": "minus_y90_Q_wf3",
            },
            "operation": "control",
        },
        "-y90_pulse4": {
            "length": 40,
            "waveforms": {
                "I": "minus_y90_I_wf4",
                "Q": "minus_y90_Q_wf4",
            },
            "operation": "control",
        },
        "-y90_pulse5": {
            "length": 40,
            "waveforms": {
                "I": "minus_y90_I_wf5",
                "Q": "minus_y90_Q_wf5",
            },
            "operation": "control",
        },
        "-y90_pulse6": {
            "length": 40,
            "waveforms": {
                "I": "minus_y90_I_wf6",
                "Q": "minus_y90_Q_wf6",
            },
            "operation": "control",
        },
    },
    "waveforms": {
        "zero_wf": {
            "sample": 0.0,
            "type": "constant",
        },
        "const_wf": {
            "sample": 0.1,
            "type": "constant",
        },
        "const_flux0_wf": {
            "sample": 0.25,
            "type": "constant",
        },
        "const_flux1_wf": {
            "sample": 0.25,
            "type": "constant",
        },
        "const_flux2_wf": {
            "sample": 0.25,
            "type": "constant",
        },
        "const_flux3_wf": {
            "sample": 0.25,
            "type": "constant",
        },
        "const_flux4_wf": {
            "sample": 0.25,
            "type": "constant",
        },
        "const_flux5_wf": {
            "sample": 0.25,
            "type": "constant",
        },
        "const_flux6_wf": {
            "sample": 0.25,
            "type": "constant",
        },
        "readout0_wf": {
            "sample": 0.3,
            "type": "constant",
        },
        "readout1_wf": {
            "sample": 0.3,
            "type": "constant",
        },
        "readout2_wf": {
            "sample": 0.3,
            "type": "constant",
        },
        "readout3_wf": {
            "sample": 0.3,
            "type": "constant",
        },
        "readout4_wf": {
            "sample": 0.3,
            "type": "constant",
        },
        "readout5_wf": {
            "sample": 0.3,
            "type": "constant",
        },
        "readout6_wf": {
            "sample": 0.3,
            "type": "constant",
        },
        "pi_wf0": {
            "sample": 0.1092,
            "type": "constant",
        },
        "pi_wf1": {
            "sample": 0.25,
            "type": "constant",
        },
        "pi_wf2": {
            "sample": 0.25,
            "type": "constant",
        },
        "pi_wf3": {
            "sample": 0.25,
            "type": "constant",
        },
        "pi_wf4": {
            "sample": 0.25,
            "type": "constant",
        },
        "pi_wf5": {
            "sample": 0.25,
            "type": "constant",
        },
        "pi_wf6": {
            "sample": 0.25,
            "type": "constant",
        },
        "pi_over_two_wf0": {
            "sample": 0.0546,
            "type": "constant",
        },
        "pi_over_two_wf1": {
            "sample": 0.125,
            "type": "constant",
        },
        "pi_over_two_wf2": {
            "sample": 0.125,
            "type": "constant",
        },
        "pi_over_two_wf3": {
            "sample": 0.125,
            "type": "constant",
        },
        "pi_over_two_wf4": {
            "sample": 0.125,
            "type": "constant",
        },
        "pi_over_two_wf5": {
            "sample": 0.125,
            "type": "constant",
        },
        "pi_over_two_wf6": {
            "sample": 0.125,
            "type": "constant",
        },
        "x90_I_wf0": {
            "samples": [0.0, 0.00040416620465755834, 0.0008320318708446434, 0.0012845788945819647, 0.001762798661865914, 0.002267689544406204, 0.002800254194721963, 0.0033614966397724627, 0.0039524191733662575, 0.004574019048730957, 0.005227284973831431, 0.005913193413293454, 0.0066327047021169545, 0.007386758977742835, 0.008176271938463344, 0.009002130437630656, 0.009865187924613631, 0.01076625974497014, 0.011706118313832137, 0.012685488178032564, 0.013705040984026638, 0.01476539037016362, 0.015867086803336754, 0.01701061238146674, 0.01819637562464483, 0.01942470627906296, 0.020695850159076677, 0.02200996405386956, 0.02336711072620154, 0.02476725403161595, 0.026210254187238206, 0.02769586321991057, 0.029223720623861513, 0.030793349258393096, 0.032404151516175934, 0.03405540579265952, 0.03574626328682754, 0.037475745163046886, 0.039242740103069274, 0.04104600227634162, 0.04288414975566317, 0.04475566340389212, 0.04665888625585296, 0.04859202341783009, 0.05055314250505774, 0.05254017463543585, 0.054550915995324765, 0.05658302999070759, 0.058634049994269, 0.060701382696035804, 0.06278231206217397, 0.06487400390335323, 0.06697351105079447, 0.06907777913472397, 0.07118365295649506, 0.07328788344212264, 0.07538713516143358, 0.07747799439348926, 0.07955697771541118, 0.08162054108826197, 0.08366508941022711, 0.085686986504034, 0.0876825655023604, 0.08964813959194799, 0.09158001307427546, 0.09347449269798133, 0.09532789921578447, 0.09713657911645074, 0.09889691648041778, 0.10060534490603643, 0.10225835945203246, 0.10385252854075183, 0.1053845057660392, 0.1068510415492232, 0.1082489945866514, 0.10957534303253762, 0.1108271953615586, 0.112001800856664, 0.1130965596689426, 0.11410903239811193, 0.11503694914426066, 0.11587821798386094, 0.11663093282577114, 0.11729338060594716, 0.11786404778285947, 0.1183416260991481, 0.11872501757881927, 0.11901333873326818, 0.11920592395357711] + [0.11930232807085857] * 2 + [0.11920592395357711, 0.11901333873326818, 0.11872501757881927, 0.1183416260991481, 0.11786404778285947, 0.11729338060594716, 0.11663093282577114, 0.11587821798386094, 0.11503694914426066, 0.11410903239811193, 0.1130965596689426, 0.112001800856664, 0.1108271953615586, 0.10957534303253762, 0.1082489945866514, 0.1068510415492232, 0.1053845057660392, 0.10385252854075183, 0.10225835945203246, 0.10060534490603643, 0.09889691648041778, 0.09713657911645074, 0.09532789921578447, 0.09347449269798133, 0.09158001307427546, 0.08964813959194799, 0.0876825655023604, 0.085686986504034, 0.08366508941022711, 0.08162054108826197, 0.07955697771541118, 0.07747799439348926, 0.07538713516143358, 0.07328788344212264, 0.07118365295649506, 0.06907777913472397, 0.06697351105079447, 0.06487400390335323, 0.06278231206217397, 0.060701382696035804, 0.058634049994269, 0.05658302999070759, 0.054550915995324765, 0.05254017463543585, 0.05055314250505774, 0.04859202341783009, 0.04665888625585296, 0.04475566340389212, 0.04288414975566317, 0.04104600227634162, 0.039242740103069274, 0.037475745163046886, 0.03574626328682754, 0.03405540579265952, 0.032404151516175934, 0.030793349258393096, 0.029223720623861513, 0.02769586321991057, 0.026210254187238206, 0.02476725403161595, 0.02336711072620154, 0.02200996405386956, 0.020695850159076677, 0.01942470627906296, 0.01819637562464483, 0.01701061238146674, 0.015867086803336754, 0.01476539037016362, 0.013705040984026638, 0.012685488178032564, 0.011706118313832137, 0.01076625974497014, 0.009865187924613631, 0.009002130437630656, 0.008176271938463344, 0.007386758977742835, 0.0066327047021169545, 0.005913193413293454, 0.005227284973831431, 0.004574019048730957, 0.0039524191733662575, 0.0033614966397724627, 0.002800254194721963, 0.002267689544406204, 0.001762798661865914, 0.0012845788945819647, 0.0008320318708446434, 0.00040416620465755834, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_I_wf1": {
            "samples": [0.0, 0.0022150469433227073, 0.005015813123173687, 0.008491584753998697, 0.012723560920712553, 0.017776666404548624, 0.023690402987698853, 0.030469425725473138, 0.03807475022143508, 0.04641664910656638, 0.05535034039512257, 0.06467547541850178, 0.0741401843068172, 0.08345003991731476, 0.09228178991126627, 0.10030113887181125, 0.10718331324880155, 0.11263469369056484, 0.11641352732340533] + [0.11834769134210223] * 2 + [0.11641352732340533, 0.11263469369056484, 0.10718331324880155, 0.10030113887181125, 0.09228178991126627, 0.08345003991731476, 0.0741401843068172, 0.06467547541850178, 0.05535034039512257, 0.04641664910656638, 0.03807475022143508, 0.030469425725473138, 0.023690402987698853, 0.017776666404548624, 0.012723560920712553, 0.008491584753998697, 0.005015813123173687, 0.0022150469433227073, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_I_wf2": {
            "samples": [0.0, 0.0022150469433227073, 0.005015813123173687, 0.008491584753998697, 0.012723560920712553, 0.017776666404548624, 0.023690402987698853, 0.030469425725473138, 0.03807475022143508, 0.04641664910656638, 0.05535034039512257, 0.06467547541850178, 0.0741401843068172, 0.08345003991731476, 0.09228178991126627, 0.10030113887181125, 0.10718331324880155, 0.11263469369056484, 0.11641352732340533] + [0.11834769134210223] * 2 + [0.11641352732340533, 0.11263469369056484, 0.10718331324880155, 0.10030113887181125, 0.09228178991126627, 0.08345003991731476, 0.0741401843068172, 0.06467547541850178, 0.05535034039512257, 0.04641664910656638, 0.03807475022143508, 0.030469425725473138, 0.023690402987698853, 0.017776666404548624, 0.012723560920712553, 0.008491584753998697, 0.005015813123173687, 0.0022150469433227073, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_I_wf3": {
            "samples": [0.0, 0.0022150469433227073, 0.005015813123173687, 0.008491584753998697, 0.012723560920712553, 0.017776666404548624, 0.023690402987698853, 0.030469425725473138, 0.03807475022143508, 0.04641664910656638, 0.05535034039512257, 0.06467547541850178, 0.0741401843068172, 0.08345003991731476, 0.09228178991126627, 0.10030113887181125, 0.10718331324880155, 0.11263469369056484, 0.11641352732340533] + [0.11834769134210223] * 2 + [0.11641352732340533, 0.11263469369056484, 0.10718331324880155, 0.10030113887181125, 0.09228178991126627, 0.08345003991731476, 0.0741401843068172, 0.06467547541850178, 0.05535034039512257, 0.04641664910656638, 0.03807475022143508, 0.030469425725473138, 0.023690402987698853, 0.017776666404548624, 0.012723560920712553, 0.008491584753998697, 0.005015813123173687, 0.0022150469433227073, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_I_wf4": {
            "samples": [0.0, 0.0022150469433227073, 0.005015813123173687, 0.008491584753998697, 0.012723560920712553, 0.017776666404548624, 0.023690402987698853, 0.030469425725473138, 0.03807475022143508, 0.04641664910656638, 0.05535034039512257, 0.06467547541850178, 0.0741401843068172, 0.08345003991731476, 0.09228178991126627, 0.10030113887181125, 0.10718331324880155, 0.11263469369056484, 0.11641352732340533] + [0.11834769134210223] * 2 + [0.11641352732340533, 0.11263469369056484, 0.10718331324880155, 0.10030113887181125, 0.09228178991126627, 0.08345003991731476, 0.0741401843068172, 0.06467547541850178, 0.05535034039512257, 0.04641664910656638, 0.03807475022143508, 0.030469425725473138, 0.023690402987698853, 0.017776666404548624, 0.012723560920712553, 0.008491584753998697, 0.005015813123173687, 0.0022150469433227073, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_I_wf5": {
            "samples": [0.0, 0.0022150469433227073, 0.005015813123173687, 0.008491584753998697, 0.012723560920712553, 0.017776666404548624, 0.023690402987698853, 0.030469425725473138, 0.03807475022143508, 0.04641664910656638, 0.05535034039512257, 0.06467547541850178, 0.0741401843068172, 0.08345003991731476, 0.09228178991126627, 0.10030113887181125, 0.10718331324880155, 0.11263469369056484, 0.11641352732340533] + [0.11834769134210223] * 2 + [0.11641352732340533, 0.11263469369056484, 0.10718331324880155, 0.10030113887181125, 0.09228178991126627, 0.08345003991731476, 0.0741401843068172, 0.06467547541850178, 0.05535034039512257, 0.04641664910656638, 0.03807475022143508, 0.030469425725473138, 0.023690402987698853, 0.017776666404548624, 0.012723560920712553, 0.008491584753998697, 0.005015813123173687, 0.0022150469433227073, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_I_wf6": {
            "samples": [0.0, 0.0022150469433227073, 0.005015813123173687, 0.008491584753998697, 0.012723560920712553, 0.017776666404548624, 0.023690402987698853, 0.030469425725473138, 0.03807475022143508, 0.04641664910656638, 0.05535034039512257, 0.06467547541850178, 0.0741401843068172, 0.08345003991731476, 0.09228178991126627, 0.10030113887181125, 0.10718331324880155, 0.11263469369056484, 0.11641352732340533] + [0.11834769134210223] * 2 + [0.11641352732340533, 0.11263469369056484, 0.10718331324880155, 0.10030113887181125, 0.09228178991126627, 0.08345003991731476, 0.0741401843068172, 0.06467547541850178, 0.05535034039512257, 0.04641664910656638, 0.03807475022143508, 0.030469425725473138, 0.023690402987698853, 0.017776666404548624, 0.012723560920712553, 0.008491584753998697, 0.005015813123173687, 0.0022150469433227073, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_Q_wf0": {
            "samples": [0.0] * 180,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_Q_wf1": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_Q_wf2": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_Q_wf3": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_Q_wf4": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_Q_wf5": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_Q_wf6": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_I_wf0": {
            "samples": [0.0, 0.0008083324093151167, 0.0016640637416892867, 0.0025691577891639294, 0.003525597323731828, 0.004535379088812408, 0.005600508389443926, 0.006722993279544925, 0.007904838346732515, 0.009148038097461914, 0.010454569947662862, 0.011826386826586908, 0.013265409404233909, 0.01477351795548567, 0.016352543876926688, 0.018004260875261312, 0.019730375849227263, 0.02153251948994028, 0.023412236627664274, 0.02537097635606513, 0.027410081968053276, 0.02953078074032724, 0.03173417360667351, 0.03402122476293348, 0.03639275124928966, 0.03884941255812592, 0.041391700318153354, 0.04401992810773912, 0.04673422145240308, 0.0495345080632319, 0.05242050837447641, 0.05539172643982114, 0.058447441247723025, 0.06158669851678619, 0.06480830303235187, 0.06811081158531904, 0.07149252657365508, 0.07495149032609377, 0.07848548020613855, 0.08209200455268324, 0.08576829951132633, 0.08951132680778424, 0.09331777251170592, 0.09718404683566018, 0.10110628501011548, 0.1050803492708717, 0.10910183199064953, 0.11316605998141518, 0.117268099988538, 0.12140276539207161, 0.12556462412434793, 0.12974800780670645, 0.13394702210158893, 0.13815555826944795, 0.14236730591299013, 0.14657576688424528, 0.15077427032286717, 0.15495598878697853, 0.15911395543082235, 0.16324108217652394, 0.16733017882045423, 0.171373973008068, 0.1753651310047208, 0.17929627918389598, 0.18316002614855093, 0.18694898539596266, 0.19065579843156893, 0.19427315823290148, 0.19779383296083555, 0.20121068981207285, 0.20451671890406492, 0.20770505708150366, 0.2107690115320784, 0.2137020830984464, 0.2164979891733028, 0.21915068606507523, 0.2216543907231172, 0.224003601713328, 0.2261931193378852, 0.22821806479622386, 0.23007389828852132, 0.23175643596772189, 0.23326186565154228, 0.2345867612118943, 0.23572809556571894, 0.2366832521982962, 0.23745003515763854, 0.23802667746653636, 0.23841184790715422] + [0.23860465614171714] * 2 + [0.23841184790715422, 0.23802667746653636, 0.23745003515763854, 0.2366832521982962, 0.23572809556571894, 0.2345867612118943, 0.23326186565154228, 0.23175643596772189, 0.23007389828852132, 0.22821806479622386, 0.2261931193378852, 0.224003601713328, 0.2216543907231172, 0.21915068606507523, 0.2164979891733028, 0.2137020830984464, 0.2107690115320784, 0.20770505708150366, 0.20451671890406492, 0.20121068981207285, 0.19779383296083555, 0.19427315823290148, 0.19065579843156893, 0.18694898539596266, 0.18316002614855093, 0.17929627918389598, 0.1753651310047208, 0.171373973008068, 0.16733017882045423, 0.16324108217652394, 0.15911395543082235, 0.15495598878697853, 0.15077427032286717, 0.14657576688424528, 0.14236730591299013, 0.13815555826944795, 0.13394702210158893, 0.12974800780670645, 0.12556462412434793, 0.12140276539207161, 0.117268099988538, 0.11316605998141518, 0.10910183199064953, 0.1050803492708717, 0.10110628501011548, 0.09718404683566018, 0.09331777251170592, 0.08951132680778424, 0.08576829951132633, 0.08209200455268324, 0.07848548020613855, 0.07495149032609377, 0.07149252657365508, 0.06811081158531904, 0.06480830303235187, 0.06158669851678619, 0.058447441247723025, 0.05539172643982114, 0.05242050837447641, 0.0495345080632319, 0.04673422145240308, 0.04401992810773912, 0.041391700318153354, 0.03884941255812592, 0.03639275124928966, 0.03402122476293348, 0.03173417360667351, 0.02953078074032724, 0.027410081968053276, 0.02537097635606513, 0.023412236627664274, 0.02153251948994028, 0.019730375849227263, 0.018004260875261312, 0.016352543876926688, 0.01477351795548567, 0.013265409404233909, 0.011826386826586908, 0.010454569947662862, 0.009148038097461914, 0.007904838346732515, 0.006722993279544925, 0.005600508389443926, 0.004535379088812408, 0.003525597323731828, 0.0025691577891639294, 0.0016640637416892867, 0.0008083324093151167, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_I_wf1": {
            "samples": [0.0, 0.004430093886645415, 0.010031626246347373, 0.016983169507997393, 0.025447121841425106, 0.03555333280909725, 0.047380805975397705, 0.060938851450946276, 0.07614950044287017, 0.09283329821313276, 0.11070068079024514, 0.12935095083700357, 0.1482803686136344, 0.1669000798346295, 0.18456357982253255, 0.2006022777436225, 0.2143666264976031, 0.22526938738112967, 0.23282705464681067] + [0.23669538268420445] * 2 + [0.23282705464681067, 0.22526938738112967, 0.2143666264976031, 0.2006022777436225, 0.18456357982253255, 0.1669000798346295, 0.1482803686136344, 0.12935095083700357, 0.11070068079024514, 0.09283329821313276, 0.07614950044287017, 0.060938851450946276, 0.047380805975397705, 0.03555333280909725, 0.025447121841425106, 0.016983169507997393, 0.010031626246347373, 0.004430093886645415, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_I_wf2": {
            "samples": [0.0, 0.004430093886645415, 0.010031626246347373, 0.016983169507997393, 0.025447121841425106, 0.03555333280909725, 0.047380805975397705, 0.060938851450946276, 0.07614950044287017, 0.09283329821313276, 0.11070068079024514, 0.12935095083700357, 0.1482803686136344, 0.1669000798346295, 0.18456357982253255, 0.2006022777436225, 0.2143666264976031, 0.22526938738112967, 0.23282705464681067] + [0.23669538268420445] * 2 + [0.23282705464681067, 0.22526938738112967, 0.2143666264976031, 0.2006022777436225, 0.18456357982253255, 0.1669000798346295, 0.1482803686136344, 0.12935095083700357, 0.11070068079024514, 0.09283329821313276, 0.07614950044287017, 0.060938851450946276, 0.047380805975397705, 0.03555333280909725, 0.025447121841425106, 0.016983169507997393, 0.010031626246347373, 0.004430093886645415, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_I_wf3": {
            "samples": [0.0, 0.004430093886645415, 0.010031626246347373, 0.016983169507997393, 0.025447121841425106, 0.03555333280909725, 0.047380805975397705, 0.060938851450946276, 0.07614950044287017, 0.09283329821313276, 0.11070068079024514, 0.12935095083700357, 0.1482803686136344, 0.1669000798346295, 0.18456357982253255, 0.2006022777436225, 0.2143666264976031, 0.22526938738112967, 0.23282705464681067] + [0.23669538268420445] * 2 + [0.23282705464681067, 0.22526938738112967, 0.2143666264976031, 0.2006022777436225, 0.18456357982253255, 0.1669000798346295, 0.1482803686136344, 0.12935095083700357, 0.11070068079024514, 0.09283329821313276, 0.07614950044287017, 0.060938851450946276, 0.047380805975397705, 0.03555333280909725, 0.025447121841425106, 0.016983169507997393, 0.010031626246347373, 0.004430093886645415, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_I_wf4": {
            "samples": [0.0, 0.004430093886645415, 0.010031626246347373, 0.016983169507997393, 0.025447121841425106, 0.03555333280909725, 0.047380805975397705, 0.060938851450946276, 0.07614950044287017, 0.09283329821313276, 0.11070068079024514, 0.12935095083700357, 0.1482803686136344, 0.1669000798346295, 0.18456357982253255, 0.2006022777436225, 0.2143666264976031, 0.22526938738112967, 0.23282705464681067] + [0.23669538268420445] * 2 + [0.23282705464681067, 0.22526938738112967, 0.2143666264976031, 0.2006022777436225, 0.18456357982253255, 0.1669000798346295, 0.1482803686136344, 0.12935095083700357, 0.11070068079024514, 0.09283329821313276, 0.07614950044287017, 0.060938851450946276, 0.047380805975397705, 0.03555333280909725, 0.025447121841425106, 0.016983169507997393, 0.010031626246347373, 0.004430093886645415, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_I_wf5": {
            "samples": [0.0, 0.004430093886645415, 0.010031626246347373, 0.016983169507997393, 0.025447121841425106, 0.03555333280909725, 0.047380805975397705, 0.060938851450946276, 0.07614950044287017, 0.09283329821313276, 0.11070068079024514, 0.12935095083700357, 0.1482803686136344, 0.1669000798346295, 0.18456357982253255, 0.2006022777436225, 0.2143666264976031, 0.22526938738112967, 0.23282705464681067] + [0.23669538268420445] * 2 + [0.23282705464681067, 0.22526938738112967, 0.2143666264976031, 0.2006022777436225, 0.18456357982253255, 0.1669000798346295, 0.1482803686136344, 0.12935095083700357, 0.11070068079024514, 0.09283329821313276, 0.07614950044287017, 0.060938851450946276, 0.047380805975397705, 0.03555333280909725, 0.025447121841425106, 0.016983169507997393, 0.010031626246347373, 0.004430093886645415, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_I_wf6": {
            "samples": [0.0, 0.004430093886645415, 0.010031626246347373, 0.016983169507997393, 0.025447121841425106, 0.03555333280909725, 0.047380805975397705, 0.060938851450946276, 0.07614950044287017, 0.09283329821313276, 0.11070068079024514, 0.12935095083700357, 0.1482803686136344, 0.1669000798346295, 0.18456357982253255, 0.2006022777436225, 0.2143666264976031, 0.22526938738112967, 0.23282705464681067] + [0.23669538268420445] * 2 + [0.23282705464681067, 0.22526938738112967, 0.2143666264976031, 0.2006022777436225, 0.18456357982253255, 0.1669000798346295, 0.1482803686136344, 0.12935095083700357, 0.11070068079024514, 0.09283329821313276, 0.07614950044287017, 0.060938851450946276, 0.047380805975397705, 0.03555333280909725, 0.025447121841425106, 0.016983169507997393, 0.010031626246347373, 0.004430093886645415, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_Q_wf0": {
            "samples": [0.0] * 180,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_Q_wf1": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_Q_wf2": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_Q_wf3": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_Q_wf4": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_Q_wf5": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_Q_wf6": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_I_wf0": {
            "samples": [0.0, -0.00040416620465755834, -0.0008320318708446434, -0.0012845788945819647, -0.001762798661865914, -0.002267689544406204, -0.002800254194721963, -0.0033614966397724627, -0.0039524191733662575, -0.004574019048730957, -0.005227284973831431, -0.005913193413293454, -0.0066327047021169545, -0.007386758977742835, -0.008176271938463344, -0.009002130437630656, -0.009865187924613631, -0.01076625974497014, -0.011706118313832137, -0.012685488178032564, -0.013705040984026638, -0.01476539037016362, -0.015867086803336754, -0.01701061238146674, -0.01819637562464483, -0.01942470627906296, -0.020695850159076677, -0.02200996405386956, -0.02336711072620154, -0.02476725403161595, -0.026210254187238206, -0.02769586321991057, -0.029223720623861513, -0.030793349258393096, -0.032404151516175934, -0.03405540579265952, -0.03574626328682754, -0.037475745163046886, -0.039242740103069274, -0.04104600227634162, -0.04288414975566317, -0.04475566340389212, -0.04665888625585296, -0.04859202341783009, -0.05055314250505774, -0.05254017463543585, -0.054550915995324765, -0.05658302999070759, -0.058634049994269, -0.060701382696035804, -0.06278231206217397, -0.06487400390335323, -0.06697351105079447, -0.06907777913472397, -0.07118365295649506, -0.07328788344212264, -0.07538713516143358, -0.07747799439348926, -0.07955697771541118, -0.08162054108826197, -0.08366508941022711, -0.085686986504034, -0.0876825655023604, -0.08964813959194799, -0.09158001307427546, -0.09347449269798133, -0.09532789921578447, -0.09713657911645074, -0.09889691648041778, -0.10060534490603643, -0.10225835945203246, -0.10385252854075183, -0.1053845057660392, -0.1068510415492232, -0.1082489945866514, -0.10957534303253762, -0.1108271953615586, -0.112001800856664, -0.1130965596689426, -0.11410903239811193, -0.11503694914426066, -0.11587821798386094, -0.11663093282577114, -0.11729338060594716, -0.11786404778285947, -0.1183416260991481, -0.11872501757881927, -0.11901333873326818, -0.11920592395357711] + [-0.11930232807085857] * 2 + [-0.11920592395357711, -0.11901333873326818, -0.11872501757881927, -0.1183416260991481, -0.11786404778285947, -0.11729338060594716, -0.11663093282577114, -0.11587821798386094, -0.11503694914426066, -0.11410903239811193, -0.1130965596689426, -0.112001800856664, -0.1108271953615586, -0.10957534303253762, -0.1082489945866514, -0.1068510415492232, -0.1053845057660392, -0.10385252854075183, -0.10225835945203246, -0.10060534490603643, -0.09889691648041778, -0.09713657911645074, -0.09532789921578447, -0.09347449269798133, -0.09158001307427546, -0.08964813959194799, -0.0876825655023604, -0.085686986504034, -0.08366508941022711, -0.08162054108826197, -0.07955697771541118, -0.07747799439348926, -0.07538713516143358, -0.07328788344212264, -0.07118365295649506, -0.06907777913472397, -0.06697351105079447, -0.06487400390335323, -0.06278231206217397, -0.060701382696035804, -0.058634049994269, -0.05658302999070759, -0.054550915995324765, -0.05254017463543585, -0.05055314250505774, -0.04859202341783009, -0.04665888625585296, -0.04475566340389212, -0.04288414975566317, -0.04104600227634162, -0.039242740103069274, -0.037475745163046886, -0.03574626328682754, -0.03405540579265952, -0.032404151516175934, -0.030793349258393096, -0.029223720623861513, -0.02769586321991057, -0.026210254187238206, -0.02476725403161595, -0.02336711072620154, -0.02200996405386956, -0.020695850159076677, -0.01942470627906296, -0.01819637562464483, -0.01701061238146674, -0.015867086803336754, -0.01476539037016362, -0.013705040984026638, -0.012685488178032564, -0.011706118313832137, -0.01076625974497014, -0.009865187924613631, -0.009002130437630656, -0.008176271938463344, -0.007386758977742835, -0.0066327047021169545, -0.005913193413293454, -0.005227284973831431, -0.004574019048730957, -0.0039524191733662575, -0.0033614966397724627, -0.002800254194721963, -0.002267689544406204, -0.001762798661865914, -0.0012845788945819647, -0.0008320318708446434, -0.00040416620465755834, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_I_wf1": {
            "samples": [0.0, -0.0022150469433227073, -0.005015813123173687, -0.008491584753998697, -0.012723560920712553, -0.017776666404548624, -0.023690402987698853, -0.030469425725473138, -0.03807475022143508, -0.04641664910656638, -0.05535034039512257, -0.06467547541850178, -0.0741401843068172, -0.08345003991731476, -0.09228178991126627, -0.10030113887181125, -0.10718331324880155, -0.11263469369056484, -0.11641352732340533] + [-0.11834769134210223] * 2 + [-0.11641352732340533, -0.11263469369056484, -0.10718331324880155, -0.10030113887181125, -0.09228178991126627, -0.08345003991731476, -0.0741401843068172, -0.06467547541850178, -0.05535034039512257, -0.04641664910656638, -0.03807475022143508, -0.030469425725473138, -0.023690402987698853, -0.017776666404548624, -0.012723560920712553, -0.008491584753998697, -0.005015813123173687, -0.0022150469433227073, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_I_wf2": {
            "samples": [0.0, -0.0022150469433227073, -0.005015813123173687, -0.008491584753998697, -0.012723560920712553, -0.017776666404548624, -0.023690402987698853, -0.030469425725473138, -0.03807475022143508, -0.04641664910656638, -0.05535034039512257, -0.06467547541850178, -0.0741401843068172, -0.08345003991731476, -0.09228178991126627, -0.10030113887181125, -0.10718331324880155, -0.11263469369056484, -0.11641352732340533] + [-0.11834769134210223] * 2 + [-0.11641352732340533, -0.11263469369056484, -0.10718331324880155, -0.10030113887181125, -0.09228178991126627, -0.08345003991731476, -0.0741401843068172, -0.06467547541850178, -0.05535034039512257, -0.04641664910656638, -0.03807475022143508, -0.030469425725473138, -0.023690402987698853, -0.017776666404548624, -0.012723560920712553, -0.008491584753998697, -0.005015813123173687, -0.0022150469433227073, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_I_wf3": {
            "samples": [0.0, -0.0022150469433227073, -0.005015813123173687, -0.008491584753998697, -0.012723560920712553, -0.017776666404548624, -0.023690402987698853, -0.030469425725473138, -0.03807475022143508, -0.04641664910656638, -0.05535034039512257, -0.06467547541850178, -0.0741401843068172, -0.08345003991731476, -0.09228178991126627, -0.10030113887181125, -0.10718331324880155, -0.11263469369056484, -0.11641352732340533] + [-0.11834769134210223] * 2 + [-0.11641352732340533, -0.11263469369056484, -0.10718331324880155, -0.10030113887181125, -0.09228178991126627, -0.08345003991731476, -0.0741401843068172, -0.06467547541850178, -0.05535034039512257, -0.04641664910656638, -0.03807475022143508, -0.030469425725473138, -0.023690402987698853, -0.017776666404548624, -0.012723560920712553, -0.008491584753998697, -0.005015813123173687, -0.0022150469433227073, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_I_wf4": {
            "samples": [0.0, -0.0022150469433227073, -0.005015813123173687, -0.008491584753998697, -0.012723560920712553, -0.017776666404548624, -0.023690402987698853, -0.030469425725473138, -0.03807475022143508, -0.04641664910656638, -0.05535034039512257, -0.06467547541850178, -0.0741401843068172, -0.08345003991731476, -0.09228178991126627, -0.10030113887181125, -0.10718331324880155, -0.11263469369056484, -0.11641352732340533] + [-0.11834769134210223] * 2 + [-0.11641352732340533, -0.11263469369056484, -0.10718331324880155, -0.10030113887181125, -0.09228178991126627, -0.08345003991731476, -0.0741401843068172, -0.06467547541850178, -0.05535034039512257, -0.04641664910656638, -0.03807475022143508, -0.030469425725473138, -0.023690402987698853, -0.017776666404548624, -0.012723560920712553, -0.008491584753998697, -0.005015813123173687, -0.0022150469433227073, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_I_wf5": {
            "samples": [0.0, -0.0022150469433227073, -0.005015813123173687, -0.008491584753998697, -0.012723560920712553, -0.017776666404548624, -0.023690402987698853, -0.030469425725473138, -0.03807475022143508, -0.04641664910656638, -0.05535034039512257, -0.06467547541850178, -0.0741401843068172, -0.08345003991731476, -0.09228178991126627, -0.10030113887181125, -0.10718331324880155, -0.11263469369056484, -0.11641352732340533] + [-0.11834769134210223] * 2 + [-0.11641352732340533, -0.11263469369056484, -0.10718331324880155, -0.10030113887181125, -0.09228178991126627, -0.08345003991731476, -0.0741401843068172, -0.06467547541850178, -0.05535034039512257, -0.04641664910656638, -0.03807475022143508, -0.030469425725473138, -0.023690402987698853, -0.017776666404548624, -0.012723560920712553, -0.008491584753998697, -0.005015813123173687, -0.0022150469433227073, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_I_wf6": {
            "samples": [0.0, -0.0022150469433227073, -0.005015813123173687, -0.008491584753998697, -0.012723560920712553, -0.017776666404548624, -0.023690402987698853, -0.030469425725473138, -0.03807475022143508, -0.04641664910656638, -0.05535034039512257, -0.06467547541850178, -0.0741401843068172, -0.08345003991731476, -0.09228178991126627, -0.10030113887181125, -0.10718331324880155, -0.11263469369056484, -0.11641352732340533] + [-0.11834769134210223] * 2 + [-0.11641352732340533, -0.11263469369056484, -0.10718331324880155, -0.10030113887181125, -0.09228178991126627, -0.08345003991731476, -0.0741401843068172, -0.06467547541850178, -0.05535034039512257, -0.04641664910656638, -0.03807475022143508, -0.030469425725473138, -0.023690402987698853, -0.017776666404548624, -0.012723560920712553, -0.008491584753998697, -0.005015813123173687, -0.0022150469433227073, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_Q_wf0": {
            "samples": [0.0] * 180,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_Q_wf1": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_Q_wf2": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_Q_wf3": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_Q_wf4": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_Q_wf5": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_Q_wf6": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_I_wf0": {
            "samples": [-0.0] * 180,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_I_wf1": {
            "samples": [-0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_I_wf2": {
            "samples": [-0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_I_wf3": {
            "samples": [-0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_I_wf4": {
            "samples": [-0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_I_wf5": {
            "samples": [-0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_I_wf6": {
            "samples": [-0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_Q_wf0": {
            "samples": [0.0, 0.00040416620465755834, 0.0008320318708446434, 0.0012845788945819647, 0.001762798661865914, 0.002267689544406204, 0.002800254194721963, 0.0033614966397724627, 0.0039524191733662575, 0.004574019048730957, 0.005227284973831431, 0.005913193413293454, 0.0066327047021169545, 0.007386758977742835, 0.008176271938463344, 0.009002130437630656, 0.009865187924613631, 0.01076625974497014, 0.011706118313832137, 0.012685488178032564, 0.013705040984026638, 0.01476539037016362, 0.015867086803336754, 0.01701061238146674, 0.01819637562464483, 0.01942470627906296, 0.020695850159076677, 0.02200996405386956, 0.02336711072620154, 0.02476725403161595, 0.026210254187238206, 0.02769586321991057, 0.029223720623861513, 0.030793349258393096, 0.032404151516175934, 0.03405540579265952, 0.03574626328682754, 0.037475745163046886, 0.039242740103069274, 0.04104600227634162, 0.04288414975566317, 0.04475566340389212, 0.04665888625585296, 0.04859202341783009, 0.05055314250505774, 0.05254017463543585, 0.054550915995324765, 0.05658302999070759, 0.058634049994269, 0.060701382696035804, 0.06278231206217397, 0.06487400390335323, 0.06697351105079447, 0.06907777913472397, 0.07118365295649506, 0.07328788344212264, 0.07538713516143358, 0.07747799439348926, 0.07955697771541118, 0.08162054108826197, 0.08366508941022711, 0.085686986504034, 0.0876825655023604, 0.08964813959194799, 0.09158001307427546, 0.09347449269798133, 0.09532789921578447, 0.09713657911645074, 0.09889691648041778, 0.10060534490603643, 0.10225835945203246, 0.10385252854075183, 0.1053845057660392, 0.1068510415492232, 0.1082489945866514, 0.10957534303253762, 0.1108271953615586, 0.112001800856664, 0.1130965596689426, 0.11410903239811193, 0.11503694914426066, 0.11587821798386094, 0.11663093282577114, 0.11729338060594716, 0.11786404778285947, 0.1183416260991481, 0.11872501757881927, 0.11901333873326818, 0.11920592395357711] + [0.11930232807085857] * 2 + [0.11920592395357711, 0.11901333873326818, 0.11872501757881927, 0.1183416260991481, 0.11786404778285947, 0.11729338060594716, 0.11663093282577114, 0.11587821798386094, 0.11503694914426066, 0.11410903239811193, 0.1130965596689426, 0.112001800856664, 0.1108271953615586, 0.10957534303253762, 0.1082489945866514, 0.1068510415492232, 0.1053845057660392, 0.10385252854075183, 0.10225835945203246, 0.10060534490603643, 0.09889691648041778, 0.09713657911645074, 0.09532789921578447, 0.09347449269798133, 0.09158001307427546, 0.08964813959194799, 0.0876825655023604, 0.085686986504034, 0.08366508941022711, 0.08162054108826197, 0.07955697771541118, 0.07747799439348926, 0.07538713516143358, 0.07328788344212264, 0.07118365295649506, 0.06907777913472397, 0.06697351105079447, 0.06487400390335323, 0.06278231206217397, 0.060701382696035804, 0.058634049994269, 0.05658302999070759, 0.054550915995324765, 0.05254017463543585, 0.05055314250505774, 0.04859202341783009, 0.04665888625585296, 0.04475566340389212, 0.04288414975566317, 0.04104600227634162, 0.039242740103069274, 0.037475745163046886, 0.03574626328682754, 0.03405540579265952, 0.032404151516175934, 0.030793349258393096, 0.029223720623861513, 0.02769586321991057, 0.026210254187238206, 0.02476725403161595, 0.02336711072620154, 0.02200996405386956, 0.020695850159076677, 0.01942470627906296, 0.01819637562464483, 0.01701061238146674, 0.015867086803336754, 0.01476539037016362, 0.013705040984026638, 0.012685488178032564, 0.011706118313832137, 0.01076625974497014, 0.009865187924613631, 0.009002130437630656, 0.008176271938463344, 0.007386758977742835, 0.0066327047021169545, 0.005913193413293454, 0.005227284973831431, 0.004574019048730957, 0.0039524191733662575, 0.0033614966397724627, 0.002800254194721963, 0.002267689544406204, 0.001762798661865914, 0.0012845788945819647, 0.0008320318708446434, 0.00040416620465755834, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_Q_wf1": {
            "samples": [0.0, 0.0022150469433227073, 0.005015813123173687, 0.008491584753998697, 0.012723560920712553, 0.017776666404548624, 0.023690402987698853, 0.030469425725473138, 0.03807475022143508, 0.04641664910656638, 0.05535034039512257, 0.06467547541850178, 0.0741401843068172, 0.08345003991731476, 0.09228178991126627, 0.10030113887181125, 0.10718331324880155, 0.11263469369056484, 0.11641352732340533] + [0.11834769134210223] * 2 + [0.11641352732340533, 0.11263469369056484, 0.10718331324880155, 0.10030113887181125, 0.09228178991126627, 0.08345003991731476, 0.0741401843068172, 0.06467547541850178, 0.05535034039512257, 0.04641664910656638, 0.03807475022143508, 0.030469425725473138, 0.023690402987698853, 0.017776666404548624, 0.012723560920712553, 0.008491584753998697, 0.005015813123173687, 0.0022150469433227073, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_Q_wf2": {
            "samples": [0.0, 0.0022150469433227073, 0.005015813123173687, 0.008491584753998697, 0.012723560920712553, 0.017776666404548624, 0.023690402987698853, 0.030469425725473138, 0.03807475022143508, 0.04641664910656638, 0.05535034039512257, 0.06467547541850178, 0.0741401843068172, 0.08345003991731476, 0.09228178991126627, 0.10030113887181125, 0.10718331324880155, 0.11263469369056484, 0.11641352732340533] + [0.11834769134210223] * 2 + [0.11641352732340533, 0.11263469369056484, 0.10718331324880155, 0.10030113887181125, 0.09228178991126627, 0.08345003991731476, 0.0741401843068172, 0.06467547541850178, 0.05535034039512257, 0.04641664910656638, 0.03807475022143508, 0.030469425725473138, 0.023690402987698853, 0.017776666404548624, 0.012723560920712553, 0.008491584753998697, 0.005015813123173687, 0.0022150469433227073, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_Q_wf3": {
            "samples": [0.0, 0.0022150469433227073, 0.005015813123173687, 0.008491584753998697, 0.012723560920712553, 0.017776666404548624, 0.023690402987698853, 0.030469425725473138, 0.03807475022143508, 0.04641664910656638, 0.05535034039512257, 0.06467547541850178, 0.0741401843068172, 0.08345003991731476, 0.09228178991126627, 0.10030113887181125, 0.10718331324880155, 0.11263469369056484, 0.11641352732340533] + [0.11834769134210223] * 2 + [0.11641352732340533, 0.11263469369056484, 0.10718331324880155, 0.10030113887181125, 0.09228178991126627, 0.08345003991731476, 0.0741401843068172, 0.06467547541850178, 0.05535034039512257, 0.04641664910656638, 0.03807475022143508, 0.030469425725473138, 0.023690402987698853, 0.017776666404548624, 0.012723560920712553, 0.008491584753998697, 0.005015813123173687, 0.0022150469433227073, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_Q_wf4": {
            "samples": [0.0, 0.0022150469433227073, 0.005015813123173687, 0.008491584753998697, 0.012723560920712553, 0.017776666404548624, 0.023690402987698853, 0.030469425725473138, 0.03807475022143508, 0.04641664910656638, 0.05535034039512257, 0.06467547541850178, 0.0741401843068172, 0.08345003991731476, 0.09228178991126627, 0.10030113887181125, 0.10718331324880155, 0.11263469369056484, 0.11641352732340533] + [0.11834769134210223] * 2 + [0.11641352732340533, 0.11263469369056484, 0.10718331324880155, 0.10030113887181125, 0.09228178991126627, 0.08345003991731476, 0.0741401843068172, 0.06467547541850178, 0.05535034039512257, 0.04641664910656638, 0.03807475022143508, 0.030469425725473138, 0.023690402987698853, 0.017776666404548624, 0.012723560920712553, 0.008491584753998697, 0.005015813123173687, 0.0022150469433227073, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_Q_wf5": {
            "samples": [0.0, 0.0022150469433227073, 0.005015813123173687, 0.008491584753998697, 0.012723560920712553, 0.017776666404548624, 0.023690402987698853, 0.030469425725473138, 0.03807475022143508, 0.04641664910656638, 0.05535034039512257, 0.06467547541850178, 0.0741401843068172, 0.08345003991731476, 0.09228178991126627, 0.10030113887181125, 0.10718331324880155, 0.11263469369056484, 0.11641352732340533] + [0.11834769134210223] * 2 + [0.11641352732340533, 0.11263469369056484, 0.10718331324880155, 0.10030113887181125, 0.09228178991126627, 0.08345003991731476, 0.0741401843068172, 0.06467547541850178, 0.05535034039512257, 0.04641664910656638, 0.03807475022143508, 0.030469425725473138, 0.023690402987698853, 0.017776666404548624, 0.012723560920712553, 0.008491584753998697, 0.005015813123173687, 0.0022150469433227073, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_Q_wf6": {
            "samples": [0.0, 0.0022150469433227073, 0.005015813123173687, 0.008491584753998697, 0.012723560920712553, 0.017776666404548624, 0.023690402987698853, 0.030469425725473138, 0.03807475022143508, 0.04641664910656638, 0.05535034039512257, 0.06467547541850178, 0.0741401843068172, 0.08345003991731476, 0.09228178991126627, 0.10030113887181125, 0.10718331324880155, 0.11263469369056484, 0.11641352732340533] + [0.11834769134210223] * 2 + [0.11641352732340533, 0.11263469369056484, 0.10718331324880155, 0.10030113887181125, 0.09228178991126627, 0.08345003991731476, 0.0741401843068172, 0.06467547541850178, 0.05535034039512257, 0.04641664910656638, 0.03807475022143508, 0.030469425725473138, 0.023690402987698853, 0.017776666404548624, 0.012723560920712553, 0.008491584753998697, 0.005015813123173687, 0.0022150469433227073, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_I_wf0": {
            "samples": [-0.0] * 180,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_I_wf1": {
            "samples": [-0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_I_wf2": {
            "samples": [-0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_I_wf3": {
            "samples": [-0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_I_wf4": {
            "samples": [-0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_I_wf5": {
            "samples": [-0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_I_wf6": {
            "samples": [-0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_Q_wf0": {
            "samples": [0.0, 0.0008083324093151167, 0.0016640637416892867, 0.0025691577891639294, 0.003525597323731828, 0.004535379088812408, 0.005600508389443926, 0.006722993279544925, 0.007904838346732515, 0.009148038097461914, 0.010454569947662862, 0.011826386826586908, 0.013265409404233909, 0.01477351795548567, 0.016352543876926688, 0.018004260875261312, 0.019730375849227263, 0.02153251948994028, 0.023412236627664274, 0.02537097635606513, 0.027410081968053276, 0.02953078074032724, 0.03173417360667351, 0.03402122476293348, 0.03639275124928966, 0.03884941255812592, 0.041391700318153354, 0.04401992810773912, 0.04673422145240308, 0.0495345080632319, 0.05242050837447641, 0.05539172643982114, 0.058447441247723025, 0.06158669851678619, 0.06480830303235187, 0.06811081158531904, 0.07149252657365508, 0.07495149032609377, 0.07848548020613855, 0.08209200455268324, 0.08576829951132633, 0.08951132680778424, 0.09331777251170592, 0.09718404683566018, 0.10110628501011548, 0.1050803492708717, 0.10910183199064953, 0.11316605998141518, 0.117268099988538, 0.12140276539207161, 0.12556462412434793, 0.12974800780670645, 0.13394702210158893, 0.13815555826944795, 0.14236730591299013, 0.14657576688424528, 0.15077427032286717, 0.15495598878697853, 0.15911395543082235, 0.16324108217652394, 0.16733017882045423, 0.171373973008068, 0.1753651310047208, 0.17929627918389598, 0.18316002614855093, 0.18694898539596266, 0.19065579843156893, 0.19427315823290148, 0.19779383296083555, 0.20121068981207285, 0.20451671890406492, 0.20770505708150366, 0.2107690115320784, 0.2137020830984464, 0.2164979891733028, 0.21915068606507523, 0.2216543907231172, 0.224003601713328, 0.2261931193378852, 0.22821806479622386, 0.23007389828852132, 0.23175643596772189, 0.23326186565154228, 0.2345867612118943, 0.23572809556571894, 0.2366832521982962, 0.23745003515763854, 0.23802667746653636, 0.23841184790715422] + [0.23860465614171714] * 2 + [0.23841184790715422, 0.23802667746653636, 0.23745003515763854, 0.2366832521982962, 0.23572809556571894, 0.2345867612118943, 0.23326186565154228, 0.23175643596772189, 0.23007389828852132, 0.22821806479622386, 0.2261931193378852, 0.224003601713328, 0.2216543907231172, 0.21915068606507523, 0.2164979891733028, 0.2137020830984464, 0.2107690115320784, 0.20770505708150366, 0.20451671890406492, 0.20121068981207285, 0.19779383296083555, 0.19427315823290148, 0.19065579843156893, 0.18694898539596266, 0.18316002614855093, 0.17929627918389598, 0.1753651310047208, 0.171373973008068, 0.16733017882045423, 0.16324108217652394, 0.15911395543082235, 0.15495598878697853, 0.15077427032286717, 0.14657576688424528, 0.14236730591299013, 0.13815555826944795, 0.13394702210158893, 0.12974800780670645, 0.12556462412434793, 0.12140276539207161, 0.117268099988538, 0.11316605998141518, 0.10910183199064953, 0.1050803492708717, 0.10110628501011548, 0.09718404683566018, 0.09331777251170592, 0.08951132680778424, 0.08576829951132633, 0.08209200455268324, 0.07848548020613855, 0.07495149032609377, 0.07149252657365508, 0.06811081158531904, 0.06480830303235187, 0.06158669851678619, 0.058447441247723025, 0.05539172643982114, 0.05242050837447641, 0.0495345080632319, 0.04673422145240308, 0.04401992810773912, 0.041391700318153354, 0.03884941255812592, 0.03639275124928966, 0.03402122476293348, 0.03173417360667351, 0.02953078074032724, 0.027410081968053276, 0.02537097635606513, 0.023412236627664274, 0.02153251948994028, 0.019730375849227263, 0.018004260875261312, 0.016352543876926688, 0.01477351795548567, 0.013265409404233909, 0.011826386826586908, 0.010454569947662862, 0.009148038097461914, 0.007904838346732515, 0.006722993279544925, 0.005600508389443926, 0.004535379088812408, 0.003525597323731828, 0.0025691577891639294, 0.0016640637416892867, 0.0008083324093151167, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_Q_wf1": {
            "samples": [0.0, 0.004430093886645415, 0.010031626246347373, 0.016983169507997393, 0.025447121841425106, 0.03555333280909725, 0.047380805975397705, 0.060938851450946276, 0.07614950044287017, 0.09283329821313276, 0.11070068079024514, 0.12935095083700357, 0.1482803686136344, 0.1669000798346295, 0.18456357982253255, 0.2006022777436225, 0.2143666264976031, 0.22526938738112967, 0.23282705464681067] + [0.23669538268420445] * 2 + [0.23282705464681067, 0.22526938738112967, 0.2143666264976031, 0.2006022777436225, 0.18456357982253255, 0.1669000798346295, 0.1482803686136344, 0.12935095083700357, 0.11070068079024514, 0.09283329821313276, 0.07614950044287017, 0.060938851450946276, 0.047380805975397705, 0.03555333280909725, 0.025447121841425106, 0.016983169507997393, 0.010031626246347373, 0.004430093886645415, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_Q_wf2": {
            "samples": [0.0, 0.004430093886645415, 0.010031626246347373, 0.016983169507997393, 0.025447121841425106, 0.03555333280909725, 0.047380805975397705, 0.060938851450946276, 0.07614950044287017, 0.09283329821313276, 0.11070068079024514, 0.12935095083700357, 0.1482803686136344, 0.1669000798346295, 0.18456357982253255, 0.2006022777436225, 0.2143666264976031, 0.22526938738112967, 0.23282705464681067] + [0.23669538268420445] * 2 + [0.23282705464681067, 0.22526938738112967, 0.2143666264976031, 0.2006022777436225, 0.18456357982253255, 0.1669000798346295, 0.1482803686136344, 0.12935095083700357, 0.11070068079024514, 0.09283329821313276, 0.07614950044287017, 0.060938851450946276, 0.047380805975397705, 0.03555333280909725, 0.025447121841425106, 0.016983169507997393, 0.010031626246347373, 0.004430093886645415, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_Q_wf3": {
            "samples": [0.0, 0.004430093886645415, 0.010031626246347373, 0.016983169507997393, 0.025447121841425106, 0.03555333280909725, 0.047380805975397705, 0.060938851450946276, 0.07614950044287017, 0.09283329821313276, 0.11070068079024514, 0.12935095083700357, 0.1482803686136344, 0.1669000798346295, 0.18456357982253255, 0.2006022777436225, 0.2143666264976031, 0.22526938738112967, 0.23282705464681067] + [0.23669538268420445] * 2 + [0.23282705464681067, 0.22526938738112967, 0.2143666264976031, 0.2006022777436225, 0.18456357982253255, 0.1669000798346295, 0.1482803686136344, 0.12935095083700357, 0.11070068079024514, 0.09283329821313276, 0.07614950044287017, 0.060938851450946276, 0.047380805975397705, 0.03555333280909725, 0.025447121841425106, 0.016983169507997393, 0.010031626246347373, 0.004430093886645415, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_Q_wf4": {
            "samples": [0.0, 0.004430093886645415, 0.010031626246347373, 0.016983169507997393, 0.025447121841425106, 0.03555333280909725, 0.047380805975397705, 0.060938851450946276, 0.07614950044287017, 0.09283329821313276, 0.11070068079024514, 0.12935095083700357, 0.1482803686136344, 0.1669000798346295, 0.18456357982253255, 0.2006022777436225, 0.2143666264976031, 0.22526938738112967, 0.23282705464681067] + [0.23669538268420445] * 2 + [0.23282705464681067, 0.22526938738112967, 0.2143666264976031, 0.2006022777436225, 0.18456357982253255, 0.1669000798346295, 0.1482803686136344, 0.12935095083700357, 0.11070068079024514, 0.09283329821313276, 0.07614950044287017, 0.060938851450946276, 0.047380805975397705, 0.03555333280909725, 0.025447121841425106, 0.016983169507997393, 0.010031626246347373, 0.004430093886645415, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_Q_wf5": {
            "samples": [0.0, 0.004430093886645415, 0.010031626246347373, 0.016983169507997393, 0.025447121841425106, 0.03555333280909725, 0.047380805975397705, 0.060938851450946276, 0.07614950044287017, 0.09283329821313276, 0.11070068079024514, 0.12935095083700357, 0.1482803686136344, 0.1669000798346295, 0.18456357982253255, 0.2006022777436225, 0.2143666264976031, 0.22526938738112967, 0.23282705464681067] + [0.23669538268420445] * 2 + [0.23282705464681067, 0.22526938738112967, 0.2143666264976031, 0.2006022777436225, 0.18456357982253255, 0.1669000798346295, 0.1482803686136344, 0.12935095083700357, 0.11070068079024514, 0.09283329821313276, 0.07614950044287017, 0.060938851450946276, 0.047380805975397705, 0.03555333280909725, 0.025447121841425106, 0.016983169507997393, 0.010031626246347373, 0.004430093886645415, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_Q_wf6": {
            "samples": [0.0, 0.004430093886645415, 0.010031626246347373, 0.016983169507997393, 0.025447121841425106, 0.03555333280909725, 0.047380805975397705, 0.060938851450946276, 0.07614950044287017, 0.09283329821313276, 0.11070068079024514, 0.12935095083700357, 0.1482803686136344, 0.1669000798346295, 0.18456357982253255, 0.2006022777436225, 0.2143666264976031, 0.22526938738112967, 0.23282705464681067] + [0.23669538268420445] * 2 + [0.23282705464681067, 0.22526938738112967, 0.2143666264976031, 0.2006022777436225, 0.18456357982253255, 0.1669000798346295, 0.1482803686136344, 0.12935095083700357, 0.11070068079024514, 0.09283329821313276, 0.07614950044287017, 0.060938851450946276, 0.047380805975397705, 0.03555333280909725, 0.025447121841425106, 0.016983169507997393, 0.010031626246347373, 0.004430093886645415, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_I_wf0": {
            "samples": [-0.0] * 180,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_I_wf1": {
            "samples": [-0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_I_wf2": {
            "samples": [-0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_I_wf3": {
            "samples": [-0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_I_wf4": {
            "samples": [-0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_I_wf5": {
            "samples": [-0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_I_wf6": {
            "samples": [-0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_Q_wf0": {
            "samples": [0.0, -0.00040416620465755834, -0.0008320318708446434, -0.0012845788945819647, -0.001762798661865914, -0.002267689544406204, -0.002800254194721963, -0.0033614966397724627, -0.0039524191733662575, -0.004574019048730957, -0.005227284973831431, -0.005913193413293454, -0.0066327047021169545, -0.007386758977742835, -0.008176271938463344, -0.009002130437630656, -0.009865187924613631, -0.01076625974497014, -0.011706118313832137, -0.012685488178032564, -0.013705040984026638, -0.01476539037016362, -0.015867086803336754, -0.01701061238146674, -0.01819637562464483, -0.01942470627906296, -0.020695850159076677, -0.02200996405386956, -0.02336711072620154, -0.02476725403161595, -0.026210254187238206, -0.02769586321991057, -0.029223720623861513, -0.030793349258393096, -0.032404151516175934, -0.03405540579265952, -0.03574626328682754, -0.037475745163046886, -0.039242740103069274, -0.04104600227634162, -0.04288414975566317, -0.04475566340389212, -0.04665888625585296, -0.04859202341783009, -0.05055314250505774, -0.05254017463543585, -0.054550915995324765, -0.05658302999070759, -0.058634049994269, -0.060701382696035804, -0.06278231206217397, -0.06487400390335323, -0.06697351105079447, -0.06907777913472397, -0.07118365295649506, -0.07328788344212264, -0.07538713516143358, -0.07747799439348926, -0.07955697771541118, -0.08162054108826197, -0.08366508941022711, -0.085686986504034, -0.0876825655023604, -0.08964813959194799, -0.09158001307427546, -0.09347449269798133, -0.09532789921578447, -0.09713657911645074, -0.09889691648041778, -0.10060534490603643, -0.10225835945203246, -0.10385252854075183, -0.1053845057660392, -0.1068510415492232, -0.1082489945866514, -0.10957534303253762, -0.1108271953615586, -0.112001800856664, -0.1130965596689426, -0.11410903239811193, -0.11503694914426066, -0.11587821798386094, -0.11663093282577114, -0.11729338060594716, -0.11786404778285947, -0.1183416260991481, -0.11872501757881927, -0.11901333873326818, -0.11920592395357711] + [-0.11930232807085857] * 2 + [-0.11920592395357711, -0.11901333873326818, -0.11872501757881927, -0.1183416260991481, -0.11786404778285947, -0.11729338060594716, -0.11663093282577114, -0.11587821798386094, -0.11503694914426066, -0.11410903239811193, -0.1130965596689426, -0.112001800856664, -0.1108271953615586, -0.10957534303253762, -0.1082489945866514, -0.1068510415492232, -0.1053845057660392, -0.10385252854075183, -0.10225835945203246, -0.10060534490603643, -0.09889691648041778, -0.09713657911645074, -0.09532789921578447, -0.09347449269798133, -0.09158001307427546, -0.08964813959194799, -0.0876825655023604, -0.085686986504034, -0.08366508941022711, -0.08162054108826197, -0.07955697771541118, -0.07747799439348926, -0.07538713516143358, -0.07328788344212264, -0.07118365295649506, -0.06907777913472397, -0.06697351105079447, -0.06487400390335323, -0.06278231206217397, -0.060701382696035804, -0.058634049994269, -0.05658302999070759, -0.054550915995324765, -0.05254017463543585, -0.05055314250505774, -0.04859202341783009, -0.04665888625585296, -0.04475566340389212, -0.04288414975566317, -0.04104600227634162, -0.039242740103069274, -0.037475745163046886, -0.03574626328682754, -0.03405540579265952, -0.032404151516175934, -0.030793349258393096, -0.029223720623861513, -0.02769586321991057, -0.026210254187238206, -0.02476725403161595, -0.02336711072620154, -0.02200996405386956, -0.020695850159076677, -0.01942470627906296, -0.01819637562464483, -0.01701061238146674, -0.015867086803336754, -0.01476539037016362, -0.013705040984026638, -0.012685488178032564, -0.011706118313832137, -0.01076625974497014, -0.009865187924613631, -0.009002130437630656, -0.008176271938463344, -0.007386758977742835, -0.0066327047021169545, -0.005913193413293454, -0.005227284973831431, -0.004574019048730957, -0.0039524191733662575, -0.0033614966397724627, -0.002800254194721963, -0.002267689544406204, -0.001762798661865914, -0.0012845788945819647, -0.0008320318708446434, -0.00040416620465755834, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_Q_wf1": {
            "samples": [0.0, -0.0022150469433227073, -0.005015813123173687, -0.008491584753998697, -0.012723560920712553, -0.017776666404548624, -0.023690402987698853, -0.030469425725473138, -0.03807475022143508, -0.04641664910656638, -0.05535034039512257, -0.06467547541850178, -0.0741401843068172, -0.08345003991731476, -0.09228178991126627, -0.10030113887181125, -0.10718331324880155, -0.11263469369056484, -0.11641352732340533] + [-0.11834769134210223] * 2 + [-0.11641352732340533, -0.11263469369056484, -0.10718331324880155, -0.10030113887181125, -0.09228178991126627, -0.08345003991731476, -0.0741401843068172, -0.06467547541850178, -0.05535034039512257, -0.04641664910656638, -0.03807475022143508, -0.030469425725473138, -0.023690402987698853, -0.017776666404548624, -0.012723560920712553, -0.008491584753998697, -0.005015813123173687, -0.0022150469433227073, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_Q_wf2": {
            "samples": [0.0, -0.0022150469433227073, -0.005015813123173687, -0.008491584753998697, -0.012723560920712553, -0.017776666404548624, -0.023690402987698853, -0.030469425725473138, -0.03807475022143508, -0.04641664910656638, -0.05535034039512257, -0.06467547541850178, -0.0741401843068172, -0.08345003991731476, -0.09228178991126627, -0.10030113887181125, -0.10718331324880155, -0.11263469369056484, -0.11641352732340533] + [-0.11834769134210223] * 2 + [-0.11641352732340533, -0.11263469369056484, -0.10718331324880155, -0.10030113887181125, -0.09228178991126627, -0.08345003991731476, -0.0741401843068172, -0.06467547541850178, -0.05535034039512257, -0.04641664910656638, -0.03807475022143508, -0.030469425725473138, -0.023690402987698853, -0.017776666404548624, -0.012723560920712553, -0.008491584753998697, -0.005015813123173687, -0.0022150469433227073, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_Q_wf3": {
            "samples": [0.0, -0.0022150469433227073, -0.005015813123173687, -0.008491584753998697, -0.012723560920712553, -0.017776666404548624, -0.023690402987698853, -0.030469425725473138, -0.03807475022143508, -0.04641664910656638, -0.05535034039512257, -0.06467547541850178, -0.0741401843068172, -0.08345003991731476, -0.09228178991126627, -0.10030113887181125, -0.10718331324880155, -0.11263469369056484, -0.11641352732340533] + [-0.11834769134210223] * 2 + [-0.11641352732340533, -0.11263469369056484, -0.10718331324880155, -0.10030113887181125, -0.09228178991126627, -0.08345003991731476, -0.0741401843068172, -0.06467547541850178, -0.05535034039512257, -0.04641664910656638, -0.03807475022143508, -0.030469425725473138, -0.023690402987698853, -0.017776666404548624, -0.012723560920712553, -0.008491584753998697, -0.005015813123173687, -0.0022150469433227073, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_Q_wf4": {
            "samples": [0.0, -0.0022150469433227073, -0.005015813123173687, -0.008491584753998697, -0.012723560920712553, -0.017776666404548624, -0.023690402987698853, -0.030469425725473138, -0.03807475022143508, -0.04641664910656638, -0.05535034039512257, -0.06467547541850178, -0.0741401843068172, -0.08345003991731476, -0.09228178991126627, -0.10030113887181125, -0.10718331324880155, -0.11263469369056484, -0.11641352732340533] + [-0.11834769134210223] * 2 + [-0.11641352732340533, -0.11263469369056484, -0.10718331324880155, -0.10030113887181125, -0.09228178991126627, -0.08345003991731476, -0.0741401843068172, -0.06467547541850178, -0.05535034039512257, -0.04641664910656638, -0.03807475022143508, -0.030469425725473138, -0.023690402987698853, -0.017776666404548624, -0.012723560920712553, -0.008491584753998697, -0.005015813123173687, -0.0022150469433227073, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_Q_wf5": {
            "samples": [0.0, -0.0022150469433227073, -0.005015813123173687, -0.008491584753998697, -0.012723560920712553, -0.017776666404548624, -0.023690402987698853, -0.030469425725473138, -0.03807475022143508, -0.04641664910656638, -0.05535034039512257, -0.06467547541850178, -0.0741401843068172, -0.08345003991731476, -0.09228178991126627, -0.10030113887181125, -0.10718331324880155, -0.11263469369056484, -0.11641352732340533] + [-0.11834769134210223] * 2 + [-0.11641352732340533, -0.11263469369056484, -0.10718331324880155, -0.10030113887181125, -0.09228178991126627, -0.08345003991731476, -0.0741401843068172, -0.06467547541850178, -0.05535034039512257, -0.04641664910656638, -0.03807475022143508, -0.030469425725473138, -0.023690402987698853, -0.017776666404548624, -0.012723560920712553, -0.008491584753998697, -0.005015813123173687, -0.0022150469433227073, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_Q_wf6": {
            "samples": [0.0, -0.0022150469433227073, -0.005015813123173687, -0.008491584753998697, -0.012723560920712553, -0.017776666404548624, -0.023690402987698853, -0.030469425725473138, -0.03807475022143508, -0.04641664910656638, -0.05535034039512257, -0.06467547541850178, -0.0741401843068172, -0.08345003991731476, -0.09228178991126627, -0.10030113887181125, -0.10718331324880155, -0.11263469369056484, -0.11641352732340533] + [-0.11834769134210223] * 2 + [-0.11641352732340533, -0.11263469369056484, -0.10718331324880155, -0.10030113887181125, -0.09228178991126627, -0.08345003991731476, -0.0741401843068172, -0.06467547541850178, -0.05535034039512257, -0.04641664910656638, -0.03807475022143508, -0.030469425725473138, -0.023690402987698853, -0.017776666404548624, -0.012723560920712553, -0.008491584753998697, -0.005015813123173687, -0.0022150469433227073, 0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights0": {
            "cosine": [(1.0, 500)],
            "sine": [(0.0, 500)],
        },
        "cosine_weights1": {
            "cosine": [(1.0, 500)],
            "sine": [(0.0, 500)],
        },
        "cosine_weights2": {
            "cosine": [(1.0, 500)],
            "sine": [(0.0, 500)],
        },
        "cosine_weights3": {
            "cosine": [(1.0, 500)],
            "sine": [(0.0, 500)],
        },
        "cosine_weights4": {
            "cosine": [(1.0, 500)],
            "sine": [(0.0, 500)],
        },
        "cosine_weights5": {
            "cosine": [(1.0, 500)],
            "sine": [(0.0, 500)],
        },
        "cosine_weights6": {
            "cosine": [(1.0, 500)],
            "sine": [(0.0, 500)],
        },
        "sine_weights0": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
        "sine_weights1": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
        "sine_weights2": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
        "sine_weights3": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
        "sine_weights4": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
        "sine_weights5": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
        "sine_weights6": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
        "minus_sine_weights0": {
            "cosine": [(0.0, 500)],
            "sine": [(-1.0, 500)],
        },
        "minus_sine_weights1": {
            "cosine": [(0.0, 500)],
            "sine": [(-1.0, 500)],
        },
        "minus_sine_weights2": {
            "cosine": [(0.0, 500)],
            "sine": [(-1.0, 500)],
        },
        "minus_sine_weights3": {
            "cosine": [(0.0, 500)],
            "sine": [(-1.0, 500)],
        },
        "minus_sine_weights4": {
            "cosine": [(0.0, 500)],
            "sine": [(-1.0, 500)],
        },
        "minus_sine_weights5": {
            "cosine": [(0.0, 500)],
            "sine": [(-1.0, 500)],
        },
        "minus_sine_weights6": {
            "cosine": [(0.0, 500)],
            "sine": [(-1.0, 500)],
        },
        "rotated_cosine_weights0": {
            "cosine": [(1.0, 500)],
            "sine": [(0.0, 500)],
        },
        "rotated_cosine_weights1": {
            "cosine": [(1.0, 500)],
            "sine": [(0.0, 500)],
        },
        "rotated_cosine_weights2": {
            "cosine": [(1.0, 500)],
            "sine": [(0.0, 500)],
        },
        "rotated_cosine_weights3": {
            "cosine": [(1.0, 500)],
            "sine": [(0.0, 500)],
        },
        "rotated_cosine_weights4": {
            "cosine": [(1.0, 500)],
            "sine": [(0.0, 500)],
        },
        "rotated_cosine_weights5": {
            "cosine": [(1.0, 500)],
            "sine": [(0.0, 500)],
        },
        "rotated_cosine_weights6": {
            "cosine": [(1.0, 500)],
            "sine": [(0.0, 500)],
        },
        "rotated_sine_weights0": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
        "rotated_sine_weights1": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
        "rotated_sine_weights2": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
        "rotated_sine_weights3": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
        "rotated_sine_weights4": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
        "rotated_sine_weights5": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
        "rotated_sine_weights6": {
            "cosine": [(0.0, 500)],
            "sine": [(1.0, 500)],
        },
        "rotated_minus_sine_weights0": {
            "cosine": [(0.0, 500)],
            "sine": [(-1.0, 500)],
        },
        "rotated_minus_sine_weights1": {
            "cosine": [(0.0, 500)],
            "sine": [(-1.0, 500)],
        },
        "rotated_minus_sine_weights2": {
            "cosine": [(0.0, 500)],
            "sine": [(-1.0, 500)],
        },
        "rotated_minus_sine_weights3": {
            "cosine": [(0.0, 500)],
            "sine": [(-1.0, 500)],
        },
        "rotated_minus_sine_weights4": {
            "cosine": [(0.0, 500)],
            "sine": [(-1.0, 500)],
        },
        "rotated_minus_sine_weights5": {
            "cosine": [(0.0, 500)],
            "sine": [(-1.0, 500)],
        },
        "rotated_minus_sine_weights6": {
            "cosine": [(0.0, 500)],
            "sine": [(-1.0, 500)],
        },
        "opt_cosine_weights0": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "opt_cosine_weights1": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "opt_cosine_weights2": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "opt_cosine_weights3": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "opt_cosine_weights4": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "opt_cosine_weights5": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "opt_cosine_weights6": {
            "cosine": [(1.0, 2000)],
            "sine": [(0.0, 2000)],
        },
        "opt_sine_weights0": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "opt_sine_weights1": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "opt_sine_weights2": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "opt_sine_weights3": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "opt_sine_weights4": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "opt_sine_weights5": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "opt_sine_weights6": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "opt_minus_sine_weights0": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
        "opt_minus_sine_weights1": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
        "opt_minus_sine_weights2": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
        "opt_minus_sine_weights3": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
        "opt_minus_sine_weights4": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
        "opt_minus_sine_weights5": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
        "opt_minus_sine_weights6": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
    },
    "mixers": {
        "octave_octave1_2": [
            {'intermediate_frequency': 184220000.0, 'lo_frequency': 6100000000.0, 'correction': [0.9843983836472034, 0.056579768657684326, 0.05430668592453003, 1.0256017595529556]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 5467000000.0, 'correction': [1.008311040699482, 0.13667917624115944, 0.1319584883749485, 1.0443823970854282]},
            {'intermediate_frequency': 186000000.0, 'lo_frequency': 6100000000.0, 'correction': [0.9844945967197418, 0.057187315076589584, 0.054889824241399765, 1.025702003389597]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6382000000.0, 'correction': [0.9780302569270134, 0.01799078658223152, 0.017183978110551834, 1.0239499509334564]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 5342000000.0, 'correction': [1.0420268923044205, 0.1728515625, 0.1728515625, 1.0420268923044205]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6189000000.0, 'correction': [0.9796239621937275, 0.021456871181726456, 0.020554695278406143, 1.0226210989058018]},
            {'intermediate_frequency': 179000000.0, 'lo_frequency': 6110000000.0, 'correction': [0.9841276444494724, 0.05483501777052879, 0.052632030099630356, 1.025319691747427]},
            {'intermediate_frequency': 169000000.0, 'lo_frequency': 6110000000.0, 'correction': [0.9832491092383862, 0.052119217813014984, 0.04997655004262924, 1.025404404848814]},
            {'intermediate_frequency': 172215300.0, 'lo_frequency': 6110000000.0, 'correction': [0.9834322556853294, 0.05336608737707138, 0.0511721596121788, 1.0255954004824162]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6007000000.0, 'correction': [0.9805241003632545, 0.04597645252943039, 0.04391460865736008, 1.0265608876943588]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 5882000000.0, 'correction': [0.9815450236201286, 0.08165643364191055, 0.0771622434258461, 1.0387135222554207]},
            {'intermediate_frequency': 40864584.0, 'lo_frequency': 6382000000.0, 'correction': [0.9785669781267643, -0.02498408779501915, -0.023869480937719345, 1.0242620408535004]},
            {'intermediate_frequency': 10139023.0, 'lo_frequency': 6352000000.0, 'correction': [0.9787439368665218, -0.012496553361415863, -0.01195981353521347, 1.022668570280075]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6391860977.0, 'correction': [0.9792955070734024, -0.026965998113155365, -0.025794409215450287, 1.0237753726541996]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6441860977.0, 'correction': [0.9828890860080719, -0.052893687039613724, -0.05066971853375435, 1.026029534637928]},
            {'intermediate_frequency': 110924023.0, 'lo_frequency': 6452785000.0, 'correction': [0.9841265715658665, -0.057854827493429184, -0.055476363748311996, 1.0263194851577282]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 5668000000.0, 'correction': [1.0, 0.0, 0.0, 1.0]},
        ],
        "octave_octave1_1": [
            {'intermediate_frequency': 35322000.0, 'lo_frequency': 7100000000.0, 'correction': [0.9942276552319527, -0.09682570397853851, -0.09318546950817108, 1.033066563308239]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6012000000.0, 'correction': [0.9902525208890438, 0.030617237091064453, 0.029937267303466797, 1.0127442739903927]},
            {'intermediate_frequency': 34000000.0, 'lo_frequency': 7100000000.0, 'correction': [0.9941620528697968, -0.09657679498195648, -0.09294591844081879, 1.0329983979463577]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6062000000.0, 'correction': [0.9920627623796463, 0.03204335272312164, 0.03143896162509918, 1.0111344456672668]},
            {'intermediate_frequency': 57620000.0, 'lo_frequency': 6062000000.0, 'correction': [0.9917549826204777, 0.031311605125665665, 0.030706021934747696, 1.0113143399357796]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 7206000000.0, 'correction': [0.9985018000006676, -0.10661306977272034, -0.10292454063892365, 1.0342853255569935]},
            {'intermediate_frequency': 56000000.0, 'lo_frequency': 6062000000.0, 'correction': [0.9918001294136047, 0.031804703176021576, 0.031189583241939545, 1.0113603807985783]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 5968000000.0, 'correction': [0.9894565418362617, 0.045296911150217056, 0.04407525435090065, 1.0168818235397339]},
            {'intermediate_frequency': 59260000.0, 'lo_frequency': 6062000000.0, 'correction': [0.9918229691684246, 0.03205125033855438, 0.03143136203289032, 1.0113836713135242]},
            {'intermediate_frequency': 53900000.0, 'lo_frequency': 5968000000.0, 'correction': [0.989488635212183, 0.04554443806409836, 0.04431610554456711, 1.0169148072600365]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 7080000000.0, 'correction': [0.9925949797034264, -0.09571203589439392, -0.09186682105064392, 1.0341414362192154]},
            {'intermediate_frequency': 54940000.0, 'lo_frequency': 7080000000.0, 'correction': [0.9928321950137615, -0.09568821638822556, -0.09188877791166306, 1.0338840521872044]},
            {'intermediate_frequency': 55100000.0, 'lo_frequency': 7080000000.0, 'correction': [0.9927028380334377, -0.09518983960151672, -0.09141018986701965, 1.0337493494153023]},
            {'intermediate_frequency': 56500000.0, 'lo_frequency': 7206000000.0, 'correction': [0.9980056993663311, -0.1069246344268322, -0.10310576483607292, 1.0349702052772045]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6949000000.0, 'correction': [0.9934355728328228, -0.0903998464345932, -0.08714990317821503, 1.030482191592455]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6825000000.0, 'correction': [0.9955396018922329, -0.0938892513513565, -0.09073497354984283, 1.0301481820642948]},
            {'intermediate_frequency': 56420000.0, 'lo_frequency': 7206000000.0, 'correction': [0.9981252439320087, -0.10691135376691818, -0.10311811417341232, 1.034841664135456]},
            {'intermediate_frequency': 54200000.0, 'lo_frequency': 7206000000.0, 'correction': [0.9981368966400623, -0.10652517899870872, -0.10277071222662926, 1.0346012897789478]},
            {'intermediate_frequency': 56520000.0, 'lo_frequency': 7206000000.0, 'correction': [0.9982746280729771, -0.10593293979763985, -0.10226170346140862, 1.0341130904853344]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6167000000.0, 'correction': [1.0, 0.0, 0.0, 1.0]},
        ],
    },
}


