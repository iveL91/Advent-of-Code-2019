"""aoc_7_lib"""

import itertools
from typing import List, Dict, Any, Sequence
from aoc_lib import IntcodeComputer


def data_input(filename: str) -> List[int]:
    with open(filename) as f:
        return [int(number) for number in f.read().split(",")]


def initializing_amplifiers(data: List[int], phase_setting: Sequence[int]) -> List[Dict[str, Any]]:
    """()"""
    if isinstance(data, str):
        data = [int(number) for number in data.split(",")]

    amplifiers: List[Dict[str, Any]] = [
        {"name": amplifier_name, "computer": IntcodeComputer(data.copy(), inpt=phase).run()} for
        amplifier_name, phase in zip(["A", "B", "C", "D", "E"], phase_setting)]

    # Connectiions
    for index, amp in enumerate(amplifiers):
        if index == 0:
            amp["connected_from"] = None
            amp["connected_to"] = amplifiers[index + 1]
        elif index == len(amplifiers) - 1:
            amp["connected_from"] = amplifiers[index - 1]
            amp["connected_to"] = None
        else:
            amp["connected_from"] = amplifiers[(index - 1) % len(amplifiers)]
            amp["connected_to"] = amplifiers[(index + 1) % len(amplifiers)]

    return amplifiers


def thruster_signal(amplifiers: List[Dict[str, Any]]) -> int:
    """()"""
    for amp in amplifiers:
        if amp is amplifiers[0]:
            amp["computer"].inpt = 0
        else:
            amp["computer"].inpt = amp["connected_from"]["computer"].outputs[-1]

        amp["computer"].stop = False
        amp["computer"].run()

    amplifiers[0]["connected_from"] = amplifiers[-1]
    amplifiers[-1]["connected_to"] = amplifiers[0]

    halt = amplifiers[-1]["computer"].data[amplifiers[-1]["computer"].address] == 99
    current_amp = amplifiers[0]

    while not halt:
        current_amp["computer"].inpt = current_amp["connected_from"]["computer"].outputs[-1]
        current_amp["computer"].stop = False
        current_amp["computer"].run()
        current_opcode = current_amp["computer"].data[current_amp["computer"].address]
        halt = (current_amp is amplifiers[-1]) and (current_opcode == 99)
        current_amp = current_amp["connected_to"]

    return amplifiers[-1]["computer"].outputs[-1]


def part_1(data: List[int]) -> int:
    """()"""
    max_thrust = -1
    phase_settings = [0, 1, 2, 3, 4]  # Phases

    for phase_setting in itertools.permutations(phase_settings):
        amplifiers = initializing_amplifiers(data, phase_setting)
        max_thrust = max(max_thrust, thruster_signal(amplifiers))

    return max_thrust


def part_2(data: List[int]) -> int:
    """()"""
    max_thrust = -1
    phase_settings = [5, 6, 7, 8, 9]  # Phases

    for phase_setting in itertools.permutations(phase_settings):
        amplifiers = initializing_amplifiers(data, phase_setting)
        max_thrust = max(max_thrust, thruster_signal(amplifiers))

    return max_thrust
