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
            height = grid[(x, y)]
            # Left
            if x > 1 and grid[(x - 1, y)] == height + 1:
                path.append((x - 1, y))

            # Right
            if x < max_x and grid[(x + 1, y)] == height + 1:
                path.append((x + 1, y))

            # Up
            if y > 1 and grid[(x, y - 1)] == height + 1:
                path.append((x, y - 1))

            # Down
            if y < max_y and grid[(x, y + 1)] == height + 1:
                path.append((x, y + 1))

    pass


main()
