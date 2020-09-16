"""aoc_09_lib"""

from typing import List
from libs.aoc_lib import IntcodeComputer
from libs.timer import timer


@timer
def part_1(data: List[int], inpt: int) -> int:
    """Part 1"""
    return IntcodeComputer(data, inpt, extension=1_000_000).run().outputs[-1]   # extension <= 1_000_000


@timer
def part_2(data: List[int], inpt: int) -> int:
    """Part 2"""
    return part_1(data, inpt)
