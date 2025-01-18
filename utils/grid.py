from collections import UserDict, namedtuple
from itertools import product
from pathlib import Path

from utils.directions import Direction

Position = namedtuple("Position", ["x", "y"])


class OutOfBoundsException(Exception):
    def __init__(self, position: Position, max_x: int, max_y: int):
        msg = f"{position} is out of bounds. Bounds of x: (0 ,{max_x}), bounds of y: (0, {max_y})"
        super().__init__(msg)


class Grid(UserDict[Position, str]):
    max_x: int
    max_y: int

    def __init__(self):
        super().__init__()

    def __hash__(self):
        return hash((self.max_y, self.max_x, frozenset(self.items())))

    def __eq__(self, other):
        if isinstance(other, Grid):
            return self.max_y == other.max_y and self.max_x == other.max_x and dict(self) == dict(other)
        return False

    def load_file(self, path: str):
        with Path(path).open("r") as handle:
            input_data = input_data = [line.strip() for line in handle.readlines()]
            self.max_y = len(input_data) - 1
            self.max_x = len(input_data[0]) - 1
            for y, line in enumerate(input_data):
                for x, char in enumerate(line):
                    self[Position(x, y)] = char

    def empty_grid(self, x: int, y: int):
        self.max_x = x - 1
        self.max_y = y - 1

        for y, x in product(range(x), range(y)):
            self[Position(x, y)] = "."
        return self

    def _within_x_bounds(self, x: int) -> bool:
        return 0 <= x <= self.max_x

    def _within_y_bounds(self, y: int) -> bool:
        return 0 <= y <= self.max_x

    def _within_bounds(self, position: Position) -> bool:
        return self._within_x_bounds(position.x) and self._within_y_bounds(position.y)

    def get_neighbour(
        self, position: Position, direction: Direction, within_bounds: bool = True, delta_factor: int = 1
    ) -> tuple[Position, str]:
        neighbor_position = Position(
            position.x + direction.delta_x * delta_factor,
            position.y + direction.delta_y * delta_factor,
        )

        if within_bounds and self._within_bounds(neighbor_position) is False:
            raise OutOfBoundsException(neighbor_position, self.max_x, self.max_y)

        return (neighbor_position, self[neighbor_position])

    def get_neighbour_position(
        self, position: Position, direction: Direction, within_bounds: bool = True, delta_factor: int = 1
    ) -> Position | None:
        """Get the neighbour position only."""

        neighbor_position = Position(
            position.x + direction.delta_x * delta_factor,
            position.y + direction.delta_y * delta_factor,
        )

        if within_bounds and self._within_bounds(neighbor_position) is False:
            raise OutOfBoundsException(neighbor_position, self.max_x, self.max_y)

        return neighbor_position

    def get_neighbour_value(self, position: Position, direction: Direction) -> str | None:
        """Get the neighbour value given a start position and a direction."""
        neighbor_position = Position(
            position.x + direction.delta_x,
            position.y + direction.delta_y,
        )

        if self._within_bounds(neighbor_position) is False:
            raise OutOfBoundsException(neighbor_position, self.max_x, self.max_y)

        return self[neighbor_position]

    def move_item(
        self,
        start_position: Position,
        direction: Direction,
        teleport: bool = False,
        replace: bool = True,
        replace_val: str = ".",
    ) -> Position:
        """Move a item in a start position given"""
        v = self[start_position]

        if teleport is False:
            new_position = Position(start_position.x + direction.delta_x, start_position.y + direction.delta_y)
        else:
            new_x = start_position.x + direction.delta_x
            if new_x > self.max_x:
                new_x = new_x - self.max_x - 1
            elif new_x < 0:
                new_x = self.max_x + new_x + 1  # plus because it's negative

            new_y = start_position.y + direction.delta_y
            if new_y > self.max_y:
                new_y = new_y - self.max_y - 1
            elif new_y < 0:
                new_y = self.max_y + new_y + 1  # plus because it's negative

            new_position = Position(new_x, new_y)

        self[new_position] = v

        if not replace:
            return new_position

        self[start_position] = replace_val

        return new_position

    def print(self):
        for i in range(self.max_y + 1):
            row = "".join([t for p, t in self.items() if p[1] == i])
            print(row)
        print()
