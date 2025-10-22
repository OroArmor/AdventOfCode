import util
from util import *
import numpy as np

test_data: str = \
    """199
200
208
210
200
207
240
269
260
263"""


def task1(input):
    inc = 0
    for i in range(1, len(input)):
        if input[i - 1] < input[i]:
            inc += 1
    return inc


def task2(input):
    inc = 0
    for i in range(1, len(input) - 2):
        if input[i - 1] + input[i] + input[i + 1] < input[i] + input[i + 1] + input[i + 2]:
            inc += 1
    return inc


def parse(data: str):
    lines = util.as_lines_of_int(data)
    return lines


def main():
    data: str = util.get(1, 2021)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
