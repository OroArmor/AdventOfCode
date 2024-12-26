import util
from util import *
import numpy as np

test_data: str = \
    """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####"""


def task1(input):
    total = 0
    for lock in input[0]:
        for key in input[1]:
            if all(lock[i] + key[i] <= 5 for i in range(len(lock))):
                total += 1
    return total




def parse(data: str):
    lines = util.as_double_lines(data)
    locks = []
    keys = []

    for option in lines:
        option_s = util.as_lines(option)
        if option.startswith("#####"):
            locks.append(
                list(
                    max(j for j in range(len(option_s)) if option_s[j][i] == "#") for i in range(len(option_s[0]))
                )
            )
        else:
            keys.append(
                list(
                    max(6 - j for j in range(len(option_s)) if option_s[j][i] == "#") for i in range(len(option_s[0]))
                )
            )

    return locks, keys


def main():
    data: str = util.get(25, 2024)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))


if __name__ == "__main__":
    main()
