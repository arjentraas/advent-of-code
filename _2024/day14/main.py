from collections import defaultdict
from math import ceil

from utils import Grid, Position, read_input_lines


def parse_input():
    positions = []
    velocities = []
    for line in read_input_lines("_2024/day14/input.txt"):
        splt = line.split(" ")
        current_pos = splt[0].split("=")[1].split(",")
        current_col = int(current_pos[0])
        current_row = int(current_pos[1])
        positions.append((current_col, current_row))

        velocity = splt[1].split("=")[1].split(",")
        delta_col = int(velocity[0])
        delta_row = int(velocity[1])
        velocities.append((delta_col, delta_row))

    return (positions, velocities)


def get_quadrant(end_pos: Position, g: Grid):
    row_perimeter = ceil((g.max_row + 1) / 2)
    col_perimeter = ceil((g.max_col + 1) / 2)

    if end_pos[0] < col_perimeter and end_pos[1] < row_perimeter:
        return "left-upper"

    if end_pos[0] > col_perimeter and end_pos[1] < row_perimeter:
        return "right-upper"

    if end_pos[0] < col_perimeter and end_pos[1] > row_perimeter:
        return "left-lower"

    if end_pos[0] > col_perimeter and end_pos[1] > row_perimeter:
        return "right-lower"


def main():
    positions, velocities = parse_input()
    grid = Grid().empty_grid(col_count=101, row_count=103)
    robot_id = 1

    end_positions = defaultdict(int)
    quadrants = defaultdict(int)
    for start_position, velocity in zip(positions, velocities):
        grid[start_position] = str(robot_id)

        new_pos = start_position
        for _ in range(100):
            new_pos = grid.move_position(new_pos, velocity[0], velocity[1], teleport=True, replace=True)

        end_positions[new_pos] += 1

        if not (q := get_quadrant(new_pos, grid)):
            continue

        quadrants[q] += 1

    safety_factor = 1
    for num in quadrants.values():
        safety_factor = safety_factor * num
    print(safety_factor)


# 227931648 - too low
main()
