"""aoc_13_lib"""

import re
from libs.aoc_lib import IntcodeComputer
from typing import List, Pattern, Set, Tuple, Union


def part_1(intcode_computer_software: List[int]) -> int:
    """"""
    intcode_computer: IntcodeComputer = IntcodeComputer(intcode_computer_software)
    intcode_computer.run()
    return intcode_computer.outputs


def part_2():
    """"""
    pass
