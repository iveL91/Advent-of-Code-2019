"""
    aoc_05
    https://adventofcode.com/2019/day/5
"""

from libs.aoc_lib import data_input
from libs.aoc_05_lib import part_1, part_2


def main() -> None:
    data = data_input("data/aoc_05_data.txt")

    # Part 1
    id_1: int = 1
    p_1 = part_1(data, id_1)
    print(f"Part 1: {p_1} is {p_1 == 11933517}")

    # Part 2
    id_2: int = 5
    p_2 = part_2(data, id_2)
    print(f"Part 2: {p_2} is {p_2 == 10428568}")


if __name__ == "__main__":
    main()
