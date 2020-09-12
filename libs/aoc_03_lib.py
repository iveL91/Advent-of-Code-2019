"""aoc_03_lib"""

from typing import List, Tuple, Dict, Set


def data_input(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def data_transform(data: str) -> List[List[Tuple[str, int]]]:
    data: List[str] = data.split("\n")
    wires: List[List[str]] = [element.split(",") for element in data]
    return [[(element[0], int(element[1:])) for element in wire] for
            wire in wires]


def path(wire: List[Tuple[str, int]]) -> List[Tuple[int, Tuple[int, ...]]]:
    """"""
    dct: Dict[str, Tuple[int, int]] = {
        "R": (0, 1), "L": (0, -1), "U": (1, 1), "D": (1, -1)}
    position: List[int] = [0, 0]
    wire_length_path: Set[Tuple[int, Tuple[int, ...]]] = set()
    wire_length: int = 0

    for element in wire:
        axes: int = dct[element[0]][0]
        direction: int = dct[element[0]][1]
        for _ in range(element[1]):
            wire_length += 1
            position[axes] += direction
            wire_length_path.add((wire_length, tuple(position.copy())))

    wire_length_path = sorted(
        list(wire_length_path), key=lambda x: x[0])

    return wire_length_path

def calculate_wires_lengths_paths(data: str) -> List[List[Tuple[int, Tuple[int, ...]]]]:
    return [path(wire) for wire in data_transform(data)]


def calculate_crossings(wires_lengths_paths: List[List[Tuple[int, Tuple[int, ...]]]]) -> Tuple[List[List[Tuple[int, Tuple[int, ...]]]], List[Tuple[int, ...]]]:
    """"""
    # wires = data_transform(data)

    # wires_lengths_paths = [path(wire) for wire in wires]
    wires_paths = [[element[1] for element in wire_length_path]
                                          for wire_length_path in wires_lengths_paths]

    crossings = list(set(wires_paths[0]).intersection(
        *[set(element) for element in wires_paths[1:]]))

    return crossings


def part_1(data: str) -> int:
    """Part 1"""
    wires_lengths_paths = calculate_wires_lengths_paths(data)
    crossings = calculate_crossings(wires_lengths_paths)
    return min((abs(element[0]) + abs(element[1]) for element in crossings))


def part_2(data: str) -> int:
    """Part 2"""
    wires_lengths_paths = calculate_wires_lengths_paths(data)
    crossings = calculate_crossings(wires_lengths_paths)

    wires_crossings_lengths: List[List[List[int]]] = [
        [[elem[0] for elem in wires_lengths_path if elem[1] == element]
         for element in crossings]
        for wires_lengths_path in wires_lengths_paths]

    crossing_lengths: List[int] = [min(element) + min(wires_crossings_lengths[1][i]) for i, element
                                   in enumerate(wires_crossings_lengths[0])]

    return min(crossing_lengths)
