from collections import defaultdict

from helper import read_input


def update(stone: int) -> list[int]:
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        return split_stone(stone)
    return multiply(stone)


def multiply(stone: int) -> list[int]:
    return [stone * 2024]


def split_stone(stone: int) -> list[int]:
    halfway = int(len(str(stone)) / 2)
    return [int(str(stone)[:halfway]), int(str(stone)[halfway:])]


def main():
    input = read_input("_2024/day11/input.txt").strip()
    stones = defaultdict(int, {int(char): 1 for char in input.split(" ")})

    for i in range(75):
        new_stones = defaultdict(int)
        for stone, num in stones.items():
            for new_stone in update(stone):
                new_stones[new_stone] += num

        stones = new_stones

    print(sum(stones.values()))


main()
