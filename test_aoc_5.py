"""test_aoc_5"""

import unittest
from typing import List
from aoc_5_lib import part_1, part_2


class TestAoC5(unittest.TestCase):
    """()"""

    def test_part_1(self):
        """()"""
        data: List[int] = [1002, 4, 3, 4, 33]
        result: int = part_1(data, 1)
        self.assertEqual(result, 0)

        data: List[int] = [1101, 100, -1, 4, 0]
        result: int = part_1(data, 1)
        self.assertEqual(result, 0)

    def test_part_2(self):
        """()"""
        data: List[int] = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        result: int = part_2(data, 7)
        self.assertEqual(result, 0)
        result: int = part_2(data, 8)
        self.assertEqual(result, 1)
        result: int = part_2(data, 9)
        self.assertEqual(result, 0)

        data: List[int] = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        result: int = part_2(data, 7)
        self.assertEqual(result, 1)
        result: int = part_2(data, 8)
        self.assertEqual(result, 0)
        result: int = part_2(data, 9)
        self.assertEqual(result, 0)

        data: List[int] = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        result: int = part_2(data, 7)
        self.assertEqual(result, 0)
        result: int = part_2(data, 8)
        self.assertEqual(result, 1)
        result: int = part_2(data, 9)
        self.assertEqual(result, 0)

        data: List[int] = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        result: int = part_2(data, 7)
        self.assertEqual(result, 1)
        result: int = part_2(data, 8)
        self.assertEqual(result, 0)
        result: int = part_2(data, 9)
        self.assertEqual(result, 0)

        data: List[int] = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        result: int = part_2(data, 0)
        self.assertEqual(result, 0)
        result: int = part_2(data, 1)
        self.assertEqual(result, 1)

        data: List[int] = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
        result: int = part_2(data, 0)
        self.assertEqual(result, 0)
        result: int = part_2(data, 1)
        self.assertEqual(result, 1)

        data: List[int] = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106,
                           0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104, 999, 1105,
                           1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
        result = part_2(data, 7)
        self.assertEqual(result, 999)
        result: int = part_2(data, 8)
        self.assertEqual(result, 1000)
        result: int = part_2(data, 9)
        self.assertEqual(result, 1001)


if __name__ == "__main__":
    unittest.main()
