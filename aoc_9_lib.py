"""aoc_9_lib"""

from typing import List
from aoc_lib import IntcodeComputer

def data_input(filename: str) -> List[int]:
    with open(filename) as f:
        return [int(number) for number in f.read().split(",")]


def part_1(data: List[int], inpt: int) -> int:
    """Part 1"""
    return IntcodeComputer(data, inpt, extension=1000000).run().outputs[-1]   # extension <= 1000000


def part_2(data: List[int], inpt: int) -> int:
    """Part 2"""
    return part_1(data, inpt)
