import util
from util import *
import numpy as np

test_data: str = \
    """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def task1(input):
    print(input)

    sum = 0
    for card in input:
        matches = 0

        for win in card[0]:
            if win in card[1]:
                matches += 1

        if matches > 0:
            sum += 2 ** (matches - 1)

    return sum


def task2(input):
    matches = []
    for card in input:
        match = 0

        for win in card[0]:
            if win in card[1]:
                match += 1

        matches.append(match)

    counts = [0 for _ in range(len(matches))]
    for i, match in enumerate(matches):
        counts[i] += 1
        for j in range(match):
            counts[i + j + 1] += counts[i]

    return sum(counts)


def parse(data: str):
    lines = util.as_lines(data)

    cards = []

    for line in lines:
        nums = util.split_on_colon(line)[1].split("|")
        cards.append((util.as_ssv_ints(nums[0]), util.as_ssv_ints(nums[1])))

    return cards


def main():
    data: str = util.get(4, 2023)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
