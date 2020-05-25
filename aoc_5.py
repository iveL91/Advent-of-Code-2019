"""
    aoc_5
    https://adventofcode.com/2019/day/5
"""

from typing import List
from aoc_5_lib import data_input, part_1, part_2


DATA: List[int] = data_input("aoc_5_data.txt")

# Part 1
ID_1: int = 1
PART_1: int = part_1(DATA, ID_1)
print(f"Part 1: {PART_1} is {PART_1 == 11933517}")

# Part 2
ID_2: int = 5
PART_2: int = part_2(DATA, ID_2)
print(f"Part 2: {PART_2} is {PART_2 == 10428568}")
