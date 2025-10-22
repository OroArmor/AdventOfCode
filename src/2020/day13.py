import itertools

import util
import numpy as np

test_data: str = \
    """939
7,13,x,x,59,x,31,19"""


def task1(input):
    arrival = int(input[0])
    busses = [int(x) for x in util.as_csv(input[1]) if x != "x"]

    min_arrival = 10000000000
    val = 0
    for bus in busses:
        a = bus - arrival % bus

        if a < min_arrival:
            min_arrival = a
            val = a * bus

    return val


def task2(input):
    busses = [(int(x), i) for i, x in enumerate(util.as_csv(input[1])) if x != "x"]

    step = 1
    time = 0
    for bus, i in busses:
        while (time + i) % bus != 0:
            time += step
        step *= bus

    return time


def parse(data: str):
    lines = util.as_lines(data)
    return lines


def main():
    data: str = util.get(13, 2020)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
