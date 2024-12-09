from collections import defaultdict
from typing import Literal

from helper import read_input_lines

type Direction = Literal["^", "v", ">", "<"]


def parse_input():
    return read_input_lines("2024/day6/input_day6.txt")


def get_start(lines: list[str]) -> tuple[int, int]:
    current_line = next(line for line in lines if "^" in line)
    current_y = lines.index(current_line)
    current_x = current_line.index("^")
    return (current_x, current_y)


def get_new_position(current_position: tuple[int, int], direction: Direction) -> tuple[int, int]:
    current_x, current_y = current_position
    match direction:
        case "^":
            new_x = current_x
            new_y = current_y - 1
        case "v":
            new_x = current_x
            new_y = current_y + 1
        case ">":
            new_x = current_x + 1
            new_y = current_y
        case "<":
            new_x = current_x - 1
            new_y = current_y
        case _:
            raise ValueError
    return (new_x, new_y)


def rotate_direction(direction: Direction) -> Direction:
    rotate_dict = {"^": ">", "v": "<", "<": "^", ">": "v"}
    return rotate_dict[direction]


def walk(grid: list[str], current_position: tuple[int, int], direction: Direction):
    new_grid = grid.copy()
    current_x, current_y = current_position

    new_position = new_x, new_y = get_new_position(current_position, direction)
    if new_grid[new_y][new_x] in ("#", "O"):
        new_direction = rotate_direction(direction)
        new_grid[current_y] = new_grid[current_y][:current_x] + new_direction + new_grid[current_y][current_x + 1 :]
        direction = new_direction
        new_position = current_position
    else:
        new_grid[current_y] = new_grid[current_y][:current_x] + "." + new_grid[current_y][current_x + 1 :]
        if direction in ["^", "v"]:
            new_grid[new_y] = new_grid[new_y][:new_x] + direction + new_grid[new_y][current_x + 1 :]
        elif direction == ">":
            new_grid[new_y] = new_grid[new_y][:new_x] + direction + new_grid[new_y][current_x + 2 :]
        else:
            new_grid[new_y] = new_grid[new_y][:new_x] + direction + new_grid[new_y][current_x:]
    return (new_grid, direction, new_position)


def part_1():
    grid = parse_input()

    start_position = start_x, start_y = get_start(grid)
    start_direction = grid[start_y][start_x]

    max_x = len(grid) - 1
    max_y = len(grid[0]) - 1

    position = start_position
    direction = start_direction
    unique_positions = set()

    while True:
        unique_positions.add(position)

        grid, direction, position = walk(grid, position, direction)
        if position[1] == max_y or position[0] == max_x:
            break

        if position[0] == 0 or position[1] == 0:
            break

    print(len(unique_positions) + 1)


# part_1()


def place_obstruction(x: int, y: int, grid: list[str]) -> list[str]:
    grid[y] = grid[y][:x] + "O" + grid[y][x + 1 :]
    return grid


def remove_obstructions(grid: list[str]) -> list[str]:
    for i in range(len(grid)):
        grid[i] = grid[i].replace("O", ".")
    return grid


def print_grid(grid: list[str]):
    for line in grid:
        print(line)
    print()


def part_2():
    grid = parse_input()
    start_position = start_x, start_y = get_start(grid)
    start_direction = grid[start_y][start_x]
    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1
    loop_count = 0
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if grid[y][x] == "#":
                continue
            if (x, y) == start_position:
                continue
            grid = parse_input()
            position = start_position
            direction = start_direction
            grid = place_obstruction(x, y, grid)
            visited: defaultdict[tuple[int, int], set[str]] = defaultdict(set)
            while True:
                visited[position].add(direction)
                grid, direction, position = walk(grid, position, direction)
                if direction in visited[position]:
                    loop_count += 1
                    break
                if position[1] == max_y or position[0] == max_x:
                    break

                if position[1] == 0 or position[0] == 0:
                    break
    print(loop_count)


part_2()
