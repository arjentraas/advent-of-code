from _2024.day7.parse_input import parse


def main():
    equations = parse()
    for equation in equations:
        string_evaluation = ""
        for index in range(len(equation.numbers) - 1):
            string_evaluation += str(equation.numbers[index])


main()
