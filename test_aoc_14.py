"""test_aoc_14"""

import unittest
from libs.aoc_14_lib import data_input, part_1, part_2


class TestAoC14(unittest.TestCase):
    def test_part_1(self):
        formulas = data_input("data/aoc_14_data_test_1.txt")
        result = part_1(formulas)
        self.assertEqual(result, 31)

        formulas = data_input("data/aoc_14_data_test_2.txt")
        result = part_1(formulas)
        self.assertEqual(result, 165)

        formulas = data_input("data/aoc_14_data_test_3.txt")
        result = part_1(formulas)
        self.assertEqual(result, 13312)

        formulas = data_input("data/aoc_14_data_test_4.txt")
        result = part_1(formulas)
        self.assertEqual(result, 180697)

        formulas = data_input("data/aoc_14_data_test_5.txt")
        result = part_1(formulas)
        self.assertEqual(result, 2210736)

    def test_part_2(self):
        formulas = data_input("data/aoc_14_data_test_3.txt")
        result = part_2(formulas)
        self.assertEqual(result, 82892753)

        formulas = data_input("data/aoc_14_data_test_4.txt")
        result = part_2(formulas)
        self.assertEqual(result, 5586022)

        formulas = data_input("data/aoc_14_data_test_5.txt")
        result = part_2(formulas)
        self.assertEqual(result, 460664)


if __name__ == '__main__':
    unittest.main()
