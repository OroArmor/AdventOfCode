from collections import defaultdict

import util
from util import *
import numpy as np

test_data: str = \
    """1
2
3
2024"""


@cache
def next_num(num: int) -> int:
    num ^= num * 64
    num %= 16777216

    num ^= num // 32
    num %= 16777216

    num ^= num * 2048
    num %= 16777216

    return num


def task1(input):
    total = 0
    for val in input:
        for _ in range(2000):
            val = next_num(val)
        total += val
    return total


def task2(input):
    patterns = defaultdict(int)
    for val in input:
        seen_this = set()
        dt = ()
        for _ in range(2000):
            nval = next_num(val)
            if len(dt) < 4:
                dt = (*dt, (nval % 10) - (val % 10))
            else:
                dt = (*dt[1:], (nval % 10) - (val % 10))
                if dt not in seen_this:
                    patterns[dt] += nval % 10
                    seen_this.add(dt)
            val = nval

    return max(patterns.values())


def parse(data: str):
    lines = util.as_lines_of_int(data)
    return lines


def main():
    data: str = util.get(22, 2024)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
