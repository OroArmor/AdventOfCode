import util
from util import *
import numpy as np

test_data: str = \
    """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


def task1(input):
    ranges, ps = input

    total = 0

    for p in ps:
        for r in ranges:
            if p in r:
                total += 1
                break

    return total


def task2(input):
    ranges, _ = input
    return sum(len(r) for r in ranges)


def parse(data: str):
    rs, ps = util.as_double_lines(data)

    ps = util.as_lines_of_int(ps)
    ranges = []
    for line in util.as_lines(rs):
        s = line.split("-")
        ranges.append(
            Range(int(s[0]), int(s[1]), inclusive=True)
        )

    return Range.reduce_ranges(ranges), ps

def main():
    data: str = util.get(5, 2025)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
