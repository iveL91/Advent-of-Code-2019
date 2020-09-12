"""
    aoc_02
    https://adventofcode.com/2019/day/2
"""

from libs.aoc_lib import data_input
from libs.aoc_02_lib import part_1, part_2


def main() -> None:
    data = data_input("data/aoc_02_data.txt")

    # Part 1
    noun: int = 12
    verb: int = 2
    p_1: int = part_1(data, noun, verb)
    print(f"Part 1: {p_1} is {p_1 == 3562672}")

    # Part 2
    output: int = 19690720
    p_2: int = part_2(data, output)
    print(f"Part 2: {p_2} is {p_2 == 8250}")


if __name__ == "__main__":
    main()
