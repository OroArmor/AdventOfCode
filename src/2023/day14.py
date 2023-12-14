from collections import defaultdict
from copy import deepcopy
from itertools import *

import util
from util import *
import numpy as np

test_data: str = \
    """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""


def task1(input):
    size, grid = input

    grid = deepcopy(grid)

    roll_north(grid, size)

    total = 0
    for point in grid:
        if grid[point] == "O":
            total += size[1] - point[1]

    return total


def roll_north(grid, size):
    for x in range(size[0]):
        for y in range(size[1]):
            if (x, y) in grid:
                if grid[(x, y)] == "O":
                    del grid[(x, y)]
                    ny = y
                    while (not (x, ny) in grid) and (ny > -1):
                        ny -= 1

                    grid[(x, ny + 1)] = "O"


def roll_south(grid, size):
    for x in range(size[0]):
        for y in reversed(range(size[1])):
            if (x, y) in grid:
                if grid[(x, y)] == "O":
                    del grid[(x, y)]
                    ny = y
                    while (not (x, ny) in grid) and (ny < size[1]):
                        ny += 1

                    grid[(x, ny - 1)] = "O"


def roll_west(grid, size):
    for x in range(size[0]):
        for y in range(size[1]):
            if (x, y) in grid:
                if grid[(x, y)] == "O":
                    del grid[(x, y)]
                    nx = x
                    while (not (nx, y) in grid) and (nx > -1):
                        nx -= 1

                    grid[(nx + 1, y)] = "O"


def roll_east(grid, size):
    for x in reversed(range(size[0])):
        for y in range(size[1]):
            if (x, y) in grid:
                if grid[(x, y)] == "O":
                    del grid[(x, y)]
                    nx = x
                    while (not (nx, y) in grid) and (nx < size[1]):
                        nx += 1

                    grid[(nx - 1, y)] = "O"
def task2(input):
    size, grid = input

    grid = deepcopy(grid)

    # blocks -> turn
    seen = {}
    t = 0
    while True:
        roll_north(grid, size)
        roll_west(grid, size)
        roll_south(grid, size)
        roll_east(grid, size)

        t += 1

        vals = tuple(sorted([(x, y) for x in range(size[0]) for y in range(size[1]) if (x, y) in grid and grid[(x, y)] == "O"]))
        if vals in seen:
            break

        seen[vals] = t

    correct = int((1000000000 - seen[vals]) % (t - seen[vals]) + seen[vals])
    for val in seen:
        if seen[val] == correct:
            total = 0
            for point in val:
                total += size[1] - point[1]
            return total


def parse(data: str):
    lines = util.as_lines(data)

    size = (len(lines[0]), len(lines))
    grid = {}

    for y, line in enumerate(lines):
        for x, c in enumerate(line.strip()):
            if not c == ".":
                grid[(x, y)] = c

    return size, grid


def main():
    data: str = util.get(14, 2023)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
