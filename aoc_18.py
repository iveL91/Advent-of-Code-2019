"""
    aoc_18
    https://adventofcode.com/2019/day/18
"""

import string
from typing import Dict, List, Set, Tuple


def data_input(filename: str) -> List[str]:
    with open(filename) as f:
        return f.read().splitlines()


class UndergroundVault:
    dct: Dict[str, str] = {"entrance": "@",
                           "open_passage": ".",
                           "stone_wall": "#",
                           "keys": string.ascii_lowercase,
                           "doors": string.ascii_uppercase}

    direction_changes: Dict[Tuple[int], List[int]] = {(1, 0): (0, 1),
                                                      (0, 1): (-1, 0),
                                                      (-1, 0): (0, -1),
                                                      (0, -1): (1, 0)}

    # Rotating 90 degrees anti-clockwise

    def __init__(self, underground_vault: List[str]) -> None:
        self.underground_vault: List[str] = underground_vault
        self.position: Tuple[int, int] = (0, 0)
        self.keys: Set[str] = set()
        self.keys.add(self.dct["entrance"])  # Consider entrance as key/door
        # Consider open_passage as key/door
        self.keys.add(self.dct["open_passage"])
        # Trying to go down at the beginning
        self.direction: Tuple[int, int] = (1, 0)
        self.path: List[Tuple[int, int]] = []

    def find_entrance(self) -> None:
        for line_index, line in enumerate(self.underground_vault):
            halt: bool = False
            for row_index, element in enumerate(line):
                if element == self.dct["entrance"]:
                    self.position = (line_index, row_index)
                    self.path.append(self.position)
                    halt = True
                    break
            if halt:
                break

    def step(self) -> None:
        height: int = len(self.underground_vault)
        width: int = len(self.underground_vault[0])
        new_position: Tuple[int, int] = (
            self.position[0] + self.direction[0], self.position[1] + self.direction[1])
        if (0 <= self.position[0] < height) and (0 <= self.position[1] < width):
            obj: str = self.underground_vault[self.position[0]
                                              ][self.position[1]]
            if obj.lower() in self.keys:  # Check for open_passage, existing key, or door with existing key
                self.position = new_position
                self.path.append(self.position)
            elif obj in self.dct["keys"]:  # Check for new key
                self.position = new_position
                self.path.append(self.position)
                self.keys.add(obj)
            else:  # obj in self.dct["doors"]+self.dct["stone_wall"]:  # Check for closed door or wall
                self.direction = self.direction_changes[self.direction]
                self.step()


def main() -> None:
    data: List[str] = data_input("data/aoc_18_data.txt")
    underground: UndergroundVault = UndergroundVault(data)
    underground.find_entrance()
    print(underground.position)
    # # Part 1
    # PART_1: int = part_1(SIGNAL)
    # print(f"Part 1: {PART_1} is {PART_1 == 19944447}")

    # # Part 2
    # PART_2: int = part_2(SIGNAL)
    # print(f"Part 2: {PART_2} is {PART_2 == 19944447}")


if __name__ == "__main__":
    main()
