from utils import read_input_lines


def parse_input():
    positions = []
    velocities = []
    for line in read_input_lines("_2024/day14/example_input.txt"):
        splt = line.split(" ")
        current_pos = splt[0].split("=")[1].split(",")
        current_col = int(current_pos[0])
        current_row = int(current_pos[1])
        positions.append((current_col, current_row))

        velocity = splt[1].split("=")[1].split(",")
        delta_col = int(velocity[0])
        delta_row = int(velocity[1])
        velocities.append((delta_col, delta_row))

    return (positions, velocities)


def main():
    positions, velocities = parse_input()


main()
