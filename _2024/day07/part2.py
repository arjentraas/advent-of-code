from itertools import product

from _2024.day7.parse_input import parse

OPERATORS = ["+", "*", "||"]


def calculate_equation(numbers: list[int], operators: list[list[str]]):
    result = numbers[0]
    for num, operator in zip(numbers[1:], operators):
        if operator == "+":
            result = result + num
        elif operator == "*":
            result = result * num
        elif operator == "||":
            result = int(str(result) + str(num))
    return result


def main():
    equations = parse()
    sum = 0
    for equation in equations:
        operator_count = equation.number_str.count(" ")
        combos = [list(i) for i in product(OPERATORS, repeat=operator_count)]
        for combo in combos:
            result = calculate_equation(equation.numbers, operators=combo)
            if result == equation.test_value:
                sum += result
                break
    print(sum)


main()
