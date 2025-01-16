from collections import defaultdict
from dataclasses import dataclass
from math import ceil, prod
from typing import Generator

import matplotlib.pyplot as plt

from utils import read_input_lines

max_x = 101
max_y = 103

x_boundary = ceil(max_x / 2) - 1
y_boundary = ceil(max_y / 2) - 1

plt.gca().invert_yaxis()


@dataclass
class Robot:
    x: int
    y: int
    delta_x: int
    delta_y: int

    def move(self, n: int = 1):
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

    @property
    def quadrant(self) -> str | None:
        if self.x < x_boundary:
            if self.y < y_boundary:
                return "leftup"
            elif self.y > y_boundary:
                return "left-down"
        elif self.x > x_boundary:
            if self.y < y_boundary:
                return "right-up"
            elif self.y > y_boundary:
                return "right-down"


def get_robots() -> Generator[Robot, None, None]:
    robots = read_input_lines("_2024/day14/input.txt")
    for robot in robots:
        robot_split = robot.split(" ")
        start_position = robot_split[0].split("=")[1].split(",")

        start_x = int(start_position[0])
        start_y = int(start_position[1])

        velocity = robot_split[1].split("=")[1].split(",")
        delta_x = int(velocity[0])
        delta_y = int(velocity[1])
        yield Robot(start_x, start_y, delta_x, delta_y)


def plot_robots(robots: list[Robot], n: int):
    plt.scatter(x=[robot.x for robot in robots], y=[robot.y for robot in robots], s=[0.2 for _ in robots])
    plt.savefig(f"_2024/day14/figs/{n}.png")
    plt.close()


def part_1():
    robots = list(get_robots())

    for robot in robots:
        robot.move(n=100)

    quadrants = defaultdict(int)

    for robot in robots:
        if robot.quadrant:
            quadrants[robot.quadrant] += 1

    print(prod(quadrants.values()))


def part_2():
    start_1 = 22
    start_2 = 79

    for _ in range(100):
        robots = list(get_robots())

        for robot in robots:
            robot.move(start_1)

        plot_robots(robots, start_1)
        start_1 += 103

    for _ in range(100):
        robots = list(get_robots())

        for robot in robots:
            robot.move(start_2)

        plot_robots(robots, start_2)

        start_2 += 101

    # 22, 79, 125, 180, 228, 281, the patterns occur
    # print only these robot formations, look manually.


part_2()
