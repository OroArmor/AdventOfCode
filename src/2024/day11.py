from collections import defaultdict

import util
from util import *
import numpy as np

test_data: str = \
    """"""

def run(input: list[int], times: int) -> int:
    stones = {s: 1 for s in input}

    for _ in range(times):
        next = defaultdict(lambda: 0)
        for s, c in stones.items():
            if s == 0:
                next[1] += c
            elif len(str(s)) % 2 == 0:
                l = len(str(s))
                a, b = int(str(s)[0:l // 2]), int(str(s)[l // 2:])
                next[a] += c
                next[b] += c
            else:
                next[s * 2024] += c

        stones = next

    total = sum(stones.values())

    return total

def task1(input):
    return run(input, 25)


def task2(input):
    return run(input, 75)


def parse(data: str):
    lines = util.as_ssv_ints(data)
    return lines


def main():
    data: str = util.get(11, 2024)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
