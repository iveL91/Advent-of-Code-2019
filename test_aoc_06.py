"""test_aoc_06"""

import unittest
from libs.aoc_06_lib import data_input, calc_orbits, orbit_counter, part_1, orbit_chain, part_2


class TestAoC06(unittest.TestCase):
    """()"""

    def test_orbit_counter(self):
        """()"""
        data = data_input("data/aoc_06_data_test_1.txt")
        orbits = calc_orbits(data)
        result = orbit_counter(orbits, "D", 0)
        self.assertEqual(result, 3)

    def test_part_1(self):
        """()"""
        data = data_input("data/aoc_06_data_test_1.txt")
        result = part_1(data)
        self.assertEqual(result, 42)

    def test_orbit_chain(self):
        """()"""
        data = data_input("data/aoc_06_data_test_2.txt")
        orbits = calc_orbits(data)
        result = orbit_chain(orbits, "YOU", [])
        self.assertEqual(result, ["K", "J", "E", "D", "C", "B", "COM"])

        data = data_input("data/aoc_06_data_test_2.txt")
        orbits = calc_orbits(data)
        result = orbit_chain(orbits, "SAN", [])
        self.assertEqual(result, ["I", "D", "C", "B", "COM"])

    def test_part_2(self):
        """()"""
        data = data_input("data/aoc_06_data_test_2.txt")
        result = part_2(data)
        self.assertEqual(result, 4)


if __name__ == "__main__":
    unittest.main()
