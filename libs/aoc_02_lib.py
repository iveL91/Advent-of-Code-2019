"""aoc_02_lib"""

import itertools
from typing import List, Optional
from libs.aoc_lib import IntcodeComputer
from libs.timer import timer


@timer
def part_1(data: List[int], noun: Optional[int] = None, verb: Optional[int] = None) -> int:
    """Part 1"""
    data[1] = noun or data[1]
    data[2] = verb or data[2]

    return IntcodeComputer(data).run().data[0]


@timer
def part_2(data: List[int], output: int) -> int:
    """Part 2"""
    wanted_noun: int
    wanted_verb: int

    for noun, verb in itertools.product(range(100), range(100)):
        if part_1(data, noun, verb) == output:
            wanted_noun, wanted_verb = noun, verb
            break
    else:
        wanted_noun, wanted_verb = 0, 0

    return 100 * wanted_noun + wanted_verb
