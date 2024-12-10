from collections import defaultdict, deque
from queue import SimpleQueue

import util
from util import *
import numpy as np

test_data: str = \
    """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

def run(grid, starts, ends, empty: Callable[[], typing.Any], starting: Callable[[Point], typing.Any], joiner: Callable[[typing.Any, typing.Any], typing.Any], size: Callable[[typing.Any], int]) -> int:
    ds = Direction.values()
    to_check = deque()
    seen = set()
    counts = defaultdict(empty)
    for s in starts:
        to_check.append(s)
        counts[s] = starting(s)

    while len(to_check) > 0:
        p = to_check.popleft()
        v = grid[p]

        for d in ds:
            step = p + d
            if step in grid.keys() and grid[step] == v + 1:
                if step not in seen:
                    seen.add(step)
                    to_check.append(step)
                counts[step] = joiner(counts[step], counts[p])

    total = 0
    for e in ends:
        total += size(counts[e])

    return total


def task1(input):
    grid, w, h, starts, ends = input
    return run(grid, starts, ends, set, lambda p: {p}, set.union, len)


def task2(input):
    grid, w, h, starts, ends = input
    return run(grid, starts, ends, lambda: 0, lambda p: 1, int.__add__, int)


def parse(data: str):
    raw, w, h = util.as_grid(data)

    grid = {}
    starts = []
    ends = []
    for x in range(w):
        for y in range(h):
            if raw[y][x] == ".":
                continue

            v = int(raw[y][x])
            grid[Point(x,y)] = v

            if v == 0:
                starts.append(Point(x,y))

            if v == 9:
                ends.append(Point(x,y))

    return grid, w, h, starts, ends


def main():
    data: str = util.get(10, 2024)
    # data = test_data
    for _ in range(100):
        input = parse(data)
        print(input)
        print(task1(input))
        print(task2(input))


if __name__ == "__main__":
    main()
