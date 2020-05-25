"""aoc_8_lib"""

import itertools
from typing import List


def data_input(filename: str) -> List[int]:
    with open(filename) as f:
        return [int(number) for number in f.read()]


def partitioning_1d(integer_seq: List[int], length: int) -> List[List[int]]:
    """()"""
    return [integer_seq[pos:(pos + length)] for pos in range(0, len(integer_seq), length)]


def partitioning_2d(integer_seq: List[int], width: int, height: int) -> List[List[List[int]]]:
    """()"""
    return [partitioning_1d(layer, width) for layer in partitioning_1d(integer_seq, width * height)]


def counting_in_layer(layer: List[List[int]], number: int) -> int:
    """()"""
    counter: int = 0

    for row in layer:
        counter += row.count(number)

    return counter


def part_1(data: List[int], width: int, height: int) -> int:
    """"""
    layers: List[List[List[int]]] = partitioning_2d(data, width, height)

    layer_minimum_0: int = 0
    minimum_0: int = width*height

    for index, layer in enumerate(layers):
        zeros: int = counting_in_layer(layer, 0)
        if zeros < minimum_0:
            minimum_0 = zeros
            layer_minimum_0 = index

    return counting_in_layer(layers[layer_minimum_0], 1) * counting_in_layer(layers[layer_minimum_0], 2)


def build_image(layers: List[List[List[int]]], width: int, height: int) -> List[List[int]]:
    """()"""
    image: List[List[int]] = [[0 for _ in range(width)] for _ in range(height)]

    for index_height, index_width in itertools.product(range(height), range(width)):
        for layer in layers:
            if layer[index_height][index_width] == 2:
                continue
            else:
                image[index_height][index_width] = layer[index_height][index_width]
                break

    return image


def part_2(data: List[int], width: int, height: int) -> List[List[int]]:
    """()"""
    layers: List[List[List[int]]] = partitioning_2d(data, width, height)

    return build_image(layers, width, height)
