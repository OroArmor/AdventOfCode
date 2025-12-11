import util
from util import *
import numpy as np

test_data: str = \
    """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

NEIGHBORS = None


def task1(input):
    rolls = np.where(input)[0]
    neighbors = rolls[:, None] + NEIGHBORS[None, :]
    neighbor_count = np.sum(input[neighbors], axis=1)
    return np.sum(neighbor_count < 4)

def task2(input):
    total = 0
    rolls = np.where(input)[0]
    neighbors = rolls[:, None] + NEIGHBORS[None, :]
    while True:
        neighbor_count = np.sum(input[neighbors], axis=1)
        removed = neighbor_count < 4
        removed_count = np.sum(removed)
        if removed_count == 0:
            break
        total += removed_count

        input[rolls[removed]] = False
        neighbors = neighbors[~removed]
        rolls = rolls[~removed]

    return total


def parse(data: str):
    global NEIGHBORS
    grid = np.array([np.fromiter(l, dtype="U1") for l in util.as_lines(data)]) == "@"
    grid = np.pad(grid, (1, 1), constant_values=0)
    s = len(grid)
    NEIGHBORS = np.array([-s-1, -s, -s+1, -1, 1, s-1, s, s+1])
    return grid.flatten()


def main():
    data: str = util.get(4, 2025)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
