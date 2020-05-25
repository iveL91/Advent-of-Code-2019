"""aoc_4_lib"""

from typing import List


def data_input(filename: str) -> List[str]:
    """"""
    with open(filename) as f:
        return f.read().split("-")


def adjacent(number: int) -> bool:
    """"""
    string = str(number)
    adj: bool = False
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            adj = True
            break
    return adj


def not_decreasing(number: int) -> bool:
    """"""
    string: str = str(number)
    not_dec: bool = True
    for i in range(len(string) - 1):
        if int(string[i]) > int(string[i + 1]):
            not_dec = False
            break
    return not_dec


def strict_adjacent(number: int) -> bool:
    """"""
    string = str(number)
    adj: bool = False
    pair_adj: bool = False
    for i in range(len(string) - 1):
        if not adj:
            if string[i] == string[i + 1]:
                adj = True
                pair_adj = True
        else:
            if string[i] == string[i + 1]:
                adj = True
                pair_adj = False
            elif not pair_adj:
                adj = False
            else:
                break
    return pair_adj


def part_1(data: List[str]) -> int:
    """"""
    minimum: int = int(data[0])
    maximum: int = int(data[1])

    return len([i for i in range(minimum, maximum) if (adjacent(i) and not_decreasing(i))])


def part_2(data: List[str]) -> int:
    """"""
    minimum: int = int(data[0])
    maximum: int = int(data[1])

    return len([i for i in range(minimum, maximum) if (strict_adjacent(i) and not_decreasing(i))])
