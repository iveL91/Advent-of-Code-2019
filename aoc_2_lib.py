"""aoc_2_lib"""

import itertools
from typing import List, Union
from aoc_lib import IntcodeComputer


def data_input(filename: str) -> List[int]:
    """"""
    with open(filename) as f:
        return [int(number) for number in f.read().split(",")]


def part_1(data: List[int], noun: Union[None, int] = None, verb: Union[None, int] = None) -> int:
    """Part 1"""
    if isinstance(data, str):
        data: List[int] = [int(number) for number in data.split(",")]

    if noun is not None:
        data[1] = noun
    if noun is not None:
        data[2] = verb

    return IntcodeComputer(data).run().data[0]


def part_2(data: List[int], output: int) -> int:
    """Part 2"""
    wanted_noun: int = 0
    wanted_verb: int = 0

    for noun, verb in itertools.product(range(100), range(100)):
        if part_1(data, noun, verb) == output:
            wanted_verb = verb
            wanted_noun = noun
            break

    return 100 * wanted_noun + wanted_verb
