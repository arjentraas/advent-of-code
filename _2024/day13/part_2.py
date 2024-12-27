import re

from sympy import Matrix, linsolve, symbols

from utils import read_input_lines


def main():
    inp = read_input_lines("_2024/day13/input.txt")

    start_i = 0

    x_pattern = r"X\+\d+"
    y_pattern = r"Y\+\d+"
    is_x_pattern = r"X=\d+"
    is_y_pattern = r"Y=\d+"

    total_price = 0

    while start_i <= len(inp):
        a_x = int(re.findall(x_pattern, inp[start_i])[0].split("+")[1])
        a_y = int(re.findall(y_pattern, inp[start_i])[0].split("+")[1])
        b_x = int(re.findall(x_pattern, inp[start_i + 1])[0].split("+")[1])
        b_y = int(re.findall(y_pattern, inp[start_i + 1])[0].split("+")[1])
        is_x = int(re.findall(is_x_pattern, inp[start_i + 2])[0].split("=")[1]) + 10000000000000
        is_y = int(re.findall(is_y_pattern, inp[start_i + 2])[0].split("=")[1]) + 10000000000000

        s = xa, xb, ya, yb = symbols("xa xb ya yb")

        var_matrix = Matrix([[a_x, b_x], [a_y, b_y]])
        sol_matrix = Matrix([[is_x], [is_y]])

        solution = linsolve((var_matrix, sol_matrix), s)
        solution = next(iter(solution))  # type: ignore
        times_a = solution[0]
        times_b = solution[1]

        if times_a.is_integer is False or times_b.is_integer is False:
            start_i += 4
            continue

        price = times_a * 3 + times_b
        total_price += price
        start_i += 4

    print(total_price)


main()
