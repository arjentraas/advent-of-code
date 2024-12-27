from collections import defaultdict
from math import ceil, prod

from utils import read_input_lines


def main():
    q = defaultdict(int)
    for line in read_input_lines("_2024/day14/input.txt"):
        splt = line.split(" ")
        start_pos = splt[0].split("=")[1].split(",")

        start_col = int(start_pos[0])
        start_row = int(start_pos[1])

        velocity = splt[1].split("=")[1].split(",")
        delta_col = int(velocity[0])
        delta_row = int(velocity[1])

        max_col = 101
        max_row = 103

        col = start_col
        row = start_row

        coll_boundary = ceil(max_col / 2) - 1
        row_boundary = ceil(max_row / 2) - 1

        for _ in range(100):
            new_col = col + delta_col
            new_row = row + delta_row

            if new_col > max_col - 1:
                new_col = new_col - max_col
            elif new_col < 0:
                new_col = max_col + new_col  # plus because it's negative

            if new_row > max_row - 1:
                new_row = new_row - max_row
            elif new_row < 0:
                new_row = max_row + new_row

            col = new_col
            row = new_row

        if new_col < coll_boundary:
            if new_row < row_boundary:
                q["left-up"] += 1  # left up
            elif new_row > row_boundary:
                q["left-down"] += 1  # left down
        elif new_col > coll_boundary:
            if new_row < row_boundary:
                q["right-up"] += 1  # right up
            elif new_row > row_boundary:
                q["right-down"] += 1  # right down

    print(prod(q.values()))


# 227931648 - too low
# 224250000
# 221369760
main()
