# QuAM class automatically generated using QuAM SDK (ver 0.11.0)
# open source code and documentation is available at
# https://github.com/entropy-lab/quam-sdk

from typing import List, Union
import sys
import os
from quam_sdk.classes import QuamComponent, quam_data, quam_tags



__all__ = ["QuAM"]


class _add_path():
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        sys.path.insert(0, self.path)

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            sys.path.remove(self.path)
        except ValueError:
            pass



@quam_data
class Network(QuamComponent):
    qop_ip: str
    octave1_ip: str
    qop_port: int
    octave_port: int
    cluster_name: str
    save_dir: str
    


@quam_data
class Digital_marker(QuamComponent):
    delay: int
    buffer: int
    


@quam_data
class Wiring(QuamComponent):
    controller: str
    I: int
    Q: int
    digital_marker: int
    


@quam_data
class Qubit(QuamComponent):
    name: str
    f_01: float
    f_tls: List[Union[str, int, float, bool, list]]
    lo: float
    rf_gain: int
    rf_switch_mode: str
    mixer_name: str
    anharmonicity: float
    drag_coefficient: float
    ac_stark_detuning: float
    x180_length: int
    x180_amp: float
    pi_length: List[Union[str, int, float, bool, list]]
    pi_amp: List[Union[str, int, float, bool, list]]
    pi_length_tls: List[Union[str, int, float, bool, list]]
    pi_amp_tls: List[Union[str, int, float, bool, list]]
    T1: int
    T2: int
    DC_tuning_curve: List[Union[str, int, float, bool, list]]
    AC_tuning_curve: List[Union[str, int, float, bool, list]]
    digital_marker: Digital_marker
    wiring: Wiring
    


@quam_data
class Iswap(QuamComponent):
    length: List[Union[str, int, float, bool, list]]
    level: List[Union[str, int, float, bool, list]]
    


@quam_data
class Filter(QuamComponent):
    iir_taps: List[Union[str, int, float, bool, list]]
    fir_taps: List[Union[str, int, float, bool, list]]
    


@quam_data
class Wiring2(QuamComponent):
    controller: str
    port: int
    filter: Filter
    


@quam_data
class Flux_line(QuamComponent):
    name: str
    flux_pulse_length: int
    flux_pulse_amp: float
    max_frequency_point: float
    Z_delay: int
    dc_voltage: float
    iswap: Iswap
    wiring: Wiring2
    


@quam_data
class Digital_marker2(QuamComponent):
    delay: int
    buffer: int
    


@quam_data
class Wiring3(QuamComponent):
    controller: str
    I: int
    Q: int
    digital_marker: int
    


@quam_data
class Resonator(QuamComponent):
    name: str
    f_readout: float
    lo: float
    rf_gain: int
    rf_switch_mode: str
    depletion_time: int
    readout_pulse_length: int
    optimal_pulse_length: int
    readout_pulse_amp: float
    rotation_angle: float
    ge_threshold: float
    RO_attenuation: List[Union[str, int, float, bool, list]]
    TWPA: List[Union[str, int, float, bool, list]]
    tuning_curve: List[Union[str, int, float, bool, list]]
    digital_marker: Digital_marker2
    wiring: Wiring3
    


@quam_data
class Global_parameters(QuamComponent):
    time_of_flight: int
    saturation_amp: float
    saturation_len: int
    con1_downconversion_offset_I: float
    con1_downconversion_offset_Q: float
    con1_downconversion_gain: int
    con2_downconversion_offset_I: float
    con2_downconversion_offset_Q: float
    con2_downconversion_gain: int
    RO_delay: int
    


@quam_data
class QuAM(QuamComponent):
    qubits: List[Qubit]
    flux_lines: List[Flux_line]
    resonators: List[Resonator]
    network: Network
    global_parameters: Global_parameters
    

