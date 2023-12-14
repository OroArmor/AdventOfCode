import util
from util import *
import numpy as np

test_data: str = \
    """Time:      7  15   30
Distance:  9  40  200"""


def task1(input):
    prod = 1
    for race in range(len(input[0])):
        # x * (t - x) > dist
        roots = np.roots([-1, input[0][race], -input[1][race]])
        tot = int(np.floor(max(roots) - 0.0001) - np.ceil(min(roots) + 0.0001) + 1)
        prod *= tot

    return prod


def task2(input):
    input = [[int("".join([str(v) for v in line]))] for line in input]
    return task1(input)


def parse(data: str):
    lines = util.as_lines(data)
    lines = [util.as_ssv_ints(split_on_colon(line)[1]) for line in lines]
    return lines


def main():
    data: str = util.get(6, 2023)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
