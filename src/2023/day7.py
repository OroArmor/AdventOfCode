import util

test_data: str = \
    """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


TYPES = ["five", "four", "full", "three", "two", "one", "high"]

class Card:
    def __init__(self, data):
        self.hand: str = data[0]
        self.bet = int(data[1])
        self.order = "AKQT98765432J"

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
        self_type = self.type()
        other_type = other.type()

        if self_type == other_type:
            index = 0
            while self.hand[index] == other.hand[index]:
                index += 1
            return self.order.index(self.hand[index]) > self.order.index(other.hand[index])

        return TYPES.index(self_type) > TYPES.index(other_type)

    def __str__(self):
        return f"{self.hand} {self.bet}"

    def __repr__(self):
        return str(self)

class Card2(Card):
    def __init__(self, card):
        super().__init__([card.hand, card.bet])
        self.order = "AKQT98765432J"

    def type(self):
        has_joker = "J" in self.hand

        if not has_joker:
            return super().type()
        else:
            cards = set(self.hand)
            cards.remove("J")
            joker_count = self.hand.count("J")

            if len(cards) in [0, 1]:
                return "five"
            elif len(cards) == 2:
                if joker_count == 1:
                    if all([self.hand.count(c) == 2 for c in cards]):
                        return "full"
                    elif any([self.hand.count(c) == 2 for c in cards]):
                        return "three"
                return "four"
            elif len(cards) == 3:
                return "three"
            elif len(cards) == 4:
                return "one"


def task1(input):
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
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
