import pytest

from day4.solution_day4 import AllCards, Card


@pytest.mark.parametrize(
    "inp,win,my,mywin,points,cardnum",
    [
        (
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            [41, 48, 83, 86, 17],
            [83, 86, 6, 31, 17, 9, 48, 53],
            [48, 83, 17, 86],
            8,
            1,
        ),
        (
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            [13, 32, 20, 16, 61],
            [61, 30, 68, 82, 17, 32, 24, 19],
            [32, 61],
            2,
            2,
        ),
        (
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            [1, 21, 53, 59, 44],
            [69, 82, 63, 72, 16, 21, 14, 1],
            [1, 21],
            2,
            3,
        ),
        (
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            [41, 92, 73, 84, 69],
            [59, 84, 76, 51, 58, 5, 54, 83],
            [84],
            1,
            4,
        ),
        (
            "Card 101: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            [87, 83, 26, 28, 32],
            [88, 30, 70, 12, 93, 22, 82, 36],
            [],
            0,
            101,
        ),
        (
            "Card 10: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
            [31, 18, 13, 56, 72],
            [74, 77, 10, 23, 35, 67, 36, 11],
            [],
            0,
            10,
        ),
    ],
)
def test_cards(inp, win, my, mywin, points, cardnum):
    card = Card(inp)
    card._parse_numbers()
    card._calculate_points()
    assert card.winnig_numbers == win
    assert card.my_numbers == my
    for num in mywin:
        assert num in card.my_winning_numbers
    assert card.card_points == points
    assert card.card_number == cardnum


class TestAllCards:
    def test_order(self):
        input = [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            "Card 7:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            "Card 8: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            "Card 107: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            "Card 15: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
        ]
        cards = [Card(c) for c in input]
        all_cards = AllCards(cards)
        all_cards._order_cards()
        assert all_cards.cards[-1].card_number == 107
        assert all_cards.cards[-2].card_number == 15

    def test_process(self):
        input = [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
        ]
        cards = [Card(c) for c in input]
        all_cards = AllCards(cards)
        all_cards._process()
        assert len(all_cards.copies) + len(all_cards.cards) == 30
