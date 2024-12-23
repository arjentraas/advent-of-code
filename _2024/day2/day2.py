from itertools import pairwise

from utils import read_input_lines


def _is_safe(nums: list[int]) -> bool:
    deltas = []
    for num_1, num_2 in pairwise(nums):
        deltas.append(num_2 - num_1)

    abs_deltas = [abs(delta) for delta in deltas]

    if not all(abs_delta <= 3 and abs_delta >= 1 for abs_delta in abs_deltas):
        return False

    if all(delta >= 0 for delta in deltas):
        return True

    if all(delta <= 0 for delta in deltas):
        return True

    return False


def part_1():
    lines = read_input_lines("2024/day2/input_day2.txt")
    safe = 0
    for line in lines:
        nums = [int(num) for num in line.split(" ") if num]
        if _is_safe(nums):
            safe += 1

    print(safe)


part_1()


def part_2():
    lines = read_input_lines("2024/day2/input_day2.txt")
    safe = 0
    for line in lines:
        nums = [int(num) for num in line.split(" ") if num]
        if _is_safe(nums):
            safe += 1
            continue

        for i in range(len(nums)):
            popped_nums = [num for index, num in enumerate(nums) if index != i]

            if _is_safe(popped_nums):
                safe += 1
                break
    print(safe)


part_2()
