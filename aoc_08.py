"""
    aoc_08
    https://adventofcode.com/2019/day/8
"""

import numpy as np
import matplotlib.pyplot as plt
from libs.aoc_08_lib import data_input, part_1, part_2


def main() -> None:
    data = data_input("data/aoc_08_data.txt")

    # Part 1
    width: int = 25
    height: int = 6
    p_1: int = part_1(data, width, height)
    print(f"Part 1: {p_1} is {p_1 == 1716}")

    # Part 2
    p_2 = part_2(data, width, height)

    IMAGE = np.array(p_2)
    print("Part 2: KFABY")
    plt.imshow(IMAGE, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
