from math import lcm

from helper import read_input_lines


def parse_input(lines):
    instructions = lines[0]
    nodes = {}
    for line in lines[2:]:
        nodes[line.split("=")[0].strip()] = {
            "L": line.split(",")[0][-3:],
            "R": line.split(",")[1][1:-1],
        }
    return {"instructions": instructions, "nodes": nodes}


def part1():
    input = read_input_lines("day8/input_day8.txt")
    parsed = parse_input(input)
    steps = 0
    node = "AAA"
    while True:
        for char in parsed["instructions"]:
            node = parsed["nodes"][node][char]
            steps += 1
        if node == "ZZZ":
            break
    return steps


print(f"Part 1: {part1()}")


def part2():
    input = read_input_lines("day8/input_day8.txt")
    parsed = parse_input(input)
    nodes = [node for node in parsed["nodes"] if node.endswith("A")]
    step_list = []
    for node in nodes:
        steps = 0
        while True:
            for instruction in parsed["instructions"]:
                steps += 1
                new_node = parsed["nodes"][node][instruction]
                if new_node.endswith("Z"):
                    step_list.append(steps)
                    break
                node = new_node
            else:
                continue
            break
    return lcm(*step_list)


print(f"Part 2: {part2()}")
