import util
from util import *
import numpy as np

test_data: str = \
    """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
L300"""


def task1(input):
    times = 0
    location = 50
    for turn in input:
        location += turn
        if location % 100 == 0:
            times += 1

    return times


def task2(input):
    times = 0
    location = 50
    for turn in input:
        if location + turn >= 100:
            times += (location + turn) // 100
        elif location + turn <= 0:
            times += -(location + turn) // 100 + (1 if location != 0 else 0)

        location += turn
        location %= 100

    return times


def parse(data: str):
    lines = util.as_lines(data)

    data = []
    for l in lines:
        data.append(int(l[1:]) * (-1 if l[0] == "L" else 1))

    return data


def main():
    data: str = util.get(1, 2025)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
