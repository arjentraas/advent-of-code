from itertools import combinations

from _2024.day8.part1 import Distance, Point, calculate_distance, get_antennas, get_frequencies
from helper import read_input_lines


def within_bounds(point: Point, max_x: int, max_y: int) -> bool:
    return -1 < point.x <= max_x and -1 < point.y <= max_y


def calculate_anti_nodes(antenna1: Point, antenna2: Point, resonant_factor: int = 1):
    distance = calculate_distance(antenna1, antenna2)
    largest_y = antenna1 if antenna1.y > antenna2.y else antenna2
    smallest_y = antenna1 if largest_y == antenna2 else antenna2
    largest_x = antenna1 if antenna1.x > antenna2.x else antenna2
    smallest_x = antenna1 if largest_x == antenna2 else antenna2
    if smallest_x == smallest_y:
        return (
            Point(largest_x.x + distance.x * resonant_factor, largest_y.y + distance.y * resonant_factor),
            Point(smallest_x.x - distance.x * resonant_factor, smallest_y.y - distance.y * resonant_factor),
        )

    elif largest_y == antenna1 and largest_x == antenna2:
        return (
            Point(antenna1.x - distance.x * resonant_factor, antenna1.y + distance.y * resonant_factor),
            Point(antenna2.x + distance.x * resonant_factor, antenna2.y - distance.y * resonant_factor),
        )

    else:
        return (
            Point(antenna2.x - distance.x * resonant_factor, antenna2.y + distance.y * resonant_factor),
            Point(antenna1.x + distance.x * resonant_factor, antenna1.y - distance.y * resonant_factor),
        )


def calculate_distance_factor(distance1: Distance, distance2: Distance):
    if distance1.x == 0 or distance1.y == 0 or distance2.x == 0 or distance2.y == 0:
        return
    x_factor = distance1.x / distance2.x
    y_factor = distance1.y / distance2.y
    if x_factor == y_factor:
        return x_factor


def points_in_line(a: Point, b: Point, c: Point) -> bool:
    """Check if three points are in line by checking the area of the ABC triangle is 0. Formula from Google :)"""
    return a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y) == 0


def antennas_in_line(anti_nodes: set[Point], all_antennas: set[Point]) -> set[Point]:
    """Check which combinations antennas are in line with two anti nodes."""
    in_line = set()
    for antenna1, antenna2 in combinations(all_antennas, r=2):
        if antenna1 in in_line and antenna2 in in_line:
            continue

        for anti_node in anti_nodes:
            if points_in_line(antenna1, antenna2, anti_node) is True:
                in_line.update({antenna1, antenna2})
                break
    return in_line


def main():
    grid = read_input_lines("_2024/day8/input.txt")
    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1
    frequencies = get_frequencies(grid)

    antinode_locations: set[Point] = set()
    for frequency in frequencies:
        antennas = get_antennas(grid, frequency)
        antenna_combos = combinations(antennas, r=2)

        for antenna1, antenna2 in antenna_combos:
            anti_nodes = calculate_anti_nodes(antenna1, antenna2)
            resonant_factor = 1
            while any(within_bounds(anti_node, max_x, max_y) for anti_node in anti_nodes):
                if within_bounds(anti_nodes[0], max_x, max_y):
                    antinode_locations.add(anti_nodes[0])

                if within_bounds(anti_nodes[1], max_x, max_y):
                    antinode_locations.add(anti_nodes[1])

                resonant_factor += 1
                anti_nodes = calculate_anti_nodes(antenna1, antenna2, resonant_factor)

        antinode_locations.update(antennas_in_line(anti_nodes=antinode_locations, all_antennas=antennas))

    print(len(antinode_locations))
    # for loc in antinode_locations:
    #     print(loc)


main()
