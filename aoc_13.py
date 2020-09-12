"""
    aoc_13
    https://adventofcode.com/2019/day/13
"""

from libs.aoc_lib import data_input
from libs.aoc_13_lib import part_1, part_2


def main() -> None:
    intcode_computer_software = data_input("data/aoc_13_data.txt")

    # Part 1
    p_1 = part_1(intcode_computer_software)
    print(f"Part 1: {p_1} is {p_1 == 10198}")

    # # Part 2
    # p_2 = part_2(UNIVERSE)
    # print(f"Part 2: {p_2} is {p_2 == 271442326847376}")


if __name__ == "__main__":
    main()
