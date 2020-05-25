"""aoc_1_lib"""

from typing import List


def data_input(filename: str) -> List[int]:
    with open(filename) as f:
        return [int(number) for number in f.read().split("\n")]

def fuel_calc(mass: int) -> int:
    return mass//3 - 2


def added_fuel_calc(fuel: int) -> int:
    """(int -> int)"""
    added_fuels: int = 0
    fuel: int = fuel // 3 - 2
    while fuel >= 0:
        added_fuels += fuel
        fuel = fuel // 3 - 2
    return added_fuels


def part_1(data: List[int]) -> int:
    """Part 1"""
    total_fuel: int = 0

    for mass in data:
        fuel: int = fuel_calc(mass)
        total_fuel += fuel
    return total_fuel


def part_2(data: List[int]) -> int:
    """Part 2"""
    total_fuel: int = 0

    for mass in data:
        fuel: int = fuel_calc(mass)
        total_fuel += fuel + added_fuel_calc(fuel)
    return total_fuel
