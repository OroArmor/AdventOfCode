from collections import defaultdict
import util
from util import *
import numpy as np

test_data: str = \
    """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""


def get_splits(point, splitters, found):
    if point in found.keys():
        return 0

    _, next_splitter = binary_search(splitters[point.x], point.y)
    splits = 0
    if next_splitter < len(splitters[point.x]):
        splitter = Point(point.x, splitters[point.x][next_splitter])
        if splitter not in found:
            splits += get_splits(Point(point.x - 1, splitters[point.x][next_splitter]), splitters, found)
            splits += get_splits(Point(point.x + 1, splitters[point.x][next_splitter]), splitters, found)
            splits += 1
            found[splitter] = splits
    return splits


def task1(input):
    s, splitters = input
    return get_splits(s, splitters, {})


@cache
def get_total_splits(point, splitters):
    _, next_splitter = binary_search(splitters[point.x], point.y)
    splits = 0
    if next_splitter < len(splitters[point.x]):
        splits += get_total_splits(Point(point.x - 1, splitters[point.x][next_splitter]), splitters)
        splits += get_total_splits(Point(point.x + 1, splitters[point.x][next_splitter]), splitters)
        splits += 1
    return splits


def task2(input):
    get_total_splits.cache_clear()
    s, splitters = input
    return get_total_splits(s, splitters) + 1


def parse(data: str):
    lines = util.as_lines(data)

    s = None
    splitters = defaultdict(list)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == 'S':
                s = Point(x, y)
            elif c == '^':
                splitters[x].append(y)
    splitters[0] = []
    splitters[x] = []

    return s, HashableDict(splitters)


def main():
    data: str = util.get(7, 2025)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
