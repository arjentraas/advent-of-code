import re
from pathlib import Path

with Path("day3/input").open("r") as handle:
    input_data = [line.strip() for line in handle.readlines()]


class _Match:
    def __init__(self, start, end, span, group) -> None:
        self.start = start
        self.end = end
        self.span = span
        self.group = group


class AdjacentNumber:
    def __init__(self, num, line_nr):
        self.num = num
        self.line_nr = line_nr


def find_symbols_indeces(line: str) -> list[int]:
    symbols = re.finditer(r"[@_\-!=%#$%^&+*()<>?/\|}{~:]", line)
    return [symbol.start() for symbol in symbols]


def find_numbers(line: str):
    numbers = re.finditer(r"\d+", line)
    return [
        _Match(start=m.start(), end=m.end(), span=m.span(), group=m.group())
        for m in numbers
    ]


def find_adjacent_same_line(numbers: list[_Match], symbol_indices: list[int]):
    result = []
    for symbol_index in symbol_indices:
        for number in numbers:
            if number.end == symbol_index:
                result.append(number)
            if number.start == symbol_index + 1:
                result.append(number)
    return [int(r.group) for r in result]


def find_adjacent_other_line(numbers: list[_Match], symbol_indices: list[int]):
    result = []
    for number in numbers:
        for symbol_index in symbol_indices:
            if number.end >= symbol_index and number.start <= symbol_index + 1:
                result.append(number)
    return [int(r.group) for r in result]


def sum_adjacent_numbers(lines: list):
    adjacent_numbers = []
    for i in range(len(lines)):
        symbol_indices = find_symbols_indeces(lines[i])
        adjacent_same_line = find_adjacent_same_line(
            find_numbers(lines[i]), symbol_indices
        )
        adjacent_numbers += [
            AdjacentNumber(num=num, line_nr=i + 1)
            for num in adjacent_same_line
            if AdjacentNumber(num=num, line_nr=i + 1) not in adjacent_numbers
        ]
        if i < len(lines) - 1:
            adjacent_lower_line = find_adjacent_other_line(
                find_numbers(lines[i + 1]), symbol_indices
            )
            adjacent_numbers += [
                AdjacentNumber(num=num, line_nr=i + 2)
                for num in adjacent_lower_line
                if AdjacentNumber(num=num, line_nr=i + 2) not in adjacent_numbers
            ]
        if i > 0:
            adjacent_upper_line = find_adjacent_other_line(
                find_numbers(lines[i - 1]), symbol_indices
            )
            adjacent_numbers += [
                AdjacentNumber(num=num, line_nr=i)
                for num in adjacent_upper_line
                if AdjacentNumber(num=num, line_nr=i) not in adjacent_numbers
            ]

    return sum([n.num for n in adjacent_numbers])


if __name__ == "__main__":
    print(sum_adjacent_numbers(input_data))
    # attempt 3: 506339
