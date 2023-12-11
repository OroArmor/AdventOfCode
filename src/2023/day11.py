import util
from util import *
import numpy as np

test_data: str = \
    """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


def run(galaxies, size_x, size_y, scale_size: int):
    galaxies = set(galaxies)

    # expand:
    x_add = []
    for x in range(size_x):
        if all([gal[0] != x for gal in galaxies]):
            x_add.append(x)

    y_add = []
    for y in range(size_y):
        if all([gal[1] != y for gal in galaxies]):
            y_add.append(y)

    for x in reversed(x_add):
        move = set()
        for gal in galaxies:
            if gal[0] > x:
                move.add(gal)

        for val in move:
            galaxies.remove(val)
            galaxies.add((val[0] + scale_size - 1, val[1]))

    for y in reversed(y_add):
        move = set()
        for gal in galaxies:
            if gal[1] > y:
                move.add(gal)

        for val in move:
            galaxies.remove(val)
            galaxies.add((val[0], val[1] + scale_size - 1))

    # for y in range(size_y + len(y_add)):
    #     for x in range(size_x + len(x_add)):
    #         print("#" if (x, y) in galaxies else ".", end = "")
    #     print()

    galaxies = list(galaxies)

    total = 0
    for a in range(len(galaxies)):
        for b in range(a + 1, len(galaxies)):
            total += abs(galaxies[a][0] - galaxies[b][0]) + abs(galaxies[a][1] - galaxies[b][1])

    return total


def task1(input):
    galaxies, (size_x, size_y) = input
    return run(galaxies, size_x, size_y, 2)


def task2(input):
    galaxies, (size_x, size_y) = input
    return run(galaxies, size_x, size_y, 1000000)


def parse(data: str):
    lines = util.as_lines(data)

    galaxies = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                galaxies.add((x, y))

    return galaxies, (len(lines[0]), len(lines))


def main():
    data: str = util.get(11, 2023)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
