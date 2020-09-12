"""
    aoc_09
    https://adventofcode.com/2019/day/9
"""

from libs.aoc_lib import data_input
from libs.aoc_09_lib import part_1, part_2


def main() -> None:
    data = data_input("data/aoc_09_data.txt")

    # Part 1
    inpt: int = 1
    p_1 = part_1(data, inpt)
    print(f"Part 1: {p_1} is {p_1 == 3780860499}")

    # Part 2
    inpt: int = 2
    p_2 = part_2(data, inpt)
    print(f"Part 2: {p_2} is {p_2 == 33343}")


if __name__ == "__main__":
    main()
