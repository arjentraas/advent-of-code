from utils import read_input_lines


def main():
    """Exactly the same, but without checking if it has been already in the path"""
    input = read_input_lines("_2024/day10/input.txt")
    hiking_trails: dict[tuple, int] = {}
    grid: dict[tuple, int] = {}
    for y, line in enumerate(input, 1):
        for x, height in enumerate(line, 1):
            grid[(x, y)] = int(height)
            if height == "0":
                hiking_trails[(x, y)] = int(height)

    max_x = len(input[0])
    max_y = len(input)

    sum_hike_trail = 0
    for coordinate, height in hiking_trails.items():
        hike_score = 0
        path = [coordinate]
        while path and height < 10:
            x, y = path.pop(0)
            height = grid[(x, y)]
            if height == 9:
                hike_score += 1

            # Left
            if x > 1 and grid[(x - 1, y)] == height + 1 and (x - 1, y):
                path.append((x - 1, y))

            # Right
            if x < max_x and grid[(x + 1, y)] == height + 1 and (x + 1, y):
                path.append((x + 1, y))

            # Up
            if y > 1 and grid[(x, y - 1)] == height + 1 and (x, y - 1):
                path.append((x, y - 1))

            # Down
            if y < max_y and grid[(x, y + 1)] == height + 1 and (x, y + 1):
                path.append((x, y + 1))

        sum_hike_trail += hike_score

    print(sum_hike_trail)


main()
