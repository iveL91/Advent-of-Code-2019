"""aoc_lib"""

import operator
from typing import Callable, Dict, List, Optional


def data_input(filename: str) -> List[int]:
    """"""
    with open(filename) as f:
        return [int(number) for number in f.read().split(",")]


def nth_decimal_position(number: int, n: int) -> int:
    return number // (10 ** n) % 10


class IntcodeComputer:
    """"""

    def __init__(self, data: List[int], inpt: Optional[int] = 0, address: int = 0, extension: int = 0,
                 relative_base: int = 0) -> None:
        """"""
        self.data = data + [0]*extension
        self.address = address
        self.inpt = inpt
        self.outputs: List[int] = []
        self.relative_base = relative_base
        self.stop: bool = False

    @property
    def opcode(self) -> int:
        return self.data[self.address] % 100

    def computation(self) -> None:
        operations: Dict[int, Callable] = {
            1: AddCommand(self),
            2: MulCommand(self),
            3: InputCommand(self),
            4: OutputCommand(self),
            5: JumpIfTrueCommand(self),
            6: JumpIfFalseCommand(self),
            7: LessThanCommand(self),
            8: EqualityCommand(self),
            9: AdjustRelativeBaseCommand(self),
            99: BreakerCommand(self)
        }
        operations[self.opcode]()

    def run(self):
        while not self.stop:
            self.computation()
        if self.data[self.address] == 3:
            self.stop = False
        return self


class Command:
    def __init__(self, intcode_computer: IntcodeComputer) -> None:
        """"""
        self.intcode_computer = intcode_computer

    def nth_parameter(self, n: int) -> int:
        return self.intcode_computer.data[self.intcode_computer.address + n]

    def nth_mode(self, n: int) -> int:
        return nth_decimal_position(self.intcode_computer.data[self.intcode_computer.address], n+1)

    def nth_mode_value(self, n: int) -> int:
        mode_value_dict: Dict[int, Callable] = {
            0: lambda x: self.intcode_computer.data[x],
            1: lambda x: x,
            2: lambda x: self.intcode_computer.data[x + self.intcode_computer.relative_base]
        }
        return mode_value_dict[self.nth_mode(n)](self.nth_parameter(n))


class BinaryCommand(Command):
    def __init__(self, intcode_computer: IntcodeComputer, opcode_operator: Callable) -> None:
        super().__init__(intcode_computer)
        self.opcode_operator = opcode_operator

    def __call__(self) -> None:
        self.intcode_computer.data[self.nth_parameter(3) + self.nth_mode(
            3) // 2 * self.intcode_computer.relative_base] = self.opcode_operator(self.nth_mode_value(1), self.nth_mode_value(2))
        self.intcode_computer.address += 4


class AddCommand(BinaryCommand):
    def __init__(self, intcode_computer: IntcodeComputer) -> None:
        super().__init__(intcode_computer, operator.add)


class MulCommand(BinaryCommand):
    def __init__(self, intcode_computer: IntcodeComputer) -> None:
        super().__init__(intcode_computer, operator.mul)


class InputCommand(Command):
    def __call__(self) -> None:
        if self.intcode_computer.inpt is not None:
            self.intcode_computer.data[self.nth_parameter(
                1) + self.nth_mode(1) // 2 * self.intcode_computer.relative_base] = self.intcode_computer.inpt
            self.intcode_computer.inpt = None
            self.intcode_computer.address += 2
        else:
            self.intcode_computer.stop = True


class OutputCommand(Command):
    def __call__(self) -> None:
        self.intcode_computer.outputs.append(self.nth_mode_value(1))
        self.intcode_computer.address += 2


class JumpCommand(Command):
    def __init__(self, intcode_computer: IntcodeComputer, truth_value: bool) -> None:
        super().__init__(intcode_computer)
        self.truth_value = truth_value

    def __call__(self) -> None:
        if (self.nth_mode_value(1) != 0) is self.truth_value:
            self.intcode_computer.address = self.nth_mode_value(2)
        else:
            self.intcode_computer.address += 3


class JumpIfTrueCommand(JumpCommand):
    def __init__(self, intcode_computer: IntcodeComputer) -> None:
        super().__init__(intcode_computer, True)


class JumpIfFalseCommand(JumpCommand):
    def __init__(self, intcode_computer: IntcodeComputer) -> None:
        super().__init__(intcode_computer, False)


class LessThanCommand(BinaryCommand):
    def __init__(self, intcode_computer: IntcodeComputer) -> None:
        super().__init__(intcode_computer, operator.lt)


class EqualityCommand(BinaryCommand):
    def __init__(self, intcode_computer: IntcodeComputer) -> None:
        super().__init__(intcode_computer, operator.eq)


class AdjustRelativeBaseCommand(Command):
    def __call__(self) -> None:
        self.intcode_computer.relative_base += self.nth_mode_value(1)
        self.intcode_computer.address += 2


class BreakerCommand(Command):
    def __call__(self) -> None:
        self.intcode_computer.stop = True
