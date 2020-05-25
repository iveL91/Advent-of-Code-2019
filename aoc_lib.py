"""aoc_lib"""

import operator
from typing import List, Dict, Callable


def data_input(filename: str) -> List[int]:
    """"""
    with open(filename) as f:
        return [int(number) for number in f.read().split(",")]


class IntcodeComputer:
    """
    opcodes = {1: "add",
               2: "multiply",
               3: "input",
               4: "output",
               5: "jump-if-true (!= 0)",
               6: "jump-if-false (== 0)",
               7: "less than",
               8: "equal to",
               9: "adjust relative base",
               99: "break"}
    """

    opcodes_operators: Dict[int, Callable[[int, int], int]] = {1: operator.add,
                                                               2: operator.mul,
                                                               7: operator.lt,
                                                               8: operator.eq}

    instruction_lengths: Dict[int, int] = {1: 3,
                                           2: 3,
                                           3: 1,
                                           4: 1,
                                           5: 2,
                                           6: 2,
                                           7: 3,
                                           8: 3,
                                           9: 1,
                                           99: 0}

    def __init__(self, data: List[int], inpt: int = 0, address: int = 0, extension: int = 0,
                 relative_base: int = 0) -> None:
        """"""
        self.data: List[int] = data + [0 for _ in range(extension)]
        self.address: int = address
        self.inpt: int = inpt
        self.outputs: List[int] = []
        self.relative_base: int = relative_base
        self.stop: bool = False

    def mode_value(self, value: int, mode: int) -> int:
        """
        Calculate the value depending on the mode
        """
        val: int
        if mode == 0:  # position mode
            val = self.data[value]
        elif mode == 1:  # immediate mode
            val = value
        else:  # if mode == 2:  # relative mode
            val = self.data[value + self.relative_base]
        return val

    def assign_operator(self, opcode: int, value_1: int, value_2: int, instr_3: int) -> None:
        """Assigning depending on the opcode and the mode of the 3rd parameter"""
        value: int = int(self.opcodes_operators[opcode](value_1, value_2))
        if instr_3 == 0:
            self.data[self.data[self.address + 3]] = value
        elif instr_3 == 2:
            self.data[self.data[self.address + 3] + self.relative_base] = value
        # return self

    def intcode_computer_computation(self) -> None:
        """
        One intcode_computer computation
        """
        instruction: int = self.data[self.address]
        opcode: int = instruction % 100
        instruction_list: List[int] = [opcode] + [instruction // (10 ** (i + 2)) % 10 for i in
                                                  range(self.instruction_lengths[opcode])]
        mode_values: List[int] = [0] + [
            IntcodeComputer.mode_value(self, self.data[self.address + i + 1], instr) for i, instr in
            enumerate(instruction_list[1:])]

        if opcode in [1, 2, 7, 8]:  # add, mult, less-than, eq
            self.assign_operator(opcode, mode_values[1], mode_values[2], instruction_list[3])
            self.address += self.instruction_lengths[opcode] + 1
        elif opcode == 3:  # input
            if self.inpt is not None:
                self.data[self.data[self.address + 1] + self.relative_base] = self.inpt
                self.inpt = None
                self.address += self.instruction_lengths[opcode] + 1
            else:
                self.stop = True
        elif opcode == 4:  # output
            self.outputs.append(mode_values[1])
            self.address += self.instruction_lengths[opcode] + 1
        elif opcode == 5:  # jump-if-true
            if mode_values[1] != 0:
                self.address = mode_values[2]
            else:
                self.address += self.instruction_lengths[opcode] + 1
        elif opcode == 6:  # jump-if-false
            if mode_values[1] == 0:
                self.address = mode_values[2]
            else:
                self.address += self.instruction_lengths[opcode] + 1
        elif opcode == 9:  # adjust relative base
            self.relative_base += mode_values[1]
            self.address += self.instruction_lengths[opcode] + 1
        else:  # opcode == 99 # break
            self.stop = True
        # return self

    def run(self):
        """Run"""
        while not self.stop:
            self.intcode_computer_computation()
        return self
