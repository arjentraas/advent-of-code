import networkx as nx

from utils import STRAIGHT_DIRECTIONS, Grid, Position, read_input, read_input_lines


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


def main():
    file = "_2024/day12/example_input.txt"
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
            perimeter = []
            sides = set()
            for node in island:
                row, col = node
                for direction in STRAIGHT_DIRECTIONS:
                    neighbor = grid.get_neighbour_position(Position(row, col), direction)
                    if neighbor and (neighbor.col, neighbor.row) in island:
                        continue
                    perimeter.append((node, (neighbor.col, neighbor.row)))
            print(sides)
            pass

    print(total_price)


main()
