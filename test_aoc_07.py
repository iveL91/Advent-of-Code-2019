"""test_aoc_07"""

import unittest
from typing import List
from libs.aoc_lib import data_input
from libs.aoc_07_lib import AmplifierSystem


class TestAoC07(unittest.TestCase):
    """()"""

    def test_thruster_signal(self):
        """()"""
        data = data_input("data/aoc_07_data_test_1.txt")
        phases: List[int] = [4, 3, 2, 1, 0]
        system = AmplifierSystem(data, phases)
        result = system.thruster_signal()
        exp_result: int = 43210
        self.assertEqual(result, exp_result)

        data = data_input("data/aoc_07_data_test_2.txt")
        phases: List[int] = [0, 1, 2, 3, 4]
        system = AmplifierSystem(data, phases)
        result = system.thruster_signal()
        exp_result: int = 54321
        self.assertEqual(result, exp_result)

        data = data_input("data/aoc_07_data_test_3.txt")
        phases: List[int] = [1, 0, 4, 3, 2]
        system = AmplifierSystem(data, phases)
        result = system.thruster_signal()
        exp_result: int = 65210
        self.assertEqual(result, exp_result)

        data = data_input("data/aoc_07_data_test_4.txt")
        phases: List[int] = [9, 8, 7, 6, 5]
        system = AmplifierSystem(data, phases)
        result = system.thruster_signal()
        exp_result: int = 139629729
        self.assertEqual(result, exp_result)

        data = data_input("data/aoc_07_data_test_5.txt")
        phases: List[int] = [9, 7, 8, 5, 6]
        system = AmplifierSystem(data, phases)
        result = system.thruster_signal()
        exp_result: int = 18216
        self.assertEqual(result, exp_result)


if __name__ == "__main__":
    unittest.main()
