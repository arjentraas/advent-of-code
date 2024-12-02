from pathlib import Path


def read_input_lines(path):
    with Path(path).open("r") as handle:
        input_data = [line.strip() for line in handle.readlines()]
        return input_data


def read_input(path):
    with Path(path).open("r") as handle:
        return handle.read()
