"""test_aoc_08"""

import unittest
from typing import List
from libs.aoc_08_lib import data_input, partitioning_2d, part_2


class TestAoC08(unittest.TestCase):
    """()"""

    def test_partitioning_2d(self):
        """"""
        data = data_input("data/aoc_08_data_test_1.txt")
        width: int = 3
        height: int = 2
        result = partitioning_2d(data, width, height)
        exp_result: List[List[List[int]]] = [
            [[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [0, 1, 2]]]
        self.assertEqual(result, exp_result)

    def test_part_2(self):
        """"""
        data = data_input("data/aoc_08_data_test_2.txt")
        width: int = 2
        height: int = 2
        result = part_2(data, width, height)
        exp_result: List[List[int]] = [[0, 1], [1, 0]]
        self.assertEqual(result, exp_result)


if __name__ == '__main__':
    unittest.main()
