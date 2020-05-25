"""
    aoc_10
    https://adventofcode.com/2019/day/10
"""

from aoc_10_lib import data_input, part_1, part_2


DATA = data_input("aoc_10_data.txt")

# Part 1
PART_1 = part_1(DATA)
print(f"Part 1: {PART_1} is {PART_1 == 329}")

# Part 2
PART_2 = part_2(DATA)
print(f"Part 2: {PART_2} is {PART_2 == 512}")
