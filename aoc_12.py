"""
    aoc_12
    https://adventofcode.com/2019/day/12
"""

from libs.aoc_12_lib import data_input, part_1, part_2


def main() -> None:
    universe = data_input("data/aoc_12_data.txt")

    # Part 1
    p_1 = part_1(universe)
    print(f"Part 1: {p_1} is {p_1 == 10198}")

    # Part 2
    p_2 = part_2(universe)
    print(f"Part 2: {p_2} is {p_2 == 271_442_326_847_376}")


if __name__ == "__main__":
    main()
