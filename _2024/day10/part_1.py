from collections import deque

from helper import read_input_lines


def main():
    input = read_input_lines("_2024/day10/example_input.txt")
    hiking_trails: dict[tuple, int] = {}
    grid: dict[tuple, int] = {}
    for y, line in enumerate(input, 1):
        for x, height in enumerate(line, 1):
            grid[(x, y)] = int(height)
            if height == "0":
                hiking_trails[(x, y)] = int(height)

    max_x = len(input[0])
    max_y = len(input)

    for coordinate, height in hiking_trails.items():
        path = [coordinate]
        while path:
            x, y = path.pop(0)
            left = grid[(x - 1, y)] if x > 1 else None
            right = grid[(x + 1, y)] if x < max_x else None
            up = grid[(x, y - 1)] if y > 1 else None
            down = grid[(x, y + 1)] if y < max_y else None
            neighbours = [left, right, up, down]

            if not any(neighbour == height + 1 for neighbour in neighbours):
                break

    pass


main()
