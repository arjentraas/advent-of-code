import networkx as nx

from helper import read_input_lines


def main():
    input = read_input_lines("_2024/day12/input.txt")
    g = nx.Graph()
    plant_types = set()

    for y, line in enumerate(input):
        for x, char in enumerate(line):
            plant_types.add(char)
            node_name = f"{x},{y}"
            g.add_node(node_name, type=char)
            if f"{x + 1},{y}" in g.nodes:
                g.add_edge(node_name, f"{x + 1},{y}")
            if f"{x - 1},{y}" in g.nodes:
                g.add_edge(node_name, f"{x - 1},{y}")
            if f"{x},{y+1}" in g.nodes:
                g.add_edge(node_name, f"{x},{y+1}")
            if f"{x},{y-1}" in g.nodes:
                g.add_edge(node_name, f"{x},{y-1}")

    total_price = 0
    for plant_type in plant_types:
        subgraph = g.copy()
        subgraph.remove_nodes_from([n for n, n_data in subgraph.nodes(data=True) if n_data.get("type") != plant_type])
        for island in nx.connected_components(subgraph):
            area = len(island)
            perimeter = 0
            if area == 1:
                perimeter = 4
            else:
                for node in island:
                    n_neighbours = len(subgraph.edges(node))
                    match n_neighbours:
                        case 1:
                            perimeter += 3
                        case 2:
                            perimeter += 2
                        case 3:
                            perimeter += 1
            total_price += area * perimeter
            pass

    print(total_price)


main()
