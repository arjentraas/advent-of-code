from collections import UserDict
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
    col: float
    row: float


@dataclass(frozen=True)
class Direction:
    name: str
    symbol: str
    delta_row: int
    delta_col: int


RIGHT = Direction(name="right", symbol=">", delta_row=0, delta_col=1)
LEFT = Direction(name="left", symbol="<", delta_row=0, delta_col=-1)
UP = Direction(name="up", symbol="^", delta_row=-1, delta_col=0)
DOWN = Direction(name="down", symbol="v", delta_row=1, delta_col=0)

LEFT_UPPER = Direction(name="left-upper", symbol="<^", delta_row=-1, delta_col=-1)
LEFT_LOWER = Direction(name="left-lower", symbol="<v", delta_row=1, delta_col=-1)
RIGHT_UPPER = Direction(name="right-upper", symbol=">^", delta_row=-1, delta_col=1)
RIGHT_LOWER = Direction(name="right-lower", symbol=">v", delta_row=1, delta_col=1)

STRAIGHT_DIRECTIONS: list[Direction] = [RIGHT, LEFT, DOWN, UP]
HORIZONTAL_DIRECTIONS: list[Direction] = [RIGHT, LEFT]
VERTICAL_DIRECTIONS: list[Direction] = [UP, DOWN]

DIAGONAL_DIRECTIONS: list[Direction] = [LEFT_UPPER, LEFT_LOWER, RIGHT_UPPER, RIGHT_LOWER]

ALL_DIRECTIONS = STRAIGHT_DIRECTIONS + DIAGONAL_DIRECTIONS


class Grid(UserDict[Position, str]):
    max_row: int
    max_col: int

    def __hash__(self):
        return hash((self.max_row, self.max_col, frozenset(self.items())))

    def __eq__(self, other):
        if isinstance(other, Grid):
            return self.max_row == other.max_row and self.max_col == other.max_col and dict(self) == dict(other)
        return False

    def __init__(self, path: str):
        super().__init__()
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
    def get_neighbour_position(
        self, position: Position, direction: Direction, within_bounds: bool = True, delta_factor: int = 1
    ) -> Position | None:
        neighbor_position = Position(
            position.col + direction.delta_col * delta_factor, position.row + direction.delta_row * delta_factor
        )
        if within_bounds:
            if self._within_bounds(neighbor_position):
                return neighbor_position
            else:
                return None
        return neighbor_position

    @cache
    def get_neighbour_value(self, position: Position, direction: Direction) -> str | None:
        neighbor_position = Position(position.col + direction.delta_col, position.row + direction.delta_row)
        if self._within_bounds(neighbor_position):
            return self[neighbor_position]
        return
