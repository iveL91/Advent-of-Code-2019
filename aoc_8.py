"""
    aoc_8
    https://adventofcode.com/2019/day/8
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import List
from aoc_8_lib import data_input, part_1, part_2


DATA: List[int] = data_input("aoc_8_data.txt")

# Part 1
WIDTH: int = 25
HEIGHT: int = 6
PART_1: int = part_1(DATA, WIDTH, HEIGHT)
print(f"Part 1: {PART_1} is {PART_1 == 1716}")

# Part 2
PART_2: List[List[int]] = part_2(DATA, WIDTH, HEIGHT)

IMAGE = np.array(PART_2)
print("Part 2: KFABY")
plt.imshow(IMAGE, cmap='gray')
plt.show()
