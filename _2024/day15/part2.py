from utils.directions import DOWN, LEFT, RIGHT, STRAIGHT_DIRECTIONS, Direction
from utils.grid import Grid, Position
from utils.read import read_input_lines


class WareHouseGrid(Grid):
    def sum_gps_coordinates(self):
        sum = 0
        for pos, val in self.items():
            if val == "[":
                sum += self._get_gps_coordinate(pos)
        print(sum)

    def _get_gps_coordinate(self, left_box_edge: Position) -> int:
        return 100 * (left_box_edge.y - 1) + left_box_edge.x - 1


def get_direction(symbol: str) -> Direction:
    for dir in STRAIGHT_DIRECTIONS:
        if dir.symbol == symbol:
            return dir
    raise KeyError


def extend_grid(lines: list[str]):
    new_lines = []
    for line in lines:
        new_line = ""
        for char in line:
            if char == "@":
                new_line += "@."
            elif char == "#":
                new_line += "##"
            elif char == ".":
                new_line += ".."
            elif char == "O":
                new_line += "[]"
        new_lines.append(new_line)
    return new_lines


def parse_input():
    inp = read_input_lines("_2024/day15/input.txt")

    grid = WareHouseGrid()
    grid.max_y = len(inp) - 1
    grid.max_x = len(inp[0]) - 1
    for y, line in enumerate(extend_grid(inp), 1):
        for x, char in enumerate(line, 1):
            grid[Position(x, y)] = char
        if line == "":
            break

    directions = []
    for direction_line in inp[y:]:  # type: ignore
        for char in direction_line:
            directions.append(get_direction(char))
    return grid, directions


def get_second_half_box(position: Position, grid: Grid, direction: Direction):
    if grid[position] == "[":
        return grid.get_neighbour_position(position, RIGHT)
    else:
        return grid.get_neighbour_position(position, LEFT)


def push(push_from_pos: Position, direction: Direction, grid: Grid):
    pos_to_push: list[Position] = []
    to_push: bool = False
    visited_positions = []
    positions_to_check = [push_from_pos]
    while positions_to_check:
        current_position = positions_to_check.pop(0)
        neighbor_pos, neighbor_val = grid.get_neighbour(current_position, direction)
        if neighbor_val in ["[", "]"] and neighbor_pos not in pos_to_push:
            pos_to_push.append(neighbor_pos)
            second_half_box = get_second_half_box(neighbor_pos, grid, direction)
            pos_to_push.append(second_half_box)  # type: ignore
            positions_to_check.append(second_half_box)  # type: ignore
        elif neighbor_val == ".":
            to_push = True
            continue
        elif neighbor_val == "#":
            break
        positions_to_check.append(neighbor_pos)
        visited_positions.append(current_position)

    if not to_push:
        return (None, False)

    for pos in pos_to_push:
        neighbor_val = grid.get_neighbour_value(pos, direction)
        if neighbor_val == "#":
            to_push = False

    if to_push is False:
        return (None, False)

    pos_to_push.reverse()  # reverse order to move the last box first
    for pos in pos_to_push:
        grid.move_item(pos, direction)

    return grid.move_item(push_from_pos, direction), to_push  # move robot itself and return the new position


def part_2():
    grid, directions = parse_input()
    position = next(pos for pos, v in grid.items() if v == "@")

    for direction in directions:
        if position == (12, 4) and direction == DOWN:
            pass
        neighbor_val = grid.get_neighbour_value(position, direction)
        if neighbor_val == "#":
            continue

        if neighbor_val in ["[", "]"]:
            new_position, pushed = push(position, direction, grid)
            if new_position and pushed:
                position = new_position

        if neighbor_val == ".":
            new_position = grid.move_item(position, direction)
            position = new_position

    # grid.print()

    grid.sum_gps_coordinates()


part_2()
