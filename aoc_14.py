"""
    aoc_14
    https://adventofcode.com/2019/day/14
"""

from libs.aoc_14_lib import data_input, part_1, part_2


def main() -> None:
    formulas = data_input("data/aoc_14_data.txt")

    # Part 1
    p_1 = part_1(formulas)
    print(f"Part 1: {p_1} is {p_1 == 2556890}")

    # Part 2
    p_2 = part_2(formulas)
    print(f"Part 2: {p_2} is {p_2 == 1120408}")


if __name__ == "__main__":
    main()
