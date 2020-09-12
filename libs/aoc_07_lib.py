"""aoc_07_lib"""

import itertools
import string
from typing import Iterable, List, Optional
from libs.aoc_lib import IntcodeComputer


class Amplifier:
    def __init__(self, name: str, data: List[int], phase: int) -> None:
        self.name = name
        self.computer = IntcodeComputer(data.copy(), inpt=phase).run()
        self.connected_from: Optional[Amplifier] = None
        self.connected_to: Optional[Amplifier] = None


class AmplifierSystem:
    def __init__(self, data: List[int], phase_setting: Iterable[int]) -> None:
        self.amplifiers = [Amplifier(amplifier_name, data, phase) for amplifier_name, phase in
                           zip(string.ascii_uppercase, phase_setting)]
        self.connect()
        self.initial_run()
        self.close_circuit()

    def __str__(self):
        return " -> ".join(amplifier.name for amplifier in self.amplifiers)

    def connect(self) -> None:
        for index, amp in enumerate(self.amplifiers):
            if index == 0:
                amp.connected_to = self.amplifiers[index + 1]
            elif index == len(self.amplifiers) - 1:
                amp.connected_from = self.amplifiers[index - 1]
            else:
                amp.connected_from = self.amplifiers[index - 1]
                amp.connected_to = self.amplifiers[index + 1]

    def initial_run(self) -> None:
        for amp in self.amplifiers:
            if amp is self.amplifiers[0]:
                amp.computer.inpt = 0
            else:
                amp.computer.inpt = amp.connected_from.computer.outputs[-1]
            amp.computer.run()

    def close_circuit(self) -> None:
        self.amplifiers[0].connected_from = self.amplifiers[-1]
        self.amplifiers[-1].connected_to = self.amplifiers[0]

    def thruster_signal(self) -> int:
        halt = self.amplifiers[-1].computer.data[self.amplifiers[-1].computer.address] == 99
        current_amp = self.amplifiers[0]

        while not halt:
            current_amp.computer.inpt = current_amp.connected_from.computer.outputs[-1]
            current_amp.computer.run()
            # (current_opcode == 99)
            halt = (
                current_amp is self.amplifiers[-1]) and current_amp.computer.stop
            current_amp = current_amp.connected_to

        return self.amplifiers[-1].computer.outputs[-1]


def max_thrust(data: List[int], phase_settings: Iterable[int]) -> int:
    result: int = -1

    for phase_setting in itertools.permutations(phase_settings):
        # system = AmplifierSystem(data, phase_setting)
        result = max(result, AmplifierSystem(
            data, phase_setting).thruster_signal())
    return result


def part_1(data: List[int]) -> int:
    return max_thrust(data, range(5))


def part_2(data: List[int]) -> int:
    return max_thrust(data, range(5, 10))
