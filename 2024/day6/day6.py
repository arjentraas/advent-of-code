import re
from collections import defaultdict
from time import sleep
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


def get_substrings(string: str) -> list[str]:
    max_window = int(len(string) / 3)
    min_window = 5
    if max_window <= min_window:
        return {}

    substrings = set()
    for window in range(min_window, max_window):
        end_window_index = len(string)
        start_window_index = len(string) - window
        substrings.add(string[start_window_index:end_window_index])

    return substrings


def substring_in_order(substring: str, string: str) -> bool:
    matches = list(re.finditer(substring, string))

    for i in range(len(matches) - 2):
        if matches[i].span()[1] == matches[i + 1].span()[0]:
            continue
        else:
            return False
    return True


def in_loop(positions_visited: list[tuple[int, int]], min_occ=3) -> bool:
    string = ""
    for x, y in positions_visited:
        string += str(x)
        string += str(y)

    occurrences = defaultdict(int)
    # tally all occurrences of all substrings
    for substring in get_substrings(string):
        occurrences[substring] = string.count(substring)

    if len(occurrences) == 0:
        return False

    for substring, count in occurrences.items():
        if count < 3:  # substring (series of steps) should at least occur 3 times to to be able to be a loop
            continue

        if substring_in_order(substring, string):
            return True

    return False


def print_grid(grid: list[str]):
    for line in grid:
        print(line)
    print()


def part_2():
    grid = parse_input()
    start_position = start_x, start_y = get_start(grid)
    start_direction = grid[start_y][start_x]

    max_x = len(grid) - 1
    max_y = len(grid[0]) - 1

    position = start_position
    direction = start_direction

    loop_count = 0

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            grid = parse_input()
            positions_visited = []
            loop_obstruction = False
            position = start_position
            direction = start_direction

            if (x, y) == start_position:
                continue

            grid = place_obstruction(x, y, grid)

            max_steps = 10000
            steps = 0
            while True:
                steps += 1

                if steps == max_steps:
                    print(f" ({x}, {y} - Too many steps")
                    loop_obstruction = True
                    break
                positions_visited.append(position)

                if in_loop(positions_visited) is True:
                    loop_obstruction = True
                    print(f" ({x}, {y} - in loop")
                    break

                grid, direction, position = walk(grid, position, direction)
                if position[1] == max_y or position[0] == max_x:
                    break

                if position[0] == 0 or position[1] == 0:
                    break

            if loop_obstruction is True:
                loop_count += 1

    print(loop_count)


part_2()
