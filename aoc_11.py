"""
    aoc_11
    https://adventofcode.com/2019/day/11
"""

from libs.aoc_lib import data_input
from libs.aoc_11_lib import part_1, part_2


def main() -> None:
    data = data_input("data/aoc_11_data.txt")

    # Part 1
    p_1 = part_1(data)
    print(f"Part 1: {p_1} is {p_1 == 329}")

    # Part 2
    p_2 = part_2(data)
    print(f"Part 2: {p_2} is {p_2 == 329}")


if __name__ == "__main__":
    main()
