import re

import numpy as np

from utils import read_input_lines


def part_1():
    straight = "XMAS"
    backwards = "SAMX"
    lines = read_input_lines("2024/day4/input_day4.txt")
    count = 0

    max_x = len(lines[0])
    max_y = len(lines) - 1

    # horizontal
    for line in lines:
        count += len(re.findall(straight, line))
        count += len(re.findall(backwards, line))

    # vertical
    for i in range(max_x):
        vertical = "".join([line[i] for line in lines])
        count += len(re.findall(straight, vertical))
        count += len(re.findall(backwards, vertical))

    # regular diagonal
    line_arrays = []
    for line in lines:
        line_arrays.append(np.array([char for char in line]))

    line_matrix = np.array(line_arrays)

    for offset in range(-max_x, max_x):
        diagonal = line_matrix.diagonal(offset)
        diagonal_string = "".join(diagonal)
        count += len(re.findall(straight, diagonal_string))
        count += len(re.findall(backwards, diagonal_string))

    # inverse diagonal
    inverse_line_arrays = []
    for line in lines:
        inverse_line_arrays.append(np.flip(np.array([char for char in line])))

    inverse_line_matrix = np.array(inverse_line_arrays)

    for offset in range(-max_x, max_x):
        diagonal = inverse_line_matrix.diagonal(offset)
        diagonal_string = "".join(diagonal)
        count += len(re.findall(straight, diagonal_string))
        count += len(re.findall(backwards, diagonal_string))
    print(count)


part_1()


def part_2():
    lines = read_input_lines("2024/day4/input_day4.txt")
    count = 0

    for i in range(1, len(lines) - 1):
        line = lines[i]
        for j in range(len(line) - 1):
            char = line[j]
            if char != "A":
                continue

            left_upper = lines[i - 1][j - 1]
            right_upper = lines[i - 1][j + 1]
            left_lower = lines[i + 1][j - 1]
            right_lower = lines[i + 1][j + 1]
            mas_count = 0
            if left_upper == "M" and right_lower == "S":
                mas_count += 1

            if left_upper == "S" and right_lower == "M":
                mas_count += 1

            if right_upper == "M" and left_lower == "S":
                mas_count += 1

            if right_upper == "S" and left_lower == "M":
                mas_count += 1

            if mas_count == 2:
                count += 1
    print(count)


part_2()
