from utils.directions import RIGHT, STRAIGHT_DIRECTIONS, Direction
from utils.grid import Grid, Position
from utils.read import read_input_lines


class FishGrid(Grid): ...


def get_direction(symbol: str) -> Direction:
    for dir in STRAIGHT_DIRECTIONS:
        if dir.symbol == symbol:
            return dir
    raise KeyError


def parse_input():
    inp = read_input_lines("_2024/day15/example_input.txt")

    grid = FishGrid()
    grid.max_y = len(inp) - 1
    grid.max_x = len(inp[0]) - 1
    for y, line in enumerate(inp, 1):
        for x, char in enumerate(line, 1):
            grid[Position(x, y)] = char
        if line == "":
            break
    directions = [get_direction(s) for s in inp[-1]]
    return grid, directions


def push(push_from_pos: Position, direction: Direction, grid: Grid):
    pos_to_push: list[Position] = []
    while True:
        neighbor_pos, neighbor_val = grid.get_neighbour(push_from_pos, direction)
        if neighbor_val == "O":
            pos_to_push.append(neighbor_pos)
        else:
            break
        push_from_pos = neighbor_pos

    return pos_to_push


def part_1():
    grid, directions = parse_input()
    position = next(pos for pos, v in grid.items() if v == "@")
    grid.print()
    assert push(Position(3, 2), RIGHT, grid) == [Position(4, 2)]
    # for direction in directions:
    #     neighbor_pos, neighbor_val = grid.get_neighbour(position, direction)
    #     if neighbor_val == "#":
    #         continue

    #     if neighbor_val == "O":
    #         push()


part_1()
