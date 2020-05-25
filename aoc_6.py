"""
    aoc_6
    https://adventofcode.com/2019/day/6
"""

from aoc_6_lib import data_input, part_1, part_2


DATA: str = data_input("aoc_6_data.txt")

# Part 1
PART_1: int = part_1(DATA)
print(f"Part 1: {PART_1} is {PART_1 == 251208}")

# Part 2
PART_2: int = part_2(DATA)
print(f"Part 2: {PART_2} is {PART_2 == 397}")
