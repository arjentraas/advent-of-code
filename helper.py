from pathlib import Path


def read_input_lines(path: str):
    with Path(path).open("r") as handle:
        input_data = [line.strip() for line in handle.readlines()]
        return input_data


def read_input(path: str):
    with Path(path).open("r") as handle:
        return handle.read()
