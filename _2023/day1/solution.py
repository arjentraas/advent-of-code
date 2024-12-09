DIGITS_SPELLED_AS_LETTERS = {
    "nine": 9,
    "one": 1,
    "five": 5,
    "six": 6,
    "two": 2,
    "seven": 7,
    "three": 3,
    "eight": 8,
    "four": 4,
}

combos = {
    "nineight": 98,
    "oneight": 18,
    "fiveight": 58,
    "twone": 21,
    "threeight": 38,
    "eightwo": 82,
    "eighthree": 83,
}


def read_input() -> list:
    with open("day1/input", "rb") as handle:
        lines = handle.readlines()
    return lines


class Line:
    def __init__(self, text: bytes, line_digits: list[str] = []) -> None:
        self.text = text.decode().strip()
        self.line_digits = line_digits

    def replace_misspelled_digits(self):
        for start_index in range(len(self.text)):
            for combo, digits in combos.items():
                self.text = self.text.replace(combo, str(digits))
            for letters, digit in DIGITS_SPELLED_AS_LETTERS.items():
                self.text = self.text.replace(letters, str(digit))

    def get_line_digits(self):
        self.line_digits = []
        for char in self.text:
            if char.isdigit():
                self.line_digits.append(char)

    def calculate_calibration(self):
        self.calibration = int(self.line_digits[0]) * 10 + int(self.line_digits[-1])

    def run(self):
        self.replace_misspelled_digits()
        self.get_line_digits()
        self.calculate_calibration()


if __name__ == "__main__":
    lines = [Line(text=line) for line in read_input()]

    for line in lines:
        line.run()

    answer = sum([line.calibration for line in lines])
    print(answer)
