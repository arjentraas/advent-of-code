from unittest import TestCase, main

from day1.solution import Line, read_input

LETTERS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


class TestSolution(TestCase):
    def test_simple(self):
        line = Line(b"5ffour295")
        line.get_line_digits()
        line.calculate_calibration()
        self.assertEqual(line.calibration, 55)

        line.replace_misspelled_digits()
        line.calculate_calibration()
        self.assertEqual(line.calibration, 55)
        self.assertIn("4", line.text)

    def test_all(self):
        lines = [Line(line) for line in read_input()]
        for line in lines:
            print(line.text)
            line.run()
            print(line.text)
            print("\n")
            for letters in LETTERS:
                self.assertNotIn(letters, line.text)

    def test_provided_cases(self):
        cases = {
            b"two1nine": 29,
            b"eightwothree": 83,
            b"abcone2threexyz": 13,
            b"xtwone3four": 24,
            b"4nineeightseven2": 42,
            b"zoneight234": 14,
            b"7pqrstsixteen": 76,
        }
        lines = []
        for inp, outp in cases.items():
            line = Line(inp)
            line.run()
            lines.append(line)
            self.assertEqual(outp, line.calibration)

        self.assertEqual(sum(line.calibration for line in lines), 281)


if __name__ == "__main__":
    main()
