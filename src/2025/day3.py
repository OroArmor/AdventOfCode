import util
from util import *
import numpy as np

test_data: str = \
    """987654321111111
811111111111119
234234234234278
818181911112111"""

def task1(input):
    total = 0
    for line in input:
        b1, b2 = ord('0'), ord('0')
        for i, c in enumerate(line):
            if c > b1 and i != len(line) - 1:
                b1 = c
                b2 = ord('0')
            elif c > b2:
                b2 = c
        total += int(chr(b1)) * 10 + int(chr(b2))
    return total


def task2(input):
    total = 0

    for line in input:
        joltage = list(line[-12:])
        for c in line[-13::-1]:
            i = 0
            while i < 12:
                if c >= joltage[i]:
                    c, joltage[i] = joltage[i], c
                    i += 1
                    continue
                break
        total += int("".join(map(chr, joltage)))

    return total


def parse(data: str):
    lines = util.as_lines(data)
    return [list(map(ord, l)) for l in lines]


def main():
    data: str = util.get(3, 2025)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
