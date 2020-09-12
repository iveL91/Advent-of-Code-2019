"""test_aoc_01"""

import unittest
from typing import List
from libs.aoc_01_lib import fuel_calc, part_2


class TestAoC01(unittest.TestCase):
    """()"""

    def test_fuel_calc(self):
        """()"""
        data: int = 12
        result = fuel_calc(data)
        self.assertEqual(result, 2)

        data: int = 14
        result = fuel_calc(data)
        self.assertEqual(result, 2)

        data: int = 1969
        result = fuel_calc(data)
        self.assertEqual(result, 654)

        data: int = 100756
        result = fuel_calc(data)
        self.assertEqual(result, 33583)

    def test_part_2(self):
        """()"""
        data: List[int] = [14]
        result = part_2(data)
        self.assertEqual(result, 2)

        data: List[int] = [1969]
        result = part_2(data)
        self.assertEqual(result, 966)

        data: List[int] = [100756]
        result = part_2(data)
        self.assertEqual(result, 50346)


if __name__ == "__main__":
    unittest.main()
