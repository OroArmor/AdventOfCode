import util
from util import *
import numpy as np

test_data: str = \
    """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""


def find_reflections(grid: list[(int, int)], size: int, reflection: int, index: int) -> (set[(int, int)], set[(int, int)]):
    behind = set()
    in_front = set()

    width = min(abs(size - reflection - 1), reflection + 1)

    for point in grid:
        if index == 0:
            if point[0] <= reflection and reflection - point[0] < width:
                behind.add((reflection - point[0], point[1]))
            elif abs(point[0] - 1 - reflection) < width:
                in_front.add((point[0] - 1 - reflection, point[1]))
        elif index == 1:
            if point[1] <= reflection and reflection - point[1] < width:
                behind.add((point[0], reflection - point[1]))
            elif abs(point[1] - 1 - reflection) < width:
                in_front.add((point[0], point[1] - 1 - reflection))

    return behind, in_front


def task1(input):
    total = 0
    for size, grid in input:
        for col in range(size[0]):
            left, right = find_reflections(grid, size[0], col, 0)

            if left == right and len(left) != 0:
                total += col + 1

        for row in range(size[1]):
            above, below = find_reflections(grid, size[1], row, 1)

            if above == below and len(above) != 0:
                total += 100 * (row + 1)

    return total


def task2(input):
    total = 0
    for size, grid in input:
        for col in range(size[0]):
            left, right = find_reflections(grid, size[0], col, 0)

            if len(left.symmetric_difference(right)) == 1 and len(left) != 0:
                total += col + 1

        for row in range(size[1]):
            above, below = find_reflections(grid, size[1], row, 1)

            if len(below.symmetric_difference(above)) == 1 and len(above) != 0:
                total += 100 * (row + 1)

    return total


def parse(data: str):
    grids_str = util.as_double_lines(data)

    grids = []

    for g_str in grids_str:
        g_str = as_lines(g_str)
        grid = []
        for y, g_line in enumerate(g_str):
            for x, c in enumerate(g_line):
                if c == "#":
                    grid.append((x, y))
        grids.append(((len(g_str[0]), len(g_str)), grid))

    return grids


def main():
    data: str = util.get(13, 2023)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
