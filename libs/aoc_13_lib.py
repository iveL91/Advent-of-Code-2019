"""aoc_13_lib"""

import re
from libs.aoc_lib import IntcodeComputer
from typing import List, Pattern, Set, Tuple, Union
from libs.timer import timer


@timer
def part_1(intcode_computer_software: List[int]) -> int:
    """"""
    intcode_computer = IntcodeComputer(intcode_computer_software)
    intcode_computer.run()
    return intcode_computer.outputs


@timer
def part_2():
    """"""
    pass
