from pathlib import Path

with Path("day4/input_day4").open("r") as handle:
    input_data = [line.strip() for line in handle.readlines()]


class Card:
    def __init__(self, text: str) -> None:
        self.text = text
        self.card_number = int(self.text.split(":")[0].split(" ")[-1])
        self._parse_numbers()

    def _parse_numbers(self):
        self.winnig_numbers = [
            int(num) for num in self.text.split("|")[0].split(":")[-1].split(" ") if num
        ]
        self.my_numbers = [
            int(num) for num in self.text.split("|")[1].split(" ") if num
        ]
        self.my_winning_numbers = [
            num for num in self.my_numbers if num in self.winnig_numbers
        ]

    def _calculate_points(self):
        self.card_points = 0
        if len(self.my_winning_numbers) > 0:
            self.card_points = 2 ** (len(self.my_winning_numbers) - 1)


class AllCards:
    def __init__(self, cards: list[Card]):
        self.cards = cards
        self.copies: list[Card] = []

    def _order_cards(self):
        self.cards.sort(key=lambda c: c.card_number)

    def _process(self):
        copies = []
        for i, card in enumerate(self.cards):
            if len(card.my_winning_numbers) > 0:
                copies = self.cards[i + 1 : i + len(card.my_winning_numbers) + 1]
                num_existing_copies = len(
                    [c for c in self.copies if c.card_number == card.card_number]
                )

                copies = copies * (num_existing_copies + 1)
                self.copies += copies


# cards = []
# for line in input_data:
#     card = Card(line)
#     card._parse_numbers()
#     card._calculate_points()
#     cards.append(card)
# print(sum([c.card_points for c in cards]))

all_cards = AllCards([Card(c) for c in input_data])
all_cards._process()
print(len(all_cards.cards) + len(all_cards.copies))
