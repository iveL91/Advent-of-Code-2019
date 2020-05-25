"""aoc_5_lib"""

from typing import List
from aoc_lib import IntcodeComputer


def data_input(filename: str) -> List[int]:
    with open(filename) as f:
        return [int(number) for number in f.read().split(",")]


def part_1(data: List[int], ship_id: int) -> int:
    """"""
    outputs: List[int] = IntcodeComputer(data, inpt=ship_id).run().outputs
    if outputs:
        return outputs[-1]
    else:
        return 0


def part_2(data: List[int], ship_id: int) -> int:
    """"""
    return IntcodeComputer(data, inpt=ship_id).run().outputs[-1]
