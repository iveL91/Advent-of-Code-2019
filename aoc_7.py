"""
    aoc_7
    https://adventofcode.com/2019/day/7
"""

from typing import List
from aoc_7_lib import data_input, part_1, part_2


DATA: List[int] = data_input("aoc_7_data.txt")

# Part 1
PART_1: int = part_1(DATA)
print(f"Part 1: {PART_1} is {PART_1 == 19650}")

# Part 2
PART_2: int = part_2(DATA)
print(f"Part 2: {PART_2} is {PART_2 == 35961106}")
