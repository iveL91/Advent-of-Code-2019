"""test_aoc_16"""

import unittest
from libs.aoc_16_lib import data_input, part_1, part_2


class TestAoC16(unittest.TestCase):
    def test_part_1(self):
        signal = data_input("data/aoc_16_data_test_1.txt")
        result = part_1(signal, 4)
        self.assertEqual(result, 1029498)

        signal = data_input("data/aoc_16_data_test_2.txt")
        result = part_1(signal)
        self.assertEqual(result, 24176176)

        signal = data_input("data/aoc_16_data_test_3.txt")
        result = part_1(signal)
        self.assertEqual(result, 73745418)

        signal = data_input("data/aoc_16_data_test_4.txt")
        result = part_1(signal)
        self.assertEqual(result, 52432133)

    def test_part_2(self):
        #     signal = data_input("data/aoc_16_data_test_5.txt")
        #     result: int = part_2(signal)
        #     self.assertEqual(result, 84462026)

        # signal = data_input("data/aoc_16_data_test_6.txt")
        # result: int = part_2(signal)
        # self.assertEqual(result, 78725270)
        #
        signal = data_input("data/aoc_16_data_test_7.txt")
        result = part_2(signal)
        self.assertEqual(result, 53553731)


if __name__ == '__main__':
    unittest.main()
