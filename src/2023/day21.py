from copy import deepcopy

import util
from util import *
import numpy as np

test_data: str = \
    """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""


def setup(grid, width, height) -> Point:
    for y in range(height):
        for x in range(width):
            if grid[y][x] == "S":
                grid[y][x] = "."
                return Point(x, y)


def task1(input):
    grid, width, height = input
    grid = deepcopy(grid)

    start = setup(grid, width, height)

    starting = {start}
    for _ in range(64):
        next_steps = set()

        for step in starting:
            for direction in cardinal_directions():
                next_step = step + direction
                if grid[next_step[1]][next_step[0]] == ".":
                    next_steps.add(next_step)
        starting = next_steps

    return len(starting)


def task2(input):
    grid, width, height = input

    grid = deepcopy(grid)
    start = setup(grid, width, height)

    steps = {start}
    seen_past = {}
    history = (0, 1)
    edge_history = []
    for s in range(width * 2 + start[0] + 1):
        next_steps = set()

        for step in steps:
            for direction in cardinal_directions():
                next_step = step + direction
                if grid[next_step[1] % height][next_step[0] % width] == "." and next_step not in seen_past:
                    next_steps.add(next_step)
        seen_past = steps
        steps = next_steps

        history = (history[1], len(steps) + history[0])
        if (s + 1) % width == start[0]:
            edge_history.append(history[1])

    x0, x1, x2 = edge_history

    a = ((x2 - x1) - (x1 - x0)) // 2
    b = x1 - a - x0
    c = x0

    x = (26501365 - start[0]) // width

    return a * x ** 2 + b * x + c


def parse(data: str):
    grid, width, height = util.as_grid(data)
    return grid, width, height


def main():
    data: str = util.get(21, 2023)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
