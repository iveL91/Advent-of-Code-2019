"""aoc_12_lib"""

import re
from math import gcd
from functools import reduce
from typing import List, Pattern, Set, Tuple, Union
from libs.timer import timer


class Moon:
    """"""

    def __init__(self, position: List[int], velocity: List[int]) -> None:
        """"""
        self.position: List[int] = position
        self.velocity: List[int] = velocity

    @property
    def kinetic_energy(self) -> int:
        """"""
        return sum((abs(vel) for vel in self.velocity))

    @property
    def potential_energy(self) -> int:
        """"""
        return sum((abs(pos) for pos in self.position))

    @property
    def total_energy(self) -> int:
        """"""
        return self.potential_energy * self.kinetic_energy

    def apply_velocity_axis(self, axis: int) -> None:
        """"""
        self.position[axis] += self.velocity[axis]


class Universe:
    """"""

    def __init__(self, moon_list: List[Moon]) -> None:
        """"""
        self.moons: List[Moon] = moon_list

    @property
    def total_energy(self) -> int:
        """"""
        return sum((moon.total_energy for moon in self.moons))

    def apply_gravity_axis(self, axis: int) -> None:
        """"""
        for moon_1_index, moon_1 in enumerate(self.moons):
            for moon_2 in self.moons[moon_1_index+1:]:
                diff: int = moon_2.position[axis] - moon_1.position[axis]
                moon_1.velocity[axis] += sign(diff)
                moon_2.velocity[axis] -= sign(diff)

    def apply_velocity_axis(self, axis: int) -> None:
        """"""
        for moon in self.moons:
            moon.apply_velocity_axis(axis)

    def step_axis(self, axis: int) -> None:
        """"""
        self.apply_gravity_axis(axis)
        self.apply_velocity_axis(axis)

    def step(self) -> None:
        """"""
        for axis in range(3):
            self.step_axis(axis)


def sign(number: Union[int, float]) -> int:
    """"""
    return -1 if number < 0 else (1 if number > 0 else 0)


def data_input(filename: str) -> Universe:
    """"""
    with open(filename) as f:
        data: str = f.read()
        pattern: Pattern[str] = re.compile(
            r"<x=(-?\d+), y=(-?\d+), z=(-?\d+)>")
        matches: List[str] = re.findall(pattern, data)
        return Universe(
            [Moon([int(x), int(y), int(z)], [0, 0, 0]) for x, y, z in matches])


@timer
def part_1(universe: Universe, steps: int = 1000) -> int:
    """"""
    for _ in range(steps):
        universe.step()
    return universe.total_energy


def lcm(denominators):
    """(https://stackoverflow.com/questions/37237954/calculate-the-lcm-of-a-list-of-given-numbers-in-python)"""
    return reduce(lambda a, b: a*b // gcd(a, b), denominators)


@timer
def part_2(universe: Universe):
    """"""
    periods: List[int] = []
    for axis in range(3):
        # Determine the first element in a period and the start of the second period
        new_universe: Universe = universe
        pos_vels: Set[Tuple[Tuple[int, int]]] = set()
        new_pos_vel: Tuple[Tuple[int, int]] = tuple(
            [(moon.position[axis], moon.velocity[axis]) for moon in new_universe.moons])
        second_occurrence: int = 0
        while new_pos_vel not in pos_vels:
            pos_vels.add(new_pos_vel)
            new_universe.step_axis(axis)
            new_pos_vel = tuple(
                [(moon.position[axis], moon.velocity[axis]) for moon in new_universe.moons])
            second_occurrence += 1

        # Determine the start of the first period
        new_universe: Universe = universe
        pos_vel: Tuple[Tuple[int, int]] = tuple(
            [(moon.position[axis], moon.velocity[axis]) for moon in new_universe.moons])
        first_occurrence: int = 0
        while pos_vel != new_pos_vel:
            new_universe.step_axis(axis)
            first_occurrence += 1

        period: int = second_occurrence - first_occurrence
        periods.append(period)
    return lcm(periods)


# class ExtTuple:
#     """"""
#     tup: tuple
#     integer: int
#
#     def __init__(self, integer: int, tup: tuple):
#         """"""
#         self.integer = integer
#         self.tup = tup
#
#     def __hash__(self) -> int:
#         """"""
#         return hash(self.tup)
#
#
# def part_2(universe: Universe):
#     """"""
#     periods: List[int] = []
#     for axis in range(3):
#         # Determine the first element in a period and the start of the second period
#         new_universe: Universe = universe
#         pos_vels: Set[ExtTuple] = set()
#         new_pos_vel: Tuple[Tuple[int, int]] = tuple([(moon.position[axis], moon.velocity[axis]) for moon in new_universe.moons])
#         counter: int = 0
#         pos_val_ext: ExtTuple = ExtTuple(counter, new_pos_vel)
#         while pos_val_ext not in pos_vels:
#             pos_vels.add(pos_val_ext)
#             new_universe.step_axis(axis)
#             new_pos_vel = tuple([(moon.position[axis], moon.velocity[axis]) for moon in new_universe.moons])
#             counter += 1
#             pos_val_ext = ExtTuple(counter, new_pos_vel)
#         print("here")
#         # Determine the start of the first period
#         new_universe: Universe = universe
#         pos_vel: Tuple[Tuple[int, int]] = tuple([(moon.position[axis], moon.velocity[axis]) for moon in new_universe.moons])
#         first_occurrence: int = 0
#         while pos_vel != new_pos_vel:
#             new_universe.step_axis(axis)
#             first_occurrence += 1
#
#         period: int = counter - first_occurrence
#         periods.append(period)
#     return lcm(periods)
