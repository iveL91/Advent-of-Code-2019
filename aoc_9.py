"""
    aoc_9
    https://adventofcode.com/2019/day/9
"""

from typing import List
from aoc_9_lib import data_input, part_1, part_2


DATA: List[int] = data_input("aoc_9_data.txt")

# Part 1
INPT: int = 1
PART_1: int = part_1(DATA, INPT)
print(f"Part 1: {PART_1} is {PART_1 == 3780860499}")

# Part 2
INPT: int = 2
PART_2: int = part_2(DATA, INPT)
print(f"Part 2: {PART_2} is {PART_2 == 33343}")
