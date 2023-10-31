
# Single QUA script generated at 2023-10-31 09:22:53.641415
# QUA library version: 1.1.3

from qm.qua import *

with program() as prog:
    v1 = declare(fixed, )
    v2 = declare(fixed, )
    v3 = declare(int, )
    v4 = declare(int, )
    v5 = declare(fixed, )
    v6 = declare(int, )
    with for_(v3,0,(v3<1000.0),(v3+1)):
        with for_(v5,1.6,(v5<1.9980000000000004),(v5+0.0040000000000000036)):
            with for_(v6,16,(v6<=200),(v6+4)):
                play("pi", "q0")
                align()
                with if_((v6==16)):
                    play("baked_Op_16"*amp(v5), "flux0")
                with elif_((v6==20)):
                    play("baked_Op_20"*amp(v5), "flux0")
                with elif_((v6==24)):
                    play("baked_Op_24"*amp(v5), "flux0")
                with elif_((v6==28)):
                    play("baked_Op_28"*amp(v5), "flux0")
                with elif_((v6==32)):
                    play("baked_Op_32"*amp(v5), "flux0")
                with elif_((v6==36)):
                    play("baked_Op_36"*amp(v5), "flux0")
                with elif_((v6==40)):
                    play("baked_Op_40"*amp(v5), "flux0")
                with elif_((v6==44)):
                    play("baked_Op_44"*amp(v5), "flux0")
                with elif_((v6==48)):
                    play("baked_Op_48"*amp(v5), "flux0")
                with elif_((v6==52)):
                    play("baked_Op_52"*amp(v5), "flux0")
                with elif_((v6==56)):
                    play("baked_Op_56"*amp(v5), "flux0")
                with elif_((v6==60)):
                    play("baked_Op_60"*amp(v5), "flux0")
                with elif_((v6==64)):
                    play("baked_Op_64"*amp(v5), "flux0")
                with elif_((v6==68)):
                    play("baked_Op_68"*amp(v5), "flux0")
                with elif_((v6==72)):
                    play("baked_Op_72"*amp(v5), "flux0")
                with elif_((v6==76)):
                    play("baked_Op_76"*amp(v5), "flux0")
                with elif_((v6==80)):
                    play("baked_Op_80"*amp(v5), "flux0")
                with elif_((v6==84)):
                    play("baked_Op_84"*amp(v5), "flux0")
                with elif_((v6==88)):
                    play("baked_Op_88"*amp(v5), "flux0")
                with elif_((v6==92)):
                    play("baked_Op_92"*amp(v5), "flux0")
                with elif_((v6==96)):
                    play("baked_Op_96"*amp(v5), "flux0")
                with elif_((v6==100)):
                    play("baked_Op_100"*amp(v5), "flux0")
                with elif_((v6==104)):
                    play("baked_Op_104"*amp(v5), "flux0")
                with elif_((v6==108)):
                    play("baked_Op_108"*amp(v5), "flux0")
                with elif_((v6==112)):
                    play("baked_Op_112"*amp(v5), "flux0")
                with elif_((v6==116)):
                    play("baked_Op_116"*amp(v5), "flux0")
                with elif_((v6==120)):
                    play("baked_Op_120"*amp(v5), "flux0")
                with elif_((v6==124)):
                    play("baked_Op_124"*amp(v5), "flux0")
                with elif_((v6==128)):
                    play("baked_Op_128"*amp(v5), "flux0")
                with elif_((v6==132)):
                    play("baked_Op_132"*amp(v5), "flux0")
                with elif_((v6==136)):
                    play("baked_Op_136"*amp(v5), "flux0")
                with elif_((v6==140)):
                    play("baked_Op_140"*amp(v5), "flux0")
                with elif_((v6==144)):
                    play("baked_Op_144"*amp(v5), "flux0")
                with elif_((v6==148)):
                    play("baked_Op_148"*amp(v5), "flux0")
                with elif_((v6==152)):
                    play("baked_Op_152"*amp(v5), "flux0")
                with elif_((v6==156)):
                    play("baked_Op_156"*amp(v5), "flux0")
                with elif_((v6==160)):
                    play("baked_Op_160"*amp(v5), "flux0")
                with elif_((v6==164)):
                    play("baked_Op_164"*amp(v5), "flux0")
                with elif_((v6==168)):
                    play("baked_Op_168"*amp(v5), "flux0")
                with elif_((v6==172)):
                    play("baked_Op_172"*amp(v5), "flux0")
                with elif_((v6==176)):
                    play("baked_Op_176"*amp(v5), "flux0")
                with elif_((v6==180)):
                    play("baked_Op_180"*amp(v5), "flux0")
                with elif_((v6==184)):
                    play("baked_Op_184"*amp(v5), "flux0")
                with elif_((v6==188)):
                    play("baked_Op_188"*amp(v5), "flux0")
                with elif_((v6==192)):
                    play("baked_Op_192"*amp(v5), "flux0")
                with elif_((v6==196)):
                    play("baked_Op_196"*amp(v5), "flux0")
                with elif_((v6==200)):
                    play("baked_Op_200"*amp(v5), "flux0")
                align()
                measure("readout"*amp(1), "r0", None, dual_demod.full("cos", "out1", "sin", "out2", v1), dual_demod.full("minus_sin", "out1", "cos", "out2", v2))
                align()
                wait(50, )
                with if_((v6==16)):
                    play("baked_Op_16"*amp((0-v5)), "flux0")
                with elif_((v6==20)):
                    play("baked_Op_20"*amp((0-v5)), "flux0")
                with elif_((v6==24)):
                    play("baked_Op_24"*amp((0-v5)), "flux0")
                with elif_((v6==28)):
                    play("baked_Op_28"*amp((0-v5)), "flux0")
                with elif_((v6==32)):
                    play("baked_Op_32"*amp((0-v5)), "flux0")
                with elif_((v6==36)):
                    play("baked_Op_36"*amp((0-v5)), "flux0")
                with elif_((v6==40)):
                    play("baked_Op_40"*amp((0-v5)), "flux0")
                with elif_((v6==44)):
                    play("baked_Op_44"*amp((0-v5)), "flux0")
                with elif_((v6==48)):
                    play("baked_Op_48"*amp((0-v5)), "flux0")
                with elif_((v6==52)):
                    play("baked_Op_52"*amp((0-v5)), "flux0")
                with elif_((v6==56)):
                    play("baked_Op_56"*amp((0-v5)), "flux0")
                with elif_((v6==60)):
                    play("baked_Op_60"*amp((0-v5)), "flux0")
                with elif_((v6==64)):
                    play("baked_Op_64"*amp((0-v5)), "flux0")
                with elif_((v6==68)):
                    play("baked_Op_68"*amp((0-v5)), "flux0")
                with elif_((v6==72)):
                    play("baked_Op_72"*amp((0-v5)), "flux0")
                with elif_((v6==76)):
                    play("baked_Op_76"*amp((0-v5)), "flux0")
                with elif_((v6==80)):
                    play("baked_Op_80"*amp((0-v5)), "flux0")
                with elif_((v6==84)):
                    play("baked_Op_84"*amp((0-v5)), "flux0")
                with elif_((v6==88)):
                    play("baked_Op_88"*amp((0-v5)), "flux0")
                with elif_((v6==92)):
                    play("baked_Op_92"*amp((0-v5)), "flux0")
                with elif_((v6==96)):
                    play("baked_Op_96"*amp((0-v5)), "flux0")
                with elif_((v6==100)):
                    play("baked_Op_100"*amp((0-v5)), "flux0")
                with elif_((v6==104)):
                    play("baked_Op_104"*amp((0-v5)), "flux0")
                with elif_((v6==108)):
                    play("baked_Op_108"*amp((0-v5)), "flux0")
                with elif_((v6==112)):
                    play("baked_Op_112"*amp((0-v5)), "flux0")
                with elif_((v6==116)):
                    play("baked_Op_116"*amp((0-v5)), "flux0")
                with elif_((v6==120)):
                    play("baked_Op_120"*amp((0-v5)), "flux0")
                with elif_((v6==124)):
                    play("baked_Op_124"*amp((0-v5)), "flux0")
                with elif_((v6==128)):
                    play("baked_Op_128"*amp((0-v5)), "flux0")
                with elif_((v6==132)):
                    play("baked_Op_132"*amp((0-v5)), "flux0")
                with elif_((v6==136)):
                    play("baked_Op_136"*amp((0-v5)), "flux0")
                with elif_((v6==140)):
                    play("baked_Op_140"*amp((0-v5)), "flux0")
                with elif_((v6==144)):
                    play("baked_Op_144"*amp((0-v5)), "flux0")
                with elif_((v6==148)):
                    play("baked_Op_148"*amp((0-v5)), "flux0")
                with elif_((v6==152)):
                    play("baked_Op_152"*amp((0-v5)), "flux0")
                with elif_((v6==156)):
                    play("baked_Op_156"*amp((0-v5)), "flux0")
                with elif_((v6==160)):
                    play("baked_Op_160"*amp((0-v5)), "flux0")
                with elif_((v6==164)):
                    play("baked_Op_164"*amp((0-v5)), "flux0")
                with elif_((v6==168)):
                    play("baked_Op_168"*amp((0-v5)), "flux0")
                with elif_((v6==172)):
                    play("baked_Op_172"*amp((0-v5)), "flux0")
                with elif_((v6==176)):
                    play("baked_Op_176"*amp((0-v5)), "flux0")
                with elif_((v6==180)):
                    play("baked_Op_180"*amp((0-v5)), "flux0")
                with elif_((v6==184)):
                    play("baked_Op_184"*amp((0-v5)), "flux0")
                with elif_((v6==188)):
                    play("baked_Op_188"*amp((0-v5)), "flux0")
                with elif_((v6==192)):
                    play("baked_Op_192"*amp((0-v5)), "flux0")
                with elif_((v6==196)):
                    play("baked_Op_196"*amp((0-v5)), "flux0")
                with elif_((v6==200)):
                    play("baked_Op_200"*amp((0-v5)), "flux0")
                r1 = declare_stream()
                save(v1, r1)
                r2 = declare_stream()
                save(v2, r2)
                wait(10000, "r0")
        r3 = declare_stream()
        save(v3, r3)
    with stream_processing():
        r3.save("iteration")
        r1.buffer(100).buffer(47).average().save("I")
        r2.buffer(100).buffer(47).average().save("Q")


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                "1": {
                    "offset": -0.001953125,
                    "delay": 0,
                },
                "2": {
                    "offset": -0.044921875,
                    "delay": 0,
                },
                "3": {
                    "offset": 0.001953125,
                },
                "4": {
                    "offset": -0.00390625,
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
                    "offset": 0.011262000000000003,
                    "gain_db": 0,
                },
                "2": {
                    "offset": 0.016203,
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
                "lo_frequency": 7313013478.0,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": -50000000.0,
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
                "lo_frequency": 7180000000.0,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": -50000000.0,
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
                "lo_frequency": 7049000000.0,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": -50000000.0,
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
                "lo_frequency": 6925000000.0,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": -50000000.0,
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
                "lo_frequency": 6267000000.0,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": -50000000.0,
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
                "lo_frequency": 6162000000.0,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": -50000000.0,
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
                "lo_frequency": 6068000000.0,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": -50000000.0,
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
                "lo_frequency": 7313013478.0,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": -50000000.0,
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
                "lo_frequency": 7180000000.0,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": -50000000.0,
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
                "lo_frequency": 7049000000.0,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": -50000000.0,
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
                "lo_frequency": 6925000000.0,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": -50000000.0,
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
                "lo_frequency": 6267000000.0,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": -50000000.0,
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
                "lo_frequency": 6162000000.0,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": -50000000.0,
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
                "lo_frequency": 6068000000.0,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": -50000000.0,
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
                "lo_frequency": 6221505924.0,
                "mixer": "octave_octave1_2",
            },
            "intermediate_frequency": 200000000.0,
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
                "lo_frequency": 6389000000.0,
                "mixer": "octave_octave1_2",
            },
            "intermediate_frequency": -100000000.0,
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
                "lo_frequency": 6207000000.0,
                "mixer": "octave_octave1_2",
            },
            "intermediate_frequency": -100000000.0,
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
                "lo_frequency": 6082000000.0,
                "mixer": "octave_octave1_2",
            },
            "intermediate_frequency": -100000000.0,
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
                "lo_frequency": 5868000000.0,
                "mixer": "octave_octave1_2",
            },
            "intermediate_frequency": -100000000.0,
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
                "lo_frequency": 5667000000.0,
                "mixer": "octave_octave1_2",
            },
            "intermediate_frequency": -100000000.0,
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
                "lo_frequency": 5542000000.0,
                "mixer": "octave_octave1_2",
            },
            "intermediate_frequency": -100000000.0,
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
                "baked_Op_0": "flux0_baked_pulse_0",
                "baked_Op_1": "flux0_baked_pulse_1",
                "baked_Op_2": "flux0_baked_pulse_2",
                "baked_Op_3": "flux0_baked_pulse_3",
                "baked_Op_4": "flux0_baked_pulse_4",
                "baked_Op_5": "flux0_baked_pulse_5",
                "baked_Op_6": "flux0_baked_pulse_6",
                "baked_Op_7": "flux0_baked_pulse_7",
                "baked_Op_8": "flux0_baked_pulse_8",
                "baked_Op_9": "flux0_baked_pulse_9",
                "baked_Op_10": "flux0_baked_pulse_10",
                "baked_Op_11": "flux0_baked_pulse_11",
                "baked_Op_12": "flux0_baked_pulse_12",
                "baked_Op_13": "flux0_baked_pulse_13",
                "baked_Op_14": "flux0_baked_pulse_14",
                "baked_Op_15": "flux0_baked_pulse_15",
                "baked_Op_16": "flux0_baked_pulse_16",
                "baked_Op_17": "flux0_baked_pulse_17",
                "baked_Op_18": "flux0_baked_pulse_18",
                "baked_Op_19": "flux0_baked_pulse_19",
                "baked_Op_20": "flux0_baked_pulse_20",
                "baked_Op_21": "flux0_baked_pulse_21",
                "baked_Op_22": "flux0_baked_pulse_22",
                "baked_Op_23": "flux0_baked_pulse_23",
                "baked_Op_24": "flux0_baked_pulse_24",
                "baked_Op_25": "flux0_baked_pulse_25",
                "baked_Op_26": "flux0_baked_pulse_26",
                "baked_Op_27": "flux0_baked_pulse_27",
                "baked_Op_28": "flux0_baked_pulse_28",
                "baked_Op_29": "flux0_baked_pulse_29",
                "baked_Op_30": "flux0_baked_pulse_30",
                "baked_Op_31": "flux0_baked_pulse_31",
                "baked_Op_32": "flux0_baked_pulse_32",
                "baked_Op_33": "flux0_baked_pulse_33",
                "baked_Op_34": "flux0_baked_pulse_34",
                "baked_Op_35": "flux0_baked_pulse_35",
                "baked_Op_36": "flux0_baked_pulse_36",
                "baked_Op_37": "flux0_baked_pulse_37",
                "baked_Op_38": "flux0_baked_pulse_38",
                "baked_Op_39": "flux0_baked_pulse_39",
                "baked_Op_40": "flux0_baked_pulse_40",
                "baked_Op_41": "flux0_baked_pulse_41",
                "baked_Op_42": "flux0_baked_pulse_42",
                "baked_Op_43": "flux0_baked_pulse_43",
                "baked_Op_44": "flux0_baked_pulse_44",
                "baked_Op_45": "flux0_baked_pulse_45",
                "baked_Op_46": "flux0_baked_pulse_46",
                "baked_Op_47": "flux0_baked_pulse_47",
                "baked_Op_48": "flux0_baked_pulse_48",
                "baked_Op_49": "flux0_baked_pulse_49",
                "baked_Op_50": "flux0_baked_pulse_50",
                "baked_Op_51": "flux0_baked_pulse_51",
                "baked_Op_52": "flux0_baked_pulse_52",
                "baked_Op_53": "flux0_baked_pulse_53",
                "baked_Op_54": "flux0_baked_pulse_54",
                "baked_Op_55": "flux0_baked_pulse_55",
                "baked_Op_56": "flux0_baked_pulse_56",
                "baked_Op_57": "flux0_baked_pulse_57",
                "baked_Op_58": "flux0_baked_pulse_58",
                "baked_Op_59": "flux0_baked_pulse_59",
                "baked_Op_60": "flux0_baked_pulse_60",
                "baked_Op_61": "flux0_baked_pulse_61",
                "baked_Op_62": "flux0_baked_pulse_62",
                "baked_Op_63": "flux0_baked_pulse_63",
                "baked_Op_64": "flux0_baked_pulse_64",
                "baked_Op_65": "flux0_baked_pulse_65",
                "baked_Op_66": "flux0_baked_pulse_66",
                "baked_Op_67": "flux0_baked_pulse_67",
                "baked_Op_68": "flux0_baked_pulse_68",
                "baked_Op_69": "flux0_baked_pulse_69",
                "baked_Op_70": "flux0_baked_pulse_70",
                "baked_Op_71": "flux0_baked_pulse_71",
                "baked_Op_72": "flux0_baked_pulse_72",
                "baked_Op_73": "flux0_baked_pulse_73",
                "baked_Op_74": "flux0_baked_pulse_74",
                "baked_Op_75": "flux0_baked_pulse_75",
                "baked_Op_76": "flux0_baked_pulse_76",
                "baked_Op_77": "flux0_baked_pulse_77",
                "baked_Op_78": "flux0_baked_pulse_78",
                "baked_Op_79": "flux0_baked_pulse_79",
                "baked_Op_80": "flux0_baked_pulse_80",
                "baked_Op_81": "flux0_baked_pulse_81",
                "baked_Op_82": "flux0_baked_pulse_82",
                "baked_Op_83": "flux0_baked_pulse_83",
                "baked_Op_84": "flux0_baked_pulse_84",
                "baked_Op_85": "flux0_baked_pulse_85",
                "baked_Op_86": "flux0_baked_pulse_86",
                "baked_Op_87": "flux0_baked_pulse_87",
                "baked_Op_88": "flux0_baked_pulse_88",
                "baked_Op_89": "flux0_baked_pulse_89",
                "baked_Op_90": "flux0_baked_pulse_90",
                "baked_Op_91": "flux0_baked_pulse_91",
                "baked_Op_92": "flux0_baked_pulse_92",
                "baked_Op_93": "flux0_baked_pulse_93",
                "baked_Op_94": "flux0_baked_pulse_94",
                "baked_Op_95": "flux0_baked_pulse_95",
                "baked_Op_96": "flux0_baked_pulse_96",
                "baked_Op_97": "flux0_baked_pulse_97",
                "baked_Op_98": "flux0_baked_pulse_98",
                "baked_Op_99": "flux0_baked_pulse_99",
                "baked_Op_100": "flux0_baked_pulse_100",
                "baked_Op_101": "flux0_baked_pulse_101",
                "baked_Op_102": "flux0_baked_pulse_102",
                "baked_Op_103": "flux0_baked_pulse_103",
                "baked_Op_104": "flux0_baked_pulse_104",
                "baked_Op_105": "flux0_baked_pulse_105",
                "baked_Op_106": "flux0_baked_pulse_106",
                "baked_Op_107": "flux0_baked_pulse_107",
                "baked_Op_108": "flux0_baked_pulse_108",
                "baked_Op_109": "flux0_baked_pulse_109",
                "baked_Op_110": "flux0_baked_pulse_110",
                "baked_Op_111": "flux0_baked_pulse_111",
                "baked_Op_112": "flux0_baked_pulse_112",
                "baked_Op_113": "flux0_baked_pulse_113",
                "baked_Op_114": "flux0_baked_pulse_114",
                "baked_Op_115": "flux0_baked_pulse_115",
                "baked_Op_116": "flux0_baked_pulse_116",
                "baked_Op_117": "flux0_baked_pulse_117",
                "baked_Op_118": "flux0_baked_pulse_118",
                "baked_Op_119": "flux0_baked_pulse_119",
                "baked_Op_120": "flux0_baked_pulse_120",
                "baked_Op_121": "flux0_baked_pulse_121",
                "baked_Op_122": "flux0_baked_pulse_122",
                "baked_Op_123": "flux0_baked_pulse_123",
                "baked_Op_124": "flux0_baked_pulse_124",
                "baked_Op_125": "flux0_baked_pulse_125",
                "baked_Op_126": "flux0_baked_pulse_126",
                "baked_Op_127": "flux0_baked_pulse_127",
                "baked_Op_128": "flux0_baked_pulse_128",
                "baked_Op_129": "flux0_baked_pulse_129",
                "baked_Op_130": "flux0_baked_pulse_130",
                "baked_Op_131": "flux0_baked_pulse_131",
                "baked_Op_132": "flux0_baked_pulse_132",
                "baked_Op_133": "flux0_baked_pulse_133",
                "baked_Op_134": "flux0_baked_pulse_134",
                "baked_Op_135": "flux0_baked_pulse_135",
                "baked_Op_136": "flux0_baked_pulse_136",
                "baked_Op_137": "flux0_baked_pulse_137",
                "baked_Op_138": "flux0_baked_pulse_138",
                "baked_Op_139": "flux0_baked_pulse_139",
                "baked_Op_140": "flux0_baked_pulse_140",
                "baked_Op_141": "flux0_baked_pulse_141",
                "baked_Op_142": "flux0_baked_pulse_142",
                "baked_Op_143": "flux0_baked_pulse_143",
                "baked_Op_144": "flux0_baked_pulse_144",
                "baked_Op_145": "flux0_baked_pulse_145",
                "baked_Op_146": "flux0_baked_pulse_146",
                "baked_Op_147": "flux0_baked_pulse_147",
                "baked_Op_148": "flux0_baked_pulse_148",
                "baked_Op_149": "flux0_baked_pulse_149",
                "baked_Op_150": "flux0_baked_pulse_150",
                "baked_Op_151": "flux0_baked_pulse_151",
                "baked_Op_152": "flux0_baked_pulse_152",
                "baked_Op_153": "flux0_baked_pulse_153",
                "baked_Op_154": "flux0_baked_pulse_154",
                "baked_Op_155": "flux0_baked_pulse_155",
                "baked_Op_156": "flux0_baked_pulse_156",
                "baked_Op_157": "flux0_baked_pulse_157",
                "baked_Op_158": "flux0_baked_pulse_158",
                "baked_Op_159": "flux0_baked_pulse_159",
                "baked_Op_160": "flux0_baked_pulse_160",
                "baked_Op_161": "flux0_baked_pulse_161",
                "baked_Op_162": "flux0_baked_pulse_162",
                "baked_Op_163": "flux0_baked_pulse_163",
                "baked_Op_164": "flux0_baked_pulse_164",
                "baked_Op_165": "flux0_baked_pulse_165",
                "baked_Op_166": "flux0_baked_pulse_166",
                "baked_Op_167": "flux0_baked_pulse_167",
                "baked_Op_168": "flux0_baked_pulse_168",
                "baked_Op_169": "flux0_baked_pulse_169",
                "baked_Op_170": "flux0_baked_pulse_170",
                "baked_Op_171": "flux0_baked_pulse_171",
                "baked_Op_172": "flux0_baked_pulse_172",
                "baked_Op_173": "flux0_baked_pulse_173",
                "baked_Op_174": "flux0_baked_pulse_174",
                "baked_Op_175": "flux0_baked_pulse_175",
                "baked_Op_176": "flux0_baked_pulse_176",
                "baked_Op_177": "flux0_baked_pulse_177",
                "baked_Op_178": "flux0_baked_pulse_178",
                "baked_Op_179": "flux0_baked_pulse_179",
                "baked_Op_180": "flux0_baked_pulse_180",
                "baked_Op_181": "flux0_baked_pulse_181",
                "baked_Op_182": "flux0_baked_pulse_182",
                "baked_Op_183": "flux0_baked_pulse_183",
                "baked_Op_184": "flux0_baked_pulse_184",
                "baked_Op_185": "flux0_baked_pulse_185",
                "baked_Op_186": "flux0_baked_pulse_186",
                "baked_Op_187": "flux0_baked_pulse_187",
                "baked_Op_188": "flux0_baked_pulse_188",
                "baked_Op_189": "flux0_baked_pulse_189",
                "baked_Op_190": "flux0_baked_pulse_190",
                "baked_Op_191": "flux0_baked_pulse_191",
                "baked_Op_192": "flux0_baked_pulse_192",
                "baked_Op_193": "flux0_baked_pulse_193",
                "baked_Op_194": "flux0_baked_pulse_194",
                "baked_Op_195": "flux0_baked_pulse_195",
                "baked_Op_196": "flux0_baked_pulse_196",
                "baked_Op_197": "flux0_baked_pulse_197",
                "baked_Op_198": "flux0_baked_pulse_198",
                "baked_Op_199": "flux0_baked_pulse_199",
                "baked_Op_200": "flux0_baked_pulse_200",
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
            "length": 100,
            "waveforms": {
                "I": "pi_wf0",
                "Q": "zero_wf",
            },
        },
        "pi_pulse1": {
            "operation": "control",
            "length": 20,
            "waveforms": {
                "I": "pi_wf1",
                "Q": "zero_wf",
            },
        },
        "pi_pulse2": {
            "operation": "control",
            "length": 20,
            "waveforms": {
                "I": "pi_wf2",
                "Q": "zero_wf",
            },
        },
        "pi_pulse3": {
            "operation": "control",
            "length": 20,
            "waveforms": {
                "I": "pi_wf3",
                "Q": "zero_wf",
            },
        },
        "pi_pulse4": {
            "operation": "control",
            "length": 20,
            "waveforms": {
                "I": "pi_wf4",
                "Q": "zero_wf",
            },
        },
        "pi_pulse5": {
            "operation": "control",
            "length": 20,
            "waveforms": {
                "I": "pi_wf5",
                "Q": "zero_wf",
            },
        },
        "pi_pulse6": {
            "operation": "control",
            "length": 20,
            "waveforms": {
                "I": "pi_wf6",
                "Q": "zero_wf",
            },
        },
        "pi_over_two_pulse0": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "pi_over_two_wf0",
                "Q": "zero_wf",
            },
        },
        "pi_over_two_pulse1": {
            "operation": "control",
            "length": 20,
            "waveforms": {
                "I": "pi_over_two_wf1",
                "Q": "zero_wf",
            },
        },
        "pi_over_two_pulse2": {
            "operation": "control",
            "length": 20,
            "waveforms": {
                "I": "pi_over_two_wf2",
                "Q": "zero_wf",
            },
        },
        "pi_over_two_pulse3": {
            "operation": "control",
            "length": 20,
            "waveforms": {
                "I": "pi_over_two_wf3",
                "Q": "zero_wf",
            },
        },
        "pi_over_two_pulse4": {
            "operation": "control",
            "length": 20,
            "waveforms": {
                "I": "pi_over_two_wf4",
                "Q": "zero_wf",
            },
        },
        "pi_over_two_pulse5": {
            "operation": "control",
            "length": 20,
            "waveforms": {
                "I": "pi_over_two_wf5",
                "Q": "zero_wf",
            },
        },
        "pi_over_two_pulse6": {
            "operation": "control",
            "length": 20,
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
        "flux0_baked_pulse_0": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_0",
            },
        },
        "flux0_baked_pulse_1": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_1",
            },
        },
        "flux0_baked_pulse_2": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_2",
            },
        },
        "flux0_baked_pulse_3": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_3",
            },
        },
        "flux0_baked_pulse_4": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_4",
            },
        },
        "flux0_baked_pulse_5": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_5",
            },
        },
        "flux0_baked_pulse_6": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_6",
            },
        },
        "flux0_baked_pulse_7": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_7",
            },
        },
        "flux0_baked_pulse_8": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_8",
            },
        },
        "flux0_baked_pulse_9": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_9",
            },
        },
        "flux0_baked_pulse_10": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_10",
            },
        },
        "flux0_baked_pulse_11": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_11",
            },
        },
        "flux0_baked_pulse_12": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_12",
            },
        },
        "flux0_baked_pulse_13": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_13",
            },
        },
        "flux0_baked_pulse_14": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_14",
            },
        },
        "flux0_baked_pulse_15": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_15",
            },
        },
        "flux0_baked_pulse_16": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_16",
            },
        },
        "flux0_baked_pulse_17": {
            "operation": "control",
            "length": 20,
            "waveforms": {
                "single": "flux0_baked_wf_17",
            },
        },
        "flux0_baked_pulse_18": {
            "operation": "control",
            "length": 20,
            "waveforms": {
                "single": "flux0_baked_wf_18",
            },
        },
        "flux0_baked_pulse_19": {
            "operation": "control",
            "length": 20,
            "waveforms": {
                "single": "flux0_baked_wf_19",
            },
        },
        "flux0_baked_pulse_20": {
            "operation": "control",
            "length": 20,
            "waveforms": {
                "single": "flux0_baked_wf_20",
            },
        },
        "flux0_baked_pulse_21": {
            "operation": "control",
            "length": 24,
            "waveforms": {
                "single": "flux0_baked_wf_21",
            },
        },
        "flux0_baked_pulse_22": {
            "operation": "control",
            "length": 24,
            "waveforms": {
                "single": "flux0_baked_wf_22",
            },
        },
        "flux0_baked_pulse_23": {
            "operation": "control",
            "length": 24,
            "waveforms": {
                "single": "flux0_baked_wf_23",
            },
        },
        "flux0_baked_pulse_24": {
            "operation": "control",
            "length": 24,
            "waveforms": {
                "single": "flux0_baked_wf_24",
            },
        },
        "flux0_baked_pulse_25": {
            "operation": "control",
            "length": 28,
            "waveforms": {
                "single": "flux0_baked_wf_25",
            },
        },
        "flux0_baked_pulse_26": {
            "operation": "control",
            "length": 28,
            "waveforms": {
                "single": "flux0_baked_wf_26",
            },
        },
        "flux0_baked_pulse_27": {
            "operation": "control",
            "length": 28,
            "waveforms": {
                "single": "flux0_baked_wf_27",
            },
        },
        "flux0_baked_pulse_28": {
            "operation": "control",
            "length": 28,
            "waveforms": {
                "single": "flux0_baked_wf_28",
            },
        },
        "flux0_baked_pulse_29": {
            "operation": "control",
            "length": 32,
            "waveforms": {
                "single": "flux0_baked_wf_29",
            },
        },
        "flux0_baked_pulse_30": {
            "operation": "control",
            "length": 32,
            "waveforms": {
                "single": "flux0_baked_wf_30",
            },
        },
        "flux0_baked_pulse_31": {
            "operation": "control",
            "length": 32,
            "waveforms": {
                "single": "flux0_baked_wf_31",
            },
        },
        "flux0_baked_pulse_32": {
            "operation": "control",
            "length": 32,
            "waveforms": {
                "single": "flux0_baked_wf_32",
            },
        },
        "flux0_baked_pulse_33": {
            "operation": "control",
            "length": 36,
            "waveforms": {
                "single": "flux0_baked_wf_33",
            },
        },
        "flux0_baked_pulse_34": {
            "operation": "control",
            "length": 36,
            "waveforms": {
                "single": "flux0_baked_wf_34",
            },
        },
        "flux0_baked_pulse_35": {
            "operation": "control",
            "length": 36,
            "waveforms": {
                "single": "flux0_baked_wf_35",
            },
        },
        "flux0_baked_pulse_36": {
            "operation": "control",
            "length": 36,
            "waveforms": {
                "single": "flux0_baked_wf_36",
            },
        },
        "flux0_baked_pulse_37": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "single": "flux0_baked_wf_37",
            },
        },
        "flux0_baked_pulse_38": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "single": "flux0_baked_wf_38",
            },
        },
        "flux0_baked_pulse_39": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "single": "flux0_baked_wf_39",
            },
        },
        "flux0_baked_pulse_40": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "single": "flux0_baked_wf_40",
            },
        },
        "flux0_baked_pulse_41": {
            "operation": "control",
            "length": 44,
            "waveforms": {
                "single": "flux0_baked_wf_41",
            },
        },
        "flux0_baked_pulse_42": {
            "operation": "control",
            "length": 44,
            "waveforms": {
                "single": "flux0_baked_wf_42",
            },
        },
        "flux0_baked_pulse_43": {
            "operation": "control",
            "length": 44,
            "waveforms": {
                "single": "flux0_baked_wf_43",
            },
        },
        "flux0_baked_pulse_44": {
            "operation": "control",
            "length": 44,
            "waveforms": {
                "single": "flux0_baked_wf_44",
            },
        },
        "flux0_baked_pulse_45": {
            "operation": "control",
            "length": 48,
            "waveforms": {
                "single": "flux0_baked_wf_45",
            },
        },
        "flux0_baked_pulse_46": {
            "operation": "control",
            "length": 48,
            "waveforms": {
                "single": "flux0_baked_wf_46",
            },
        },
        "flux0_baked_pulse_47": {
            "operation": "control",
            "length": 48,
            "waveforms": {
                "single": "flux0_baked_wf_47",
            },
        },
        "flux0_baked_pulse_48": {
            "operation": "control",
            "length": 48,
            "waveforms": {
                "single": "flux0_baked_wf_48",
            },
        },
        "flux0_baked_pulse_49": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "single": "flux0_baked_wf_49",
            },
        },
        "flux0_baked_pulse_50": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "single": "flux0_baked_wf_50",
            },
        },
        "flux0_baked_pulse_51": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "single": "flux0_baked_wf_51",
            },
        },
        "flux0_baked_pulse_52": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "single": "flux0_baked_wf_52",
            },
        },
        "flux0_baked_pulse_53": {
            "operation": "control",
            "length": 56,
            "waveforms": {
                "single": "flux0_baked_wf_53",
            },
        },
        "flux0_baked_pulse_54": {
            "operation": "control",
            "length": 56,
            "waveforms": {
                "single": "flux0_baked_wf_54",
            },
        },
        "flux0_baked_pulse_55": {
            "operation": "control",
            "length": 56,
            "waveforms": {
                "single": "flux0_baked_wf_55",
            },
        },
        "flux0_baked_pulse_56": {
            "operation": "control",
            "length": 56,
            "waveforms": {
                "single": "flux0_baked_wf_56",
            },
        },
        "flux0_baked_pulse_57": {
            "operation": "control",
            "length": 60,
            "waveforms": {
                "single": "flux0_baked_wf_57",
            },
        },
        "flux0_baked_pulse_58": {
            "operation": "control",
            "length": 60,
            "waveforms": {
                "single": "flux0_baked_wf_58",
            },
        },
        "flux0_baked_pulse_59": {
            "operation": "control",
            "length": 60,
            "waveforms": {
                "single": "flux0_baked_wf_59",
            },
        },
        "flux0_baked_pulse_60": {
            "operation": "control",
            "length": 60,
            "waveforms": {
                "single": "flux0_baked_wf_60",
            },
        },
        "flux0_baked_pulse_61": {
            "operation": "control",
            "length": 64,
            "waveforms": {
                "single": "flux0_baked_wf_61",
            },
        },
        "flux0_baked_pulse_62": {
            "operation": "control",
            "length": 64,
            "waveforms": {
                "single": "flux0_baked_wf_62",
            },
        },
        "flux0_baked_pulse_63": {
            "operation": "control",
            "length": 64,
            "waveforms": {
                "single": "flux0_baked_wf_63",
            },
        },
        "flux0_baked_pulse_64": {
            "operation": "control",
            "length": 64,
            "waveforms": {
                "single": "flux0_baked_wf_64",
            },
        },
        "flux0_baked_pulse_65": {
            "operation": "control",
            "length": 68,
            "waveforms": {
                "single": "flux0_baked_wf_65",
            },
        },
        "flux0_baked_pulse_66": {
            "operation": "control",
            "length": 68,
            "waveforms": {
                "single": "flux0_baked_wf_66",
            },
        },
        "flux0_baked_pulse_67": {
            "operation": "control",
            "length": 68,
            "waveforms": {
                "single": "flux0_baked_wf_67",
            },
        },
        "flux0_baked_pulse_68": {
            "operation": "control",
            "length": 68,
            "waveforms": {
                "single": "flux0_baked_wf_68",
            },
        },
        "flux0_baked_pulse_69": {
            "operation": "control",
            "length": 72,
            "waveforms": {
                "single": "flux0_baked_wf_69",
            },
        },
        "flux0_baked_pulse_70": {
            "operation": "control",
            "length": 72,
            "waveforms": {
                "single": "flux0_baked_wf_70",
            },
        },
        "flux0_baked_pulse_71": {
            "operation": "control",
            "length": 72,
            "waveforms": {
                "single": "flux0_baked_wf_71",
            },
        },
        "flux0_baked_pulse_72": {
            "operation": "control",
            "length": 72,
            "waveforms": {
                "single": "flux0_baked_wf_72",
            },
        },
        "flux0_baked_pulse_73": {
            "operation": "control",
            "length": 76,
            "waveforms": {
                "single": "flux0_baked_wf_73",
            },
        },
        "flux0_baked_pulse_74": {
            "operation": "control",
            "length": 76,
            "waveforms": {
                "single": "flux0_baked_wf_74",
            },
        },
        "flux0_baked_pulse_75": {
            "operation": "control",
            "length": 76,
            "waveforms": {
                "single": "flux0_baked_wf_75",
            },
        },
        "flux0_baked_pulse_76": {
            "operation": "control",
            "length": 76,
            "waveforms": {
                "single": "flux0_baked_wf_76",
            },
        },
        "flux0_baked_pulse_77": {
            "operation": "control",
            "length": 80,
            "waveforms": {
                "single": "flux0_baked_wf_77",
            },
        },
        "flux0_baked_pulse_78": {
            "operation": "control",
            "length": 80,
            "waveforms": {
                "single": "flux0_baked_wf_78",
            },
        },
        "flux0_baked_pulse_79": {
            "operation": "control",
            "length": 80,
            "waveforms": {
                "single": "flux0_baked_wf_79",
            },
        },
        "flux0_baked_pulse_80": {
            "operation": "control",
            "length": 80,
            "waveforms": {
                "single": "flux0_baked_wf_80",
            },
        },
        "flux0_baked_pulse_81": {
            "operation": "control",
            "length": 84,
            "waveforms": {
                "single": "flux0_baked_wf_81",
            },
        },
        "flux0_baked_pulse_82": {
            "operation": "control",
            "length": 84,
            "waveforms": {
                "single": "flux0_baked_wf_82",
            },
        },
        "flux0_baked_pulse_83": {
            "operation": "control",
            "length": 84,
            "waveforms": {
                "single": "flux0_baked_wf_83",
            },
        },
        "flux0_baked_pulse_84": {
            "operation": "control",
            "length": 84,
            "waveforms": {
                "single": "flux0_baked_wf_84",
            },
        },
        "flux0_baked_pulse_85": {
            "operation": "control",
            "length": 88,
            "waveforms": {
                "single": "flux0_baked_wf_85",
            },
        },
        "flux0_baked_pulse_86": {
            "operation": "control",
            "length": 88,
            "waveforms": {
                "single": "flux0_baked_wf_86",
            },
        },
        "flux0_baked_pulse_87": {
            "operation": "control",
            "length": 88,
            "waveforms": {
                "single": "flux0_baked_wf_87",
            },
        },
        "flux0_baked_pulse_88": {
            "operation": "control",
            "length": 88,
            "waveforms": {
                "single": "flux0_baked_wf_88",
            },
        },
        "flux0_baked_pulse_89": {
            "operation": "control",
            "length": 92,
            "waveforms": {
                "single": "flux0_baked_wf_89",
            },
        },
        "flux0_baked_pulse_90": {
            "operation": "control",
            "length": 92,
            "waveforms": {
                "single": "flux0_baked_wf_90",
            },
        },
        "flux0_baked_pulse_91": {
            "operation": "control",
            "length": 92,
            "waveforms": {
                "single": "flux0_baked_wf_91",
            },
        },
        "flux0_baked_pulse_92": {
            "operation": "control",
            "length": 92,
            "waveforms": {
                "single": "flux0_baked_wf_92",
            },
        },
        "flux0_baked_pulse_93": {
            "operation": "control",
            "length": 96,
            "waveforms": {
                "single": "flux0_baked_wf_93",
            },
        },
        "flux0_baked_pulse_94": {
            "operation": "control",
            "length": 96,
            "waveforms": {
                "single": "flux0_baked_wf_94",
            },
        },
        "flux0_baked_pulse_95": {
            "operation": "control",
            "length": 96,
            "waveforms": {
                "single": "flux0_baked_wf_95",
            },
        },
        "flux0_baked_pulse_96": {
            "operation": "control",
            "length": 96,
            "waveforms": {
                "single": "flux0_baked_wf_96",
            },
        },
        "flux0_baked_pulse_97": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "flux0_baked_wf_97",
            },
        },
        "flux0_baked_pulse_98": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "flux0_baked_wf_98",
            },
        },
        "flux0_baked_pulse_99": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "flux0_baked_wf_99",
            },
        },
        "flux0_baked_pulse_100": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "flux0_baked_wf_100",
            },
        },
        "flux0_baked_pulse_101": {
            "operation": "control",
            "length": 104,
            "waveforms": {
                "single": "flux0_baked_wf_101",
            },
        },
        "flux0_baked_pulse_102": {
            "operation": "control",
            "length": 104,
            "waveforms": {
                "single": "flux0_baked_wf_102",
            },
        },
        "flux0_baked_pulse_103": {
            "operation": "control",
            "length": 104,
            "waveforms": {
                "single": "flux0_baked_wf_103",
            },
        },
        "flux0_baked_pulse_104": {
            "operation": "control",
            "length": 104,
            "waveforms": {
                "single": "flux0_baked_wf_104",
            },
        },
        "flux0_baked_pulse_105": {
            "operation": "control",
            "length": 108,
            "waveforms": {
                "single": "flux0_baked_wf_105",
            },
        },
        "flux0_baked_pulse_106": {
            "operation": "control",
            "length": 108,
            "waveforms": {
                "single": "flux0_baked_wf_106",
            },
        },
        "flux0_baked_pulse_107": {
            "operation": "control",
            "length": 108,
            "waveforms": {
                "single": "flux0_baked_wf_107",
            },
        },
        "flux0_baked_pulse_108": {
            "operation": "control",
            "length": 108,
            "waveforms": {
                "single": "flux0_baked_wf_108",
            },
        },
        "flux0_baked_pulse_109": {
            "operation": "control",
            "length": 112,
            "waveforms": {
                "single": "flux0_baked_wf_109",
            },
        },
        "flux0_baked_pulse_110": {
            "operation": "control",
            "length": 112,
            "waveforms": {
                "single": "flux0_baked_wf_110",
            },
        },
        "flux0_baked_pulse_111": {
            "operation": "control",
            "length": 112,
            "waveforms": {
                "single": "flux0_baked_wf_111",
            },
        },
        "flux0_baked_pulse_112": {
            "operation": "control",
            "length": 112,
            "waveforms": {
                "single": "flux0_baked_wf_112",
            },
        },
        "flux0_baked_pulse_113": {
            "operation": "control",
            "length": 116,
            "waveforms": {
                "single": "flux0_baked_wf_113",
            },
        },
        "flux0_baked_pulse_114": {
            "operation": "control",
            "length": 116,
            "waveforms": {
                "single": "flux0_baked_wf_114",
            },
        },
        "flux0_baked_pulse_115": {
            "operation": "control",
            "length": 116,
            "waveforms": {
                "single": "flux0_baked_wf_115",
            },
        },
        "flux0_baked_pulse_116": {
            "operation": "control",
            "length": 116,
            "waveforms": {
                "single": "flux0_baked_wf_116",
            },
        },
        "flux0_baked_pulse_117": {
            "operation": "control",
            "length": 120,
            "waveforms": {
                "single": "flux0_baked_wf_117",
            },
        },
        "flux0_baked_pulse_118": {
            "operation": "control",
            "length": 120,
            "waveforms": {
                "single": "flux0_baked_wf_118",
            },
        },
        "flux0_baked_pulse_119": {
            "operation": "control",
            "length": 120,
            "waveforms": {
                "single": "flux0_baked_wf_119",
            },
        },
        "flux0_baked_pulse_120": {
            "operation": "control",
            "length": 120,
            "waveforms": {
                "single": "flux0_baked_wf_120",
            },
        },
        "flux0_baked_pulse_121": {
            "operation": "control",
            "length": 124,
            "waveforms": {
                "single": "flux0_baked_wf_121",
            },
        },
        "flux0_baked_pulse_122": {
            "operation": "control",
            "length": 124,
            "waveforms": {
                "single": "flux0_baked_wf_122",
            },
        },
        "flux0_baked_pulse_123": {
            "operation": "control",
            "length": 124,
            "waveforms": {
                "single": "flux0_baked_wf_123",
            },
        },
        "flux0_baked_pulse_124": {
            "operation": "control",
            "length": 124,
            "waveforms": {
                "single": "flux0_baked_wf_124",
            },
        },
        "flux0_baked_pulse_125": {
            "operation": "control",
            "length": 128,
            "waveforms": {
                "single": "flux0_baked_wf_125",
            },
        },
        "flux0_baked_pulse_126": {
            "operation": "control",
            "length": 128,
            "waveforms": {
                "single": "flux0_baked_wf_126",
            },
        },
        "flux0_baked_pulse_127": {
            "operation": "control",
            "length": 128,
            "waveforms": {
                "single": "flux0_baked_wf_127",
            },
        },
        "flux0_baked_pulse_128": {
            "operation": "control",
            "length": 128,
            "waveforms": {
                "single": "flux0_baked_wf_128",
            },
        },
        "flux0_baked_pulse_129": {
            "operation": "control",
            "length": 132,
            "waveforms": {
                "single": "flux0_baked_wf_129",
            },
        },
        "flux0_baked_pulse_130": {
            "operation": "control",
            "length": 132,
            "waveforms": {
                "single": "flux0_baked_wf_130",
            },
        },
        "flux0_baked_pulse_131": {
            "operation": "control",
            "length": 132,
            "waveforms": {
                "single": "flux0_baked_wf_131",
            },
        },
        "flux0_baked_pulse_132": {
            "operation": "control",
            "length": 132,
            "waveforms": {
                "single": "flux0_baked_wf_132",
            },
        },
        "flux0_baked_pulse_133": {
            "operation": "control",
            "length": 136,
            "waveforms": {
                "single": "flux0_baked_wf_133",
            },
        },
        "flux0_baked_pulse_134": {
            "operation": "control",
            "length": 136,
            "waveforms": {
                "single": "flux0_baked_wf_134",
            },
        },
        "flux0_baked_pulse_135": {
            "operation": "control",
            "length": 136,
            "waveforms": {
                "single": "flux0_baked_wf_135",
            },
        },
        "flux0_baked_pulse_136": {
            "operation": "control",
            "length": 136,
            "waveforms": {
                "single": "flux0_baked_wf_136",
            },
        },
        "flux0_baked_pulse_137": {
            "operation": "control",
            "length": 140,
            "waveforms": {
                "single": "flux0_baked_wf_137",
            },
        },
        "flux0_baked_pulse_138": {
            "operation": "control",
            "length": 140,
            "waveforms": {
                "single": "flux0_baked_wf_138",
            },
        },
        "flux0_baked_pulse_139": {
            "operation": "control",
            "length": 140,
            "waveforms": {
                "single": "flux0_baked_wf_139",
            },
        },
        "flux0_baked_pulse_140": {
            "operation": "control",
            "length": 140,
            "waveforms": {
                "single": "flux0_baked_wf_140",
            },
        },
        "flux0_baked_pulse_141": {
            "operation": "control",
            "length": 144,
            "waveforms": {
                "single": "flux0_baked_wf_141",
            },
        },
        "flux0_baked_pulse_142": {
            "operation": "control",
            "length": 144,
            "waveforms": {
                "single": "flux0_baked_wf_142",
            },
        },
        "flux0_baked_pulse_143": {
            "operation": "control",
            "length": 144,
            "waveforms": {
                "single": "flux0_baked_wf_143",
            },
        },
        "flux0_baked_pulse_144": {
            "operation": "control",
            "length": 144,
            "waveforms": {
                "single": "flux0_baked_wf_144",
            },
        },
        "flux0_baked_pulse_145": {
            "operation": "control",
            "length": 148,
            "waveforms": {
                "single": "flux0_baked_wf_145",
            },
        },
        "flux0_baked_pulse_146": {
            "operation": "control",
            "length": 148,
            "waveforms": {
                "single": "flux0_baked_wf_146",
            },
        },
        "flux0_baked_pulse_147": {
            "operation": "control",
            "length": 148,
            "waveforms": {
                "single": "flux0_baked_wf_147",
            },
        },
        "flux0_baked_pulse_148": {
            "operation": "control",
            "length": 148,
            "waveforms": {
                "single": "flux0_baked_wf_148",
            },
        },
        "flux0_baked_pulse_149": {
            "operation": "control",
            "length": 152,
            "waveforms": {
                "single": "flux0_baked_wf_149",
            },
        },
        "flux0_baked_pulse_150": {
            "operation": "control",
            "length": 152,
            "waveforms": {
                "single": "flux0_baked_wf_150",
            },
        },
        "flux0_baked_pulse_151": {
            "operation": "control",
            "length": 152,
            "waveforms": {
                "single": "flux0_baked_wf_151",
            },
        },
        "flux0_baked_pulse_152": {
            "operation": "control",
            "length": 152,
            "waveforms": {
                "single": "flux0_baked_wf_152",
            },
        },
        "flux0_baked_pulse_153": {
            "operation": "control",
            "length": 156,
            "waveforms": {
                "single": "flux0_baked_wf_153",
            },
        },
        "flux0_baked_pulse_154": {
            "operation": "control",
            "length": 156,
            "waveforms": {
                "single": "flux0_baked_wf_154",
            },
        },
        "flux0_baked_pulse_155": {
            "operation": "control",
            "length": 156,
            "waveforms": {
                "single": "flux0_baked_wf_155",
            },
        },
        "flux0_baked_pulse_156": {
            "operation": "control",
            "length": 156,
            "waveforms": {
                "single": "flux0_baked_wf_156",
            },
        },
        "flux0_baked_pulse_157": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "single": "flux0_baked_wf_157",
            },
        },
        "flux0_baked_pulse_158": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "single": "flux0_baked_wf_158",
            },
        },
        "flux0_baked_pulse_159": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "single": "flux0_baked_wf_159",
            },
        },
        "flux0_baked_pulse_160": {
            "operation": "control",
            "length": 160,
            "waveforms": {
                "single": "flux0_baked_wf_160",
            },
        },
        "flux0_baked_pulse_161": {
            "operation": "control",
            "length": 164,
            "waveforms": {
                "single": "flux0_baked_wf_161",
            },
        },
        "flux0_baked_pulse_162": {
            "operation": "control",
            "length": 164,
            "waveforms": {
                "single": "flux0_baked_wf_162",
            },
        },
        "flux0_baked_pulse_163": {
            "operation": "control",
            "length": 164,
            "waveforms": {
                "single": "flux0_baked_wf_163",
            },
        },
        "flux0_baked_pulse_164": {
            "operation": "control",
            "length": 164,
            "waveforms": {
                "single": "flux0_baked_wf_164",
            },
        },
        "flux0_baked_pulse_165": {
            "operation": "control",
            "length": 168,
            "waveforms": {
                "single": "flux0_baked_wf_165",
            },
        },
        "flux0_baked_pulse_166": {
            "operation": "control",
            "length": 168,
            "waveforms": {
                "single": "flux0_baked_wf_166",
            },
        },
        "flux0_baked_pulse_167": {
            "operation": "control",
            "length": 168,
            "waveforms": {
                "single": "flux0_baked_wf_167",
            },
        },
        "flux0_baked_pulse_168": {
            "operation": "control",
            "length": 168,
            "waveforms": {
                "single": "flux0_baked_wf_168",
            },
        },
        "flux0_baked_pulse_169": {
            "operation": "control",
            "length": 172,
            "waveforms": {
                "single": "flux0_baked_wf_169",
            },
        },
        "flux0_baked_pulse_170": {
            "operation": "control",
            "length": 172,
            "waveforms": {
                "single": "flux0_baked_wf_170",
            },
        },
        "flux0_baked_pulse_171": {
            "operation": "control",
            "length": 172,
            "waveforms": {
                "single": "flux0_baked_wf_171",
            },
        },
        "flux0_baked_pulse_172": {
            "operation": "control",
            "length": 172,
            "waveforms": {
                "single": "flux0_baked_wf_172",
            },
        },
        "flux0_baked_pulse_173": {
            "operation": "control",
            "length": 176,
            "waveforms": {
                "single": "flux0_baked_wf_173",
            },
        },
        "flux0_baked_pulse_174": {
            "operation": "control",
            "length": 176,
            "waveforms": {
                "single": "flux0_baked_wf_174",
            },
        },
        "flux0_baked_pulse_175": {
            "operation": "control",
            "length": 176,
            "waveforms": {
                "single": "flux0_baked_wf_175",
            },
        },
        "flux0_baked_pulse_176": {
            "operation": "control",
            "length": 176,
            "waveforms": {
                "single": "flux0_baked_wf_176",
            },
        },
        "flux0_baked_pulse_177": {
            "operation": "control",
            "length": 180,
            "waveforms": {
                "single": "flux0_baked_wf_177",
            },
        },
        "flux0_baked_pulse_178": {
            "operation": "control",
            "length": 180,
            "waveforms": {
                "single": "flux0_baked_wf_178",
            },
        },
        "flux0_baked_pulse_179": {
            "operation": "control",
            "length": 180,
            "waveforms": {
                "single": "flux0_baked_wf_179",
            },
        },
        "flux0_baked_pulse_180": {
            "operation": "control",
            "length": 180,
            "waveforms": {
                "single": "flux0_baked_wf_180",
            },
        },
        "flux0_baked_pulse_181": {
            "operation": "control",
            "length": 184,
            "waveforms": {
                "single": "flux0_baked_wf_181",
            },
        },
        "flux0_baked_pulse_182": {
            "operation": "control",
            "length": 184,
            "waveforms": {
                "single": "flux0_baked_wf_182",
            },
        },
        "flux0_baked_pulse_183": {
            "operation": "control",
            "length": 184,
            "waveforms": {
                "single": "flux0_baked_wf_183",
            },
        },
        "flux0_baked_pulse_184": {
            "operation": "control",
            "length": 184,
            "waveforms": {
                "single": "flux0_baked_wf_184",
            },
        },
        "flux0_baked_pulse_185": {
            "operation": "control",
            "length": 188,
            "waveforms": {
                "single": "flux0_baked_wf_185",
            },
        },
        "flux0_baked_pulse_186": {
            "operation": "control",
            "length": 188,
            "waveforms": {
                "single": "flux0_baked_wf_186",
            },
        },
        "flux0_baked_pulse_187": {
            "operation": "control",
            "length": 188,
            "waveforms": {
                "single": "flux0_baked_wf_187",
            },
        },
        "flux0_baked_pulse_188": {
            "operation": "control",
            "length": 188,
            "waveforms": {
                "single": "flux0_baked_wf_188",
            },
        },
        "flux0_baked_pulse_189": {
            "operation": "control",
            "length": 192,
            "waveforms": {
                "single": "flux0_baked_wf_189",
            },
        },
        "flux0_baked_pulse_190": {
            "operation": "control",
            "length": 192,
            "waveforms": {
                "single": "flux0_baked_wf_190",
            },
        },
        "flux0_baked_pulse_191": {
            "operation": "control",
            "length": 192,
            "waveforms": {
                "single": "flux0_baked_wf_191",
            },
        },
        "flux0_baked_pulse_192": {
            "operation": "control",
            "length": 192,
            "waveforms": {
                "single": "flux0_baked_wf_192",
            },
        },
        "flux0_baked_pulse_193": {
            "operation": "control",
            "length": 196,
            "waveforms": {
                "single": "flux0_baked_wf_193",
            },
        },
        "flux0_baked_pulse_194": {
            "operation": "control",
            "length": 196,
            "waveforms": {
                "single": "flux0_baked_wf_194",
            },
        },
        "flux0_baked_pulse_195": {
            "operation": "control",
            "length": 196,
            "waveforms": {
                "single": "flux0_baked_wf_195",
            },
        },
        "flux0_baked_pulse_196": {
            "operation": "control",
            "length": 196,
            "waveforms": {
                "single": "flux0_baked_wf_196",
            },
        },
        "flux0_baked_pulse_197": {
            "operation": "control",
            "length": 200,
            "waveforms": {
                "single": "flux0_baked_wf_197",
            },
        },
        "flux0_baked_pulse_198": {
            "operation": "control",
            "length": 200,
            "waveforms": {
                "single": "flux0_baked_wf_198",
            },
        },
        "flux0_baked_pulse_199": {
            "operation": "control",
            "length": 200,
            "waveforms": {
                "single": "flux0_baked_wf_199",
            },
        },
        "flux0_baked_pulse_200": {
            "operation": "control",
            "length": 200,
            "waveforms": {
                "single": "flux0_baked_wf_200",
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
            "sample": 0.125,
        },
        "readout1_wf": {
            "type": "constant",
            "sample": 0.125,
        },
        "readout2_wf": {
            "type": "constant",
            "sample": 0.125,
        },
        "readout3_wf": {
            "type": "constant",
            "sample": 0.125,
        },
        "readout4_wf": {
            "type": "constant",
            "sample": 0.125,
        },
        "readout5_wf": {
            "type": "constant",
            "sample": 0.125,
        },
        "readout6_wf": {
            "type": "constant",
            "sample": 0.125,
        },
        "pi_wf0": {
            "type": "constant",
            "sample": 0.022,
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
            "sample": 0.011,
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
        "flux0_baked_wf_0": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
        },
        "flux0_baked_wf_1": {
            "type": "arbitrary",
            "samples": [0.25] + [0] * 15,
            "is_overridable": False,
        },
        "flux0_baked_wf_2": {
            "type": "arbitrary",
            "samples": [0.25] * 2 + [0] * 14,
            "is_overridable": False,
        },
        "flux0_baked_wf_3": {
            "type": "arbitrary",
            "samples": [0.25] * 3 + [0] * 13,
            "is_overridable": False,
        },
        "flux0_baked_wf_4": {
            "type": "arbitrary",
            "samples": [0.25] * 4 + [0] * 12,
            "is_overridable": False,
        },
        "flux0_baked_wf_5": {
            "type": "arbitrary",
            "samples": [0.25] * 5 + [0] * 11,
            "is_overridable": False,
        },
        "flux0_baked_wf_6": {
            "type": "arbitrary",
            "samples": [0.25] * 6 + [0] * 10,
            "is_overridable": False,
        },
        "flux0_baked_wf_7": {
            "type": "arbitrary",
            "samples": [0.25] * 7 + [0] * 9,
            "is_overridable": False,
        },
        "flux0_baked_wf_8": {
            "type": "arbitrary",
            "samples": [0.25] * 8 + [0] * 8,
            "is_overridable": False,
        },
        "flux0_baked_wf_9": {
            "type": "arbitrary",
            "samples": [0.25] * 9 + [0] * 7,
            "is_overridable": False,
        },
        "flux0_baked_wf_10": {
            "type": "arbitrary",
            "samples": [0.25] * 10 + [0] * 6,
            "is_overridable": False,
        },
        "flux0_baked_wf_11": {
            "type": "arbitrary",
            "samples": [0.25] * 11 + [0] * 5,
            "is_overridable": False,
        },
        "flux0_baked_wf_12": {
            "type": "arbitrary",
            "samples": [0.25] * 12 + [0] * 4,
            "is_overridable": False,
        },
        "flux0_baked_wf_13": {
            "type": "arbitrary",
            "samples": [0.25] * 13 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_14": {
            "type": "arbitrary",
            "samples": [0.25] * 14 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_15": {
            "type": "arbitrary",
            "samples": [0.25] * 15 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_16": {
            "type": "arbitrary",
            "samples": [0.25] * 16,
            "is_overridable": False,
        },
        "flux0_baked_wf_17": {
            "type": "arbitrary",
            "samples": [0.25] * 17 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_18": {
            "type": "arbitrary",
            "samples": [0.25] * 18 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_19": {
            "type": "arbitrary",
            "samples": [0.25] * 19 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_20": {
            "type": "arbitrary",
            "samples": [0.25] * 20,
            "is_overridable": False,
        },
        "flux0_baked_wf_21": {
            "type": "arbitrary",
            "samples": [0.25] * 21 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_22": {
            "type": "arbitrary",
            "samples": [0.25] * 22 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_23": {
            "type": "arbitrary",
            "samples": [0.25] * 23 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_24": {
            "type": "arbitrary",
            "samples": [0.25] * 24,
            "is_overridable": False,
        },
        "flux0_baked_wf_25": {
            "type": "arbitrary",
            "samples": [0.25] * 25 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_26": {
            "type": "arbitrary",
            "samples": [0.25] * 26 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_27": {
            "type": "arbitrary",
            "samples": [0.25] * 27 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_28": {
            "type": "arbitrary",
            "samples": [0.25] * 28,
            "is_overridable": False,
        },
        "flux0_baked_wf_29": {
            "type": "arbitrary",
            "samples": [0.25] * 29 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_30": {
            "type": "arbitrary",
            "samples": [0.25] * 30 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_31": {
            "type": "arbitrary",
            "samples": [0.25] * 31 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_32": {
            "type": "arbitrary",
            "samples": [0.25] * 32,
            "is_overridable": False,
        },
        "flux0_baked_wf_33": {
            "type": "arbitrary",
            "samples": [0.25] * 33 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_34": {
            "type": "arbitrary",
            "samples": [0.25] * 34 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_35": {
            "type": "arbitrary",
            "samples": [0.25] * 35 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_36": {
            "type": "arbitrary",
            "samples": [0.25] * 36,
            "is_overridable": False,
        },
        "flux0_baked_wf_37": {
            "type": "arbitrary",
            "samples": [0.25] * 37 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_38": {
            "type": "arbitrary",
            "samples": [0.25] * 38 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_39": {
            "type": "arbitrary",
            "samples": [0.25] * 39 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_40": {
            "type": "arbitrary",
            "samples": [0.25] * 40,
            "is_overridable": False,
        },
        "flux0_baked_wf_41": {
            "type": "arbitrary",
            "samples": [0.25] * 41 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_42": {
            "type": "arbitrary",
            "samples": [0.25] * 42 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_43": {
            "type": "arbitrary",
            "samples": [0.25] * 43 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_44": {
            "type": "arbitrary",
            "samples": [0.25] * 44,
            "is_overridable": False,
        },
        "flux0_baked_wf_45": {
            "type": "arbitrary",
            "samples": [0.25] * 45 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_46": {
            "type": "arbitrary",
            "samples": [0.25] * 46 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_47": {
            "type": "arbitrary",
            "samples": [0.25] * 47 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_48": {
            "type": "arbitrary",
            "samples": [0.25] * 48,
            "is_overridable": False,
        },
        "flux0_baked_wf_49": {
            "type": "arbitrary",
            "samples": [0.25] * 49 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_50": {
            "type": "arbitrary",
            "samples": [0.25] * 50 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_51": {
            "type": "arbitrary",
            "samples": [0.25] * 51 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_52": {
            "type": "arbitrary",
            "samples": [0.25] * 52,
            "is_overridable": False,
        },
        "flux0_baked_wf_53": {
            "type": "arbitrary",
            "samples": [0.25] * 53 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_54": {
            "type": "arbitrary",
            "samples": [0.25] * 54 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_55": {
            "type": "arbitrary",
            "samples": [0.25] * 55 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_56": {
            "type": "arbitrary",
            "samples": [0.25] * 56,
            "is_overridable": False,
        },
        "flux0_baked_wf_57": {
            "type": "arbitrary",
            "samples": [0.25] * 57 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_58": {
            "type": "arbitrary",
            "samples": [0.25] * 58 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_59": {
            "type": "arbitrary",
            "samples": [0.25] * 59 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_60": {
            "type": "arbitrary",
            "samples": [0.25] * 60,
            "is_overridable": False,
        },
        "flux0_baked_wf_61": {
            "type": "arbitrary",
            "samples": [0.25] * 61 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_62": {
            "type": "arbitrary",
            "samples": [0.25] * 62 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_63": {
            "type": "arbitrary",
            "samples": [0.25] * 63 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_64": {
            "type": "arbitrary",
            "samples": [0.25] * 64,
            "is_overridable": False,
        },
        "flux0_baked_wf_65": {
            "type": "arbitrary",
            "samples": [0.25] * 65 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_66": {
            "type": "arbitrary",
            "samples": [0.25] * 66 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_67": {
            "type": "arbitrary",
            "samples": [0.25] * 67 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_68": {
            "type": "arbitrary",
            "samples": [0.25] * 68,
            "is_overridable": False,
        },
        "flux0_baked_wf_69": {
            "type": "arbitrary",
            "samples": [0.25] * 69 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_70": {
            "type": "arbitrary",
            "samples": [0.25] * 70 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_71": {
            "type": "arbitrary",
            "samples": [0.25] * 71 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_72": {
            "type": "arbitrary",
            "samples": [0.25] * 72,
            "is_overridable": False,
        },
        "flux0_baked_wf_73": {
            "type": "arbitrary",
            "samples": [0.25] * 73 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_74": {
            "type": "arbitrary",
            "samples": [0.25] * 74 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_75": {
            "type": "arbitrary",
            "samples": [0.25] * 75 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_76": {
            "type": "arbitrary",
            "samples": [0.25] * 76,
            "is_overridable": False,
        },
        "flux0_baked_wf_77": {
            "type": "arbitrary",
            "samples": [0.25] * 77 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_78": {
            "type": "arbitrary",
            "samples": [0.25] * 78 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_79": {
            "type": "arbitrary",
            "samples": [0.25] * 79 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_80": {
            "type": "arbitrary",
            "samples": [0.25] * 80,
            "is_overridable": False,
        },
        "flux0_baked_wf_81": {
            "type": "arbitrary",
            "samples": [0.25] * 81 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_82": {
            "type": "arbitrary",
            "samples": [0.25] * 82 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_83": {
            "type": "arbitrary",
            "samples": [0.25] * 83 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_84": {
            "type": "arbitrary",
            "samples": [0.25] * 84,
            "is_overridable": False,
        },
        "flux0_baked_wf_85": {
            "type": "arbitrary",
            "samples": [0.25] * 85 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_86": {
            "type": "arbitrary",
            "samples": [0.25] * 86 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_87": {
            "type": "arbitrary",
            "samples": [0.25] * 87 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_88": {
            "type": "arbitrary",
            "samples": [0.25] * 88,
            "is_overridable": False,
        },
        "flux0_baked_wf_89": {
            "type": "arbitrary",
            "samples": [0.25] * 89 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_90": {
            "type": "arbitrary",
            "samples": [0.25] * 90 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_91": {
            "type": "arbitrary",
            "samples": [0.25] * 91 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_92": {
            "type": "arbitrary",
            "samples": [0.25] * 92,
            "is_overridable": False,
        },
        "flux0_baked_wf_93": {
            "type": "arbitrary",
            "samples": [0.25] * 93 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_94": {
            "type": "arbitrary",
            "samples": [0.25] * 94 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_95": {
            "type": "arbitrary",
            "samples": [0.25] * 95 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_96": {
            "type": "arbitrary",
            "samples": [0.25] * 96,
            "is_overridable": False,
        },
        "flux0_baked_wf_97": {
            "type": "arbitrary",
            "samples": [0.25] * 97 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_98": {
            "type": "arbitrary",
            "samples": [0.25] * 98 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_99": {
            "type": "arbitrary",
            "samples": [0.25] * 99 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_100": {
            "type": "arbitrary",
            "samples": [0.25] * 100,
            "is_overridable": False,
        },
        "flux0_baked_wf_101": {
            "type": "arbitrary",
            "samples": [0.25] * 101 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_102": {
            "type": "arbitrary",
            "samples": [0.25] * 102 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_103": {
            "type": "arbitrary",
            "samples": [0.25] * 103 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_104": {
            "type": "arbitrary",
            "samples": [0.25] * 104,
            "is_overridable": False,
        },
        "flux0_baked_wf_105": {
            "type": "arbitrary",
            "samples": [0.25] * 105 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_106": {
            "type": "arbitrary",
            "samples": [0.25] * 106 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_107": {
            "type": "arbitrary",
            "samples": [0.25] * 107 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_108": {
            "type": "arbitrary",
            "samples": [0.25] * 108,
            "is_overridable": False,
        },
        "flux0_baked_wf_109": {
            "type": "arbitrary",
            "samples": [0.25] * 109 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_110": {
            "type": "arbitrary",
            "samples": [0.25] * 110 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_111": {
            "type": "arbitrary",
            "samples": [0.25] * 111 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_112": {
            "type": "arbitrary",
            "samples": [0.25] * 112,
            "is_overridable": False,
        },
        "flux0_baked_wf_113": {
            "type": "arbitrary",
            "samples": [0.25] * 113 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_114": {
            "type": "arbitrary",
            "samples": [0.25] * 114 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_115": {
            "type": "arbitrary",
            "samples": [0.25] * 115 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_116": {
            "type": "arbitrary",
            "samples": [0.25] * 116,
            "is_overridable": False,
        },
        "flux0_baked_wf_117": {
            "type": "arbitrary",
            "samples": [0.25] * 117 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_118": {
            "type": "arbitrary",
            "samples": [0.25] * 118 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_119": {
            "type": "arbitrary",
            "samples": [0.25] * 119 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_120": {
            "type": "arbitrary",
            "samples": [0.25] * 120,
            "is_overridable": False,
        },
        "flux0_baked_wf_121": {
            "type": "arbitrary",
            "samples": [0.25] * 121 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_122": {
            "type": "arbitrary",
            "samples": [0.25] * 122 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_123": {
            "type": "arbitrary",
            "samples": [0.25] * 123 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_124": {
            "type": "arbitrary",
            "samples": [0.25] * 124,
            "is_overridable": False,
        },
        "flux0_baked_wf_125": {
            "type": "arbitrary",
            "samples": [0.25] * 125 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_126": {
            "type": "arbitrary",
            "samples": [0.25] * 126 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_127": {
            "type": "arbitrary",
            "samples": [0.25] * 127 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_128": {
            "type": "arbitrary",
            "samples": [0.25] * 128,
            "is_overridable": False,
        },
        "flux0_baked_wf_129": {
            "type": "arbitrary",
            "samples": [0.25] * 129 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_130": {
            "type": "arbitrary",
            "samples": [0.25] * 130 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_131": {
            "type": "arbitrary",
            "samples": [0.25] * 131 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_132": {
            "type": "arbitrary",
            "samples": [0.25] * 132,
            "is_overridable": False,
        },
        "flux0_baked_wf_133": {
            "type": "arbitrary",
            "samples": [0.25] * 133 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_134": {
            "type": "arbitrary",
            "samples": [0.25] * 134 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_135": {
            "type": "arbitrary",
            "samples": [0.25] * 135 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_136": {
            "type": "arbitrary",
            "samples": [0.25] * 136,
            "is_overridable": False,
        },
        "flux0_baked_wf_137": {
            "type": "arbitrary",
            "samples": [0.25] * 137 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_138": {
            "type": "arbitrary",
            "samples": [0.25] * 138 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_139": {
            "type": "arbitrary",
            "samples": [0.25] * 139 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_140": {
            "type": "arbitrary",
            "samples": [0.25] * 140,
            "is_overridable": False,
        },
        "flux0_baked_wf_141": {
            "type": "arbitrary",
            "samples": [0.25] * 141 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_142": {
            "type": "arbitrary",
            "samples": [0.25] * 142 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_143": {
            "type": "arbitrary",
            "samples": [0.25] * 143 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_144": {
            "type": "arbitrary",
            "samples": [0.25] * 144,
            "is_overridable": False,
        },
        "flux0_baked_wf_145": {
            "type": "arbitrary",
            "samples": [0.25] * 145 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_146": {
            "type": "arbitrary",
            "samples": [0.25] * 146 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_147": {
            "type": "arbitrary",
            "samples": [0.25] * 147 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_148": {
            "type": "arbitrary",
            "samples": [0.25] * 148,
            "is_overridable": False,
        },
        "flux0_baked_wf_149": {
            "type": "arbitrary",
            "samples": [0.25] * 149 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_150": {
            "type": "arbitrary",
            "samples": [0.25] * 150 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_151": {
            "type": "arbitrary",
            "samples": [0.25] * 151 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_152": {
            "type": "arbitrary",
            "samples": [0.25] * 152,
            "is_overridable": False,
        },
        "flux0_baked_wf_153": {
            "type": "arbitrary",
            "samples": [0.25] * 153 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_154": {
            "type": "arbitrary",
            "samples": [0.25] * 154 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_155": {
            "type": "arbitrary",
            "samples": [0.25] * 155 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_156": {
            "type": "arbitrary",
            "samples": [0.25] * 156,
            "is_overridable": False,
        },
        "flux0_baked_wf_157": {
            "type": "arbitrary",
            "samples": [0.25] * 157 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_158": {
            "type": "arbitrary",
            "samples": [0.25] * 158 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_159": {
            "type": "arbitrary",
            "samples": [0.25] * 159 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_160": {
            "type": "arbitrary",
            "samples": [0.25] * 160,
            "is_overridable": False,
        },
        "flux0_baked_wf_161": {
            "type": "arbitrary",
            "samples": [0.25] * 161 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_162": {
            "type": "arbitrary",
            "samples": [0.25] * 162 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_163": {
            "type": "arbitrary",
            "samples": [0.25] * 163 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_164": {
            "type": "arbitrary",
            "samples": [0.25] * 164,
            "is_overridable": False,
        },
        "flux0_baked_wf_165": {
            "type": "arbitrary",
            "samples": [0.25] * 165 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_166": {
            "type": "arbitrary",
            "samples": [0.25] * 166 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_167": {
            "type": "arbitrary",
            "samples": [0.25] * 167 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_168": {
            "type": "arbitrary",
            "samples": [0.25] * 168,
            "is_overridable": False,
        },
        "flux0_baked_wf_169": {
            "type": "arbitrary",
            "samples": [0.25] * 169 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_170": {
            "type": "arbitrary",
            "samples": [0.25] * 170 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_171": {
            "type": "arbitrary",
            "samples": [0.25] * 171 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_172": {
            "type": "arbitrary",
            "samples": [0.25] * 172,
            "is_overridable": False,
        },
        "flux0_baked_wf_173": {
            "type": "arbitrary",
            "samples": [0.25] * 173 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_174": {
            "type": "arbitrary",
            "samples": [0.25] * 174 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_175": {
            "type": "arbitrary",
            "samples": [0.25] * 175 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_176": {
            "type": "arbitrary",
            "samples": [0.25] * 176,
            "is_overridable": False,
        },
        "flux0_baked_wf_177": {
            "type": "arbitrary",
            "samples": [0.25] * 177 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_178": {
            "type": "arbitrary",
            "samples": [0.25] * 178 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_179": {
            "type": "arbitrary",
            "samples": [0.25] * 179 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_180": {
            "type": "arbitrary",
            "samples": [0.25] * 180,
            "is_overridable": False,
        },
        "flux0_baked_wf_181": {
            "type": "arbitrary",
            "samples": [0.25] * 181 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_182": {
            "type": "arbitrary",
            "samples": [0.25] * 182 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_183": {
            "type": "arbitrary",
            "samples": [0.25] * 183 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_184": {
            "type": "arbitrary",
            "samples": [0.25] * 184,
            "is_overridable": False,
        },
        "flux0_baked_wf_185": {
            "type": "arbitrary",
            "samples": [0.25] * 185 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_186": {
            "type": "arbitrary",
            "samples": [0.25] * 186 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_187": {
            "type": "arbitrary",
            "samples": [0.25] * 187 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_188": {
            "type": "arbitrary",
            "samples": [0.25] * 188,
            "is_overridable": False,
        },
        "flux0_baked_wf_189": {
            "type": "arbitrary",
            "samples": [0.25] * 189 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_190": {
            "type": "arbitrary",
            "samples": [0.25] * 190 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_191": {
            "type": "arbitrary",
            "samples": [0.25] * 191 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_192": {
            "type": "arbitrary",
            "samples": [0.25] * 192,
            "is_overridable": False,
        },
        "flux0_baked_wf_193": {
            "type": "arbitrary",
            "samples": [0.25] * 193 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_194": {
            "type": "arbitrary",
            "samples": [0.25] * 194 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_195": {
            "type": "arbitrary",
            "samples": [0.25] * 195 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_196": {
            "type": "arbitrary",
            "samples": [0.25] * 196,
            "is_overridable": False,
        },
        "flux0_baked_wf_197": {
            "type": "arbitrary",
            "samples": [0.25] * 197 + [0] * 3,
            "is_overridable": False,
        },
        "flux0_baked_wf_198": {
            "type": "arbitrary",
            "samples": [0.25] * 198 + [0] * 2,
            "is_overridable": False,
        },
        "flux0_baked_wf_199": {
            "type": "arbitrary",
            "samples": [0.25] * 199 + [0],
            "is_overridable": False,
        },
        "flux0_baked_wf_200": {
            "type": "arbitrary",
            "samples": [0.25] * 200,
            "is_overridable": False,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
        "OFF": {
            "samples": [(0, 0)],
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
            {'intermediate_frequency': 100000000, 'lo_frequency': 6189000000, 'correction': [0.9792498461902142, 0.02296530455350876, 0.02197825163602829, 1.0232283771038055]},
            {'intermediate_frequency': 179000000, 'lo_frequency': 6110000000, 'correction': [0.9841276444494724, 0.05483501777052879, 0.052632030099630356, 1.025319691747427]},
            {'intermediate_frequency': 169000000, 'lo_frequency': 6110000000, 'correction': [0.9832491092383862, 0.052119217813014984, 0.04997655004262924, 1.025404404848814]},
            {'intermediate_frequency': 172215300, 'lo_frequency': 6110000000, 'correction': [0.9834322556853294, 0.05336608737707138, 0.0511721596121788, 1.0255954004824162]},
            {'intermediate_frequency': 100000000, 'lo_frequency': 6007000000, 'correction': [0.9805241003632545, 0.04597645252943039, 0.04391460865736008, 1.0265608876943588]},
            {'intermediate_frequency': 100000000, 'lo_frequency': 5882000000, 'correction': [0.9815450236201286, 0.08165643364191055, 0.0771622434258461, 1.0387135222554207]},
            {'intermediate_frequency': -40864584, 'lo_frequency': 6382000000, 'correction': [0.9785669781267643, -0.02498408779501915, -0.023869480937719345, 1.0242620408535004]},
            {'intermediate_frequency': -10139023, 'lo_frequency': 6352000000, 'correction': [0.9787439368665218, -0.012496553361415863, -0.01195981353521347, 1.022668570280075]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6391860977, 'correction': [0.9792955070734024, -0.026965998113155365, -0.025794409215450287, 1.0237753726541996]},
            {'intermediate_frequency': -100000000, 'lo_frequency': 6441860977, 'correction': [0.9828890860080719, -0.052893687039613724, -0.05066971853375435, 1.026029534637928]},
            {'intermediate_frequency': -110924023, 'lo_frequency': 6452785000, 'correction': [0.9836567975580692, -0.05788365751504898, -0.05544988065958023, 1.026830941438675]},
            {'intermediate_frequency': -103030023, 'lo_frequency': 6444891000, 'correction': [0.9831880666315556, -0.05488967522978783, -0.0525817833840847, 1.0263416394591331]},
            {'intermediate_frequency': -150000000, 'lo_frequency': 6491860977, 'correction': [0.987505380064249, -0.07377802953124046, -0.07081400975584984, 1.0288388058543205]},
            {'intermediate_frequency': -193424023, 'lo_frequency': 6452785000, 'correction': [0.9909583926200867, -0.08515872806310654, -0.08189716190099716, 1.0304234512150288]},
            {'intermediate_frequency': -193724023, 'lo_frequency': 6452785000, 'correction': [0.9908422231674194, -0.08466072380542755, -0.0814182311296463, 1.0303026549518108]},
            {'intermediate_frequency': -93724023, 'lo_frequency': 6352785000, 'correction': [0.9798078313469887, -0.03997952863574028, -0.03818662092089653, 1.0258109867572784]},
            {'intermediate_frequency': -81371023, 'lo_frequency': 6340432000, 'correction': [0.9782580099999905, -0.03401654586195946, -0.032427724450826645, 1.0261885188519955]},
            {'intermediate_frequency': -193939023, 'lo_frequency': 6453000000, 'correction': [0.9909583926200867, -0.08515872806310654, -0.08189716190099716, 1.0304234512150288]},
            {'intermediate_frequency': -194739023, 'lo_frequency': 6453000000, 'correction': [0.9915495328605175, -0.0856141448020935, -0.08241552114486694, 1.0300325006246567]},
            {'intermediate_frequency': 5260977, 'lo_frequency': 6253000000, 'correction': [0.974171694368124, -0.003511127084493637, -0.0033296309411525726, 1.0272732116281986]},
            {'intermediate_frequency': -94739023, 'lo_frequency': 6353000000, 'correction': [0.9798637628555298, -0.04047927260398865, -0.03866395354270935, 1.0258695483207703]},
            {'intermediate_frequency': -61400000, 'lo_frequency': 6391860977, 'correction': [0.9797676913440228, -0.02995475009083748, -0.02866728976368904, 1.0237694792449474]},
            {'intermediate_frequency': -121400000, 'lo_frequency': 6451860977, 'correction': [0.9846197217702866, -0.06084731966257095, -0.05834583193063736, 1.0268337801098824]},
            {'intermediate_frequency': -21400000, 'lo_frequency': 6351860977, 'correction': [0.9770599342882633, -0.018385089933872223, -0.01752423495054245, 1.0250567235052586]},
            {'intermediate_frequency': -119100000, 'lo_frequency': 6451860977, 'correction': [0.9844526499509811, -0.0598498210310936, -0.05738934129476547, 1.026659544557333]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6382760977, 'correction': [0.9790809527039528, -0.027222469449043274, -0.02602703869342804, 1.0240504741668701]},
            {'intermediate_frequency': -100000000, 'lo_frequency': 6432760977, 'correction': [0.9824609197676182, -0.04989970475435257, -0.04780162125825882, 1.0255825743079185]},
            {'intermediate_frequency': -186300000, 'lo_frequency': 6382760977, 'correction': [0.9869083389639854, -0.07078702747821808, -0.06794317066669464, 1.0282167755067348]},
            {'intermediate_frequency': -86300000, 'lo_frequency': 6382760977, 'correction': [0.9805256128311157, -0.037942685186862946, -0.03631190210580826, 1.0245614387094975]},
            {'intermediate_frequency': -300000000, 'lo_frequency': 6054816000, 'correction': [0.9898257069289684, -0.08017868548631668, -0.07710785418748856, 1.0292456597089767]},
            {'intermediate_frequency': 300000000, 'lo_frequency': 6054816000, 'correction': [0.9997894875705242, 0.11495320126414299, 0.1107124499976635, 1.0380856171250343]},
            {'intermediate_frequency': -150000000, 'lo_frequency': 6054816000, 'correction': [0.9796853885054588, -0.028956260532140732, -0.027711715549230576, 1.0236834809184074]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6054816000, 'correction': [0.9785227365791798, 0.002995472401380539, 0.002866726368665695, 1.0224686153233051]},
            {'intermediate_frequency': -100000000, 'lo_frequency': 6054816000, 'correction': [0.9792138114571571, -0.012973923236131668, -0.012428421527147293, 1.022192943841219]},
            {'intermediate_frequency': 295184000, 'lo_frequency': 6054816000, 'correction': [0.999255582690239, 0.1132114864885807, 0.10903498902916908, 1.0375312604010105]},
            {'intermediate_frequency': -104816000, 'lo_frequency': 6454816000, 'correction': [0.9838112369179726, -0.05585983395576477, -0.05356338620185852, 1.0259906314313412]},
            {'intermediate_frequency': -245416000, 'lo_frequency': 6504816000, 'correction': [0.9981252439320087, -0.10691135376691818, -0.10311811417341232, 1.034841664135456]},
            {'intermediate_frequency': -195416000, 'lo_frequency': 6454816000, 'correction': [0.9910751916468143, -0.08565673232078552, -0.08237609267234802, 1.0305449031293392]},
            {'intermediate_frequency': -145416000, 'lo_frequency': 6404816000, 'correction': [0.9845968261361122, -0.057826023548841476, -0.05550287291407585, 1.02580850943923]},
            {'intermediate_frequency': 115584000, 'lo_frequency': 6254816000, 'correction': [0.9764660634100437, 0.029558632522821426, 0.02809569612145424, 1.02731042355299]},
            {'intermediate_frequency': 0, 'lo_frequency': 6350000000, 'correction': [0.9961768016219139, 0.008134439587593079, 0.008070643991231918, 1.004051111638546]},
            {'intermediate_frequency': 60000000, 'lo_frequency': 6400000000, 'correction': [0.9778789803385735, 0.006994668394327164, 0.006684247404336929, 1.0232923179864883]},
            {'intermediate_frequency': 260000000, 'lo_frequency': 6200000000, 'correction': [0.9916873052716255, 0.07421163842082024, 0.07182351872324944, 1.024660736322403]},
            {'intermediate_frequency': 201500000, 'lo_frequency': 6250000000, 'correction': [0.9839086309075356, 0.05648326501250267, 0.054161187261343, 1.0260922014713287]},
            {'intermediate_frequency': 251500000, 'lo_frequency': 6200000000, 'correction': [0.9905178360641003, 0.0720314309000969, 0.06961148232221603, 1.0249518416821957]},
            {'intermediate_frequency': 151500000, 'lo_frequency': 6300000000, 'correction': [0.976955521851778, 0.04363008961081505, 0.04138990864157677, 1.0298321060836315]},
            {'intermediate_frequency': 120000000, 'lo_frequency': 6300000000, 'correction': [0.9760312810540199, 0.035104669630527496, 0.033302225172519684, 1.0288578420877457]},
            {'intermediate_frequency': 117600000, 'lo_frequency': 6300000000, 'correction': [0.9759355634450912, 0.03410167992115021, 0.03235073387622833, 1.0287569426000118]},
            {'intermediate_frequency': 155300000, 'lo_frequency': 6300000000, 'correction': [0.9773092120885849, 0.04462191462516785, 0.04235145449638367, 1.029702726751566]},
            {'intermediate_frequency': 136300000, 'lo_frequency': 6319000000, 'correction': [0.976851649582386, 0.03859582170844078, 0.03664984926581383, 1.0287188850343227]},
            {'intermediate_frequency': -94700000, 'lo_frequency': 6550000000, 'correction': [0.9867146015167236, -0.06979002803564072, -0.06698622554540634, 1.0280149281024933]},
            {'intermediate_frequency': -119700000, 'lo_frequency': 6575000000, 'correction': [0.9901381880044937, -0.08370635658502579, -0.08042190223932266, 1.0305757261812687]},
            {'intermediate_frequency': -110000000, 'lo_frequency': 6427161000, 'correction': [0.9831412509083748, -0.051371097564697266, -0.049259185791015625, 1.025291919708252]},
            {'intermediate_frequency': -100000000, 'lo_frequency': 6427161000, 'correction': [0.9821890406310558, -0.04790371656417847, -0.04588955640792847, 1.0252987630665302]},
            {'intermediate_frequency': -100000000, 'lo_frequency': 6594760000, 'correction': [0.9892123863101006, -0.08175403252243996, -0.07846957817673683, 1.0306172594428062]},
            {'intermediate_frequency': -100000000, 'lo_frequency': 6427205000, 'correction': [0.9821890406310558, -0.04790371656417847, -0.04588955640792847, 1.0252987630665302]},
            {'intermediate_frequency': -100000000, 'lo_frequency': 6594787000, 'correction': [0.9892123863101006, -0.08175403252243996, -0.07846957817673683, 1.0306172594428062]},
            {'intermediate_frequency': -100000000, 'lo_frequency': 6272511000, 'correction': [0.9767700545489788, -0.033065591007471085, -0.03142908588051796, 1.027630239725113]},
            {'intermediate_frequency': -100000000, 'lo_frequency': 6581509000, 'correction': [0.9885527677834034, -0.07876303046941757, -0.07559873908758163, 1.0299300327897072]},
            {'intermediate_frequency': -100000000, 'lo_frequency': 6692538000, 'correction': [0.9944543987512589, -0.1192365251481533, -0.11333518847823143, 1.0462354086339474]},
            {'intermediate_frequency': -100000000, 'lo_frequency': 6722538000, 'correction': [0.996755201369524, -0.1293857954442501, -0.12274250015616417, 1.0507034212350845]},
            {'intermediate_frequency': -100000000, 'lo_frequency': 6720538000, 'correction': [0.996538769453764, -0.12836674228310585, -0.12180546298623085, 1.0502191968262196]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6722538000, 'correction': [0.9922946915030479, -0.11378249153494835, -0.10804566368460655, 1.0449818968772888]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6577520000, 'correction': [0.9852600395679474, -0.06181402504444122, -0.05933065712451935, 1.0264994837343693]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 5180969000, 'correction': [1.0352607257664204, 0.16766245663166046, 0.16632725298404694, 1.0435713529586792]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 5490362000, 'correction': [0.9915705248713493, 0.08930196613073349, 0.08581626787781715, 1.031846284866333]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 5765376000, 'correction': [0.9748025089502335, 0.052087198942899704, 0.049076687544584274, 1.03459981828928]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6006013000, 'correction': [0.9776982106268406, 0.0017488859593868256, 0.0016708634793758392, 1.0233527086675167]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6302511000, 'correction': [0.9763297103345394, -0.01652040332555771, -0.0157257542014122, 1.0256653130054474]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6521660000, 'correction': [0.9819214791059494, -0.047666095197200775, -0.045639656484127045, 1.025519609451294]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6732203000, 'correction': [0.9923459030687809, -0.11637603864073753, -0.11034690961241722, 1.0465656518936157]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6457205000, 'correction': [0.9803989082574844, -0.03895088657736778, -0.03725859150290489, 1.0249288901686668]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6679572000, 'correction': [0.9898084290325642, -0.09804768487811089, -0.09346814081072807, 1.0383048616349697]},
            {'intermediate_frequency': -100000000, 'lo_frequency': 6555300000, 'correction': [0.9873037338256836, -0.0727810300886631, -0.06985706463456154, 1.028628721833229]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6681116000, 'correction': [0.9895871318876743, -0.0985848531126976, -0.09391149133443832, 1.038832426071167]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6458138000, 'correction': [0.9804397858679295, -0.03932541236281395, -0.03761684522032738, 1.0249716266989708]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6578991000, 'correction': [0.9850246943533421, -0.06182941794395447, -0.059316486120224, 1.0267550833523273]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 5070871000, 'correction': [1.04546457529068, 0.18754782155156136, 0.18641798943281174, 1.0518008582293987]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 5284592000, 'correction': [1.030311793088913, 0.14396827667951584, 0.14411773532629013, 1.0292432978749275]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 5498310000, 'correction': [0.9903644733130932, 0.08775787800550461, 0.08419113606214523, 1.0323210805654526]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 5708368000, 'correction': [0.9789737202227116, 0.06375371664762497, 0.060362450778484344, 1.033974140882492]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 5922768000, 'correction': [0.9751980826258659, 0.02507476508617401, 0.023787304759025574, 1.0279795452952385]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6137733000, 'correction': [0.9799221903085709, -0.009472683072090149, -0.00908990204334259, 1.0211872830986977]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6348757000, 'correction': [0.9779209643602371, -0.025752883404493332, -0.02456800267100334, 1.025084737688303]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6560354000, 'correction': [0.9841667450964451, -0.05810420215129852, -0.05571548640727997, 1.0263613797724247]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 5936760000, 'correction': [0.9753614589571953, 0.02406575158238411, 0.022841233760118484, 1.0276505537331104]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6202899000, 'correction': [0.9757312163710594, -0.018536772578954697, -0.017619337886571884, 1.0265373140573502]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6465096000, 'correction': [0.9804810471832752, -0.039699941873550415, -0.03797510266304016, 1.0250147618353367]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6728075000, 'correction': [0.9923943243920803, -0.11532949656248093, -0.1094345971941948, 1.04585150629282]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6492011000, 'correction': [0.981060903519392, -0.040678396821022034, -0.03894902765750885, 1.0246208235621452]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6756342000, 'correction': [0.9929599463939667, -0.11994742602109909, -0.11362241953611374, 1.048234935849905]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6462011000, 'correction': [0.9806873649358749, -0.039440423250198364, -0.037745267152786255, 1.024730458855629]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6693594000, 'correction': [0.9904900677502155, -0.10415462777018547, -0.09909633919596672, 1.0410487949848175]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 5900187000, 'correction': [0.9742775671184063, 0.03113945573568344, 0.029454313218593597, 1.0300180055201054]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6173481000, 'correction': [0.977913748472929, -0.017993032932281494, -0.01718193292617798, 1.0240776985883713]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6433254000, 'correction': [0.980220690369606, -0.03494720906019211, -0.033445172011852264, 1.024242825806141]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6663917000, 'correction': [0.988731786608696, -0.09097612276673317, -0.08685386553406715, 1.0356589630246162]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 5003780000, 'correction': [1.0474614091217518, 0.19149423763155937, 0.19037548825144768, 1.0536168590188026]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 5238110000, 'correction': [1.0328116305172443, 0.15576476231217384, 0.15527117624878883, 1.0360947996377945]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 5471023000, 'correction': [0.9951350092887878, 0.09036701172590256, 0.08741634339094162, 1.0287249870598316]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 5705465000, 'correction': [0.9791630133986473, 0.06450267136096954, 0.061079010367393494, 1.0340480208396912]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 5940914000, 'correction': [0.9756268449127674, 0.024560976773500443, 0.023322630673646927, 1.0274290479719639]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6172568000, 'correction': [0.9780054688453674, -0.017491046339273453, -0.016706649214029312, 1.0239240042865276]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6406483000, 'correction': [0.979586411267519, -0.02770814672112465, -0.026517245918512344, 1.0235800594091415]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6636660000, 'correction': [0.987319465726614, -0.07861162349581718, -0.07526959106326103, 1.031157273799181]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 4953780000, 'correction': [1.054568573832512, 0.20054659619927406, 0.20030193775892258, 1.0558566749095917]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 5137493000, 'correction': [1.03913040086627, 0.17623627558350563, 0.1748434640467167, 1.0474081635475159]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 5319018000, 'correction': [1.025615930557251, 0.13030487671494484, 0.13055962696671486, 1.0236147306859493]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 5504283000, 'correction': [0.989299688488245, 0.08658137917518616, 0.08293086290359497, 1.032847460359335]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 5689958000, 'correction': [0.9805289581418037, 0.06720037013292313, 0.06374997645616531, 1.0335989519953728]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 5872437000, 'correction': [0.9732900932431221, 0.04000900685787201, 0.037696585059165955, 1.0329946279525757]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6053324000, 'correction': [0.9785298220813274, 0.0037443414330482483, 0.0035834088921546936, 1.0224760212004185]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6235504000, 'correction': [0.9741485230624676, -0.014299776405096054, -0.013552334159612656, 1.0278750583529472]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6417476000, 'correction': [0.979539267718792, -0.030024640262126923, -0.02872016280889511, 1.0240302048623562]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6597917000, 'correction': [0.9858676344156265, -0.0665663480758667, -0.06386089324951172, 1.0276337340474129]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6425794000, 'correction': [0.9797745794057846, -0.03270875662565231, -0.03128766268491745, 1.0242762044072151]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6613646000, 'correction': [0.9862014837563038, -0.07083993032574654, -0.06789450719952583, 1.028985220938921]},
            {'intermediate_frequency': -100000000, 'lo_frequency': 6552600000, 'correction': [0.9873037338256836, -0.0727810300886631, -0.06985706463456154, 1.028628721833229]},
            {'intermediate_frequency': -100000000, 'lo_frequency': 6525320000, 'correction': [0.9848443865776062, -0.06486961618065834, -0.062142107635736465, 1.0280706584453583]},
            {'intermediate_frequency': 100000000, 'lo_frequency': 6509320000, 'correction': [0.9775788448750973, 0.0009994879364967346, 0.0009546652436256409, 1.0234773494303226]},
            {'intermediate_frequency': 100000000, 'lo_frequency': 6209320000, 'correction': [0.9779843427240849, 0.024999678134918213, 0.023855268955230713, 1.0249012000858784]},
            {'intermediate_frequency': 82000000, 'lo_frequency': 6149320000, 'correction': [0.9797676913440228, 0.02995474636554718, 0.028667286038398743, 1.0237694792449474]},
            {'intermediate_frequency': 104300000, 'lo_frequency': 6351000000, 'correction': [0.9763623885810375, 0.02153196558356285, 0.020486261695623398, 1.0261999815702438]},
            {'intermediate_frequency': 154300000, 'lo_frequency': 6301000000, 'correction': [0.9768762178719044, 0.04489506408572197, 0.04256917163729668, 1.0302507318556309]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6617349000, 'correction': [0.9863977245986462, -0.07183767855167389, -0.06885077059268951, 1.0291899740695953]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6474284462, 'correction': [0.9807426519691944, -0.03993966802954674, -0.03822305426001549, 1.0247882269322872]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6474284462, 'correction': [0.9807426519691944, -0.03993966802954674, -0.03822305426001549, 1.0247882269322872]},
            {'intermediate_frequency': -50825177, 'lo_frequency': 6475109639, 'correction': [0.9803893975913525, -0.040456563234329224, -0.038684695959091187, 1.0252939760684967]},
            {'intermediate_frequency': -50126997, 'lo_frequency': 6474411459, 'correction': [0.9803029000759125, -0.0402093380689621, -0.038443610072135925, 1.0253285467624664]},
            {'intermediate_frequency': -47903614, 'lo_frequency': 6472188076, 'correction': [0.9806873649358749, -0.039440423250198364, -0.037745267152786255, 1.024730458855629]},
            {'intermediate_frequency': -50304047, 'lo_frequency': 6474588509, 'correction': [0.9805087670683861, -0.039949625730514526, -0.03821393847465515, 1.0250437371432781]},
            {'intermediate_frequency': -40940637, 'lo_frequency': 6465225099, 'correction': [0.9802359864115715, -0.037421565502882004, -0.03579571470618248, 1.0247585698962212]},
            {'intermediate_frequency': -36832370, 'lo_frequency': 6461116832, 'correction': [0.979938168078661, -0.035944659262895584, -0.034372493624687195, 1.0247595980763435]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6462598467, 'correction': [0.9804534949362278, -0.039450254291296005, -0.03773626312613487, 1.0249859541654587]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6474014720, 'correction': [0.9805087670683861, -0.039949625730514526, -0.03821393847465515, 1.0250437371432781]},
            {'intermediate_frequency': 228589943, 'lo_frequency': 6195424777, 'correction': [0.9880342558026314, 0.06534403935074806, 0.06299487128853798, 1.024879451841116]},
            {'intermediate_frequency': 399606783, 'lo_frequency': 6024407937, 'correction': [0.99720349162817, 0.14623839035630226, 0.13725000992417336, 1.0625094585120678]},
            {'intermediate_frequency': -150000000, 'lo_frequency': 6195424777, 'correction': [0.9813192263245583, -0.048451002687215805, -0.04632335528731346, 1.026391550898552]},
            {'intermediate_frequency': -150000000, 'lo_frequency': 6024407937, 'correction': [0.9803640507161617, -0.03143681585788727, -0.030115023255348206, 1.0233936719596386]},
            {'intermediate_frequency': -150000000, 'lo_frequency': 5819163687, 'correction': [0.9708429351449013, 0.01208425685763359, 0.01137472316622734, 1.0314022786915302]},
            {'intermediate_frequency': -150000000, 'lo_frequency': 6574720675, 'correction': [0.9925557225942612, -0.09367139637470245, -0.08999593555927277, 1.0330919958651066]},
            {'intermediate_frequency': -150000000, 'lo_frequency': 6398675849, 'correction': [0.9845968261361122, -0.057826023548841476, -0.05550287291407585, 1.02580850943923]},
            {'intermediate_frequency': -150000000, 'lo_frequency': 6178619815, 'correction': [0.9813192263245583, -0.048451002687215805, -0.04632335528731346, 1.026391550898552]},
            {'intermediate_frequency': -120000000, 'lo_frequency': 6544720675, 'correction': [0.9879165031015873, -0.07577202841639519, -0.07272789999842644, 1.0292671360075474]},
            {'intermediate_frequency': -120000000, 'lo_frequency': 6148619815, 'correction': [0.979940589517355, -0.03195173293352127, -0.03057844191789627, 1.0239501409232616]},
            {'intermediate_frequency': -120000000, 'lo_frequency': 5840541369, 'correction': [0.9711980111896992, 0.020140428096055984, 0.018957871943712234, 1.0317795015871525]},
            {'intermediate_frequency': -120000000, 'lo_frequency': 5444440509, 'correction': [0.9933649562299252, 0.06679845973849297, 0.06506038829684258, 1.019902441650629]},
            {'intermediate_frequency': -120000000, 'lo_frequency': 4960317235, 'correction': [1.0454695709049702, 0.17437895759940147, 0.17523249611258507, 1.040377203375101]},
            {'intermediate_frequency': -120000000, 'lo_frequency': 4388171548, 'correction': [1.0029978305101395, 0.15548938140273094, 0.14659176766872406, 1.0638763345777988]},
            {'intermediate_frequency': -120000000, 'lo_frequency': 3728003448, 'correction': [1.015494029968977, 0.06778844073414803, 0.06894000247120857, 0.9985313974320889]},
            {'intermediate_frequency': -120000000, 'lo_frequency': 2979812935, 'correction': [0.99745062738657, 0.012975882738828659, 0.012903224676847458, 1.0030672699213028]},
            {'intermediate_frequency': -120000000, 'lo_frequency': 2143600008, 'correction': [1.1682398915290833, -0.28230468928813934, -0.31303589046001434, 1.053552035242319]},
            {'intermediate_frequency': 200000000, 'lo_frequency': 6224720675, 'correction': [0.9849939420819283, 0.058808378875255585, 0.05647330731153488, 1.0257217027246952]},
            {'intermediate_frequency': 200000000, 'lo_frequency': 5504720675, 'correction': [1.0182311050593853, 0.16732943058013916, 0.16092073917388916, 1.0587823055684566]},
            {'intermediate_frequency': 200000000, 'lo_frequency': 4944720675, 'correction': [1.1068267114460468, 0.294921875, 0.294921875, 1.1068267114460468]},
            {'intermediate_frequency': 200000000, 'lo_frequency': 5583790864, 'correction': [1.0149101801216602, 0.1630907580256462, 0.15638595074415207, 1.0584228932857513]},
            {'intermediate_frequency': 250000000, 'lo_frequency': 6176539346, 'correction': [0.9898693487048149, 0.07119742408394814, 0.06873837485909462, 1.025280974805355]},
            {'intermediate_frequency': -100000000, 'lo_frequency': 5868000000, 'correction': [1.1353193446993828, -0.2059326171875, -0.2332763671875, 1.0022416189312935]},
            {'intermediate_frequency': -100000000, 'lo_frequency': 6389000000, 'correction': [1.0034327507019043, -0.161285400390625, -0.151519775390625, 1.0681051537394524]},
            {'intermediate_frequency': 50000000, 'lo_frequency': 6000000000, 'correction': [1.061584122478962, -0.1363677978515625, -0.1451568603515625, 0.9973065592348576]},
            {'intermediate_frequency': -100000000, 'lo_frequency': 6523302920, 'correction': [0.9849618934094906, -0.06284231320023537, -0.060258809477090836, 1.0271906219422817]},
            {'intermediate_frequency': 250000000, 'lo_frequency': 5552050968, 'correction': [1.0206382237374783, 0.1765514723956585, 0.16930360719561577, 1.0643316134810448]},
            {'intermediate_frequency': 200000000, 'lo_frequency': 6226539346, 'correction': [0.9852294065058231, 0.058793745934963226, 0.05648680776357651, 1.0254664719104767]},
            {'intermediate_frequency': 200000000, 'lo_frequency': 5602050968, 'correction': [1.0132064558565617, 0.1601780503988266, 0.15344320237636566, 1.0576775781810284]},
            {'intermediate_frequency': 100000000, 'lo_frequency': 6294000000, 'correction': [0.9750760272145271, 0.029603037983179092, 0.028055701404809952, 1.028853714466095]},
            {'intermediate_frequency': -100000000, 'lo_frequency': 6525491202, 'correction': [0.9856077060103416, -0.06380802392959595, -0.06124454736709595, 1.0268617011606693]},
            {'intermediate_frequency': 290000000, 'lo_frequency': 6136539346, 'correction': [0.9983679875731468, 0.09717368334531784, 0.09427642077207565, 1.0290494039654732]},
            {'intermediate_frequency': 290000000, 'lo_frequency': 5616539346, 'correction': [1.0312877669930458, 0.18967142328619957, 0.18347826227545738, 1.066098053008318]},
            {'intermediate_frequency': 290000000, 'lo_frequency': 5096539346, 'correction': [1.1188673302531242, 0.3118908405303955, 0.3131115436553955, 1.1145052909851074]},
            {'intermediate_frequency': 290000000, 'lo_frequency': 4576539346, 'correction': [1.1583629325032234, 0.380952425301075, 0.3846908286213875, 1.1471060290932655]},
            {'intermediate_frequency': 290000000, 'lo_frequency': 5632539346, 'correction': [1.0308289490640163, 0.18867838010191917, 0.1825176440179348, 1.0656237490475178]},
            {'intermediate_frequency': 290000000, 'lo_frequency': 5128539346, 'correction': [1.1144964508712292, 0.3040935695171356, 0.3052837550640106, 1.1101514548063278]},
            {'intermediate_frequency': 290000000, 'lo_frequency': 4624539346, 'correction': [1.1544516310095787, 0.36434125900268555, 0.37007856369018555, 1.13655424118042]},
            {'intermediate_frequency': 290000000, 'lo_frequency': 6010000000, 'correction': [0.9981551170349121, 0.10870577022433281, 0.10474659129977226, 1.0358830690383911]},
            {'intermediate_frequency': 290000000, 'lo_frequency': 6090000000, 'correction': [0.9961284399032593, 0.0933229960501194, 0.09031987562775612, 1.0292495377361774]},
            {'intermediate_frequency': 290000000, 'lo_frequency': 5910000000, 'correction': [1.0040552951395512, 0.13466209173202515, 0.12912601232528687, 1.0471026226878166]},
            {'intermediate_frequency': 200000000, 'lo_frequency': 6129969799, 'correction': [0.9867832139134407, 0.06763772293925285, 0.06498376652598381, 1.027083732187748]},
            {'intermediate_frequency': 200000000, 'lo_frequency': 5929969799, 'correction': [0.9906096756458282, 0.10104914009571075, 0.09632940590381622, 1.0391453690826893]},
            {'intermediate_frequency': 200000000, 'lo_frequency': 5329969799, 'correction': [1.062568947672844, 0.21592574194073677, 0.215714979916811, 1.0636071227490902]},
            {'intermediate_frequency': 200000000, 'lo_frequency': 5129969799, 'correction': [1.0844337567687035, 0.26594697311520576, 0.2633625157177448, 1.095075637102127]},
            {'intermediate_frequency': 200000000, 'lo_frequency': 4529969799, 'correction': [1.1175559610128403, 0.3373394273221493, 0.330815102905035, 1.1395963616669178]},
            {'intermediate_frequency': 200000000, 'lo_frequency': 4329969799, 'correction': [1.032392043620348, 0.225799560546875, 0.212127685546875, 1.0989309065043926]},
            {'intermediate_frequency': 200000000, 'lo_frequency': 6100000000, 'correction': [0.9857261218130589, 0.0645567774772644, 0.061961330473423004, 1.0270163901150227]},
            {'intermediate_frequency': 200000000, 'lo_frequency': 5900000000, 'correction': [0.9912025965750217, 0.1092439591884613, 0.10378655791282654, 1.0433229319751263]},
            {'intermediate_frequency': 240000000, 'lo_frequency': 6088750287, 'correction': [0.9886813312768936, 0.07824504747986794, 0.07513821497559547, 1.0295615568757057]},
            {'intermediate_frequency': 300000000, 'lo_frequency': 6125791423, 'correction': [0.998919028788805, 0.1001112125813961, 0.09707897529006004, 1.0301200114190578]},
            {'intermediate_frequency': 300000000, 'lo_frequency': 5925791423, 'correction': [1.004887230694294, 0.1355920508503914, 0.1301446631550789, 1.0469481982290745]},
            {'intermediate_frequency': 240000000, 'lo_frequency': 6169044076, 'correction': [0.9899058230221272, 0.07258223742246628, 0.07004117220640182, 1.0258192047476768]},
            {'intermediate_frequency': 240000000, 'lo_frequency': 5582357496, 'correction': [1.0202825739979744, 0.1758088432252407, 0.16858118399977684, 1.0640256218612194]},
            {'intermediate_frequency': 200000000, 'lo_frequency': 6125791423, 'correction': [0.986666914075613, 0.0670149065554142, 0.06438538804650307, 1.02696268633008]},
            {'intermediate_frequency': 234208577, 'lo_frequency': 6125791423, 'correction': [0.9889937378466129, 0.0774589255452156, 0.07445592433214188, 1.0288824290037155]},
            {'intermediate_frequency': 74208577, 'lo_frequency': 6125791423, 'correction': [0.9810896888375282, 0.02891300991177559, 0.027751434594392776, 1.022154577076435]},
            {'intermediate_frequency': 40000000, 'lo_frequency': 6280000000, 'correction': [0.9747943617403507, 0.009274180978536606, 0.008804436773061752, 1.0268026776611805]},
            {'intermediate_frequency': 214208577, 'lo_frequency': 6125791423, 'correction': [0.9871930666267872, 0.07101859524846077, 0.06819869950413704, 1.0280117578804493]},
            {'intermediate_frequency': 200000000, 'lo_frequency': 5925791423, 'correction': [0.9899207577109337, 0.10163820534944534, 0.0967257097363472, 1.040196754038334]},
            {'intermediate_frequency': 290000000, 'lo_frequency': 6111661923, 'correction': [0.9963526800274849, 0.0922844223678112, 0.08940194174647331, 1.0284768976271152]},
            {'intermediate_frequency': -100000000, 'lo_frequency': 6485047515, 'correction': [0.9831880666315556, -0.05488967522978783, -0.0525817833840847, 1.0263416394591331]},
            {'intermediate_frequency': 200000000, 'lo_frequency': 6222629958, 'correction': [0.9853113479912281, 0.05929199978709221, 0.05696551129221916, 1.0255517587065697]},
            {'intermediate_frequency': 200000000, 'lo_frequency': 6221227134, 'correction': [0.9854651875793934, 0.059502579271793365, 0.05718177556991577, 1.0254616923630238]},
            {'intermediate_frequency': 200000000, 'lo_frequency': 6221505924, 'correction': [0.9847585968673229, 0.05882301926612854, 0.05645981431007385, 1.0259770527482033]},
            {'intermediate_frequency': -100000000.0, 'lo_frequency': 6207000000.0, 'correction': [1.0, 0.0, 0.0, 1.0]},
            {'intermediate_frequency': -100000000.0, 'lo_frequency': 6082000000.0, 'correction': [1.0, 0.0, 0.0, 1.0]},
            {'intermediate_frequency': -100000000.0, 'lo_frequency': 5667000000.0, 'correction': [1.0, 0.0, 0.0, 1.0]},
            {'intermediate_frequency': -100000000.0, 'lo_frequency': 5542000000.0, 'correction': [1.0, 0.0, 0.0, 1.0]},
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
            {'intermediate_frequency': 56520000, 'lo_frequency': 7206000000, 'correction': [0.9980175569653511, -0.10589710250496864, -0.10217723622918129, 1.0343514010310173]},
            {'intermediate_frequency': 56440000, 'lo_frequency': 7206000000, 'correction': [0.9978232942521572, -0.10591847449541092, -0.1021573469042778, 1.0345601588487625]},
            {'intermediate_frequency': 56760000, 'lo_frequency': 7206000000, 'correction': [0.998047448694706, -0.1058938167989254, -0.10218029841780663, 1.0343192927539349]},
            {'intermediate_frequency': 56890000, 'lo_frequency': 7206000000, 'correction': [0.9977668561041355, -0.10566820204257965, -0.10191906988620758, 1.034470096230507]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 7312490000, 'correction': [1.0003017038106918, -0.11257394403219223, -0.10868581384420395, 1.0360865332186222]},
            {'intermediate_frequency': -49600000, 'lo_frequency': 7312490000, 'correction': [1.0004660375416279, -0.11229755356907845, -0.10847188904881477, 1.0357511937618256]},
            {'intermediate_frequency': -1000000, 'lo_frequency': 7080000000, 'correction': [0.9985253363847733, -0.09309209883213043, -0.09053720533847809, 1.0267029888927937]},
            {'intermediate_frequency': 50000000, 'lo_frequency': 7029000000, 'correction': [0.9924078099429607, -0.09164418280124664, -0.0881127268075943, 1.032182365655899]},
            {'intermediate_frequency': 50000000, 'lo_frequency': 7079000000, 'correction': [0.9926108457148075, -0.09341064840555191, -0.08976731449365616, 1.0328973680734634]},
            {'intermediate_frequency': 49500000, 'lo_frequency': 7079000000, 'correction': [0.9927930608391762, -0.09364809468388557, -0.09001745656132698, 1.0328349880874157]},
            {'intermediate_frequency': -51000000, 'lo_frequency': 7312490000, 'correction': [1.0004660375416279, -0.11229755356907845, -0.10847188904881477, 1.0357511937618256]},
            {'intermediate_frequency': -49200000, 'lo_frequency': 7312490000, 'correction': [1.0005793273448944, -0.11267022415995598, -0.10883186385035515, 1.035868477076292]},
            {'intermediate_frequency': -49500000, 'lo_frequency': 7312490000, 'correction': [1.0004660375416279, -0.11229755356907845, -0.10847188904881477, 1.0357511937618256]},
            {'intermediate_frequency': 100000000, 'lo_frequency': 7100000000, 'correction': [0.9932862967252731, -0.09462080895900726, -0.09099684655666351, 1.032844066619873]},
            {'intermediate_frequency': 56000000, 'lo_frequency': 7200000000, 'correction': [0.9974122568964958, -0.10442504659295082, -0.10072002187371254, 1.0341024547815323]},
            {'intermediate_frequency': 63200000, 'lo_frequency': 7200000000, 'correction': [0.9974122568964958, -0.10442504659295082, -0.10072002187371254, 1.0341024547815323]},
            {'intermediate_frequency': 57200000, 'lo_frequency': 7206000000, 'correction': [0.9976956285536289, -0.1054195687174797, -0.1016792580485344, 1.0343962460756302]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 7313380000, 'correction': [1.0004471875727177, -0.11223544180393219, -0.10841189324855804, 1.035731676965952]},
            {'intermediate_frequency': -49820000, 'lo_frequency': 7313200000, 'correction': [1.0003161393105984, -0.11231497675180435, -0.10845563560724258, 1.0359119027853012]},
            {'intermediate_frequency': -49940000, 'lo_frequency': 7313320000, 'correction': [1.0004283487796783, -0.11217333003878593, -0.10835189744830132, 1.0357121750712395]},
            {'intermediate_frequency': -49833478, 'lo_frequency': 7313213478, 'correction': [1.0004060715436935, -0.11230452358722687, -0.10846538841724396, 1.0358154736459255]},
            {'intermediate_frequency': -49983478, 'lo_frequency': 7313363478, 'correction': [1.00034611672163, -0.11231149360537529, -0.10845888778567314, 1.0358797572553158]},
            {'intermediate_frequency': -49783478, 'lo_frequency': 7313163478, 'correction': [1.00034611672163, -0.11231149360537529, -0.10845888778567314, 1.0358797572553158]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 7313113478, 'correction': [1.0004660375416279, -0.11229755356907845, -0.10847188904881477, 1.0357511937618256]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 7313513478, 'correction': [0.9310230351984501, 0.050823211669921875, 0.043498992919921875, 1.0877856612205505]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 6267000000, 'correction': [0.9793037101626396, -0.1138143539428711, -0.1052694320678711, 1.0587956719100475]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 7180000000, 'correction': [0.9293350912630558, 0.03388214111328125, 0.02899932861328125, 1.085813507437706]},
            {'intermediate_frequency': -49700000, 'lo_frequency': 7313513478, 'correction': [1.00037731975317, -0.11282245069742203, -0.10892573744058609, 1.0361648574471474]},
            {'intermediate_frequency': 50000000, 'lo_frequency': 6000000000, 'correction': [1.034758448600769, -0.15625, -0.15625, 1.034758448600769]},
            {'intermediate_frequency': -50200000, 'lo_frequency': 7313513478, 'correction': [1.0001375935971737, -0.11285046860575676, -0.10889963433146477, 1.0364221781492233]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 7313263478, 'correction': [1.00037731975317, -0.11282245069742203, -0.10892573744058609, 1.0361648574471474]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 7313413478, 'correction': [1.0003017038106918, -0.11257394403219223, -0.10868581384420395, 1.0360865332186222]},
            {'intermediate_frequency': -50000000, 'lo_frequency': 7313013478, 'correction': [1.0001375935971737, -0.11285046860575676, -0.10889963433146477, 1.0364221781492233]},
            {'intermediate_frequency': -50000000.0, 'lo_frequency': 7049000000.0, 'correction': [1.0, 0.0, 0.0, 1.0]},
            {'intermediate_frequency': -50000000.0, 'lo_frequency': 6925000000.0, 'correction': [1.0, 0.0, 0.0, 1.0]},
            {'intermediate_frequency': -50000000.0, 'lo_frequency': 6162000000.0, 'correction': [1.0, 0.0, 0.0, 1.0]},
            {'intermediate_frequency': -50000000.0, 'lo_frequency': 6068000000.0, 'correction': [1.0, 0.0, 0.0, 1.0]},
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
                    "offset": -0.001953125,
                    "delay": 0,
                    "shareable": False,
                },
                "2": {
                    "offset": -0.044921875,
                    "delay": 0,
                    "shareable": False,
                },
                "3": {
                    "offset": 0.001953125,
                    "delay": 0,
                    "shareable": False,
                },
                "4": {
                    "offset": -0.00390625,
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
                    "offset": 0.011262000000000003,
                    "gain_db": 0,
                    "shareable": False,
                },
                "2": {
                    "offset": 0.016203,
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
            "intermediate_frequency": 50000000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q0",
            },
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "mixer": "octave_octave1_1",
                "lo_frequency": 7313013478.0,
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
                "lo_frequency": 7180000000.0,
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
                "lo_frequency": 7049000000.0,
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
                "lo_frequency": 6925000000.0,
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
                "lo_frequency": 6267000000.0,
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
                "lo_frequency": 6162000000.0,
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
                "lo_frequency": 6068000000.0,
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
            "intermediate_frequency": 50000000.0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q0",
            },
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "mixer": "octave_octave1_1",
                "lo_frequency": 7313013478.0,
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
                "lo_frequency": 7180000000.0,
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
                "lo_frequency": 7049000000.0,
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
                "lo_frequency": 6925000000.0,
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
                "lo_frequency": 6267000000.0,
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
                "lo_frequency": 6162000000.0,
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
                "lo_frequency": 6068000000.0,
            },
        },
        "q0": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 200000000.0,
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
                "lo_frequency": 6221505924.0,
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
                "lo_frequency": 6389000000.0,
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
                "lo_frequency": 6207000000.0,
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
                "lo_frequency": 6082000000.0,
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
                "lo_frequency": 5868000000.0,
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
                "lo_frequency": 5667000000.0,
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
                "lo_frequency": 5542000000.0,
            },
        },
        "flux0": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "operations": {
                "const": "const_flux_pulse0",
                "baked_Op_0": "flux0_baked_pulse_0",
                "baked_Op_1": "flux0_baked_pulse_1",
                "baked_Op_2": "flux0_baked_pulse_2",
                "baked_Op_3": "flux0_baked_pulse_3",
                "baked_Op_4": "flux0_baked_pulse_4",
                "baked_Op_5": "flux0_baked_pulse_5",
                "baked_Op_6": "flux0_baked_pulse_6",
                "baked_Op_7": "flux0_baked_pulse_7",
                "baked_Op_8": "flux0_baked_pulse_8",
                "baked_Op_9": "flux0_baked_pulse_9",
                "baked_Op_10": "flux0_baked_pulse_10",
                "baked_Op_11": "flux0_baked_pulse_11",
                "baked_Op_12": "flux0_baked_pulse_12",
                "baked_Op_13": "flux0_baked_pulse_13",
                "baked_Op_14": "flux0_baked_pulse_14",
                "baked_Op_15": "flux0_baked_pulse_15",
                "baked_Op_16": "flux0_baked_pulse_16",
                "baked_Op_17": "flux0_baked_pulse_17",
                "baked_Op_18": "flux0_baked_pulse_18",
                "baked_Op_19": "flux0_baked_pulse_19",
                "baked_Op_20": "flux0_baked_pulse_20",
                "baked_Op_21": "flux0_baked_pulse_21",
                "baked_Op_22": "flux0_baked_pulse_22",
                "baked_Op_23": "flux0_baked_pulse_23",
                "baked_Op_24": "flux0_baked_pulse_24",
                "baked_Op_25": "flux0_baked_pulse_25",
                "baked_Op_26": "flux0_baked_pulse_26",
                "baked_Op_27": "flux0_baked_pulse_27",
                "baked_Op_28": "flux0_baked_pulse_28",
                "baked_Op_29": "flux0_baked_pulse_29",
                "baked_Op_30": "flux0_baked_pulse_30",
                "baked_Op_31": "flux0_baked_pulse_31",
                "baked_Op_32": "flux0_baked_pulse_32",
                "baked_Op_33": "flux0_baked_pulse_33",
                "baked_Op_34": "flux0_baked_pulse_34",
                "baked_Op_35": "flux0_baked_pulse_35",
                "baked_Op_36": "flux0_baked_pulse_36",
                "baked_Op_37": "flux0_baked_pulse_37",
                "baked_Op_38": "flux0_baked_pulse_38",
                "baked_Op_39": "flux0_baked_pulse_39",
                "baked_Op_40": "flux0_baked_pulse_40",
                "baked_Op_41": "flux0_baked_pulse_41",
                "baked_Op_42": "flux0_baked_pulse_42",
                "baked_Op_43": "flux0_baked_pulse_43",
                "baked_Op_44": "flux0_baked_pulse_44",
                "baked_Op_45": "flux0_baked_pulse_45",
                "baked_Op_46": "flux0_baked_pulse_46",
                "baked_Op_47": "flux0_baked_pulse_47",
                "baked_Op_48": "flux0_baked_pulse_48",
                "baked_Op_49": "flux0_baked_pulse_49",
                "baked_Op_50": "flux0_baked_pulse_50",
                "baked_Op_51": "flux0_baked_pulse_51",
                "baked_Op_52": "flux0_baked_pulse_52",
                "baked_Op_53": "flux0_baked_pulse_53",
                "baked_Op_54": "flux0_baked_pulse_54",
                "baked_Op_55": "flux0_baked_pulse_55",
                "baked_Op_56": "flux0_baked_pulse_56",
                "baked_Op_57": "flux0_baked_pulse_57",
                "baked_Op_58": "flux0_baked_pulse_58",
                "baked_Op_59": "flux0_baked_pulse_59",
                "baked_Op_60": "flux0_baked_pulse_60",
                "baked_Op_61": "flux0_baked_pulse_61",
                "baked_Op_62": "flux0_baked_pulse_62",
                "baked_Op_63": "flux0_baked_pulse_63",
                "baked_Op_64": "flux0_baked_pulse_64",
                "baked_Op_65": "flux0_baked_pulse_65",
                "baked_Op_66": "flux0_baked_pulse_66",
                "baked_Op_67": "flux0_baked_pulse_67",
                "baked_Op_68": "flux0_baked_pulse_68",
                "baked_Op_69": "flux0_baked_pulse_69",
                "baked_Op_70": "flux0_baked_pulse_70",
                "baked_Op_71": "flux0_baked_pulse_71",
                "baked_Op_72": "flux0_baked_pulse_72",
                "baked_Op_73": "flux0_baked_pulse_73",
                "baked_Op_74": "flux0_baked_pulse_74",
                "baked_Op_75": "flux0_baked_pulse_75",
                "baked_Op_76": "flux0_baked_pulse_76",
                "baked_Op_77": "flux0_baked_pulse_77",
                "baked_Op_78": "flux0_baked_pulse_78",
                "baked_Op_79": "flux0_baked_pulse_79",
                "baked_Op_80": "flux0_baked_pulse_80",
                "baked_Op_81": "flux0_baked_pulse_81",
                "baked_Op_82": "flux0_baked_pulse_82",
                "baked_Op_83": "flux0_baked_pulse_83",
                "baked_Op_84": "flux0_baked_pulse_84",
                "baked_Op_85": "flux0_baked_pulse_85",
                "baked_Op_86": "flux0_baked_pulse_86",
                "baked_Op_87": "flux0_baked_pulse_87",
                "baked_Op_88": "flux0_baked_pulse_88",
                "baked_Op_89": "flux0_baked_pulse_89",
                "baked_Op_90": "flux0_baked_pulse_90",
                "baked_Op_91": "flux0_baked_pulse_91",
                "baked_Op_92": "flux0_baked_pulse_92",
                "baked_Op_93": "flux0_baked_pulse_93",
                "baked_Op_94": "flux0_baked_pulse_94",
                "baked_Op_95": "flux0_baked_pulse_95",
                "baked_Op_96": "flux0_baked_pulse_96",
                "baked_Op_97": "flux0_baked_pulse_97",
                "baked_Op_98": "flux0_baked_pulse_98",
                "baked_Op_99": "flux0_baked_pulse_99",
                "baked_Op_100": "flux0_baked_pulse_100",
                "baked_Op_101": "flux0_baked_pulse_101",
                "baked_Op_102": "flux0_baked_pulse_102",
                "baked_Op_103": "flux0_baked_pulse_103",
                "baked_Op_104": "flux0_baked_pulse_104",
                "baked_Op_105": "flux0_baked_pulse_105",
                "baked_Op_106": "flux0_baked_pulse_106",
                "baked_Op_107": "flux0_baked_pulse_107",
                "baked_Op_108": "flux0_baked_pulse_108",
                "baked_Op_109": "flux0_baked_pulse_109",
                "baked_Op_110": "flux0_baked_pulse_110",
                "baked_Op_111": "flux0_baked_pulse_111",
                "baked_Op_112": "flux0_baked_pulse_112",
                "baked_Op_113": "flux0_baked_pulse_113",
                "baked_Op_114": "flux0_baked_pulse_114",
                "baked_Op_115": "flux0_baked_pulse_115",
                "baked_Op_116": "flux0_baked_pulse_116",
                "baked_Op_117": "flux0_baked_pulse_117",
                "baked_Op_118": "flux0_baked_pulse_118",
                "baked_Op_119": "flux0_baked_pulse_119",
                "baked_Op_120": "flux0_baked_pulse_120",
                "baked_Op_121": "flux0_baked_pulse_121",
                "baked_Op_122": "flux0_baked_pulse_122",
                "baked_Op_123": "flux0_baked_pulse_123",
                "baked_Op_124": "flux0_baked_pulse_124",
                "baked_Op_125": "flux0_baked_pulse_125",
                "baked_Op_126": "flux0_baked_pulse_126",
                "baked_Op_127": "flux0_baked_pulse_127",
                "baked_Op_128": "flux0_baked_pulse_128",
                "baked_Op_129": "flux0_baked_pulse_129",
                "baked_Op_130": "flux0_baked_pulse_130",
                "baked_Op_131": "flux0_baked_pulse_131",
                "baked_Op_132": "flux0_baked_pulse_132",
                "baked_Op_133": "flux0_baked_pulse_133",
                "baked_Op_134": "flux0_baked_pulse_134",
                "baked_Op_135": "flux0_baked_pulse_135",
                "baked_Op_136": "flux0_baked_pulse_136",
                "baked_Op_137": "flux0_baked_pulse_137",
                "baked_Op_138": "flux0_baked_pulse_138",
                "baked_Op_139": "flux0_baked_pulse_139",
                "baked_Op_140": "flux0_baked_pulse_140",
                "baked_Op_141": "flux0_baked_pulse_141",
                "baked_Op_142": "flux0_baked_pulse_142",
                "baked_Op_143": "flux0_baked_pulse_143",
                "baked_Op_144": "flux0_baked_pulse_144",
                "baked_Op_145": "flux0_baked_pulse_145",
                "baked_Op_146": "flux0_baked_pulse_146",
                "baked_Op_147": "flux0_baked_pulse_147",
                "baked_Op_148": "flux0_baked_pulse_148",
                "baked_Op_149": "flux0_baked_pulse_149",
                "baked_Op_150": "flux0_baked_pulse_150",
                "baked_Op_151": "flux0_baked_pulse_151",
                "baked_Op_152": "flux0_baked_pulse_152",
                "baked_Op_153": "flux0_baked_pulse_153",
                "baked_Op_154": "flux0_baked_pulse_154",
                "baked_Op_155": "flux0_baked_pulse_155",
                "baked_Op_156": "flux0_baked_pulse_156",
                "baked_Op_157": "flux0_baked_pulse_157",
                "baked_Op_158": "flux0_baked_pulse_158",
                "baked_Op_159": "flux0_baked_pulse_159",
                "baked_Op_160": "flux0_baked_pulse_160",
                "baked_Op_161": "flux0_baked_pulse_161",
                "baked_Op_162": "flux0_baked_pulse_162",
                "baked_Op_163": "flux0_baked_pulse_163",
                "baked_Op_164": "flux0_baked_pulse_164",
                "baked_Op_165": "flux0_baked_pulse_165",
                "baked_Op_166": "flux0_baked_pulse_166",
                "baked_Op_167": "flux0_baked_pulse_167",
                "baked_Op_168": "flux0_baked_pulse_168",
                "baked_Op_169": "flux0_baked_pulse_169",
                "baked_Op_170": "flux0_baked_pulse_170",
                "baked_Op_171": "flux0_baked_pulse_171",
                "baked_Op_172": "flux0_baked_pulse_172",
                "baked_Op_173": "flux0_baked_pulse_173",
                "baked_Op_174": "flux0_baked_pulse_174",
                "baked_Op_175": "flux0_baked_pulse_175",
                "baked_Op_176": "flux0_baked_pulse_176",
                "baked_Op_177": "flux0_baked_pulse_177",
                "baked_Op_178": "flux0_baked_pulse_178",
                "baked_Op_179": "flux0_baked_pulse_179",
                "baked_Op_180": "flux0_baked_pulse_180",
                "baked_Op_181": "flux0_baked_pulse_181",
                "baked_Op_182": "flux0_baked_pulse_182",
                "baked_Op_183": "flux0_baked_pulse_183",
                "baked_Op_184": "flux0_baked_pulse_184",
                "baked_Op_185": "flux0_baked_pulse_185",
                "baked_Op_186": "flux0_baked_pulse_186",
                "baked_Op_187": "flux0_baked_pulse_187",
                "baked_Op_188": "flux0_baked_pulse_188",
                "baked_Op_189": "flux0_baked_pulse_189",
                "baked_Op_190": "flux0_baked_pulse_190",
                "baked_Op_191": "flux0_baked_pulse_191",
                "baked_Op_192": "flux0_baked_pulse_192",
                "baked_Op_193": "flux0_baked_pulse_193",
                "baked_Op_194": "flux0_baked_pulse_194",
                "baked_Op_195": "flux0_baked_pulse_195",
                "baked_Op_196": "flux0_baked_pulse_196",
                "baked_Op_197": "flux0_baked_pulse_197",
                "baked_Op_198": "flux0_baked_pulse_198",
                "baked_Op_199": "flux0_baked_pulse_199",
                "baked_Op_200": "flux0_baked_pulse_200",
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
            "length": 100,
            "waveforms": {
                "I": "pi_wf0",
                "Q": "zero_wf",
            },
            "operation": "control",
        },
        "pi_pulse1": {
            "length": 20,
            "waveforms": {
                "I": "pi_wf1",
                "Q": "zero_wf",
            },
            "operation": "control",
        },
        "pi_pulse2": {
            "length": 20,
            "waveforms": {
                "I": "pi_wf2",
                "Q": "zero_wf",
            },
            "operation": "control",
        },
        "pi_pulse3": {
            "length": 20,
            "waveforms": {
                "I": "pi_wf3",
                "Q": "zero_wf",
            },
            "operation": "control",
        },
        "pi_pulse4": {
            "length": 20,
            "waveforms": {
                "I": "pi_wf4",
                "Q": "zero_wf",
            },
            "operation": "control",
        },
        "pi_pulse5": {
            "length": 20,
            "waveforms": {
                "I": "pi_wf5",
                "Q": "zero_wf",
            },
            "operation": "control",
        },
        "pi_pulse6": {
            "length": 20,
            "waveforms": {
                "I": "pi_wf6",
                "Q": "zero_wf",
            },
            "operation": "control",
        },
        "pi_over_two_pulse0": {
            "length": 100,
            "waveforms": {
                "I": "pi_over_two_wf0",
                "Q": "zero_wf",
            },
            "operation": "control",
        },
        "pi_over_two_pulse1": {
            "length": 20,
            "waveforms": {
                "I": "pi_over_two_wf1",
                "Q": "zero_wf",
            },
            "operation": "control",
        },
        "pi_over_two_pulse2": {
            "length": 20,
            "waveforms": {
                "I": "pi_over_two_wf2",
                "Q": "zero_wf",
            },
            "operation": "control",
        },
        "pi_over_two_pulse3": {
            "length": 20,
            "waveforms": {
                "I": "pi_over_two_wf3",
                "Q": "zero_wf",
            },
            "operation": "control",
        },
        "pi_over_two_pulse4": {
            "length": 20,
            "waveforms": {
                "I": "pi_over_two_wf4",
                "Q": "zero_wf",
            },
            "operation": "control",
        },
        "pi_over_two_pulse5": {
            "length": 20,
            "waveforms": {
                "I": "pi_over_two_wf5",
                "Q": "zero_wf",
            },
            "operation": "control",
        },
        "pi_over_two_pulse6": {
            "length": 20,
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
        "flux0_baked_pulse_0": {
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_0",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_1": {
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_1",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_2": {
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_2",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_3": {
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_3",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_4": {
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_4",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_5": {
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_5",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_6": {
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_6",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_7": {
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_7",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_8": {
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_8",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_9": {
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_9",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_10": {
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_10",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_11": {
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_11",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_12": {
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_12",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_13": {
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_13",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_14": {
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_14",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_15": {
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_15",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_16": {
            "length": 16,
            "waveforms": {
                "single": "flux0_baked_wf_16",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_17": {
            "length": 20,
            "waveforms": {
                "single": "flux0_baked_wf_17",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_18": {
            "length": 20,
            "waveforms": {
                "single": "flux0_baked_wf_18",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_19": {
            "length": 20,
            "waveforms": {
                "single": "flux0_baked_wf_19",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_20": {
            "length": 20,
            "waveforms": {
                "single": "flux0_baked_wf_20",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_21": {
            "length": 24,
            "waveforms": {
                "single": "flux0_baked_wf_21",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_22": {
            "length": 24,
            "waveforms": {
                "single": "flux0_baked_wf_22",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_23": {
            "length": 24,
            "waveforms": {
                "single": "flux0_baked_wf_23",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_24": {
            "length": 24,
            "waveforms": {
                "single": "flux0_baked_wf_24",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_25": {
            "length": 28,
            "waveforms": {
                "single": "flux0_baked_wf_25",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_26": {
            "length": 28,
            "waveforms": {
                "single": "flux0_baked_wf_26",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_27": {
            "length": 28,
            "waveforms": {
                "single": "flux0_baked_wf_27",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_28": {
            "length": 28,
            "waveforms": {
                "single": "flux0_baked_wf_28",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_29": {
            "length": 32,
            "waveforms": {
                "single": "flux0_baked_wf_29",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_30": {
            "length": 32,
            "waveforms": {
                "single": "flux0_baked_wf_30",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_31": {
            "length": 32,
            "waveforms": {
                "single": "flux0_baked_wf_31",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_32": {
            "length": 32,
            "waveforms": {
                "single": "flux0_baked_wf_32",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_33": {
            "length": 36,
            "waveforms": {
                "single": "flux0_baked_wf_33",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_34": {
            "length": 36,
            "waveforms": {
                "single": "flux0_baked_wf_34",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_35": {
            "length": 36,
            "waveforms": {
                "single": "flux0_baked_wf_35",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_36": {
            "length": 36,
            "waveforms": {
                "single": "flux0_baked_wf_36",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_37": {
            "length": 40,
            "waveforms": {
                "single": "flux0_baked_wf_37",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_38": {
            "length": 40,
            "waveforms": {
                "single": "flux0_baked_wf_38",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_39": {
            "length": 40,
            "waveforms": {
                "single": "flux0_baked_wf_39",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_40": {
            "length": 40,
            "waveforms": {
                "single": "flux0_baked_wf_40",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_41": {
            "length": 44,
            "waveforms": {
                "single": "flux0_baked_wf_41",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_42": {
            "length": 44,
            "waveforms": {
                "single": "flux0_baked_wf_42",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_43": {
            "length": 44,
            "waveforms": {
                "single": "flux0_baked_wf_43",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_44": {
            "length": 44,
            "waveforms": {
                "single": "flux0_baked_wf_44",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_45": {
            "length": 48,
            "waveforms": {
                "single": "flux0_baked_wf_45",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_46": {
            "length": 48,
            "waveforms": {
                "single": "flux0_baked_wf_46",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_47": {
            "length": 48,
            "waveforms": {
                "single": "flux0_baked_wf_47",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_48": {
            "length": 48,
            "waveforms": {
                "single": "flux0_baked_wf_48",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_49": {
            "length": 52,
            "waveforms": {
                "single": "flux0_baked_wf_49",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_50": {
            "length": 52,
            "waveforms": {
                "single": "flux0_baked_wf_50",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_51": {
            "length": 52,
            "waveforms": {
                "single": "flux0_baked_wf_51",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_52": {
            "length": 52,
            "waveforms": {
                "single": "flux0_baked_wf_52",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_53": {
            "length": 56,
            "waveforms": {
                "single": "flux0_baked_wf_53",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_54": {
            "length": 56,
            "waveforms": {
                "single": "flux0_baked_wf_54",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_55": {
            "length": 56,
            "waveforms": {
                "single": "flux0_baked_wf_55",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_56": {
            "length": 56,
            "waveforms": {
                "single": "flux0_baked_wf_56",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_57": {
            "length": 60,
            "waveforms": {
                "single": "flux0_baked_wf_57",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_58": {
            "length": 60,
            "waveforms": {
                "single": "flux0_baked_wf_58",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_59": {
            "length": 60,
            "waveforms": {
                "single": "flux0_baked_wf_59",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_60": {
            "length": 60,
            "waveforms": {
                "single": "flux0_baked_wf_60",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_61": {
            "length": 64,
            "waveforms": {
                "single": "flux0_baked_wf_61",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_62": {
            "length": 64,
            "waveforms": {
                "single": "flux0_baked_wf_62",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_63": {
            "length": 64,
            "waveforms": {
                "single": "flux0_baked_wf_63",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_64": {
            "length": 64,
            "waveforms": {
                "single": "flux0_baked_wf_64",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_65": {
            "length": 68,
            "waveforms": {
                "single": "flux0_baked_wf_65",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_66": {
            "length": 68,
            "waveforms": {
                "single": "flux0_baked_wf_66",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_67": {
            "length": 68,
            "waveforms": {
                "single": "flux0_baked_wf_67",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_68": {
            "length": 68,
            "waveforms": {
                "single": "flux0_baked_wf_68",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_69": {
            "length": 72,
            "waveforms": {
                "single": "flux0_baked_wf_69",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_70": {
            "length": 72,
            "waveforms": {
                "single": "flux0_baked_wf_70",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_71": {
            "length": 72,
            "waveforms": {
                "single": "flux0_baked_wf_71",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_72": {
            "length": 72,
            "waveforms": {
                "single": "flux0_baked_wf_72",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_73": {
            "length": 76,
            "waveforms": {
                "single": "flux0_baked_wf_73",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_74": {
            "length": 76,
            "waveforms": {
                "single": "flux0_baked_wf_74",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_75": {
            "length": 76,
            "waveforms": {
                "single": "flux0_baked_wf_75",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_76": {
            "length": 76,
            "waveforms": {
                "single": "flux0_baked_wf_76",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_77": {
            "length": 80,
            "waveforms": {
                "single": "flux0_baked_wf_77",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_78": {
            "length": 80,
            "waveforms": {
                "single": "flux0_baked_wf_78",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_79": {
            "length": 80,
            "waveforms": {
                "single": "flux0_baked_wf_79",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_80": {
            "length": 80,
            "waveforms": {
                "single": "flux0_baked_wf_80",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_81": {
            "length": 84,
            "waveforms": {
                "single": "flux0_baked_wf_81",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_82": {
            "length": 84,
            "waveforms": {
                "single": "flux0_baked_wf_82",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_83": {
            "length": 84,
            "waveforms": {
                "single": "flux0_baked_wf_83",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_84": {
            "length": 84,
            "waveforms": {
                "single": "flux0_baked_wf_84",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_85": {
            "length": 88,
            "waveforms": {
                "single": "flux0_baked_wf_85",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_86": {
            "length": 88,
            "waveforms": {
                "single": "flux0_baked_wf_86",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_87": {
            "length": 88,
            "waveforms": {
                "single": "flux0_baked_wf_87",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_88": {
            "length": 88,
            "waveforms": {
                "single": "flux0_baked_wf_88",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_89": {
            "length": 92,
            "waveforms": {
                "single": "flux0_baked_wf_89",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_90": {
            "length": 92,
            "waveforms": {
                "single": "flux0_baked_wf_90",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_91": {
            "length": 92,
            "waveforms": {
                "single": "flux0_baked_wf_91",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_92": {
            "length": 92,
            "waveforms": {
                "single": "flux0_baked_wf_92",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_93": {
            "length": 96,
            "waveforms": {
                "single": "flux0_baked_wf_93",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_94": {
            "length": 96,
            "waveforms": {
                "single": "flux0_baked_wf_94",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_95": {
            "length": 96,
            "waveforms": {
                "single": "flux0_baked_wf_95",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_96": {
            "length": 96,
            "waveforms": {
                "single": "flux0_baked_wf_96",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_97": {
            "length": 100,
            "waveforms": {
                "single": "flux0_baked_wf_97",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_98": {
            "length": 100,
            "waveforms": {
                "single": "flux0_baked_wf_98",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_99": {
            "length": 100,
            "waveforms": {
                "single": "flux0_baked_wf_99",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_100": {
            "length": 100,
            "waveforms": {
                "single": "flux0_baked_wf_100",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_101": {
            "length": 104,
            "waveforms": {
                "single": "flux0_baked_wf_101",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_102": {
            "length": 104,
            "waveforms": {
                "single": "flux0_baked_wf_102",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_103": {
            "length": 104,
            "waveforms": {
                "single": "flux0_baked_wf_103",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_104": {
            "length": 104,
            "waveforms": {
                "single": "flux0_baked_wf_104",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_105": {
            "length": 108,
            "waveforms": {
                "single": "flux0_baked_wf_105",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_106": {
            "length": 108,
            "waveforms": {
                "single": "flux0_baked_wf_106",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_107": {
            "length": 108,
            "waveforms": {
                "single": "flux0_baked_wf_107",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_108": {
            "length": 108,
            "waveforms": {
                "single": "flux0_baked_wf_108",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_109": {
            "length": 112,
            "waveforms": {
                "single": "flux0_baked_wf_109",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_110": {
            "length": 112,
            "waveforms": {
                "single": "flux0_baked_wf_110",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_111": {
            "length": 112,
            "waveforms": {
                "single": "flux0_baked_wf_111",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_112": {
            "length": 112,
            "waveforms": {
                "single": "flux0_baked_wf_112",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_113": {
            "length": 116,
            "waveforms": {
                "single": "flux0_baked_wf_113",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_114": {
            "length": 116,
            "waveforms": {
                "single": "flux0_baked_wf_114",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_115": {
            "length": 116,
            "waveforms": {
                "single": "flux0_baked_wf_115",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_116": {
            "length": 116,
            "waveforms": {
                "single": "flux0_baked_wf_116",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_117": {
            "length": 120,
            "waveforms": {
                "single": "flux0_baked_wf_117",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_118": {
            "length": 120,
            "waveforms": {
                "single": "flux0_baked_wf_118",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_119": {
            "length": 120,
            "waveforms": {
                "single": "flux0_baked_wf_119",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_120": {
            "length": 120,
            "waveforms": {
                "single": "flux0_baked_wf_120",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_121": {
            "length": 124,
            "waveforms": {
                "single": "flux0_baked_wf_121",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_122": {
            "length": 124,
            "waveforms": {
                "single": "flux0_baked_wf_122",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_123": {
            "length": 124,
            "waveforms": {
                "single": "flux0_baked_wf_123",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_124": {
            "length": 124,
            "waveforms": {
                "single": "flux0_baked_wf_124",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_125": {
            "length": 128,
            "waveforms": {
                "single": "flux0_baked_wf_125",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_126": {
            "length": 128,
            "waveforms": {
                "single": "flux0_baked_wf_126",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_127": {
            "length": 128,
            "waveforms": {
                "single": "flux0_baked_wf_127",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_128": {
            "length": 128,
            "waveforms": {
                "single": "flux0_baked_wf_128",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_129": {
            "length": 132,
            "waveforms": {
                "single": "flux0_baked_wf_129",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_130": {
            "length": 132,
            "waveforms": {
                "single": "flux0_baked_wf_130",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_131": {
            "length": 132,
            "waveforms": {
                "single": "flux0_baked_wf_131",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_132": {
            "length": 132,
            "waveforms": {
                "single": "flux0_baked_wf_132",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_133": {
            "length": 136,
            "waveforms": {
                "single": "flux0_baked_wf_133",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_134": {
            "length": 136,
            "waveforms": {
                "single": "flux0_baked_wf_134",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_135": {
            "length": 136,
            "waveforms": {
                "single": "flux0_baked_wf_135",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_136": {
            "length": 136,
            "waveforms": {
                "single": "flux0_baked_wf_136",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_137": {
            "length": 140,
            "waveforms": {
                "single": "flux0_baked_wf_137",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_138": {
            "length": 140,
            "waveforms": {
                "single": "flux0_baked_wf_138",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_139": {
            "length": 140,
            "waveforms": {
                "single": "flux0_baked_wf_139",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_140": {
            "length": 140,
            "waveforms": {
                "single": "flux0_baked_wf_140",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_141": {
            "length": 144,
            "waveforms": {
                "single": "flux0_baked_wf_141",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_142": {
            "length": 144,
            "waveforms": {
                "single": "flux0_baked_wf_142",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_143": {
            "length": 144,
            "waveforms": {
                "single": "flux0_baked_wf_143",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_144": {
            "length": 144,
            "waveforms": {
                "single": "flux0_baked_wf_144",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_145": {
            "length": 148,
            "waveforms": {
                "single": "flux0_baked_wf_145",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_146": {
            "length": 148,
            "waveforms": {
                "single": "flux0_baked_wf_146",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_147": {
            "length": 148,
            "waveforms": {
                "single": "flux0_baked_wf_147",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_148": {
            "length": 148,
            "waveforms": {
                "single": "flux0_baked_wf_148",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_149": {
            "length": 152,
            "waveforms": {
                "single": "flux0_baked_wf_149",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_150": {
            "length": 152,
            "waveforms": {
                "single": "flux0_baked_wf_150",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_151": {
            "length": 152,
            "waveforms": {
                "single": "flux0_baked_wf_151",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_152": {
            "length": 152,
            "waveforms": {
                "single": "flux0_baked_wf_152",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_153": {
            "length": 156,
            "waveforms": {
                "single": "flux0_baked_wf_153",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_154": {
            "length": 156,
            "waveforms": {
                "single": "flux0_baked_wf_154",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_155": {
            "length": 156,
            "waveforms": {
                "single": "flux0_baked_wf_155",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_156": {
            "length": 156,
            "waveforms": {
                "single": "flux0_baked_wf_156",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_157": {
            "length": 160,
            "waveforms": {
                "single": "flux0_baked_wf_157",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_158": {
            "length": 160,
            "waveforms": {
                "single": "flux0_baked_wf_158",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_159": {
            "length": 160,
            "waveforms": {
                "single": "flux0_baked_wf_159",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_160": {
            "length": 160,
            "waveforms": {
                "single": "flux0_baked_wf_160",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_161": {
            "length": 164,
            "waveforms": {
                "single": "flux0_baked_wf_161",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_162": {
            "length": 164,
            "waveforms": {
                "single": "flux0_baked_wf_162",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_163": {
            "length": 164,
            "waveforms": {
                "single": "flux0_baked_wf_163",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_164": {
            "length": 164,
            "waveforms": {
                "single": "flux0_baked_wf_164",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_165": {
            "length": 168,
            "waveforms": {
                "single": "flux0_baked_wf_165",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_166": {
            "length": 168,
            "waveforms": {
                "single": "flux0_baked_wf_166",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_167": {
            "length": 168,
            "waveforms": {
                "single": "flux0_baked_wf_167",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_168": {
            "length": 168,
            "waveforms": {
                "single": "flux0_baked_wf_168",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_169": {
            "length": 172,
            "waveforms": {
                "single": "flux0_baked_wf_169",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_170": {
            "length": 172,
            "waveforms": {
                "single": "flux0_baked_wf_170",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_171": {
            "length": 172,
            "waveforms": {
                "single": "flux0_baked_wf_171",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_172": {
            "length": 172,
            "waveforms": {
                "single": "flux0_baked_wf_172",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_173": {
            "length": 176,
            "waveforms": {
                "single": "flux0_baked_wf_173",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_174": {
            "length": 176,
            "waveforms": {
                "single": "flux0_baked_wf_174",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_175": {
            "length": 176,
            "waveforms": {
                "single": "flux0_baked_wf_175",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_176": {
            "length": 176,
            "waveforms": {
                "single": "flux0_baked_wf_176",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_177": {
            "length": 180,
            "waveforms": {
                "single": "flux0_baked_wf_177",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_178": {
            "length": 180,
            "waveforms": {
                "single": "flux0_baked_wf_178",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_179": {
            "length": 180,
            "waveforms": {
                "single": "flux0_baked_wf_179",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_180": {
            "length": 180,
            "waveforms": {
                "single": "flux0_baked_wf_180",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_181": {
            "length": 184,
            "waveforms": {
                "single": "flux0_baked_wf_181",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_182": {
            "length": 184,
            "waveforms": {
                "single": "flux0_baked_wf_182",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_183": {
            "length": 184,
            "waveforms": {
                "single": "flux0_baked_wf_183",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_184": {
            "length": 184,
            "waveforms": {
                "single": "flux0_baked_wf_184",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_185": {
            "length": 188,
            "waveforms": {
                "single": "flux0_baked_wf_185",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_186": {
            "length": 188,
            "waveforms": {
                "single": "flux0_baked_wf_186",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_187": {
            "length": 188,
            "waveforms": {
                "single": "flux0_baked_wf_187",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_188": {
            "length": 188,
            "waveforms": {
                "single": "flux0_baked_wf_188",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_189": {
            "length": 192,
            "waveforms": {
                "single": "flux0_baked_wf_189",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_190": {
            "length": 192,
            "waveforms": {
                "single": "flux0_baked_wf_190",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_191": {
            "length": 192,
            "waveforms": {
                "single": "flux0_baked_wf_191",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_192": {
            "length": 192,
            "waveforms": {
                "single": "flux0_baked_wf_192",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_193": {
            "length": 196,
            "waveforms": {
                "single": "flux0_baked_wf_193",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_194": {
            "length": 196,
            "waveforms": {
                "single": "flux0_baked_wf_194",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_195": {
            "length": 196,
            "waveforms": {
                "single": "flux0_baked_wf_195",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_196": {
            "length": 196,
            "waveforms": {
                "single": "flux0_baked_wf_196",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_197": {
            "length": 200,
            "waveforms": {
                "single": "flux0_baked_wf_197",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_198": {
            "length": 200,
            "waveforms": {
                "single": "flux0_baked_wf_198",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_199": {
            "length": 200,
            "waveforms": {
                "single": "flux0_baked_wf_199",
            },
            "operation": "control",
        },
        "flux0_baked_pulse_200": {
            "length": 200,
            "waveforms": {
                "single": "flux0_baked_wf_200",
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
            "sample": 0.125,
            "type": "constant",
        },
        "readout1_wf": {
            "sample": 0.125,
            "type": "constant",
        },
        "readout2_wf": {
            "sample": 0.125,
            "type": "constant",
        },
        "readout3_wf": {
            "sample": 0.125,
            "type": "constant",
        },
        "readout4_wf": {
            "sample": 0.125,
            "type": "constant",
        },
        "readout5_wf": {
            "sample": 0.125,
            "type": "constant",
        },
        "readout6_wf": {
            "sample": 0.125,
            "type": "constant",
        },
        "pi_wf0": {
            "sample": 0.022,
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
            "sample": 0.011,
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
        "flux0_baked_wf_0": {
            "samples": [0.0] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_1": {
            "samples": [0.25] + [0.0] * 15,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_2": {
            "samples": [0.25] * 2 + [0.0] * 14,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_3": {
            "samples": [0.25] * 3 + [0.0] * 13,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_4": {
            "samples": [0.25] * 4 + [0.0] * 12,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_5": {
            "samples": [0.25] * 5 + [0.0] * 11,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_6": {
            "samples": [0.25] * 6 + [0.0] * 10,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_7": {
            "samples": [0.25] * 7 + [0.0] * 9,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_8": {
            "samples": [0.25] * 8 + [0.0] * 8,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_9": {
            "samples": [0.25] * 9 + [0.0] * 7,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_10": {
            "samples": [0.25] * 10 + [0.0] * 6,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_11": {
            "samples": [0.25] * 11 + [0.0] * 5,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_12": {
            "samples": [0.25] * 12 + [0.0] * 4,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_13": {
            "samples": [0.25] * 13 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_14": {
            "samples": [0.25] * 14 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_15": {
            "samples": [0.25] * 15 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_16": {
            "samples": [0.25] * 16,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_17": {
            "samples": [0.25] * 17 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_18": {
            "samples": [0.25] * 18 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_19": {
            "samples": [0.25] * 19 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_20": {
            "samples": [0.25] * 20,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_21": {
            "samples": [0.25] * 21 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_22": {
            "samples": [0.25] * 22 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_23": {
            "samples": [0.25] * 23 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_24": {
            "samples": [0.25] * 24,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_25": {
            "samples": [0.25] * 25 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_26": {
            "samples": [0.25] * 26 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_27": {
            "samples": [0.25] * 27 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_28": {
            "samples": [0.25] * 28,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_29": {
            "samples": [0.25] * 29 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_30": {
            "samples": [0.25] * 30 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_31": {
            "samples": [0.25] * 31 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_32": {
            "samples": [0.25] * 32,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_33": {
            "samples": [0.25] * 33 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_34": {
            "samples": [0.25] * 34 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_35": {
            "samples": [0.25] * 35 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_36": {
            "samples": [0.25] * 36,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_37": {
            "samples": [0.25] * 37 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_38": {
            "samples": [0.25] * 38 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_39": {
            "samples": [0.25] * 39 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_40": {
            "samples": [0.25] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_41": {
            "samples": [0.25] * 41 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_42": {
            "samples": [0.25] * 42 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_43": {
            "samples": [0.25] * 43 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_44": {
            "samples": [0.25] * 44,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_45": {
            "samples": [0.25] * 45 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_46": {
            "samples": [0.25] * 46 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_47": {
            "samples": [0.25] * 47 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_48": {
            "samples": [0.25] * 48,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_49": {
            "samples": [0.25] * 49 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_50": {
            "samples": [0.25] * 50 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_51": {
            "samples": [0.25] * 51 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_52": {
            "samples": [0.25] * 52,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_53": {
            "samples": [0.25] * 53 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_54": {
            "samples": [0.25] * 54 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_55": {
            "samples": [0.25] * 55 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_56": {
            "samples": [0.25] * 56,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_57": {
            "samples": [0.25] * 57 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_58": {
            "samples": [0.25] * 58 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_59": {
            "samples": [0.25] * 59 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_60": {
            "samples": [0.25] * 60,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_61": {
            "samples": [0.25] * 61 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_62": {
            "samples": [0.25] * 62 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_63": {
            "samples": [0.25] * 63 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_64": {
            "samples": [0.25] * 64,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_65": {
            "samples": [0.25] * 65 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_66": {
            "samples": [0.25] * 66 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_67": {
            "samples": [0.25] * 67 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_68": {
            "samples": [0.25] * 68,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_69": {
            "samples": [0.25] * 69 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_70": {
            "samples": [0.25] * 70 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_71": {
            "samples": [0.25] * 71 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_72": {
            "samples": [0.25] * 72,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_73": {
            "samples": [0.25] * 73 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_74": {
            "samples": [0.25] * 74 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_75": {
            "samples": [0.25] * 75 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_76": {
            "samples": [0.25] * 76,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_77": {
            "samples": [0.25] * 77 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_78": {
            "samples": [0.25] * 78 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_79": {
            "samples": [0.25] * 79 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_80": {
            "samples": [0.25] * 80,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_81": {
            "samples": [0.25] * 81 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_82": {
            "samples": [0.25] * 82 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_83": {
            "samples": [0.25] * 83 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_84": {
            "samples": [0.25] * 84,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_85": {
            "samples": [0.25] * 85 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_86": {
            "samples": [0.25] * 86 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_87": {
            "samples": [0.25] * 87 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_88": {
            "samples": [0.25] * 88,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_89": {
            "samples": [0.25] * 89 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_90": {
            "samples": [0.25] * 90 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_91": {
            "samples": [0.25] * 91 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_92": {
            "samples": [0.25] * 92,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_93": {
            "samples": [0.25] * 93 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_94": {
            "samples": [0.25] * 94 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_95": {
            "samples": [0.25] * 95 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_96": {
            "samples": [0.25] * 96,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_97": {
            "samples": [0.25] * 97 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_98": {
            "samples": [0.25] * 98 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_99": {
            "samples": [0.25] * 99 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_100": {
            "samples": [0.25] * 100,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_101": {
            "samples": [0.25] * 101 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_102": {
            "samples": [0.25] * 102 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_103": {
            "samples": [0.25] * 103 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_104": {
            "samples": [0.25] * 104,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_105": {
            "samples": [0.25] * 105 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_106": {
            "samples": [0.25] * 106 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_107": {
            "samples": [0.25] * 107 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_108": {
            "samples": [0.25] * 108,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_109": {
            "samples": [0.25] * 109 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_110": {
            "samples": [0.25] * 110 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_111": {
            "samples": [0.25] * 111 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_112": {
            "samples": [0.25] * 112,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_113": {
            "samples": [0.25] * 113 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_114": {
            "samples": [0.25] * 114 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_115": {
            "samples": [0.25] * 115 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_116": {
            "samples": [0.25] * 116,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_117": {
            "samples": [0.25] * 117 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_118": {
            "samples": [0.25] * 118 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_119": {
            "samples": [0.25] * 119 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_120": {
            "samples": [0.25] * 120,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_121": {
            "samples": [0.25] * 121 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_122": {
            "samples": [0.25] * 122 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_123": {
            "samples": [0.25] * 123 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_124": {
            "samples": [0.25] * 124,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_125": {
            "samples": [0.25] * 125 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_126": {
            "samples": [0.25] * 126 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_127": {
            "samples": [0.25] * 127 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_128": {
            "samples": [0.25] * 128,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_129": {
            "samples": [0.25] * 129 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_130": {
            "samples": [0.25] * 130 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_131": {
            "samples": [0.25] * 131 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_132": {
            "samples": [0.25] * 132,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_133": {
            "samples": [0.25] * 133 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_134": {
            "samples": [0.25] * 134 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_135": {
            "samples": [0.25] * 135 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_136": {
            "samples": [0.25] * 136,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_137": {
            "samples": [0.25] * 137 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_138": {
            "samples": [0.25] * 138 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_139": {
            "samples": [0.25] * 139 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_140": {
            "samples": [0.25] * 140,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_141": {
            "samples": [0.25] * 141 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_142": {
            "samples": [0.25] * 142 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_143": {
            "samples": [0.25] * 143 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_144": {
            "samples": [0.25] * 144,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_145": {
            "samples": [0.25] * 145 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_146": {
            "samples": [0.25] * 146 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_147": {
            "samples": [0.25] * 147 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_148": {
            "samples": [0.25] * 148,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_149": {
            "samples": [0.25] * 149 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_150": {
            "samples": [0.25] * 150 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_151": {
            "samples": [0.25] * 151 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_152": {
            "samples": [0.25] * 152,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_153": {
            "samples": [0.25] * 153 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_154": {
            "samples": [0.25] * 154 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_155": {
            "samples": [0.25] * 155 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_156": {
            "samples": [0.25] * 156,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_157": {
            "samples": [0.25] * 157 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_158": {
            "samples": [0.25] * 158 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_159": {
            "samples": [0.25] * 159 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_160": {
            "samples": [0.25] * 160,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_161": {
            "samples": [0.25] * 161 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_162": {
            "samples": [0.25] * 162 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_163": {
            "samples": [0.25] * 163 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_164": {
            "samples": [0.25] * 164,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_165": {
            "samples": [0.25] * 165 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_166": {
            "samples": [0.25] * 166 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_167": {
            "samples": [0.25] * 167 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_168": {
            "samples": [0.25] * 168,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_169": {
            "samples": [0.25] * 169 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_170": {
            "samples": [0.25] * 170 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_171": {
            "samples": [0.25] * 171 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_172": {
            "samples": [0.25] * 172,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_173": {
            "samples": [0.25] * 173 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_174": {
            "samples": [0.25] * 174 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_175": {
            "samples": [0.25] * 175 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_176": {
            "samples": [0.25] * 176,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_177": {
            "samples": [0.25] * 177 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_178": {
            "samples": [0.25] * 178 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_179": {
            "samples": [0.25] * 179 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_180": {
            "samples": [0.25] * 180,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_181": {
            "samples": [0.25] * 181 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_182": {
            "samples": [0.25] * 182 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_183": {
            "samples": [0.25] * 183 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_184": {
            "samples": [0.25] * 184,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_185": {
            "samples": [0.25] * 185 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_186": {
            "samples": [0.25] * 186 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_187": {
            "samples": [0.25] * 187 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_188": {
            "samples": [0.25] * 188,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_189": {
            "samples": [0.25] * 189 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_190": {
            "samples": [0.25] * 190 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_191": {
            "samples": [0.25] * 191 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_192": {
            "samples": [0.25] * 192,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_193": {
            "samples": [0.25] * 193 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_194": {
            "samples": [0.25] * 194 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_195": {
            "samples": [0.25] * 195 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_196": {
            "samples": [0.25] * 196,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_197": {
            "samples": [0.25] * 197 + [0.0] * 3,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_198": {
            "samples": [0.25] * 198 + [0.0] * 2,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_199": {
            "samples": [0.25] * 199 + [0.0],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "flux0_baked_wf_200": {
            "samples": [0.25] * 200,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
        "OFF": {
            "samples": [(0, 0)],
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
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6189000000.0, 'correction': [0.9792498461902142, 0.02296530455350876, 0.02197825163602829, 1.0232283771038055]},
            {'intermediate_frequency': 179000000.0, 'lo_frequency': 6110000000.0, 'correction': [0.9841276444494724, 0.05483501777052879, 0.052632030099630356, 1.025319691747427]},
            {'intermediate_frequency': 169000000.0, 'lo_frequency': 6110000000.0, 'correction': [0.9832491092383862, 0.052119217813014984, 0.04997655004262924, 1.025404404848814]},
            {'intermediate_frequency': 172215300.0, 'lo_frequency': 6110000000.0, 'correction': [0.9834322556853294, 0.05336608737707138, 0.0511721596121788, 1.0255954004824162]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6007000000.0, 'correction': [0.9805241003632545, 0.04597645252943039, 0.04391460865736008, 1.0265608876943588]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 5882000000.0, 'correction': [0.9815450236201286, 0.08165643364191055, 0.0771622434258461, 1.0387135222554207]},
            {'intermediate_frequency': 40864584.0, 'lo_frequency': 6382000000.0, 'correction': [0.9785669781267643, -0.02498408779501915, -0.023869480937719345, 1.0242620408535004]},
            {'intermediate_frequency': 10139023.0, 'lo_frequency': 6352000000.0, 'correction': [0.9787439368665218, -0.012496553361415863, -0.01195981353521347, 1.022668570280075]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6391860977.0, 'correction': [0.9792955070734024, -0.026965998113155365, -0.025794409215450287, 1.0237753726541996]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6441860977.0, 'correction': [0.9828890860080719, -0.052893687039613724, -0.05066971853375435, 1.026029534637928]},
            {'intermediate_frequency': 110924023.0, 'lo_frequency': 6452785000.0, 'correction': [0.9836567975580692, -0.05788365751504898, -0.05544988065958023, 1.026830941438675]},
            {'intermediate_frequency': 103030023.0, 'lo_frequency': 6444891000.0, 'correction': [0.9831880666315556, -0.05488967522978783, -0.0525817833840847, 1.0263416394591331]},
            {'intermediate_frequency': 150000000.0, 'lo_frequency': 6491860977.0, 'correction': [0.987505380064249, -0.07377802953124046, -0.07081400975584984, 1.0288388058543205]},
            {'intermediate_frequency': 193424023.0, 'lo_frequency': 6452785000.0, 'correction': [0.9909583926200867, -0.08515872806310654, -0.08189716190099716, 1.0304234512150288]},
            {'intermediate_frequency': 193724023.0, 'lo_frequency': 6452785000.0, 'correction': [0.9908422231674194, -0.08466072380542755, -0.0814182311296463, 1.0303026549518108]},
            {'intermediate_frequency': 93724023.0, 'lo_frequency': 6352785000.0, 'correction': [0.9798078313469887, -0.03997952863574028, -0.03818662092089653, 1.0258109867572784]},
            {'intermediate_frequency': 81371023.0, 'lo_frequency': 6340432000.0, 'correction': [0.9782580099999905, -0.03401654586195946, -0.032427724450826645, 1.0261885188519955]},
            {'intermediate_frequency': 193939023.0, 'lo_frequency': 6453000000.0, 'correction': [0.9909583926200867, -0.08515872806310654, -0.08189716190099716, 1.0304234512150288]},
            {'intermediate_frequency': 194739023.0, 'lo_frequency': 6453000000.0, 'correction': [0.9915495328605175, -0.0856141448020935, -0.08241552114486694, 1.0300325006246567]},
            {'intermediate_frequency': 5260977.0, 'lo_frequency': 6253000000.0, 'correction': [0.974171694368124, -0.003511127084493637, -0.0033296309411525726, 1.0272732116281986]},
            {'intermediate_frequency': 94739023.0, 'lo_frequency': 6353000000.0, 'correction': [0.9798637628555298, -0.04047927260398865, -0.03866395354270935, 1.0258695483207703]},
            {'intermediate_frequency': 61400000.0, 'lo_frequency': 6391860977.0, 'correction': [0.9797676913440228, -0.02995475009083748, -0.02866728976368904, 1.0237694792449474]},
            {'intermediate_frequency': 121400000.0, 'lo_frequency': 6451860977.0, 'correction': [0.9846197217702866, -0.06084731966257095, -0.05834583193063736, 1.0268337801098824]},
            {'intermediate_frequency': 21400000.0, 'lo_frequency': 6351860977.0, 'correction': [0.9770599342882633, -0.018385089933872223, -0.01752423495054245, 1.0250567235052586]},
            {'intermediate_frequency': 119100000.0, 'lo_frequency': 6451860977.0, 'correction': [0.9844526499509811, -0.0598498210310936, -0.05738934129476547, 1.026659544557333]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6382760977.0, 'correction': [0.9790809527039528, -0.027222469449043274, -0.02602703869342804, 1.0240504741668701]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6432760977.0, 'correction': [0.9824609197676182, -0.04989970475435257, -0.04780162125825882, 1.0255825743079185]},
            {'intermediate_frequency': 186300000.0, 'lo_frequency': 6382760977.0, 'correction': [0.9869083389639854, -0.07078702747821808, -0.06794317066669464, 1.0282167755067348]},
            {'intermediate_frequency': 86300000.0, 'lo_frequency': 6382760977.0, 'correction': [0.9805256128311157, -0.037942685186862946, -0.03631190210580826, 1.0245614387094975]},
            {'intermediate_frequency': 300000000.0, 'lo_frequency': 6054816000.0, 'correction': [0.9898257069289684, -0.08017868548631668, -0.07710785418748856, 1.0292456597089767]},
            {'intermediate_frequency': 300000000.0, 'lo_frequency': 6054816000.0, 'correction': [0.9997894875705242, 0.11495320126414299, 0.1107124499976635, 1.0380856171250343]},
            {'intermediate_frequency': 150000000.0, 'lo_frequency': 6054816000.0, 'correction': [0.9796853885054588, -0.028956260532140732, -0.027711715549230576, 1.0236834809184074]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6054816000.0, 'correction': [0.9785227365791798, 0.002995472401380539, 0.002866726368665695, 1.0224686153233051]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6054816000.0, 'correction': [0.9792138114571571, -0.012973923236131668, -0.012428421527147293, 1.022192943841219]},
            {'intermediate_frequency': 295184000.0, 'lo_frequency': 6054816000.0, 'correction': [0.999255582690239, 0.1132114864885807, 0.10903498902916908, 1.0375312604010105]},
            {'intermediate_frequency': 104816000.0, 'lo_frequency': 6454816000.0, 'correction': [0.9838112369179726, -0.05585983395576477, -0.05356338620185852, 1.0259906314313412]},
            {'intermediate_frequency': 245416000.0, 'lo_frequency': 6504816000.0, 'correction': [0.9981252439320087, -0.10691135376691818, -0.10311811417341232, 1.034841664135456]},
            {'intermediate_frequency': 195416000.0, 'lo_frequency': 6454816000.0, 'correction': [0.9910751916468143, -0.08565673232078552, -0.08237609267234802, 1.0305449031293392]},
            {'intermediate_frequency': 145416000.0, 'lo_frequency': 6404816000.0, 'correction': [0.9845968261361122, -0.057826023548841476, -0.05550287291407585, 1.02580850943923]},
            {'intermediate_frequency': 115584000.0, 'lo_frequency': 6254816000.0, 'correction': [0.9764660634100437, 0.029558632522821426, 0.02809569612145424, 1.02731042355299]},
            {'intermediate_frequency': 0.0, 'lo_frequency': 6350000000.0, 'correction': [0.9961768016219139, 0.008134439587593079, 0.008070643991231918, 1.004051111638546]},
            {'intermediate_frequency': 60000000.0, 'lo_frequency': 6400000000.0, 'correction': [0.9778789803385735, 0.006994668394327164, 0.006684247404336929, 1.0232923179864883]},
            {'intermediate_frequency': 260000000.0, 'lo_frequency': 6200000000.0, 'correction': [0.9916873052716255, 0.07421163842082024, 0.07182351872324944, 1.024660736322403]},
            {'intermediate_frequency': 201500000.0, 'lo_frequency': 6250000000.0, 'correction': [0.9839086309075356, 0.05648326501250267, 0.054161187261343, 1.0260922014713287]},
            {'intermediate_frequency': 251500000.0, 'lo_frequency': 6200000000.0, 'correction': [0.9905178360641003, 0.0720314309000969, 0.06961148232221603, 1.0249518416821957]},
            {'intermediate_frequency': 151500000.0, 'lo_frequency': 6300000000.0, 'correction': [0.976955521851778, 0.04363008961081505, 0.04138990864157677, 1.0298321060836315]},
            {'intermediate_frequency': 120000000.0, 'lo_frequency': 6300000000.0, 'correction': [0.9760312810540199, 0.035104669630527496, 0.033302225172519684, 1.0288578420877457]},
            {'intermediate_frequency': 117600000.0, 'lo_frequency': 6300000000.0, 'correction': [0.9759355634450912, 0.03410167992115021, 0.03235073387622833, 1.0287569426000118]},
            {'intermediate_frequency': 155300000.0, 'lo_frequency': 6300000000.0, 'correction': [0.9773092120885849, 0.04462191462516785, 0.04235145449638367, 1.029702726751566]},
            {'intermediate_frequency': 136300000.0, 'lo_frequency': 6319000000.0, 'correction': [0.976851649582386, 0.03859582170844078, 0.03664984926581383, 1.0287188850343227]},
            {'intermediate_frequency': 94700000.0, 'lo_frequency': 6550000000.0, 'correction': [0.9867146015167236, -0.06979002803564072, -0.06698622554540634, 1.0280149281024933]},
            {'intermediate_frequency': 119700000.0, 'lo_frequency': 6575000000.0, 'correction': [0.9901381880044937, -0.08370635658502579, -0.08042190223932266, 1.0305757261812687]},
            {'intermediate_frequency': 110000000.0, 'lo_frequency': 6427161000.0, 'correction': [0.9831412509083748, -0.051371097564697266, -0.049259185791015625, 1.025291919708252]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6427161000.0, 'correction': [0.9821890406310558, -0.04790371656417847, -0.04588955640792847, 1.0252987630665302]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6594760000.0, 'correction': [0.9892123863101006, -0.08175403252243996, -0.07846957817673683, 1.0306172594428062]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6427205000.0, 'correction': [0.9821890406310558, -0.04790371656417847, -0.04588955640792847, 1.0252987630665302]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6594787000.0, 'correction': [0.9892123863101006, -0.08175403252243996, -0.07846957817673683, 1.0306172594428062]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6272511000.0, 'correction': [0.9767700545489788, -0.033065591007471085, -0.03142908588051796, 1.027630239725113]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6581509000.0, 'correction': [0.9885527677834034, -0.07876303046941757, -0.07559873908758163, 1.0299300327897072]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6692538000.0, 'correction': [0.9944543987512589, -0.1192365251481533, -0.11333518847823143, 1.0462354086339474]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6722538000.0, 'correction': [0.996755201369524, -0.1293857954442501, -0.12274250015616417, 1.0507034212350845]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6720538000.0, 'correction': [0.996538769453764, -0.12836674228310585, -0.12180546298623085, 1.0502191968262196]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6722538000.0, 'correction': [0.9922946915030479, -0.11378249153494835, -0.10804566368460655, 1.0449818968772888]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6577520000.0, 'correction': [0.9852600395679474, -0.06181402504444122, -0.05933065712451935, 1.0264994837343693]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 5180969000.0, 'correction': [1.0352607257664204, 0.16766245663166046, 0.16632725298404694, 1.0435713529586792]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 5490362000.0, 'correction': [0.9915705248713493, 0.08930196613073349, 0.08581626787781715, 1.031846284866333]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 5765376000.0, 'correction': [0.9748025089502335, 0.052087198942899704, 0.049076687544584274, 1.03459981828928]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6006013000.0, 'correction': [0.9776982106268406, 0.0017488859593868256, 0.0016708634793758392, 1.0233527086675167]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6302511000.0, 'correction': [0.9763297103345394, -0.01652040332555771, -0.0157257542014122, 1.0256653130054474]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6521660000.0, 'correction': [0.9819214791059494, -0.047666095197200775, -0.045639656484127045, 1.025519609451294]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6732203000.0, 'correction': [0.9923459030687809, -0.11637603864073753, -0.11034690961241722, 1.0465656518936157]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6457205000.0, 'correction': [0.9803989082574844, -0.03895088657736778, -0.03725859150290489, 1.0249288901686668]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6679572000.0, 'correction': [0.9898084290325642, -0.09804768487811089, -0.09346814081072807, 1.0383048616349697]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6555300000.0, 'correction': [0.9873037338256836, -0.0727810300886631, -0.06985706463456154, 1.028628721833229]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6681116000.0, 'correction': [0.9895871318876743, -0.0985848531126976, -0.09391149133443832, 1.038832426071167]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6458138000.0, 'correction': [0.9804397858679295, -0.03932541236281395, -0.03761684522032738, 1.0249716266989708]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6578991000.0, 'correction': [0.9850246943533421, -0.06182941794395447, -0.059316486120224, 1.0267550833523273]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 5070871000.0, 'correction': [1.04546457529068, 0.18754782155156136, 0.18641798943281174, 1.0518008582293987]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 5284592000.0, 'correction': [1.030311793088913, 0.14396827667951584, 0.14411773532629013, 1.0292432978749275]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 5498310000.0, 'correction': [0.9903644733130932, 0.08775787800550461, 0.08419113606214523, 1.0323210805654526]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 5708368000.0, 'correction': [0.9789737202227116, 0.06375371664762497, 0.060362450778484344, 1.033974140882492]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 5922768000.0, 'correction': [0.9751980826258659, 0.02507476508617401, 0.023787304759025574, 1.0279795452952385]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6137733000.0, 'correction': [0.9799221903085709, -0.009472683072090149, -0.00908990204334259, 1.0211872830986977]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6348757000.0, 'correction': [0.9779209643602371, -0.025752883404493332, -0.02456800267100334, 1.025084737688303]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6560354000.0, 'correction': [0.9841667450964451, -0.05810420215129852, -0.05571548640727997, 1.0263613797724247]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 5936760000.0, 'correction': [0.9753614589571953, 0.02406575158238411, 0.022841233760118484, 1.0276505537331104]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6202899000.0, 'correction': [0.9757312163710594, -0.018536772578954697, -0.017619337886571884, 1.0265373140573502]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6465096000.0, 'correction': [0.9804810471832752, -0.039699941873550415, -0.03797510266304016, 1.0250147618353367]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6728075000.0, 'correction': [0.9923943243920803, -0.11532949656248093, -0.1094345971941948, 1.04585150629282]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6492011000.0, 'correction': [0.981060903519392, -0.040678396821022034, -0.03894902765750885, 1.0246208235621452]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6756342000.0, 'correction': [0.9929599463939667, -0.11994742602109909, -0.11362241953611374, 1.048234935849905]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6462011000.0, 'correction': [0.9806873649358749, -0.039440423250198364, -0.037745267152786255, 1.024730458855629]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6693594000.0, 'correction': [0.9904900677502155, -0.10415462777018547, -0.09909633919596672, 1.0410487949848175]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 5900187000.0, 'correction': [0.9742775671184063, 0.03113945573568344, 0.029454313218593597, 1.0300180055201054]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6173481000.0, 'correction': [0.977913748472929, -0.017993032932281494, -0.01718193292617798, 1.0240776985883713]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6433254000.0, 'correction': [0.980220690369606, -0.03494720906019211, -0.033445172011852264, 1.024242825806141]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6663917000.0, 'correction': [0.988731786608696, -0.09097612276673317, -0.08685386553406715, 1.0356589630246162]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 5003780000.0, 'correction': [1.0474614091217518, 0.19149423763155937, 0.19037548825144768, 1.0536168590188026]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 5238110000.0, 'correction': [1.0328116305172443, 0.15576476231217384, 0.15527117624878883, 1.0360947996377945]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 5471023000.0, 'correction': [0.9951350092887878, 0.09036701172590256, 0.08741634339094162, 1.0287249870598316]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 5705465000.0, 'correction': [0.9791630133986473, 0.06450267136096954, 0.061079010367393494, 1.0340480208396912]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 5940914000.0, 'correction': [0.9756268449127674, 0.024560976773500443, 0.023322630673646927, 1.0274290479719639]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6172568000.0, 'correction': [0.9780054688453674, -0.017491046339273453, -0.016706649214029312, 1.0239240042865276]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6406483000.0, 'correction': [0.979586411267519, -0.02770814672112465, -0.026517245918512344, 1.0235800594091415]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6636660000.0, 'correction': [0.987319465726614, -0.07861162349581718, -0.07526959106326103, 1.031157273799181]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 4953780000.0, 'correction': [1.054568573832512, 0.20054659619927406, 0.20030193775892258, 1.0558566749095917]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 5137493000.0, 'correction': [1.03913040086627, 0.17623627558350563, 0.1748434640467167, 1.0474081635475159]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 5319018000.0, 'correction': [1.025615930557251, 0.13030487671494484, 0.13055962696671486, 1.0236147306859493]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 5504283000.0, 'correction': [0.989299688488245, 0.08658137917518616, 0.08293086290359497, 1.032847460359335]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 5689958000.0, 'correction': [0.9805289581418037, 0.06720037013292313, 0.06374997645616531, 1.0335989519953728]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 5872437000.0, 'correction': [0.9732900932431221, 0.04000900685787201, 0.037696585059165955, 1.0329946279525757]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6053324000.0, 'correction': [0.9785298220813274, 0.0037443414330482483, 0.0035834088921546936, 1.0224760212004185]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6235504000.0, 'correction': [0.9741485230624676, -0.014299776405096054, -0.013552334159612656, 1.0278750583529472]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6417476000.0, 'correction': [0.979539267718792, -0.030024640262126923, -0.02872016280889511, 1.0240302048623562]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6597917000.0, 'correction': [0.9858676344156265, -0.0665663480758667, -0.06386089324951172, 1.0276337340474129]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6425794000.0, 'correction': [0.9797745794057846, -0.03270875662565231, -0.03128766268491745, 1.0242762044072151]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6613646000.0, 'correction': [0.9862014837563038, -0.07083993032574654, -0.06789450719952583, 1.028985220938921]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6552600000.0, 'correction': [0.9873037338256836, -0.0727810300886631, -0.06985706463456154, 1.028628721833229]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6525320000.0, 'correction': [0.9848443865776062, -0.06486961618065834, -0.062142107635736465, 1.0280706584453583]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6509320000.0, 'correction': [0.9775788448750973, 0.0009994879364967346, 0.0009546652436256409, 1.0234773494303226]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6209320000.0, 'correction': [0.9779843427240849, 0.024999678134918213, 0.023855268955230713, 1.0249012000858784]},
            {'intermediate_frequency': 82000000.0, 'lo_frequency': 6149320000.0, 'correction': [0.9797676913440228, 0.02995474636554718, 0.028667286038398743, 1.0237694792449474]},
            {'intermediate_frequency': 104300000.0, 'lo_frequency': 6351000000.0, 'correction': [0.9763623885810375, 0.02153196558356285, 0.020486261695623398, 1.0261999815702438]},
            {'intermediate_frequency': 154300000.0, 'lo_frequency': 6301000000.0, 'correction': [0.9768762178719044, 0.04489506408572197, 0.04256917163729668, 1.0302507318556309]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6617349000.0, 'correction': [0.9863977245986462, -0.07183767855167389, -0.06885077059268951, 1.0291899740695953]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6474284462.0, 'correction': [0.9807426519691944, -0.03993966802954674, -0.03822305426001549, 1.0247882269322872]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6474284462.0, 'correction': [0.9807426519691944, -0.03993966802954674, -0.03822305426001549, 1.0247882269322872]},
            {'intermediate_frequency': 50825177.0, 'lo_frequency': 6475109639.0, 'correction': [0.9803893975913525, -0.040456563234329224, -0.038684695959091187, 1.0252939760684967]},
            {'intermediate_frequency': 50126997.0, 'lo_frequency': 6474411459.0, 'correction': [0.9803029000759125, -0.0402093380689621, -0.038443610072135925, 1.0253285467624664]},
            {'intermediate_frequency': 47903614.0, 'lo_frequency': 6472188076.0, 'correction': [0.9806873649358749, -0.039440423250198364, -0.037745267152786255, 1.024730458855629]},
            {'intermediate_frequency': 50304047.0, 'lo_frequency': 6474588509.0, 'correction': [0.9805087670683861, -0.039949625730514526, -0.03821393847465515, 1.0250437371432781]},
            {'intermediate_frequency': 40940637.0, 'lo_frequency': 6465225099.0, 'correction': [0.9802359864115715, -0.037421565502882004, -0.03579571470618248, 1.0247585698962212]},
            {'intermediate_frequency': 36832370.0, 'lo_frequency': 6461116832.0, 'correction': [0.979938168078661, -0.035944659262895584, -0.034372493624687195, 1.0247595980763435]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6462598467.0, 'correction': [0.9804534949362278, -0.039450254291296005, -0.03773626312613487, 1.0249859541654587]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6474014720.0, 'correction': [0.9805087670683861, -0.039949625730514526, -0.03821393847465515, 1.0250437371432781]},
            {'intermediate_frequency': 228589943.0, 'lo_frequency': 6195424777.0, 'correction': [0.9880342558026314, 0.06534403935074806, 0.06299487128853798, 1.024879451841116]},
            {'intermediate_frequency': 399606783.0, 'lo_frequency': 6024407937.0, 'correction': [0.99720349162817, 0.14623839035630226, 0.13725000992417336, 1.0625094585120678]},
            {'intermediate_frequency': 150000000.0, 'lo_frequency': 6195424777.0, 'correction': [0.9813192263245583, -0.048451002687215805, -0.04632335528731346, 1.026391550898552]},
            {'intermediate_frequency': 150000000.0, 'lo_frequency': 6024407937.0, 'correction': [0.9803640507161617, -0.03143681585788727, -0.030115023255348206, 1.0233936719596386]},
            {'intermediate_frequency': 150000000.0, 'lo_frequency': 5819163687.0, 'correction': [0.9708429351449013, 0.01208425685763359, 0.01137472316622734, 1.0314022786915302]},
            {'intermediate_frequency': 150000000.0, 'lo_frequency': 6574720675.0, 'correction': [0.9925557225942612, -0.09367139637470245, -0.08999593555927277, 1.0330919958651066]},
            {'intermediate_frequency': 150000000.0, 'lo_frequency': 6398675849.0, 'correction': [0.9845968261361122, -0.057826023548841476, -0.05550287291407585, 1.02580850943923]},
            {'intermediate_frequency': 150000000.0, 'lo_frequency': 6178619815.0, 'correction': [0.9813192263245583, -0.048451002687215805, -0.04632335528731346, 1.026391550898552]},
            {'intermediate_frequency': 120000000.0, 'lo_frequency': 6544720675.0, 'correction': [0.9879165031015873, -0.07577202841639519, -0.07272789999842644, 1.0292671360075474]},
            {'intermediate_frequency': 120000000.0, 'lo_frequency': 6148619815.0, 'correction': [0.979940589517355, -0.03195173293352127, -0.03057844191789627, 1.0239501409232616]},
            {'intermediate_frequency': 120000000.0, 'lo_frequency': 5840541369.0, 'correction': [0.9711980111896992, 0.020140428096055984, 0.018957871943712234, 1.0317795015871525]},
            {'intermediate_frequency': 120000000.0, 'lo_frequency': 5444440509.0, 'correction': [0.9933649562299252, 0.06679845973849297, 0.06506038829684258, 1.019902441650629]},
            {'intermediate_frequency': 120000000.0, 'lo_frequency': 4960317235.0, 'correction': [1.0454695709049702, 0.17437895759940147, 0.17523249611258507, 1.040377203375101]},
            {'intermediate_frequency': 120000000.0, 'lo_frequency': 4388171548.0, 'correction': [1.0029978305101395, 0.15548938140273094, 0.14659176766872406, 1.0638763345777988]},
            {'intermediate_frequency': 120000000.0, 'lo_frequency': 3728003448.0, 'correction': [1.015494029968977, 0.06778844073414803, 0.06894000247120857, 0.9985313974320889]},
            {'intermediate_frequency': 120000000.0, 'lo_frequency': 2979812935.0, 'correction': [0.99745062738657, 0.012975882738828659, 0.012903224676847458, 1.0030672699213028]},
            {'intermediate_frequency': 120000000.0, 'lo_frequency': 2143600008.0, 'correction': [1.1682398915290833, -0.28230468928813934, -0.31303589046001434, 1.053552035242319]},
            {'intermediate_frequency': 200000000.0, 'lo_frequency': 6224720675.0, 'correction': [0.9849939420819283, 0.058808378875255585, 0.05647330731153488, 1.0257217027246952]},
            {'intermediate_frequency': 200000000.0, 'lo_frequency': 5504720675.0, 'correction': [1.0182311050593853, 0.16732943058013916, 0.16092073917388916, 1.0587823055684566]},
            {'intermediate_frequency': 200000000.0, 'lo_frequency': 4944720675.0, 'correction': [1.1068267114460468, 0.294921875, 0.294921875, 1.1068267114460468]},
            {'intermediate_frequency': 200000000.0, 'lo_frequency': 5583790864.0, 'correction': [1.0149101801216602, 0.1630907580256462, 0.15638595074415207, 1.0584228932857513]},
            {'intermediate_frequency': 250000000.0, 'lo_frequency': 6176539346.0, 'correction': [0.9898693487048149, 0.07119742408394814, 0.06873837485909462, 1.025280974805355]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 5868000000.0, 'correction': [1.1353193446993828, -0.2059326171875, -0.2332763671875, 1.0022416189312935]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6389000000.0, 'correction': [1.0034327507019043, -0.161285400390625, -0.151519775390625, 1.0681051537394524]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6000000000.0, 'correction': [1.061584122478962, -0.1363677978515625, -0.1451568603515625, 0.9973065592348576]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6523302920.0, 'correction': [0.9849618934094906, -0.06284231320023537, -0.060258809477090836, 1.0271906219422817]},
            {'intermediate_frequency': 250000000.0, 'lo_frequency': 5552050968.0, 'correction': [1.0206382237374783, 0.1765514723956585, 0.16930360719561577, 1.0643316134810448]},
            {'intermediate_frequency': 200000000.0, 'lo_frequency': 6226539346.0, 'correction': [0.9852294065058231, 0.058793745934963226, 0.05648680776357651, 1.0254664719104767]},
            {'intermediate_frequency': 200000000.0, 'lo_frequency': 5602050968.0, 'correction': [1.0132064558565617, 0.1601780503988266, 0.15344320237636566, 1.0576775781810284]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6294000000.0, 'correction': [0.9750760272145271, 0.029603037983179092, 0.028055701404809952, 1.028853714466095]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6525491202.0, 'correction': [0.9856077060103416, -0.06380802392959595, -0.06124454736709595, 1.0268617011606693]},
            {'intermediate_frequency': 290000000.0, 'lo_frequency': 6136539346.0, 'correction': [0.9983679875731468, 0.09717368334531784, 0.09427642077207565, 1.0290494039654732]},
            {'intermediate_frequency': 290000000.0, 'lo_frequency': 5616539346.0, 'correction': [1.0312877669930458, 0.18967142328619957, 0.18347826227545738, 1.066098053008318]},
            {'intermediate_frequency': 290000000.0, 'lo_frequency': 5096539346.0, 'correction': [1.1188673302531242, 0.3118908405303955, 0.3131115436553955, 1.1145052909851074]},
            {'intermediate_frequency': 290000000.0, 'lo_frequency': 4576539346.0, 'correction': [1.1583629325032234, 0.380952425301075, 0.3846908286213875, 1.1471060290932655]},
            {'intermediate_frequency': 290000000.0, 'lo_frequency': 5632539346.0, 'correction': [1.0308289490640163, 0.18867838010191917, 0.1825176440179348, 1.0656237490475178]},
            {'intermediate_frequency': 290000000.0, 'lo_frequency': 5128539346.0, 'correction': [1.1144964508712292, 0.3040935695171356, 0.3052837550640106, 1.1101514548063278]},
            {'intermediate_frequency': 290000000.0, 'lo_frequency': 4624539346.0, 'correction': [1.1544516310095787, 0.36434125900268555, 0.37007856369018555, 1.13655424118042]},
            {'intermediate_frequency': 290000000.0, 'lo_frequency': 6010000000.0, 'correction': [0.9981551170349121, 0.10870577022433281, 0.10474659129977226, 1.0358830690383911]},
            {'intermediate_frequency': 290000000.0, 'lo_frequency': 6090000000.0, 'correction': [0.9961284399032593, 0.0933229960501194, 0.09031987562775612, 1.0292495377361774]},
            {'intermediate_frequency': 290000000.0, 'lo_frequency': 5910000000.0, 'correction': [1.0040552951395512, 0.13466209173202515, 0.12912601232528687, 1.0471026226878166]},
            {'intermediate_frequency': 200000000.0, 'lo_frequency': 6129969799.0, 'correction': [0.9867832139134407, 0.06763772293925285, 0.06498376652598381, 1.027083732187748]},
            {'intermediate_frequency': 200000000.0, 'lo_frequency': 5929969799.0, 'correction': [0.9906096756458282, 0.10104914009571075, 0.09632940590381622, 1.0391453690826893]},
            {'intermediate_frequency': 200000000.0, 'lo_frequency': 5329969799.0, 'correction': [1.062568947672844, 0.21592574194073677, 0.215714979916811, 1.0636071227490902]},
            {'intermediate_frequency': 200000000.0, 'lo_frequency': 5129969799.0, 'correction': [1.0844337567687035, 0.26594697311520576, 0.2633625157177448, 1.095075637102127]},
            {'intermediate_frequency': 200000000.0, 'lo_frequency': 4529969799.0, 'correction': [1.1175559610128403, 0.3373394273221493, 0.330815102905035, 1.1395963616669178]},
            {'intermediate_frequency': 200000000.0, 'lo_frequency': 4329969799.0, 'correction': [1.032392043620348, 0.225799560546875, 0.212127685546875, 1.0989309065043926]},
            {'intermediate_frequency': 200000000.0, 'lo_frequency': 6100000000.0, 'correction': [0.9857261218130589, 0.0645567774772644, 0.061961330473423004, 1.0270163901150227]},
            {'intermediate_frequency': 200000000.0, 'lo_frequency': 5900000000.0, 'correction': [0.9912025965750217, 0.1092439591884613, 0.10378655791282654, 1.0433229319751263]},
            {'intermediate_frequency': 240000000.0, 'lo_frequency': 6088750287.0, 'correction': [0.9886813312768936, 0.07824504747986794, 0.07513821497559547, 1.0295615568757057]},
            {'intermediate_frequency': 300000000.0, 'lo_frequency': 6125791423.0, 'correction': [0.998919028788805, 0.1001112125813961, 0.09707897529006004, 1.0301200114190578]},
            {'intermediate_frequency': 300000000.0, 'lo_frequency': 5925791423.0, 'correction': [1.004887230694294, 0.1355920508503914, 0.1301446631550789, 1.0469481982290745]},
            {'intermediate_frequency': 240000000.0, 'lo_frequency': 6169044076.0, 'correction': [0.9899058230221272, 0.07258223742246628, 0.07004117220640182, 1.0258192047476768]},
            {'intermediate_frequency': 240000000.0, 'lo_frequency': 5582357496.0, 'correction': [1.0202825739979744, 0.1758088432252407, 0.16858118399977684, 1.0640256218612194]},
            {'intermediate_frequency': 200000000.0, 'lo_frequency': 6125791423.0, 'correction': [0.986666914075613, 0.0670149065554142, 0.06438538804650307, 1.02696268633008]},
            {'intermediate_frequency': 234208577.0, 'lo_frequency': 6125791423.0, 'correction': [0.9889937378466129, 0.0774589255452156, 0.07445592433214188, 1.0288824290037155]},
            {'intermediate_frequency': 74208577.0, 'lo_frequency': 6125791423.0, 'correction': [0.9810896888375282, 0.02891300991177559, 0.027751434594392776, 1.022154577076435]},
            {'intermediate_frequency': 40000000.0, 'lo_frequency': 6280000000.0, 'correction': [0.9747943617403507, 0.009274180978536606, 0.008804436773061752, 1.0268026776611805]},
            {'intermediate_frequency': 214208577.0, 'lo_frequency': 6125791423.0, 'correction': [0.9871930666267872, 0.07101859524846077, 0.06819869950413704, 1.0280117578804493]},
            {'intermediate_frequency': 200000000.0, 'lo_frequency': 5925791423.0, 'correction': [0.9899207577109337, 0.10163820534944534, 0.0967257097363472, 1.040196754038334]},
            {'intermediate_frequency': 290000000.0, 'lo_frequency': 6111661923.0, 'correction': [0.9963526800274849, 0.0922844223678112, 0.08940194174647331, 1.0284768976271152]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6485047515.0, 'correction': [0.9831880666315556, -0.05488967522978783, -0.0525817833840847, 1.0263416394591331]},
            {'intermediate_frequency': 200000000.0, 'lo_frequency': 6222629958.0, 'correction': [0.9853113479912281, 0.05929199978709221, 0.05696551129221916, 1.0255517587065697]},
            {'intermediate_frequency': 200000000.0, 'lo_frequency': 6221227134.0, 'correction': [0.9854651875793934, 0.059502579271793365, 0.05718177556991577, 1.0254616923630238]},
            {'intermediate_frequency': 200000000.0, 'lo_frequency': 6221505924.0, 'correction': [0.9847585968673229, 0.05882301926612854, 0.05645981431007385, 1.0259770527482033]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6207000000.0, 'correction': [1.0, 0.0, 0.0, 1.0]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 6082000000.0, 'correction': [1.0, 0.0, 0.0, 1.0]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 5667000000.0, 'correction': [1.0, 0.0, 0.0, 1.0]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 5542000000.0, 'correction': [1.0, 0.0, 0.0, 1.0]},
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
            {'intermediate_frequency': 56520000.0, 'lo_frequency': 7206000000.0, 'correction': [0.9980175569653511, -0.10589710250496864, -0.10217723622918129, 1.0343514010310173]},
            {'intermediate_frequency': 56440000.0, 'lo_frequency': 7206000000.0, 'correction': [0.9978232942521572, -0.10591847449541092, -0.1021573469042778, 1.0345601588487625]},
            {'intermediate_frequency': 56760000.0, 'lo_frequency': 7206000000.0, 'correction': [0.998047448694706, -0.1058938167989254, -0.10218029841780663, 1.0343192927539349]},
            {'intermediate_frequency': 56890000.0, 'lo_frequency': 7206000000.0, 'correction': [0.9977668561041355, -0.10566820204257965, -0.10191906988620758, 1.034470096230507]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 7312490000.0, 'correction': [1.0003017038106918, -0.11257394403219223, -0.10868581384420395, 1.0360865332186222]},
            {'intermediate_frequency': 49600000.0, 'lo_frequency': 7312490000.0, 'correction': [1.0004660375416279, -0.11229755356907845, -0.10847188904881477, 1.0357511937618256]},
            {'intermediate_frequency': 1000000.0, 'lo_frequency': 7080000000.0, 'correction': [0.9985253363847733, -0.09309209883213043, -0.09053720533847809, 1.0267029888927937]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 7029000000.0, 'correction': [0.9924078099429607, -0.09164418280124664, -0.0881127268075943, 1.032182365655899]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 7079000000.0, 'correction': [0.9926108457148075, -0.09341064840555191, -0.08976731449365616, 1.0328973680734634]},
            {'intermediate_frequency': 49500000.0, 'lo_frequency': 7079000000.0, 'correction': [0.9927930608391762, -0.09364809468388557, -0.09001745656132698, 1.0328349880874157]},
            {'intermediate_frequency': 51000000.0, 'lo_frequency': 7312490000.0, 'correction': [1.0004660375416279, -0.11229755356907845, -0.10847188904881477, 1.0357511937618256]},
            {'intermediate_frequency': 49200000.0, 'lo_frequency': 7312490000.0, 'correction': [1.0005793273448944, -0.11267022415995598, -0.10883186385035515, 1.035868477076292]},
            {'intermediate_frequency': 49500000.0, 'lo_frequency': 7312490000.0, 'correction': [1.0004660375416279, -0.11229755356907845, -0.10847188904881477, 1.0357511937618256]},
            {'intermediate_frequency': 100000000.0, 'lo_frequency': 7100000000.0, 'correction': [0.9932862967252731, -0.09462080895900726, -0.09099684655666351, 1.032844066619873]},
            {'intermediate_frequency': 56000000.0, 'lo_frequency': 7200000000.0, 'correction': [0.9974122568964958, -0.10442504659295082, -0.10072002187371254, 1.0341024547815323]},
            {'intermediate_frequency': 63200000.0, 'lo_frequency': 7200000000.0, 'correction': [0.9974122568964958, -0.10442504659295082, -0.10072002187371254, 1.0341024547815323]},
            {'intermediate_frequency': 57200000.0, 'lo_frequency': 7206000000.0, 'correction': [0.9976956285536289, -0.1054195687174797, -0.1016792580485344, 1.0343962460756302]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 7313380000.0, 'correction': [1.0004471875727177, -0.11223544180393219, -0.10841189324855804, 1.035731676965952]},
            {'intermediate_frequency': 49820000.0, 'lo_frequency': 7313200000.0, 'correction': [1.0003161393105984, -0.11231497675180435, -0.10845563560724258, 1.0359119027853012]},
            {'intermediate_frequency': 49940000.0, 'lo_frequency': 7313320000.0, 'correction': [1.0004283487796783, -0.11217333003878593, -0.10835189744830132, 1.0357121750712395]},
            {'intermediate_frequency': 49833478.0, 'lo_frequency': 7313213478.0, 'correction': [1.0004060715436935, -0.11230452358722687, -0.10846538841724396, 1.0358154736459255]},
            {'intermediate_frequency': 49983478.0, 'lo_frequency': 7313363478.0, 'correction': [1.00034611672163, -0.11231149360537529, -0.10845888778567314, 1.0358797572553158]},
            {'intermediate_frequency': 49783478.0, 'lo_frequency': 7313163478.0, 'correction': [1.00034611672163, -0.11231149360537529, -0.10845888778567314, 1.0358797572553158]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 7313113478.0, 'correction': [1.0004660375416279, -0.11229755356907845, -0.10847188904881477, 1.0357511937618256]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 7313513478.0, 'correction': [0.9310230351984501, 0.050823211669921875, 0.043498992919921875, 1.0877856612205505]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6267000000.0, 'correction': [0.9793037101626396, -0.1138143539428711, -0.1052694320678711, 1.0587956719100475]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 7180000000.0, 'correction': [0.9293350912630558, 0.03388214111328125, 0.02899932861328125, 1.085813507437706]},
            {'intermediate_frequency': 49700000.0, 'lo_frequency': 7313513478.0, 'correction': [1.00037731975317, -0.11282245069742203, -0.10892573744058609, 1.0361648574471474]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6000000000.0, 'correction': [1.034758448600769, -0.15625, -0.15625, 1.034758448600769]},
            {'intermediate_frequency': 50200000.0, 'lo_frequency': 7313513478.0, 'correction': [1.0001375935971737, -0.11285046860575676, -0.10889963433146477, 1.0364221781492233]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 7313263478.0, 'correction': [1.00037731975317, -0.11282245069742203, -0.10892573744058609, 1.0361648574471474]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 7313413478.0, 'correction': [1.0003017038106918, -0.11257394403219223, -0.10868581384420395, 1.0360865332186222]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 7313013478.0, 'correction': [1.0001375935971737, -0.11285046860575676, -0.10889963433146477, 1.0364221781492233]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 7049000000.0, 'correction': [1.0, 0.0, 0.0, 1.0]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6925000000.0, 'correction': [1.0, 0.0, 0.0, 1.0]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6162000000.0, 'correction': [1.0, 0.0, 0.0, 1.0]},
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6068000000.0, 'correction': [1.0, 0.0, 0.0, 1.0]},
        ],
    },
}


