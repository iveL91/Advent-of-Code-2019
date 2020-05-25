"""test_aoc_2"""

import unittest
from typing import List
from aoc_lib import IntcodeComputer
from aoc_2_lib import part_1


class TestAoC2(unittest.TestCase):
    """()"""

    def test_intcode_computer(self):
        """()"""
        data: List[int] = [1, 0, 0, 0, 99]
        outputs: List[int] = [2, 0, 0, 0, 99]
        result: List[int] = IntcodeComputer(data).run().data
        self.assertEqual(result, outputs)

        data: List[int] = [2, 3, 0, 3, 99]
        output: List[int] = [2, 3, 0, 6, 99]
        result: List[int] = IntcodeComputer(data).run().data
        self.assertEqual(result, output)

        data: List[int] = [2, 4, 4, 5, 99, 0]
        output: List[int] = [2, 4, 4, 5, 99, 9801]
        result: List[int] = IntcodeComputer(data).run().data
        self.assertEqual(result, output)

        data: List[int] = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        output: List[int] = [30, 1, 1, 4, 2, 5, 6, 0, 99]
        result: List[int] = IntcodeComputer(data).run().data
        self.assertEqual(result, output)

    def test_part_1(self):
        """()"""
        data: List[int] = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        output: int = 3500
        result: int = part_1(data)
        self.assertEqual(result, output)


if __name__ == "__main__":
    unittest.main()
