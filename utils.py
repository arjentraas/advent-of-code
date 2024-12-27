from collections import UserDict, namedtuple
from dataclasses import dataclass
from functools import cache
from itertools import product
from pathlib import Path


def read_input_lines(path: str):
    with Path(path).open("r") as handle:
        input_data = [line.strip() for line in handle.readlines()]
        return input_data


def read_input(path: str):
    with Path(path).open("r") as handle:
        return handle.read()


Position = namedtuple("Position", ["col", "row"])


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


class OutOfBoundsException(Exception):
    def __init__(self, position: Position, max_col: int, max_row: int):
        msg = f"{position} is out of bounds. Bounds col: (0 ,{max_col}), bounds row: (0, {max_row})"
        super().__init__(msg)


class Grid(UserDict[Position, str]):
    max_row: int
    max_col: int

    def __init__(self):
        super().__init__()

    def __hash__(self):
        return hash((self.max_row, self.max_col, frozenset(self.items())))

    def __eq__(self, other):
        if isinstance(other, Grid):
            return self.max_row == other.max_row and self.max_col == other.max_col and dict(self) == dict(other)
        return False

    def load_file(self, path: str):
        with Path(path).open("r") as handle:
            input_data = input_data = [line.strip() for line in handle.readlines()]
            self.max_row = len(input_data) - 1
            self.max_col = len(input_data[0]) - 1
            for row, line in enumerate(input_data):
                for col, char in enumerate(line):
                    self[Position(col=col, row=row)] = char

    def empty_grid(self, col_count: int, row_count: int):
        self.max_col = col_count - 1
        self.max_row = row_count - 1

        for c, r in product(range(col_count), range(row_count)):
            self[Position(col=c, row=r)] = "."
        return self

    def _within_col_bounds(self, col: int) -> bool:
        return 0 <= col <= self.max_col

    def _within_row_bounds(self, row: int) -> bool:
        return 0 <= row <= self.max_row

    def _within_bounds(self, position: Position) -> bool:
        return self._within_col_bounds(position[0]) and self._within_row_bounds(position[1])

    def get_neighbour_position(
        self, position: Position, direction: Direction, within_bounds: bool = True, delta_factor: int = 1
    ) -> Position | None:
        neighbor_position = Position(
            position[0] + direction.delta_col * delta_factor, position[1] + direction.delta_row * delta_factor
        )

        if within_bounds and self._within_bounds(neighbor_position) is False:
            raise OutOfBoundsException(neighbor_position, self.max_col, self.max_row)

        if within_bounds is False:
            return neighbor_position

        return neighbor_position

    def get_neighbour_value(self, position: Position, direction: Direction) -> str | None:
        neighbor_position = Position(position.col + direction.delta_col, position.row + direction.delta_row)
        if self._within_bounds(neighbor_position) is False:
            raise OutOfBoundsException(neighbor_position, self.max_col, self.max_row)

        return self[neighbor_position]

    def move_position(
        self,
        start_position: Position,
        delta_col: int,
        delta_row: int,
        teleport: bool = False,
        replace: bool = True,
        replace_val: str = ".",
    ) -> Position:
        v = self[start_position]

        if not teleport:
            new_position = Position(start_position[0] + delta_col, start_position[1] + delta_row)
        else:
            new_col = start_position[0] + delta_col
            if new_col > self.max_col:
                new_col = new_col - self.max_col - 1
            elif new_col < 0:
                new_col = self.max_col + new_col + 1  # plus because it's negative

            new_row = start_position[1] + delta_row
            if new_row > self.max_row:
                new_row = new_row - self.max_row - 1
            elif new_row < 0:
                new_row = self.max_row + new_row + 1  # plus because it's negative

            new_position = Position(new_col, new_row)

        self[new_position] = v

        if not replace:
            return new_position

        self[start_position] = replace_val

        return new_position

    def print(self):
        for i in range(self.max_row + 1):
            row = "".join([t for p, t in self.items() if p[1] == i])
            print(row)
        print()
