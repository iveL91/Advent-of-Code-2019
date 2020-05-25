"""aoc_6_lib"""

from typing import List


def data_input(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def orbits_objects(data: str) -> (List[List[str]], List[str]):
    """"""
    data: List[str] = data.split("\n")
    orbits: List[List[str]] = [element.split(")") for element in data]
    objects: List[str] = [element[1] for element in orbits]
    return orbits, objects


def orbit_counter(orbits: List[List[str]], obj: str, counter: int) -> int:
    """"""
    if obj != "COM":
        for orbit in orbits:
            if obj == orbit[1]:
                counter += 1
                obj = orbit[0]
                counter = orbit_counter(orbits, obj, counter)
                break
    return counter


def part_1(data: str) -> int:
    """"""
    orbits, objects = orbits_objects(data)
    total_counter: int = 0
    for obj in objects:
        counter: int = 0
        total_counter += orbit_counter(orbits, obj, counter)
    return total_counter


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


def part_2(data: str) -> int:
    """"""
    orbits: List[List[str]] = orbits_objects(data)[0]
    you_chain: List[str] = orbit_chain(orbits, "YOU", [])
    san_chain: List[str] = orbit_chain(orbits, "SAN", [])

    while you_chain[-1] == san_chain[-1]:
        del you_chain[-1]
        del san_chain[-1]

    return len(you_chain)+len(san_chain)+1-1
