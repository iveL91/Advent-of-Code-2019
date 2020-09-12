"""aoc_01_lib"""

from typing import Iterable, List


def data_input(filename: str) -> List[int]:
    with open(filename) as f:
        return [int(number) for number in f.read().splitlines()]


def fuel_calc(mass: int) -> int:
    return mass//3 - 2


def added_fuel_calc(fuel: int) -> int:
    """"""
    added_fuels: int = 0
    fuel: int = fuel // 3 - 2
    while fuel >= 0:
        added_fuels += fuel
        fuel = fuel // 3 - 2
    return added_fuels


def part_1(data: Iterable[int]) -> int:
    """Part 1"""
    return sum(fuel_calc(mass) for mass in data)


def part_2(data: Iterable[int]) -> int:
    """Part 2"""
    fuels = (fuel_calc(mass) for mass in data)
    return sum(fuel + added_fuel_calc(fuel) for fuel in fuels)
