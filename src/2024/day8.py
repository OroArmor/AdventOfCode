import itertools
from collections import defaultdict

import util
from util import *
import numpy as np

test_data: str = \
    """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""


def task1(input):
    grid, w, h = input

    anti = set()
    for ante in grid.values():
        for a, b in itertools.combinations(ante, r=2):
            dist = a - b
            p = a + dist
            if 0 <= p.x < w and 0 <= p.y < h:
                anti.add(p)
            n = b - dist
            if 0 <= n.x < w and 0 <= n.y < h:
                anti.add(n)

    return len(anti)


def task2(input):
    grid, w, h = input
    anti = set()
    for ante in grid.values():
        anti |= ante
        for a, b in itertools.combinations(ante, r=2):
            dist = a - b

            p = a + dist
            while 0 <= p.x < w and 0 <= p.y < h:
                anti.add(p)
                p += dist

            n = b - dist
            while 0 <= n.x < w and 0 <= n.y < h:
                anti.add(n)
                n -= dist

    return len(anti)


def parse(data: str):
    raw, w, h = util.as_grid(data)
    grid = defaultdict(set)

    for y in range(h):
        for x in range(w):
            if raw[y][x] != ".":
                grid[raw[y][x]].add(Point(x, y))

    return grid, w, h


def main():
    data: str = util.get(8, 2024)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
