"""aoc_06_lib"""

from typing import List
from libs.timer import timer


def data_input(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def calc_orbits(data: str) -> List[List[str]]:
    """"""
    return [element.split(")") for element in data.split("\n")]


def orbit_counter(orbits: List[List[str]], obj: str, counter: int) -> int:
    """"""
    if obj != "COM":
        for orbit in orbits:
            if obj == orbit[1]:
                obj = orbit[0]
                counter += 1
                counter = orbit_counter(orbits, obj, counter)
                break
    return counter


def orbit_chain(orbits: List[List[str]], obj: str, chain: List[str]) -> List[str]:
    """"""
    if obj != "COM":
        for orbit in orbits:
            if obj == orbit[1]:
                obj = orbit[0]
                chain.append(obj)
                chain = orbit_chain(orbits, obj, chain)
                break
    return chain


@timer
def part_1(data: str) -> int:
    """"""
    orbits = calc_orbits(data)
    objects: List[str] = [element[1] for element in orbits]
    return sum(orbit_counter(orbits, obj, 0) for obj in objects)
    # return sum(len(orbit_chain(orbits, obj, [])) for obj in objects)


@timer
def part_2(data: str) -> int:
    """"""
    orbits: List[List[str]] = calc_orbits(data)
    you_chain: List[str] = orbit_chain(orbits, "YOU", [])
    san_chain: List[str] = orbit_chain(orbits, "SAN", [])

    while you_chain[-1] == san_chain[-1]:
        del you_chain[-1]
        del san_chain[-1]

    return len(you_chain)+len(san_chain)+1-1
