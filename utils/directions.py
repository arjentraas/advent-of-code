from dataclasses import dataclass


@dataclass(frozen=True)
class Direction:
    name: str
    symbol: str
    delta_x: int
    delta_y: int


RIGHT = Direction(name="right", symbol=">", delta_x=1, delta_y=0)
LEFT = Direction(name="left", symbol="<", delta_x=-1, delta_y=0)
UP = Direction(name="up", symbol="^", delta_x=0, delta_y=-1)
DOWN = Direction(name="down", symbol="v", delta_x=0, delta_y=1)

LEFT_UPPER = Direction(name="left-upper", symbol="<^", delta_x=-1, delta_y=-1)
LEFT_LOWER = Direction(name="left-lower", symbol="<v", delta_x=-1, delta_y=1)
RIGHT_UPPER = Direction(name="right-upper", symbol=">^", delta_x=1, delta_y=-1)
RIGHT_LOWER = Direction(name="right-lower", symbol=">v", delta_x=1, delta_y=1)

STRAIGHT_DIRECTIONS: list[Direction] = [RIGHT, LEFT, DOWN, UP]
HORIZONTAL_DIRECTIONS: list[Direction] = [RIGHT, LEFT]
VERTICAL_DIRECTIONS: list[Direction] = [UP, DOWN]
DIAGONAL_DIRECTIONS: list[Direction] = [LEFT_UPPER, LEFT_LOWER, RIGHT_UPPER, RIGHT_LOWER]
ALL_DIRECTIONS = STRAIGHT_DIRECTIONS + DIAGONAL_DIRECTIONS
