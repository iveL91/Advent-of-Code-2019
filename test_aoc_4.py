"""test_aoc_4"""

import unittest
from aoc_4_lib import adjacent, not_decreasing, strict_adjacent


class TestAoC4(unittest.TestCase):
    """()"""

    def test_adjacent(self):
        """()"""
        data: int = 122345
        output: bool = True
        result: bool = adjacent(data)
        self.assertEqual(result, output)

        data: int = 123789
        output: bool = False
        result: bool = adjacent(data)
        self.assertEqual(result, output)

    def test_not_decreasing(self):
        """()"""
        data: int = 111123
        output: bool = True
        result: bool = not_decreasing(data)
        self.assertEqual(result, output)

        data: int = 135679
        output: bool = True
        result: bool = not_decreasing(data)
        self.assertEqual(result, output)

        data: int = 111111
        output: bool = True
        result: bool = not_decreasing(data)
        self.assertEqual(result, output)

        data: int = 223450
        output: bool = False
        result: bool = not_decreasing(data)
        self.assertEqual(result, output)

        data: int = 112233
        output: bool = True
        result: bool = not_decreasing(data)
        self.assertEqual(result, output)

    def test_strict_adjacent(self):
        """()"""
        data: int = 112233
        output: bool = True
        result: bool = strict_adjacent(data)
        self.assertEqual(result, output)

        data: int = 123444
        output: bool = False
        result: bool = strict_adjacent(data)
        self.assertEqual(result, output)

        data: int = 111122
        output: bool = True
        result: bool = strict_adjacent(data)
        self.assertEqual(result, output)

if __name__ == "__main__":
    unittest.main()
