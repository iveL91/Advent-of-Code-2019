"""test_aoc_6"""

import unittest
from typing import List
from aoc_6_lib import data_input, orbits_objects, orbit_counter, part_1, orbit_chain, part_2


class TestAoC6(unittest.TestCase):
    """()"""

    def test_orbit_counter(self):
        """()"""
        data: str = data_input("aoc_6_data_test_1.txt")
        orbits = orbits_objects(data)[0]
        result: int = orbit_counter(orbits, "D", 0)
        self.assertEqual(result, 3)

    def test_part_1(self):
        """()"""
        data: str = data_input("aoc_6_data_test_1.txt")
        result: int = part_1(data)
        self.assertEqual(result, 42)

    def test_orbit_chain(self):
        """()"""
        data: str = data_input("aoc_6_data_test_2.txt")
        orbits: List[List[str]] = orbits_objects(data)[0]
        result: List[str] = orbit_chain(orbits, "YOU", [])
        self.assertEqual(result, ["K", "J", "E", "D", "C", "B", "COM"])

        data: str = data_input("aoc_6_data_test_2.txt")
        orbits: List[List[str]] = orbits_objects(data)[0]
        result: List[str] = orbit_chain(orbits, "SAN", [])
        self.assertEqual(result, ["I", "D", "C", "B", "COM"])

    def test_part_2(self):
        """()"""
        data: str = data_input("aoc_6_data_test_2.txt")
        result: int = part_2(data)
        self.assertEqual(result, 4)


if __name__ == "__main__":
    unittest.main()
