from typing import Generator

import networkx as nx

from utils import (
    DIAGONAL_DIRECTIONS,
    DOWN,
    HORIZONTAL_DIRECTIONS,
    LEFT,
    LEFT_LOWER,
    LEFT_UPPER,
    RIGHT,
    RIGHT_LOWER,
    RIGHT_UPPER,
    STRAIGHT_DIRECTIONS,
    UP,
    VERTICAL_DIRECTIONS,
    Grid,
    Position,
    read_input,
    read_input_lines,
)


def get_graph(file):
    input = read_input_lines(file)
    g = nx.Graph()

    for y, line in enumerate(input):
        for x, char in enumerate(line):
            node_name = (x, y)
            g.add_node(node_name, type=char)
            if (x + 1, y) in g.nodes:
                g.add_edge(node_name, (x + 1, y))
            if (x - 1, y) in g.nodes:
                g.add_edge(node_name, (x - 1, y))
            if (x, y + 1) in g.nodes:
                g.add_edge(node_name, (x, y + 1))
            if (x, y - 1) in g.nodes:
                g.add_edge(node_name, (x, y - 1))
    return g


INNER_CORNER_COMBOS = [
    ((UP, LEFT), LEFT_UPPER),
    ((UP, RIGHT), RIGHT_UPPER),
    ((DOWN, RIGHT), RIGHT_LOWER),
    ((DOWN, LEFT), LEFT_LOWER),
]

OUTER_CORNER_COMBOS = [(LEFT, UP), (LEFT, DOWN), (RIGHT, DOWN), (RIGHT, UP)]


def get_corners(grid: Grid, island: Generator) -> int:
    if len(list(island)) == 1:
        return 4

    if len(list(island)) == 2:
        return 4

    corners = 0
    for node in island:
        col, row = node
        pos = Position(col, row)
        straight_neighbors = set()
        straight_neighbors_in_island = set()
        straight_neighbors_outside = set()

        for d in STRAIGHT_DIRECTIONS:
            neighbor_pos = grid.get_neighbour_position(pos, d, False)
            straight_neighbors.add(neighbor_pos)
            if neighbor_pos and (neighbor_pos.col, neighbor_pos.row) in island:
                straight_neighbors_in_island.add((neighbor_pos, d))
            else:
                straight_neighbors_outside.add((neighbor_pos, d))

        horizontal_outside = {n[1] for n in straight_neighbors_outside if n[1] in HORIZONTAL_DIRECTIONS}
        vertical_outside = {n[1] for n in straight_neighbors_outside if n[1] in VERTICAL_DIRECTIONS}

        if len(straight_neighbors_outside) == 3 and len(straight_neighbors_in_island) == 1:
            corners += 2
            continue

        if len(horizontal_outside) == 1 and len(vertical_outside) == 1:
            corners += 1

        if len(horizontal_outside) == 2 and len(vertical_outside) == 0:
            continue

        if len(horizontal_outside) == 0 and len(vertical_outside) == 2:
            continue

        diagonal_not_in_island = set()
        for d in DIAGONAL_DIRECTIONS:
            neighbor_pos = grid.get_neighbour_position(pos, d, False)
            if neighbor_pos is None:
                continue

            if (neighbor_pos.col, neighbor_pos.row) not in island:
                diagonal_not_in_island.add(d)

        straight_neighbors_in_island_directions = {n[1] for n in straight_neighbors_in_island}
        for straights, diagonal in INNER_CORNER_COMBOS:
            if (
                all(d in straight_neighbors_in_island_directions for d in straights)
                and diagonal in diagonal_not_in_island
            ):
                corners += 1
        pass

    return corners


def main():
    file = "_2024/day12/input.txt"
    g = get_graph(file)
    grid = Grid(file)
    plant_types = set(read_input(file).strip())
    plant_types.remove("\n")

    total_price = 0
    for plant_type in plant_types:
        plant_graph = g.copy()
        plant_graph.remove_nodes_from(
            [n for n, n_data in plant_graph.nodes(data=True) if n_data.get("type") != plant_type]
        )
        for island in nx.connected_components(plant_graph):
            area = len(island)
            corners = get_corners(grid, island)
            island_price = area * corners
            total_price += island_price

    print(total_price)


main()
