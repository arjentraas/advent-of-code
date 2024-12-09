import re

from helper import read_input_lines


def part_1():
    lines = read_input_lines("2024/day3/input_day3.txt")
    mul_pattern = "mul\(\d+,\d+\)"
    num_pattern = "\d+,\d+"
    sum = 0
    for line in lines:
        muls = re.findall(mul_pattern, line)
        for mul in muls:
            nums = re.search(num_pattern, mul).group()
            split = nums.split(",")
            multiplication = int(split[0]) * int(split[1])
            sum += multiplication

    print(sum)


part_1()


def part_2():
    lines = read_input_lines("2024/day3/input_day3.txt")
    mul_pattern = "mul\(\d+,\d+\)"
    do_pattern = "do\(\)"
    dont_pattern = "don't\(\)"
    num_pattern = "\d+,\d+"
    sum = 0

    do = True
    for line in lines:
        mul_matches = list(re.finditer(mul_pattern, line))
        do_matches = list(re.finditer(do_pattern, line))
        dont_matches = list(re.finditer(dont_pattern, line))

        matches = mul_matches + do_matches + dont_matches
        matches = sorted(matches, key=lambda x: x.span())

        for match in matches:
            if match in do_matches:
                do = True
                continue
            if match in dont_matches:
                do = False
                continue
            if do is False:
                continue

            mul = match.group()
            nums = re.search(num_pattern, mul).group()
            split = nums.split(",")
            multiplication = int(split[0]) * int(split[1])
            sum += multiplication

    print(sum)


part_2()
