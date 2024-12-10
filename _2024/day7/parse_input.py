from dataclasses import dataclass

from helper import read_input_lines


@dataclass
class Equation:
    test_value: int
    number_str: str
    numbers: list[int]


def parse() -> list[Equation]:
    lines = read_input_lines("_2024/day7/input.txt")
    equations: list[Equation] = []

    for line in lines:
        split = line.split(":")
        numbers = split[1].strip()
        equations.append(
            Equation(test_value=int(split[0]), number_str=numbers, numbers=[int(num) for num in numbers.split()])
        )
    return equations
