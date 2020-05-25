"""
    aoc_3
    https://adventofcode.com/2019/day/3
"""

from aoc_3_lib import data_input, part_1, part_2


DATA: str = data_input("aoc_3_data.txt")

# Part 1
PART_1: int = part_1(DATA)
print(f"Part 1: {PART_1} is {PART_1 == 855}")

# Part 2
PART_2: int = part_2(DATA)
print(f"Part 2: {PART_2} is {PART_2 == 11238}")
