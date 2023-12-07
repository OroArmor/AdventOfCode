import util
from util import *
import numpy as np

test_data: str = \
    """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


ORDER = "AKQJT98765432"
TYPES = ["five", "four", "full", "three", "two", "one", "high"]

class Card:
    def __init__(self, data):
        self.hand: str = data[0]
        self.bet = int(data[1])

    def type(self):
        cards = set(self.hand)

        if len(cards) == 1:
            return "five"
        elif len(cards) == 2:
            if self.hand.count(cards.pop()) in [2, 3]:
                return "full"
            else:
                return "four"
        elif len(cards) == 3:
            if any([self.hand.count(c) == 3 for c in cards]):
                return "three"
            else:
                return "two"
        elif len(cards) == 4:
            return "one"

        return "high"

    def __lt__(self, other):
        selftype = self.type()
        othertype = other.type()

        if selftype == othertype:
            index = 0
            while self.hand[index] == other.hand[index]:
                index += 1
            return ORDER.index(self.hand[index]) > ORDER.index(other.hand[index])

        return TYPES.index(selftype) > TYPES.index(othertype)

    def __str__(self):
        return f"{self.hand}: {self.bet}"

    def __repr__(self):
        return str(self)

ORDER2 = "AKQT98765432J"

class Card2(Card):
    def __init__(self, card):
        super().__init__([card.hand, card.bet])

    def type(self):
        cards = set(self.hand)
        has_joker = "J" in cards

        if not has_joker:
            return super().type()
        else:
            cards.remove("J")
            joker_count = self.hand.count("J")

            if len(cards) == 0: # JJJJJ
                return "five"
            elif len(cards) == 1: #AJJJJ
                return "five"
            elif len(cards) == 2: # AKJJJ, AAKJJ, AAAKJ
                if joker_count == 3: # AKJJJ
                    return "four"
                elif joker_count == 2: # AAKJJ
                    return "four"
                else: # AAAKJ, AAKKJ
                    if any([self.hand.count(c) == 3 for c in cards]):
                        return "four"
                    if all([self.hand.count(c) == 2 for c in cards]):
                        return "full"
                    else:
                        return "three"
            elif len(cards) == 3: # AAKQJ, AKQJJ
                return "three"
            elif len(cards) == 4:
                return "one"

            return "high"

    def __lt__(self, other):
        selftype = self.type()
        othertype = other.type()

        if selftype == othertype:
            index = 0
            while self.hand[index] == other.hand[index]:
                index += 1
            return ORDER2.index(self.hand[index]) > ORDER2.index(other.hand[index])

        return TYPES.index(selftype) > TYPES.index(othertype)


def task1(input):
    print(input)
    return sum([(i + 1) * card.bet for i, card in enumerate(sorted(input))])

def task2(input):
    return sum([(i + 1) * card.bet for i, card in enumerate(sorted([Card2(c) for c in input]))])


def parse(data: str):
    lines = util.as_lines(data)
    return [Card(card.split(" ")) for card in lines]


def main():
    data: str = util.get(7, 2023)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
