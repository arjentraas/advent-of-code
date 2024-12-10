from itertools import combinations

from _2024.day8.part1 import Distance, Point, calculate_anti_nodes, get_antennas, get_frequencies
from helper import read_input_lines


def within_bounds(point: Point, max_x: int, max_y: int) -> bool:
    return -1 < point.x <= max_x and -1 < point.y <= max_y


def main():
    grid = read_input_lines("_2024/day8/example2_input.txt")
    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1
    frequencies = get_frequencies(grid)

    antinode_locations: set[Point] = set()
    for frequency in frequencies:
        antennas = get_antennas(grid, frequency)
        antenna_combos = combinations(antennas, r=2)

        for antenna1, antenna2 in antenna_combos:
            anti_nodes = calculate_anti_nodes(antenna1, antenna2)
            while any(within_bounds(anti_node, max_x, max_y) for anti_node in anti_nodes):
                if within_bounds(anti_nodes[0], max_x, max_y):
                    antinode_locations.add(anti_nodes[0])

                if within_bounds(anti_nodes[1], max_x, max_y):
                    antinode_locations.add(anti_nodes[1])

                anti_nodes = calculate_anti_nodes(anti_nodes[0], anti_nodes[1])

    print(len(antinode_locations))
    for loc in antinode_locations:
        print(loc)


main()
