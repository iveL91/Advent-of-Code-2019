"""test_aoc_9"""

import unittest
from typing import List
from aoc_lib import IntcodeComputer


class TestAoC9(unittest.TestCase):
    """()"""

    def test_intcode_computer_computation(self):
        """Testing intcode_computer_computation"""
        data: List[int] = [109, 19]
        relative_base: int = 2000
        computer = IntcodeComputer(data, 0, 0, 0, relative_base)
        computer.intcode_computer_computation()
        result: int = computer.relative_base
        self.assertEqual(result, 2019)

        data: List[int] = [109, 19] + [0 for _ in range(10000)]
        relative_base: int = 2019
        output: int = 1234
        data[1985] = output
        computer = IntcodeComputer(data, 0, 0, 0, relative_base)
        computer.intcode_computer_computation()
        result: int = computer.data[1985]
        self.assertEqual(result, output)

    def test_intcode_computer(self):
        """Testing intcode_computer"""
        data: List[int] = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
        extension: int = 100000
        output: List[int] = data.copy()
        result: List[int] = IntcodeComputer(data.copy(), 0, 0, extension).run().outputs
        self.assertEqual(result, output)

        data: List[int] = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
        extension: int = 100000
        output: int = 16
        result: int = len(str(IntcodeComputer(data.copy(), 0, 0, extension).run().outputs[-1]))
        self.assertEqual(result, output)

        data: List[int] = [104, 1125899906842624, 99]
        extension: int = 100000
        output: int = 1125899906842624
        result: int = IntcodeComputer(data.copy(), 0, 0, extension).run().outputs[-1]
        self.assertEqual(result, output)


if __name__ == '__main__':
    unittest.main()
