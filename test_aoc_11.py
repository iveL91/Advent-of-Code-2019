"""test_aoc_11"""

import unittest
from libs.aoc_lib import data_input
from libs.aoc_11_lib import part_1


class TestAoC11(unittest.TestCase):
    def test_part_1(self):
        data = data_input("data/aoc_11_data_test.txt") + [0]*100
        result = part_1(data, grid_size=5)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
