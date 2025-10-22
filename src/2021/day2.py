import util
from util import *
import numpy as np

test_data: str = \
    """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


def task1(input):
    pos = np.array([0, 0])

    for move, length in input:
        if move == "forward":
            pos += RIGHT * length
        elif move == "down":
            pos += -DOWN * length
        elif move == "up":
            pos += -UP * length

    return pos[0] * pos[1]


def task2(input):
    pos = np.array([0, 0])
    aim = 0

    for move, length in input:
        if move == "forward":
            pos += RIGHT * length
            pos += -DOWN * aim * length
        elif move == "down":
            aim += length
        elif move == "up":
            aim -= length

    return pos[0] * pos[1]


def parse(data: str):
    lines = util.as_lines(data)
    return [(split[0], int(split[1])) for split in [line.split(" ") for line in lines]]


def main():
    data: str = util.get(2, 2021)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
