from dataclasses import dataclass
from typing import Optional

from utils import read_input_lines


@dataclass
class Pipe:
    char: str
    y: int
    x: int
    step: Optional[int] = 0


WEST = ["-", "L", "F", "S"]
EAST = ["-", "7", "J", "S"]
NORTH = ["|", "F", "7", "S"]
SOUTH = ["|", "L", "J", "S"]


def part1():
    input = read_input_lines("day10/input_day10.txt")

    pipes: list[Pipe] = []
    for ind, line in enumerate(reversed(input), 1):
        for line_ind, char in enumerate(line):
            if char in EAST + WEST + NORTH + SOUTH:
                pipes.append(Pipe(char, ind, line_ind + 1))

    start_pipe = next(pipe for pipe in pipes if pipe.char == "S")
    queue = [start_pipe]
    visited_pipes: list[Pipe] = []

    while queue:
        current_pipe = queue.pop()

        for pipe in pipes:
            if (
                (
                    (
                        pipe.y == current_pipe.y + 1
                        and pipe.x == current_pipe.x
                        and pipe.char in NORTH
                        and current_pipe.char in SOUTH
                    )
                    or (
                        pipe.y == current_pipe.y
                        and pipe.x == current_pipe.x + 1
                        and pipe.char in EAST
                        and current_pipe.char in WEST
                    )
                    or (
                        pipe.y == current_pipe.y - 1
                        and pipe.x == current_pipe.x
                        and pipe.char in SOUTH
                        and current_pipe.char in NORTH
                    )
                    or (
                        pipe.y == current_pipe.y
                        and pipe.x == current_pipe.x - 1
                        and pipe.char in WEST
                        and current_pipe.char in EAST
                    )
                )
                and pipe not in queue
                and pipe not in visited_pipes
            ):
                queue.append(pipe)

        visited_pipes.append(current_pipe)

    print(f"Answer part1: {len(visited_pipes)/2}")


part1()
