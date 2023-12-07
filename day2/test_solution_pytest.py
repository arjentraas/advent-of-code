from solution import Game, find_color_amounts, sum_possible_game_ids

test_cases = {
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green": True,
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue": True,
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red": False,
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red": False,
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green": True,
    "Game 19: 6 red, 1 green, 18 blue; 2 red, 1 blue; 7 blue, 3 red, 2 green; 18 blue, 2 green, 1 red; 7 red, 10 blue": False,
    "Game 20: 13 blue, 2 red; 2 green, 2 red; 1 green, 9 blue": True,
    "Game 100: 8 red, 3 green; 4 green, 1 blue, 15 red; 10 red, 8 green, 1 blue": False,
}


def test_find_color_amounts():
    test_result = find_color_amounts(
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    )
    assert len(test_result) == 3
    assert test_result[0].red == 20
    assert test_result[1].blue == 5
    assert test_result[2].green == 5


def test_zero_in_grab():
    test_result = find_color_amounts(
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    )
    assert test_result[0].green == 0


def test_outcome_testcases():
    for text, outcome in test_cases.items():
        print(text)
        game = Game(text)
        game.check_input_numbers(red=12, green=13, blue=14)
        assert game.possible == outcome


def test_sum_possible_game_ids():
    games = []
    for text, outcome in test_cases.items():
        game = Game(text)
        game.check_input_numbers(red=12, green=13, blue=14)
        games.append(game)

    assert sum_possible_game_ids(games) == 28


def test_game_ids():
    game1 = Game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert game1.game_id == 1

    game19 = Game(
        "Game 19: 6 red, 1 green, 18 blue; 2 red, 1 blue; 7 blue, 3 red, 2 green; 18 blue, 2 green, 1 red; 7 red, 10 blue"
    )
    assert game19.game_id == 19

    game100 = Game(
        "Game 100: 8 red, 3 green; 4 green, 1 blue, 15 red; 10 red, 8 green, 1 blue"
    )
    assert game100.game_id == 100
