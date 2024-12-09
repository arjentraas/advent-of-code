from dataclasses import dataclass

from helper import read_input_lines


@dataclass
class Equation:
    test_value: int
    numbers: list[int]


def parse() -> list[Equation]:
    lines = read_input_lines("_2024/day7/example_input.txt")
    equations: list[Equation] = []
    for line in lines:
        split = line.split(":")
        numbers = split[1].split(" ")
        equations.append(Equation(test_value=int(split[0]), numbers=[int(number) for number in numbers if number]))
    return [equations]
