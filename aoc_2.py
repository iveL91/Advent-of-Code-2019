"""
    aoc_2
    https://adventofcode.com/2019/day/2
"""

from typing import List
from aoc_2_lib import data_input, part_1, part_2


DATA: List[int] = data_input("aoc_2_data.txt")

# Part 1
NOUN: int = 12
VERB: int = 2
PART_1: int = part_1(DATA, NOUN, VERB)
print(f"Part 1: {PART_1} is {PART_1 == 3562672}")

# Part 2
OUTPUT: int = 19690720
PART_2: int = part_2(DATA, OUTPUT)
print(f"Part 2: {PART_2} is {PART_2 == 8250}")
