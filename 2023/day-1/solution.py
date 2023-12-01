DIGITS_SPELLED_AS_LETTERS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def read_input():
    with open("day-1/input", "rb") as handle:
        lines = handle.readlines()
    return lines


def calculate_calibration(lines: list) -> int:
    all_calibration_values = []
    lines = read_input()
    for line in lines:
        line_digits = []
        for char in line.decode().strip():
            if char.isdigit():
                line_digits.append(char)
        line_calibration_value = int(line_digits[0]) * 10 + int(line_digits[-1])
        all_calibration_values.append(line_calibration_value)
    return sum(all_calibration_values)


def first_puzzle():
    lines = read_input()
    print(f"The answer is: {calculate_calibration(lines)}")


def replace_spelled_digits(line: str) -> str:
    for spelled_digit, digit in DIGITS_SPELLED_AS_LETTERS.items():
        line = line.replace(spelled_digit, str(digit))
    return line


def second_puzzle():
    lines = read_input()
    parsed_lines = []
    for line in lines:
        parsed_lines.append(replace_spelled_digits(line.decode().strip()))
    print(f"The answer to the second puzzle is: {calculate_calibration(parsed_lines)}")


second_puzzle()
