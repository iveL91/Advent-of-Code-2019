"""aoc_14_lib"""

import math
import re
from collections import defaultdict
from typing import Dict, List, Optional, Pattern, Tuple, Union
from libs.timer import timer


class Nanofactory:
    """"""

    def __init__(self, formulas: Dict[str, Dict[str, Union[int, List[Tuple[str, int]]]]],
                 chemicals_dict: Dict[str, int], extra_dict: Optional[dict] = None) -> None:
        self.reactions = formulas
        self.chemicals = chemicals_dict
        self.extra = extra_dict or {chemical: 0 for chemical in self.reactions}

    def step(self) -> None:
        new_chemicals: Dict[str, int] = defaultdict(int)
        for chemical, chemical_amount in self.chemicals.items():
            if chemical == "ORE":
                new_chemicals[chemical] += chemical_amount
            else:
                reaction_amount = math.ceil(
                    chemical_amount / self.reactions[chemical]["amount"])
                for reactant, reactant_amount in self.reactions[chemical]["reactants"]:
                    new_chemicals[reactant] += reactant_amount * \
                        reaction_amount
                produced_amount = self.reactions[chemical]["amount"] * \
                    reaction_amount
                self.extra[chemical] += produced_amount - chemical_amount

        for chemical, chemical_amount in new_chemicals.items():
            if chemical != "ORE":
                new_chemicals[chemical], self.extra[chemical] = reduce_extra(
                    chemical_amount, self.extra[chemical])

        self.chemicals = {key: value for key,
                          value in new_chemicals.items() if value}

    def calculate_ore(self) -> None:
        while True:
            if len(self.chemicals) == 1 and "ORE" in self.chemicals:
                break
            else:
                self.step()


def reduce_extra(number_1: int, number_2: int) -> Tuple[int, int]:
    if number_1 >= number_2:
        return number_1-number_2, 0
    else:
        return 0,  number_2 - number_1


def data_input(filename: str) -> Dict[str, Dict[str, Union[int, List[Tuple[str, int]]]]]:
    """"""
    with open(filename) as f:
        data = [line.split(" => ") for line in f.read().splitlines()]
        formulas: Dict[str, Dict[str, Union[int, List[Tuple[str, int]]]]] = {}
        for input_chemicals, output_chemical in data:
            pattern: Pattern[str] = re.compile(r"(\d+) (\w+)")
            matches: List[Tuple[str, str]] = re.findall(
                pattern, input_chemicals)
            prod: List[str] = output_chemical.split(" ")
            # formulas[prod[1]] = (int(prod[0]), [(match[1], int(match[0])) for match in matches])
            formulas[prod[1]] = {"amount": int(prod[0]),
                                 "reactants": [(match[1], int(match[0])) for match in matches]}
        return formulas


@timer
def part_1(formulas: Dict[str, Dict[str, Union[int, List[Tuple[str, int]]]]]) -> int:
    """"""
    nanofactory = Nanofactory(formulas, {"FUEL": 1})
    nanofactory.calculate_ore()
    return nanofactory.chemicals["ORE"]


@timer
def part_2(formulas: Dict[str, Dict[str, Union[int, List[Tuple[str, int]]]]]) -> int:
    """"""
    ore_total: int = 1_000_000_000_000
    fuel_total: int = 0
    nanofactory = Nanofactory(formulas, {"FUEL": 1})
    while True:
        nanofactory.calculate_ore()
        ore_total -= nanofactory.chemicals["ORE"]
        if ore_total > 0:
            fuel_total += 1
            nanofactory.chemicals = {"FUEL": 1}
        elif not ore_total:
            fuel_total += 1
            break
        else:
            break

    return fuel_total
