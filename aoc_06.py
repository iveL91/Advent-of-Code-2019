"""
    aoc_06
    https://adventofcode.com/2019/day/6
"""

from libs.aoc_06_lib import data_input, part_1, part_2


def main() -> None:
    data: str = data_input("data/aoc_06_data.txt")

    # Part 1
    p_1: int = part_1(data)
    print(f"Part 1: {p_1} is {p_1 == 251208}")

    # Part 2
    p_2: int = part_2(data)
    print(f"Part 2: {p_2} is {p_2 == 397}")


if __name__ == "__main__":
    main()
