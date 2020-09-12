"""aoc_05_lib"""

from typing import List
from libs.aoc_lib import IntcodeComputer


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
