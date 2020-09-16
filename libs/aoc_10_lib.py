"""aoc_10_lib"""

import itertools
import math
from math import inf
from typing import List, Dict, Tuple


def data_input(filename: str) -> List[List[int]]:
    """"""
    with open(filename) as f:
        return [[0 if symbol == "." else 1 for symbol in line] for line in f.read().splitlines()]


def calc_direction(point_1: Tuple[int, int], point_2: Tuple[int, int]) -> Tuple[int, int, int]:
    """"""
    x_diff: int = point_2[0] - point_1[0]
    y_diff: int = point_2[1] - point_1[1]
    gcd: int = math.gcd(x_diff, y_diff)
    return gcd, x_diff//gcd, y_diff//gcd


def clear_view(grid_dct: Dict[Tuple[int, int], int],
               point_1: Tuple[int, int],
               point_2: Tuple[int, int])\
        -> bool:
    """"""
    gcd, x_dir, y_dir = calc_direction(point_1, point_2)
    clearness: bool = True

    for i in range(1, gcd):
        if grid_dct[(point_1[0] + i*x_dir, point_1[1] + i*y_dir)]:
            clearness = False
            break
    return clearness


def calc_grid_size(data: List[List[int]]) -> Tuple[int, int]:
    """"""
    return len(data), len(data[0])


def create_grid_dct(data: List[List[int]]) -> Dict[Tuple[int, int], int]:
    """"""
    height, width = calc_grid_size(data)
    return {(index_width, index_height): data[index_height][index_width] for
            index_height, index_width in itertools.product(range(height), range(width))}


def create_view_dct(data: List[List[int]]) -> Dict[Tuple[int, int], int]:
    """"""
    grid_dct = create_grid_dct(data)
    view_dct: Dict[Tuple[int, int], int] = {}

    for point_1 in grid_dct:
        counter: int = 0
        if grid_dct[point_1]:
            for point_2 in grid_dct:
                if (point_1 != point_2) and grid_dct[point_2]:
                    if clear_view(grid_dct, point_1, point_2):
                        counter += 1

        view_dct[point_1] = counter
    return view_dct


def part_1(data: List[List[int]]) -> int:
    """Part 1"""
    return max(create_view_dct(data).values())


def sign(x: int) -> int:
    """"""
    return -1 if x < 0 else (1 if x > 0 else 0)


def slope(direction: Tuple[int, int]) -> float:
    """"""
    return direction[1]/direction[0] if direction[0] else float(inf)


def create_slope_dct_quadrant(grid_dct: Dict[Tuple[int, int], int],
                              station_point: Tuple[int, int],
                              quadrant: List[Tuple[int, int]])\
        -> Dict[Tuple[int, int], List[Tuple[int, int]]]:
    """"""
    slope_dct_quadrant: Dict[Tuple[int, int], List[Tuple[int, int]]] = {}
    for index_width, index_height in itertools.product(range(quadrant[0][0], quadrant[0][1]),
                                                       range(quadrant[1][0], quadrant[1][1])):
        point: Tuple[int, int] = (index_width, index_height)
        if grid_dct[point] and station_point != point:
            direction: Tuple[int, int] = calc_direction(
                station_point, point)[1:]
            if direction in slope_dct_quadrant:
                slope_dct_quadrant[direction].append(point)
            else:
                slope_dct_quadrant[direction] = [point]

    slope_dct_quadrant = dict(sorted(
        slope_dct_quadrant.items(), key=lambda item: slope(item[0])))
    for lst in slope_dct_quadrant.values():
        lst.sort(key=lambda point_2: (
            point_2[0]-station_point[0])**2 + (point_2[1]-station_point[1])**2)

    return slope_dct_quadrant


def one_turn_destroy(slope_dct: Dict[Tuple[int, int], List[Tuple[int, int]]],
                     destroyed: List[Tuple[int, int]])\
        -> Tuple[Dict[Tuple[int, int], List[Tuple[int, int]]],
                 List[Tuple[int, int]]]:
    """"""
    del_keys: List[Tuple[int, int]] = []
    for direction, lst in slope_dct.items():
        if lst:
            destroyed.append(lst.pop(0))
        else:
            del_keys.append(direction)

    for key in del_keys:
        del slope_dct[key]

    return slope_dct, destroyed


def destroy(slope_dct: Dict[Tuple[int, int], List[Tuple[int, int]]]) -> List[Tuple[int, int]]:
    """"""
    destroyed: List[Tuple[int, int]] = []
    while slope_dct:
        slope_dct, destroyed = one_turn_destroy(slope_dct, destroyed)
    return destroyed


def part_2(data: List[List[int]]) -> int:
    """Part 2"""
    width, height = calc_grid_size(data)
    grid_dct: Dict[Tuple[int, int], int] = create_grid_dct(data)
    view_dct: Dict[Tuple[int, int], int] = create_view_dct(data)
    station_point: Tuple[int, int] = max(view_dct, key=view_dct.get)

    quadrants: List[List[Tuple[int, int]]] = [[(station_point[0], width), (0, station_point[1])],
                                              [(station_point[0], width),
                                               (station_point[1], height)],
                                              [(0, station_point[0]),
                                               (station_point[1], height)],
                                              [(0, station_point[0]), (0, station_point[1])]]

    slope_dct_quadrants: List[Dict[Tuple[int, int], List[Tuple[int, int]]]] = [
        create_slope_dct_quadrant(grid_dct, station_point, quadrant) for quadrant in
        quadrants]

    slope_dct: Dict[Tuple[int, int], List[Tuple[int, int]]] = {}
    for slope_dct_quadrant in slope_dct_quadrants:
        slope_dct.update(slope_dct_quadrant)

    destroyed: List[Tuple[int, int]] = destroy(slope_dct)

    return destroyed[200-1][0]*100 + destroyed[200-1][1]
