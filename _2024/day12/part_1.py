from collections import defaultdict

from helper import read_input_lines


def get_garden_plots():
    input = read_input_lines("_2024/day12/example_input.txt")
    garden_plots = defaultdict(list)
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            garden_plots[char].append((x, y))

    return garden_plots


def are_adjacent(location1: tuple[int, int], location2: tuple[int, int]) -> bool:
    return (abs(location1[0] - location2[0]) == 1 and location1[1] == location2[1]) or (
        abs(location1[1] - location2[1]) == 1 and location1[0] == location2[0]
    )


def calc_perimeter(region: list[tuple[int, int]]):
    if len(region) == 1:
        return 4

    p = 0
    for loc in region:
        neighbours = {l for l in region if l != loc and are_adjacent(loc, l)}
        neighbour_count = len(neighbours)
        if neighbour_count == 1:
            p += 3
        elif neighbour_count == 2:
            p += 2
        elif neighbour_count == 3:
            p += 1
    return p


def main():
    garden_plots = get_garden_plots()
    sum = 0
    for plant_type, regions in garden_plots.items():
        for region in regions:
            area = len(region)
            perimeter = calc_perimeter(region)
            sum += area * perimeter
    print(sum)


main()
# 779940 - too low
