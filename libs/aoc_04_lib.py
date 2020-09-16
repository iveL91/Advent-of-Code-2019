"""aoc_04_lib"""

from typing import List
from libs.timer import timer


def data_input(filename: str) -> List[str]:
    """"""
    with open(filename) as f:
        return f.read().split("-")


def adjacent(number: int) -> bool:
    """"""
    string = str(number)
    adj: bool
    for i, symbol in enumerate(string[:-1]):
        if symbol == string[i + 1]:
            adj = True
            break
    else:
        adj = False
    return adj


def not_decreasing(number: int) -> bool:
    """"""
    string: str = str(number)
    not_dec: bool
    for i, symbol in enumerate(string[:-1]):
        if int(symbol) > int(string[i + 1]):
            not_dec = False
            break
    else:
        not_dec = True
    return not_dec


def strict_adjacent(number: int) -> bool:
    """"""
    string: str = str(number)
    adj: bool = False
    pair_adj: bool = False
    for i, symbol in enumerate(string[:-1]):
        if not adj:
            if symbol == string[i + 1]:
                adj = True
                pair_adj = True
        else:
            if symbol == string[i + 1]:
                adj = True
                pair_adj = False
            elif not pair_adj:
                adj = False
            else:
                break
    return pair_adj


@timer
def part_1(data: List[str]) -> int:
    """"""
    minimum: int = int(data[0])
    maximum: int = int(data[1])

    return len([1 for i in range(minimum, maximum) if (adjacent(i) and not_decreasing(i))])


@timer
def part_2(data: List[str]) -> int:
    """"""
    minimum: int = int(data[0])
    maximum: int = int(data[1])

    return len([1 for i in range(minimum, maximum) if (strict_adjacent(i) and not_decreasing(i))])
