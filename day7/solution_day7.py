from collections import Counter, namedtuple

from helper import read_input_lines

rank_dict = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 1,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


class BestHand:
    def __init__(self, count_most_card, count_jokers, _type) -> None:
        self.count_most_card = count_most_card
        self.count_jokers = count_jokers
        self._type = _type


jokers_combos = [BestHand(4, 1, "5-of-a-kind"), BestHand(5, 0, "5-of-akind")]


def parse_input(lines: list):
    hand_bids = {}
    for line in lines:
        _split = line.split(" ")
        hand = _split[0]
        bid = _split[1]
        hand_bids[hand] = bid
    return hand_bids


class Card:
    def __init__(self, label: str):
        self.label = label
        self.rank = rank_dict[label]


class Hand:
    def __init__(self, text: str, bid: str) -> None:
        self.text = text
        self.bid = int(bid)
        self.type = self.get_hand_type()
        self.cards = [Card(char) for char in self.text]
        self.rank: int = None

    def get_hand_type(self):
        jokers = self.text.count("J")
        if jokers:
            without_jokers = self.text.replace("J", "")
            counter = Counter(without_jokers)
            counter = dict(
                sorted(counter.items(), key=lambda item: item[1], reverse=True)
            )
            if jokers == 5:
                return ("a", "5-of-a-kind")
            most_card = list(counter.keys())[0]
            count_most_card = counter[most_card]

            if count_most_card >= 4:
                return ("a", "5-of-a-kind")
            if count_most_card == 3 and jokers == 2:
                return ("a", "5-of-a-kind")
            if count_most_card == 3 and jokers == 1:
                return ("b", "4-of-a-kind")
            if count_most_card == 2 and jokers == 3:
                return ("a", "5-of-a-kind")
            if count_most_card == 2 and jokers == 2:
                return ("b", "4-of-a-kind")
            if count_most_card == 2 and jokers == 1:
                second_most_card = list(counter.keys())[1]
                count_second_most_card = counter[second_most_card]
                if count_second_most_card == 2:
                    return ("c", "full-house")
                else:
                    return ("d", "3-of-a-kind")
            if count_most_card == 1 and jokers == 4:
                return ("a", "5-of-a-kind")
            if count_most_card == 1 and jokers == 3:
                return ("b", "4-of-a-kind")
            if count_most_card == 1 and jokers == 2:
                return ("d", "3-of-a-kind")
            if count_most_card == 1 and jokers == 1:
                return ("f", "1-pair")
        else:
            counter = Counter(self.text)
            if 5 in counter.values():
                return ("a", "5-of-a-kind")
            if 4 in counter.values():
                return ("b", "4-of-a-kind")
            if 3 in counter.values() and 2 in counter.values():
                return ("c", "full-house")
            if 3 in counter.values() and 1 in counter.values():
                return ("d", "3-of-a-kind")
            if list(counter.values()).count(2) == 2:
                return ("e", "2-pair")
            if list(counter.values()).count(2) == 1:
                return ("f", "1-pair")
            else:
                return ("g", "high-card")


def split_hands_by_type(lst: list[Hand]):
    d = {
        "5-of-a-kind": [],
        "4-of-a-kind": [],
        "full-house": [],
        "3-of-a-kind": [],
        "2-pair": [],
        "1-pair": [],
        "high-card": [],
    }
    for hand in lst:
        d[hand.type[1]].append(hand)
    return d


def order_by_type(lst: list[Hand]):
    return sorted(lst, key=lambda x: (x.type[0]))


def calculate_total_winnigs(lst: list[Hand]):
    sum = 0
    for hand in lst:
        sum += hand.bid * hand.rank
    return sum


def main():
    hand_bids = parse_input(read_input_lines("day7/input_day7"))
    hands = [Hand(text=hand, bid=bid) for hand, bid in hand_bids.items()]
    ordered_hands = order_by_type(hands)
    d = split_hands_by_type(ordered_hands)
    for _type, hands in d.items():
        ordered_hands_per_type = sorted(
            hands,
            key=lambda x: (
                x.cards[0].rank,
                x.cards[1].rank,
                x.cards[2].rank,
                x.cards[3].rank,
                x.cards[4].rank,
            ),
            reverse=True,
        )
        d[_type] = ordered_hands_per_type
    flat_list = []
    for _type, hands in d.items():
        for hand in hands:
            flat_list.append(hand)

    for ind, hand in enumerate(flat_list):
        hand.rank = len(flat_list) - ind

    print(calculate_total_winnigs(flat_list))


if __name__ == "__main__":
    main()
