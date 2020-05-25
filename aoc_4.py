"""
    aoc_4
    https://adventofcode.com/2019/day/4
"""

from typing import List
from aoc_4_lib import data_input, part_1, part_2


DATA: List[str] = data_input("aoc_4_data.txt")

# Part 1
PART_1: int = part_1(DATA)
print(f"Part 1: {PART_1} is {PART_1 == 2220}")

# Part 2
PART_2: int = part_2(DATA)
print(f"Part 2: {PART_2} is {PART_2 == 1515}")
