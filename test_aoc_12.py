"""test_aoc_12"""

import unittest
from libs.aoc_12_lib import data_input, part_1, part_2


class TestAoC12(unittest.TestCase):
    def test_part_1(self):
        universe = data_input("data/aoc_12_data_test_1.txt")
        result = part_1(universe, 10)
        self.assertEqual(result, 179)

        universe = data_input("data/aoc_12_data_test_2.txt")
        result = part_1(universe, 100)
        self.assertEqual(result, 1940)

    def test_part_2(self):
        universe = data_input("data/aoc_12_data_test_1.txt")
        result = part_2(universe)
        self.assertEqual(result, 2772)

        universe = data_input("data/aoc_12_data_test_2.txt")
        result = part_2(universe)
        self.assertEqual(result, 4686774924)


if __name__ == '__main__':
    unittest.main()
