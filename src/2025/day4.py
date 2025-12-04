import scipy
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

KERNEL = np.ones((3, 3))


def task1(input):
    counts = np.multiply(scipy.signal.convolve2d(input, KERNEL, mode="same"), input)
    return np.logical_and(counts < 5, counts > 0).sum()


def task2(input):
    total = 0

    while True:
        counts = np.multiply(scipy.signal.convolve2d(input, KERNEL, mode="same"), input)

        removed = np.logical_and(counts < 5, counts > 0)
        removed_count = np.sum(removed)

        input = np.logical_xor(input, removed)

        if removed_count == 0:
            return total
        total += removed_count


def parse(data: str):
    return np.array([np.fromiter(l, dtype="U1") for l in util.as_lines(data)]) == "@"


def main():
    data: str = util.get(4, 2025)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
