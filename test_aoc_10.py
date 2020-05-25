"""test_aoc_10"""

import unittest
from typing import List
from aoc_10_lib import data_input, part_1, part_2


class TestAoC10(unittest.TestCase):
    """"""

    def test_part_1(self):
        """"""
        data: List[List[int]] = data_input("aoc_10_data_test_1.txt")
        self.assertEqual(part_1(data), 8)

        data: List[List[int]] = data_input("aoc_10_data_test_2.txt")
        self.assertEqual(part_1(data), 33)

        data: List[List[int]] = data_input("aoc_10_data_test_3.txt")
        self.assertEqual(part_1(data), 35)

        data: List[List[int]] = data_input("aoc_10_data_test_4.txt")
        self.assertEqual(part_1(data), 41)

        data: List[List[int]] = data_input("aoc_10_data_test_5.txt")
        self.assertEqual(part_1(data), 210)

    def test_part_2(self):
        """"""
        data: List[List[int]] = data_input("aoc_10_data_test_5.txt")
        self.assertEqual(part_2(data), 802)


if __name__ == '__main__':
    unittest.main()
