import re
from pathlib import Path

with Path("day2/input").open("r") as handle:
    input_data = [line.strip() for line in handle.readlines()]


def find_color_amounts(grab_txt: str) -> list:
    grabs = grab_txt.split(":")[1].split(";")
    grabs = [grab.strip() for grab in grabs]
    parsed_grabs = []
    for grab in grabs:
        color_pairs = grab.split(",")
        grab = Grab()
        for color_pair in color_pairs:
            color_pair = color_pair.strip()
            color = color_pair.split(" ")[1]
            amount = int(color_pair.split(" ")[0])
            grab.__setattr__(color, amount)
        parsed_grabs.append(grab)

    return parsed_grabs


class Grab:
    def __init__(self, red: int = 0, blue: int = 0, green: int = 0) -> None:
        self.red = red
        self.blue = blue
        self.green = green


class Game:
    def __init__(self, text: str) -> None:
        self.text = text
        self.game_id = int(text.split(":")[0].split(" ")[-1])
        self.grabs = find_color_amounts(self.text)

    def check_input_numbers(self, red: int, blue: int, green: int):
        for grab in self.grabs:
            if grab.red <= red and grab.blue <= blue and grab.green <= green:
                self.possible = True
            else:
                self.possible = False
                break


def sum_possible_game_ids(games: list[Game]):
    return sum([game.game_id for game in games if game.possible])


games = []
for line in input_data:
    game = Game(line)
    game.check_input_numbers(red=12, green=13, blue=14)
    games.append(game)
    # print(
    #     f"Game id: {game.game_id}, grabs: {[vars(grab) for grab in game.grabs if not game.possible]}"
    # )
    # # print(game.possible)

# first try: 174 - too low
print(sum_possible_game_ids(games))
