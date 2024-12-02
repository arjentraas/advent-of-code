from collections import Counter
from pathlib import Path


def part_1():
    left_nums = []
    right_nums = []
    with Path("2024/day1/input_day1.txt").open("r") as handle:
        for line in handle.readlines():
            split = line.split(" ")
            left_nums.append(int(split[0]))
            right_nums.append(int(split[-1]))

    total_diff = 0
    for left, right in zip(sorted(left_nums), sorted(right_nums)):
        total_diff += abs(left - right)

    print(total_diff)


part_1()


def part_2():
    left_nums = []
    right_nums = []
    with Path("2024/day1/input_day1.txt").open("r") as handle:
        for line in handle.readlines():
            split = line.split(" ")
            left_nums.append(int(split[0]))
            right_nums.append(int(split[-1]))

    left_nums = Counter(left_nums)
    right_nums = Counter(right_nums)

    total_simularity = 0
    for left in left_nums:
        right_count = right_nums.get(left, 0)
        similarity = left * right_count
        total_simularity += similarity
    print(total_simularity)


part_2()
