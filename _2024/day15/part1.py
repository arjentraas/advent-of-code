from utils.directions import STRAIGHT_DIRECTIONS, Direction
from utils.grid import Grid, Position
from utils.read import read_input_lines


class WareHouseGrid(Grid):
    def sum_gps_coordinates(self):
        sum = 0
        for pos, val in self.items():
            if val == "O":
                sum += self._get_gps_coordinate(pos)
        print(sum)

    def _get_gps_coordinate(self, position: Position) -> int:
        top_edge_distance = position.y - 1
        left_edge_distance = position.x - 1
        return 100 * top_edge_distance + left_edge_distance


def get_direction(symbol: str) -> Direction:
    for dir in STRAIGHT_DIRECTIONS:
        if dir.symbol == symbol:
            return dir
    raise KeyError


def parse_input():
    inp = read_input_lines("_2024/day15/input.txt")

    grid = WareHouseGrid()
    grid.max_y = len(inp) - 1
    grid.max_x = len(inp[0]) - 1
    for y, line in enumerate(inp, 1):
        for x, char in enumerate(line, 1):
            grid[Position(x, y)] = char
        if line == "":
            break

    directions = []
    for direction_line in inp[y:]:  # type: ignore
        for char in direction_line:
            directions.append(get_direction(char))
    return grid, directions


def push(push_from_pos: Position, direction: Direction, grid: Grid):
    pos_to_push: list[Position] = []
    to_push: bool = False
    current_position = push_from_pos
    while True:
        neighbor_pos, neighbor_val = grid.get_neighbour(current_position, direction)
        if neighbor_val == "O":
            pos_to_push.append(neighbor_pos)
        elif neighbor_val == ".":
            to_push = True
            break
        else:
            break
        current_position = neighbor_pos

    if not to_push:
        return (None, False)

    pos_to_push.reverse()  # reverse order to move the last box first
    for pos in pos_to_push:
        grid.move_item(pos, direction)

    return grid.move_item(push_from_pos, direction), to_push  # move robot itself and return the new position


def part_1():
    grid, directions = parse_input()
    position = next(pos for pos, v in grid.items() if v == "@")

    for direction in directions:
        neighbor_val = grid.get_neighbour_value(position, direction)
        if neighbor_val == "#":
            continue

        if neighbor_val == "O":
            new_position, pushed = push(position, direction, grid)
            if new_position and pushed:
                position = new_position

        if neighbor_val == ".":
            new_position = grid.move_item(position, direction)
            position = new_position

    grid.sum_gps_coordinates()


part_1()
