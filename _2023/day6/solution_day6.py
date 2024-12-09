from tqdm import tqdm

from helper import read_input_lines


class Race:
    def __init__(self, time: int, record_distance: int) -> None:
        self.time = time
        self.record_distance = record_distance

    def _calculate_distance(self, button_time: int):
        speed = button_time
        remaining_time = self.time - button_time
        return remaining_time * speed

    def possibilites_to_win(self):
        button_times = []
        for i in tqdm(range(1, self.time)):
            distance = self._calculate_distance(i)
            if distance > self.record_distance:
                button_times.append(i)
        self.possibilites_to_win = len(button_times)


def parse_input_part1(lines: list):
    races = []
    times = [p for p in lines[0].split(" ")[1:] if p]
    distances = [p for p in lines[1].split(" ")[1:] if p]
    for i in range(len(times)):
        races.append(Race(time=int(times[i]), record_distance=int(distances[i])))
    return races


def parse_input_part2(lines: list):
    time = int(lines[0].split(":")[-1].replace(" ", ""))
    distance = int(lines[1].split(":")[-1].replace(" ", ""))
    return Race(time, distance)


def multiply_win_possibilites(lst: list):
    result = 1
    for x in lst:
        result = result * x
    return result


def main():
    # Part 1
    # input = read_input("day6/input_day6")
    # races = parse_input_part1(input)
    # for race in races:
    #     race.possibilites_to_win()
    # print(multiply_win_possibilites([race.possibilites_to_win for race in races]))

    # Part 2
    # race = parse_input_part2(read_input("day6/test_input_day6"))
    race = parse_input_part2(read_input_lines("day6/input_day6"))
    race.possibilites_to_win()
    print(race.possibilites_to_win)


if __name__ == "__main__":
    main()
