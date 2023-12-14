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


def find_asterisk_indeces(line: str):
    return [ind for ind, char in enumerate(line) if char == "*"]


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


class GearRatio:
    def __init__(self, num1, num2, ast_line_number) -> None:
        self.num1 = num1
        self.num2 = num2
        self.ast_line_number = ast_line_number
        self.gear_ratio = self.num1 * self.num2


if __name__ == "__main__":
    # part 1: print(sum_adjacent_numbers(input_data))
    # part 2:
    #   attempt1: 4292993 - too low
    gear_ratios = []
    for ind, line in enumerate(input_data):
        ast = find_asterisk_indeces(line)
        num_curr_line = find_numbers(line)
        if ind > 0:
            num_prev_line = find_numbers(input_data[ind - 1])
        if ind < len(input_data) - 1:
            num_next_line = find_numbers(input_data[ind + 1])
        for ast_ind in ast:
            adj_numbers = []
            for curr_num in num_curr_line:
                if curr_num.end == ast_ind:  # left
                    adj_numbers.append(curr_num)
                if curr_num.start == ast_ind + 1:  # right
                    adj_numbers.append(curr_num)
            if ind > 0:
                for prev_num in num_prev_line:
                    if prev_num.end >= ast_ind and prev_num.start <= ast_ind + 1:
                        adj_numbers.append(prev_num)
            if ind < len(input_data) - 1:
                for next_num in num_next_line:
                    if next_num.end >= ast_ind and next_num.start <= ast_ind + 1:
                        adj_numbers.append(next_num)
            if len(adj_numbers) == 2:
                gear_ratios.append(
                    GearRatio(int(adj_numbers[0].group), int(adj_numbers[1].group), ind)
                )
    print(sum(gr.gear_ratio for gr in gear_ratios))
