from utils import read_input_lines

# from numpy import diff


def part1():
    inp = read_input_lines("day9/input_day9.txt")
    predictions = []
    for line in inp:
        history = [int(p) for p in line.split(" ")]
        diffs = [[j - i for i, j in zip(history[:-1], history[1:])]]

        while True:
            diff = [j - i for i, j in zip(diffs[-1][:-1], diffs[-1][1:])]
            if all(i == 0 for i in diff):
                break
            diffs.append(diff)

        diffs.insert(0, history)
        diffs.reverse()
        for ind, nums in enumerate(diffs):
            if ind == 0:
                continue
            nums[-1] = nums[-1] + diffs[ind - 1][-1]
        predictions.append(nums[-1])
    return sum(predictions)


# print(f"Part 1: {part1()}")


def part2():
    inp = read_input_lines("day9/input_day9.txt")
    predictions = []
    for line in inp:
        history = [int(p) for p in line.split(" ")]
        history.reverse()
        diffs = [[i - j for i, j in zip(history[:-1], history[1:])]]
        while True:
            diff = [i - j for i, j in zip(diffs[-1][:-1], diffs[-1][1:])]
            if all(i == 0 for i in diff):
                break
            diffs.append(diff)

        diffs.reverse()
        diffs.append(history)
        for ind, nums in enumerate(diffs):
            if ind == 0:
                nums.append(nums[-1])
                continue
            nums.append(nums[-1] - diffs[ind - 1][-1])
        predictions.append(nums[-1])
    return sum(predictions)


print(f"Part 2: {part2()}")
