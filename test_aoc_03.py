"""test_aoc_03"""

import unittest
from libs.aoc_03_lib import part_1, part_2


class TestAoC03(unittest.TestCase):
    """()"""

    def test_part_1(self):
        """()"""
        data: str = "R8,U5,L5,D3\nU7,R6,D4,L4"
        result = part_1(data)
        self.assertEqual(result, 6)

        data: str = "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83"
        result = part_1(data)
        self.assertEqual(result, 159)

        data: str = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
        result = part_1(data)
        self.assertEqual(result, 135)

    def test_part_2(self):
        """()"""
        data: str = "R8,U5,L5,D3\nU7,R6,D4,L4"
        result = part_2(data)
        self.assertEqual(result, 30)

        data: str = "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83"
        result = part_2(data)
        self.assertEqual(result, 610)

        data: str = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
        result = part_2(data)
        self.assertEqual(result, 410)


if __name__ == "__main__":
    unittest.main()
