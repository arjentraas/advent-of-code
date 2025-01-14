from dataclasses import dataclass
from typing import Generator

from utils import read_input_lines

max_x = 11
max_y = 7


@dataclass
class Robot:
    x: int
    y: int
    delta_x: int
    delta_y: int

    def move(self, n: int = 0):
        for _ in range(n):
            new_x = self.x + self.delta_x
            new_y = self.y + self.delta_y

            # Teleport from right to left or left to right.
            if new_x > max_x - 1:
                new_x = new_x - max_x
            elif new_x < 0:
                new_x = max_x + new_x

            # Teleport from top to bottom or bottom to top.
            if new_y > max_y - 1:
                new_y = new_y - max_y
            elif new_y < 0:
                new_y = max_y + new_y

            self.x = new_x
            self.y = new_y


def get_robots() -> Generator[Robot, None, None]:
    robots = read_input_lines("_2024/day14/example_input.txt")
    for robot in robots:
        robot_split = robot.split(" ")
        start_position = robot_split[0].split("=")[1].split(",")

        start_x = int(start_position[0])
        start_y = int(start_position[1])

        velocity = robot_split[1].split("=")[1].split(",")
        delta_x = int(velocity[0])
        delta_y = int(velocity[1])
        yield Robot(start_x, start_y, delta_x, delta_y)


most_robots_count = 251


def robots_forming_tree(robots: list[Robot]) -> bool:
    return False


def main():
    robots = list(get_robots())
    n_seconds = 1
    while True:
        for robot in robots:
            robot.move()

        if robots_forming_tree(robots):
            break

        n_seconds += 1

    print(n_seconds)


main()
