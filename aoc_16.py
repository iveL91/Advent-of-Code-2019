"""
    aoc_16
    https://adventofcode.com/2019/day/16
"""

import time
import resource
from libs.aoc_16_lib import data_input, part_1  # , part_2


def main() -> None:
    time_start = time.perf_counter()
    signal = data_input("data/aoc_16_data.txt")

    # Part 1
    p_1: int = part_1(signal)
    print(f"Part 1: {p_1} is {p_1 == 19944447}")

    time_elapsed = (time.perf_counter() - time_start)
    memMb = resource.getrusage(
        resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print("%5.1f secs %5.1f MByte" % (time_elapsed, memMb))

    # # Part 2
    # PART_2: int = part_2(SIGNAL)
    # print(f"Part 2: {PART_2} is {PART_2 == 1120408}")


if __name__ == "__main__":
    main()
