"""aoc_11_lib"""

from typing import List, Set, Tuple
from libs.aoc_lib import IntcodeComputer
from libs.timer import timer


def vector_addition_2d(vector_1: Tuple[int, int], vector_2: Tuple[int, int]) -> Tuple[int, int]:
    return tuple(element_1 + element_2 for element_1, element_2 in zip(vector_1, vector_2))


class EmergencyHullPaintingRobot:
    """"""

    def __init__(self,
                 program: List[int],
                 grid: List[List[int]],
                 position: Tuple[int, int],
                 direction: Tuple[int, int],
                 painted_fields: Set[Tuple[int, int]])\
            -> None:
        self.computer = IntcodeComputer(program)
        self.grid = grid
        self.position = position
        self.direction = direction
        self.painted_fields = painted_fields

    def calc_new_direction(self) -> None:
        """"""
        if self.computer.outputs[-1]:  # right turn
            self.direction = (-self.direction[1], self.direction[0])
        else:  # left turn
            self.direction = (self.direction[1], -self.direction[0])

    def move(self) -> None:
        """"""
        self.computer.inpt = self.grid[self.position[1]][self.position[0]]
        print(self.computer.address)
        print(self.position)
        # for line in self.grid:
        #     print(line)
        self.computer.run()
        self.grid[self.position[1]][self.position[0]] = self.computer.outputs[0]
        self.painted_fields.add(self.position)
        self.calc_new_direction()
        self.position = vector_addition_2d(self.position, self.direction)


def initialize_painting_robot(program: List[int], grid_size: int):
    """"""
    grid: List[List[int]] = [[0 for _ in range(grid_size)] for _ in range(grid_size)]  # [[0] * grid_size] * grid_size
    position: Tuple[int, int] = (grid_size // 2, grid_size // 2)
    direction: Tuple[int, int] = (0, -1)
    painted_fields: Set[Tuple[int, int]] = set()
    return EmergencyHullPaintingRobot(program.copy(), grid, position, direction, painted_fields)


@timer
def part_1(program: List[int], grid_size: int = 1_0-1) -> int:
    """Part 1"""

    painting_robot = initialize_painting_robot(program, grid_size)
    counter = 0

    while not painting_robot.computer.stop:
        
        painting_robot.move()
        counter += 1
        # opcode = painting_robot.computer.data[painting_robot.computer.address]
        # for line in painting_robot.grid:
        #     print(line)
        # print("\n")
        # print(painting_robot.computer.outputs)
        # print(opcode, painting_robot.computer.address, painting_robot.position,
        #       painting_robot.computer.outputs, painting_robot.direction,
        #       painting_robot.painted_fields)
        # painting_robot.computer.outputs = []
        # print("\n")
        print("\ncounter", counter)

        # if opcode == 99:  # or counter == 7:
        #     print("here")
        #     break

    return len(painting_robot.painted_fields)

@timer
def part_2(data: List[int]) -> int:
    """Part 2"""
    pass
