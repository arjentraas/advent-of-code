from itertools import combinations
from typing import NamedTuple

from helper import read_input_lines


class Point(NamedTuple):
    x: int
    y: int


class Distance(NamedTuple):
    x: int
    y: int


def get_frequencies(grid: list[str]) -> set[str]:
    return {char for line in grid for char in line if char != "."}


def get_antennas(grid: list[str], frequency: str) -> set[Point]:
    return {Point(x=x, y=y) for y, line in enumerate(grid) for x, char in enumerate(line) if char == frequency}


def calculate_distance(antenna1: Point, antenna2: Point):
    """Get the absolute distance between two points."""
    return Distance(x=abs(antenna1.x - antenna2.x), y=abs(antenna1.y - antenna2.y))


def calculate_anti_nodes(antenna1: Point, antenna2: Point):
    distance = calculate_distance(antenna1, antenna2)
    largest_y = antenna1 if antenna1.y > antenna2.y else antenna2
    smallest_y = antenna1 if largest_y == antenna2 else antenna2
    largest_x = antenna1 if antenna1.x > antenna2.x else antenna2
    smallest_x = antenna1 if largest_x == antenna2 else antenna2
    if smallest_x == smallest_y:
        return (
            Point(largest_x.x + distance.x, largest_y.y + distance.y),
            Point(smallest_x.x - distance.x, smallest_y.y - distance.y),
        )

    elif largest_y == antenna1 and largest_x == antenna2:
        return (
            Point(antenna1.x - distance.x, antenna1.y + distance.y),
            Point(antenna2.x + distance.x, antenna2.y - distance.y),
        )

    else:
        return (
            Point(antenna2.x - distance.x, antenna2.y + distance.y),
            Point(antenna1.x + distance.x, antenna1.y - distance.y),
        )


def main():
    grid = read_input_lines("_2024/day8/example_input.txt")
    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1
    frequencies = get_frequencies(grid)

    antinode_locations: set[Point] = set()
    for frequency in frequencies:
        antennas = get_antennas(grid, frequency)
        antenna_combos = combinations(antennas, r=2)

        for antenna1, antenna2 in antenna_combos:
            anti_nodes = calculate_anti_nodes(antenna1, antenna2)
            for anti_node in anti_nodes:
                if anti_node.x > max_x or anti_node.y > max_y:
                    continue
                if anti_node.x < 0 or anti_node.y < 0:
                    continue
                antinode_locations.add(anti_node)

    # print(len(antinode_locations))


main()
