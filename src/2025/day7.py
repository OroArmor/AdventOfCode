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

def get_splits(point, splitters, max_y, found):
    if point.y >= max_y or point in found.keys():
        return 0

    splits = 0

    beam = point + Point(0, 1)
    while beam.y < max_y and not beam in splitters:
        beam.y += 1

    if beam in splitters and beam not in found:
        splits += get_splits(beam + Point(-1, 0), splitters, max_y, found)
        splits += get_splits(beam + Point(1, 0), splitters, max_y, found)
        splits += 1
        found[beam] = splits

    return splits

def task1(input):
    s, splitters, max_y = input
    return get_splits(s, splitters, max_y, {})

@cache
def get_total_splits(point, splitters, max_y):
    if point.y >= max_y:
        return 0

    splits = 0

    beam = point + Point(0, 1)
    while beam.y < max_y and not beam in splitters:
        beam.y += 1

    if beam in splitters:
        splits += get_total_splits(beam + Point(-1, 0), splitters, max_y)
        splits += get_total_splits(beam + Point(1, 0), splitters, max_y)
        splits += 1

    return splits

def task2(input):
    get_total_splits.cache_clear()
    s, splitters, max_y = input
    return get_total_splits(s, splitters, max_y) + 1


def parse(data: str):
    lines = util.as_lines(data)

    s = None
    splitters = set()

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == 'S':
                s = Point(x, y)
            elif c == '^':
                splitters.add(Point(x, y))

    return s, frozenset(splitters), y + 1


def main():
    data: str = util.get(7, 2025)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
