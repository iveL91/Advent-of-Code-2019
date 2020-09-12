"""test_aoc_04"""

import unittest
from libs.aoc_04_lib import adjacent, not_decreasing, strict_adjacent


class TestAoC04(unittest.TestCase):
    """()"""

    def test_adjacent(self):
        """()"""
        data: int = 122345
        output: bool = True
        result = adjacent(data)
        self.assertEqual(result, output)

        data: int = 123789
        output: bool = False
        result = adjacent(data)
        self.assertEqual(result, output)

    def test_not_decreasing(self):
        """()"""
        data: int = 111123
        output: bool = True
        result = not_decreasing(data)
        self.assertEqual(result, output)

        data: int = 135679
        output: bool = True
        result = not_decreasing(data)
        self.assertEqual(result, output)

        data: int = 111111
        output: bool = True
        result = not_decreasing(data)
        self.assertEqual(result, output)

        data: int = 223450
        output: bool = False
        result = not_decreasing(data)
        self.assertEqual(result, output)

        data: int = 112233
        output: bool = True
        result = not_decreasing(data)
        self.assertEqual(result, output)

    def test_strict_adjacent(self):
        """()"""
        data: int = 112233
        output: bool = True
        result = strict_adjacent(data)
        self.assertEqual(result, output)

        data: int = 123444
        output: bool = False
        result = strict_adjacent(data)
        self.assertEqual(result, output)

        data: int = 111122
        output: bool = True
        result = strict_adjacent(data)
        self.assertEqual(result, output)


if __name__ == "__main__":
    unittest.main()
