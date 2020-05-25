"""aoc_3_lib"""

from typing import List, Tuple, Dict, Set


def data_input(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def path(dct: Dict[str, Tuple[int, int]], wire: List[Tuple[str, int]])\
        -> Tuple[List[Tuple[int, Tuple[int, ...]]], List[Tuple[int, ...]]]:
    """"""
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

    wire_length_path: List[Tuple[int, Tuple[int, ...]]] = sorted(list(wire_length_path),
                                                                 key=lambda x: x[0])
    wire_path: List[Tuple[int, ...]] = [element[1] for element in wire_length_path]

    return wire_length_path, wire_path


def part_1_construction(data: str)\
        -> Tuple[List[List[Tuple[str, int]]], List[List[Tuple[int, Tuple[int, ...]]]], List[Tuple[int, ...]], List[int]]:
    """"""

    dct: Dict[str, Tuple[int, int]] = {"R": (0, 1), "L": (0, -1), "U": (1, 1), "D": (1, -1)}
    data: List[str] = data.split("\n")

    wires: List[List[str]] = [element.split(",") for element in data]
    wires: List[List[Tuple[str, int]]] = [[(element[0], int(element[1:])) for element in wire] for
                                          wire in wires]

    wires_lengths_paths: List[List[Tuple[int, Tuple[int, ...]]]] = [[] for _ in wires]
    wires_paths: List[List[Tuple[int, ...]]] = [[] for _ in wires]

    for i, wire in enumerate(wires):
        wires_lengths_paths[i], wires_paths[i] = path(dct, wire)

    crossings: List[Tuple[int, ...]] = list(
        set(wires_paths[0]).intersection(*[set(element) for element in wires_paths]))

    crossings_distance: List[int] = [abs(element[0]) + abs(element[1]) for element in crossings]
    return wires, wires_lengths_paths, crossings, crossings_distance


def part_1(data: str) -> int:
    """Part 1"""
    crossings_distance: List[int] = part_1_construction(data)[3]
    return min(crossings_distance)


def part_2(data: str) -> int:
    """Part 2"""
    _, wires_lengths_paths, crossings, _ = part_1_construction(data)

    wires_crossings_lengths: List[List[List[int]]] = [
        [[elem[0] for elem in wires_lengths_path if elem[1] == element] for element in crossings]
        for wires_lengths_path in wires_lengths_paths]

    crossing_lengths: List[int] = [min(element) + min(wires_crossings_lengths[1][i]) for i, element
                                   in enumerate(wires_crossings_lengths[0])]

    return min(crossing_lengths)
