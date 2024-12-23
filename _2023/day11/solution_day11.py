from itertools import pairwise

import networkx as nx

from utils import read_input_lines


def expand_space(lines: list):
    current_space = lines

    for i in range(len(lines[0])):
        column = [line[i] for line in current_space]
        if "#" in column:
            continue

        new_space = []
        for line in lines:
            new_space.append(line[: i + 1] + "." + line[i + 1 :])

        current_space == new_space

    new_space = []
    for space_line in current_space:
        new_space.append(space_line)

        if "#" in space_line:
            continue

        new_space.append(space_line)

    return new_space


def get_network(space: list):
    G = nx.Graph()

    galaxy_nr = 1
    for y, space_line in enumerate(reversed(space), 1):
        for x, pixel in enumerate(space_line, 1):
            if pixel == "#":
                new_node = str(galaxy_nr)
                galaxy_nr += 1
            else:
                new_node = f"empty {x} {y}"

            G.add_node(new_node, x=x, y=y)

    galaxy_nr = 1
    for y, space_line in enumerate(reversed(space), 1):
        for (xa, pixela), (xb, pixelb) in pairwise(enumerate(space_line, 1)):
            if pixela == "#":
                node_a = str(galaxy_nr)
                galaxy_nr += 1
            else:
                node_a = f"empty {xa} {y}"

            if pixelb == "#":
                node_b = str(galaxy_nr)
                galaxy_nr += 1
            else:
                node_b = f"empty {xb} {y}"

            G.add_edge(node_a, node_b)

    return G


def part1():
    input = read_input_lines("day11/test_input_day11.txt")
    expanded_space = expand_space(input)
    for i in expanded_space:
        print(i)
    graph = get_network(expanded_space)


part1()
