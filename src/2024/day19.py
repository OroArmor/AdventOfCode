import util
from util import *
import numpy as np

test_data: str = \
    """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

PATTERNS = None

@cache
def dfs(towel: str) -> int:
    global PATTERNS
    if len(towel) == 0:
        return 1

    total = 0
    for pattern in PATTERNS:
        if towel.startswith(pattern):
            total += dfs(towel[len(pattern):])
    return total


def task1(input):
    global PATTERNS
    patterns, towels = input
    PATTERNS = patterns
    dfs.cache_clear()
    return sum(dfs(towel) > 0 for towel in towels)


def task2(input):
    _, towels = input
    return sum(dfs(towel) for towel in towels)


def parse(data: str):
    patterns, towels = util.as_double_lines(data)
    patterns = tuple(patterns.split(", "))
    towels = towels.split("\n")
    return patterns, towels


def main():
    data: str = util.get(19, 2024)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
