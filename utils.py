from dataclasses import dataclass
from functools import cache
from pathlib import Path


def read_input_lines(path: str):
    with Path(path).open("r") as handle:
        input_data = [line.strip() for line in handle.readlines()]
        return input_data


def read_input(path: str):
    with Path(path).open("r") as handle:
        return handle.read()


@dataclass(frozen=True)
class Position:
    col: int
    row: int


@dataclass(frozen=True)
class Direction:
    name: str
    symbol: str
    delta_row: int
    delta_col: int


STRAIGHT_DIRECTIONS: list[Direction] = [
    Direction(name="up", symbol="^", delta_row=-1, delta_col=0),
    Direction(name="down", symbol="v", delta_row=1, delta_col=0),
    Direction(name="right", symbol=">", delta_row=0, delta_col=1),
    Direction(name="left", symbol="<", delta_row=0, delta_col=-1),
]


class Grid(dict[Position, str]):
    max_row: int
    max_col: int

    def __hash__(self):
        return hash((self.max_row, self.max_col, frozenset(self.items())))

    def __init__(self, path: str):
        self._from_file(path)

    def _from_file(self, path: str):
        with Path(path).open("r") as handle:
            input_data = input_data = [line.strip() for line in handle.readlines()]
            self.max_row = len(input_data) - 1
            self.max_col = len(input_data[0]) - 1
            for row, line in enumerate(input_data):
                for col, char in enumerate(line):
                    self[Position(col=col, row=row)] = char

    def _within_bounds(self, position: Position) -> bool:
        return 0 <= position.col <= self.max_col and 0 <= position.row <= self.max_row

    @cache
    def get_neighbour_position(self, position: Position, direction: Direction) -> Position | None:
        neighbor_position = Position(position.col + direction.delta_col, position.row + direction.delta_row)
        if self._within_bounds(neighbor_position):
            return neighbor_position
        return

    @cache
    def get_neighbour_value(self, position: Position, direction: Direction) -> str | None:
        neighbor_position = Position(position.col + direction.delta_col, position.row + direction.delta_row)
        if self._within_bounds(neighbor_position):
            return self[neighbor_position]
        return
