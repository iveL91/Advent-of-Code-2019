"""test_aoc_7"""

import unittest
from typing import List, Dict, Any
from aoc_7_lib import data_input, thruster_signal, initializing_amplifiers


class TestAoC7(unittest.TestCase):
    """()"""

    def test_thruster_signal(self):
        """()"""
        data: List[int] = data_input("aoc_7_data_test_1.txt")
        phases: List[int] = [4, 3, 2, 1, 0]
        amplifiers: List[Dict[str, Any]] = initializing_amplifiers(data, phases)
        result: int = thruster_signal(amplifiers)
        exp_result: int = 43210
        self.assertEqual(result, exp_result)

        data: List[int] = data_input("aoc_7_data_test_2.txt")
        phases: List[int] = [0, 1, 2, 3, 4]
        amplifiers: List[Dict[str, Any]] = initializing_amplifiers(data, phases)
        result: int = thruster_signal(amplifiers)
        exp_result: int = 54321
        self.assertEqual(result, exp_result)

        data: List[int] = data_input("aoc_7_data_test_3.txt")
        phases: List[int] = [1, 0, 4, 3, 2]
        amplifiers: List[Dict[str, Any]] = initializing_amplifiers(data, phases)
        result: int = thruster_signal(amplifiers)
        exp_result: int = 65210
        self.assertEqual(result, exp_result)

        data: List[int] = data_input("aoc_7_data_test_4.txt")
        phases: List[int] = [9, 8, 7, 6, 5]
        amplifiers: List[Dict[str, Any]] = initializing_amplifiers(data, phases)
        result: int = thruster_signal(amplifiers)
        exp_result: int = 139629729
        self.assertEqual(result, exp_result)

        data: List[int] = data_input("aoc_7_data_test_5.txt")
        phases: List[int] = [9, 7, 8, 5, 6]
        amplifiers: List[Dict[str, Any]] = initializing_amplifiers(data, phases)
        result: int = thruster_signal(amplifiers)
        exp_result: int = 18216
        self.assertEqual(result, exp_result)


if __name__ == "__main__":
    unittest.main()
