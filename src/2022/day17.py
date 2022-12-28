import timeit
from functools import reduce

import util
import numpy as np

test_data: str = \
    """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""


rock_shapes = """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##""".split("\n\n")

def task1(input):
    fallen = np.zeros((7, 2022 * 4), dtype=int)

    top = 0
    right = np.array([1, 0])
    left = np.array([-1, 0])
    down = np.array([0, -1])
    wind_index = 0

    for rock in range(2022):
        rock_lines = rock_shapes[rock % 5].split("\n")
        size = (len(rock_lines[0]), len(rock_lines))

        rock_grid = np.array([[0 if c == "." else 1 for c in line] for line in reversed(rock_lines)]).transpose()
        pos = np.array([2, top + 3])

        while True:
            wind = input[wind_index]
            wind_index += 1
            wind_index %= len(input)

            if wind == ">":  # right
                pos += right

                if pos[0] + size[0] > 7 or pos[0] < 0:  # cant move right, hits wall
                    pos -= right
                else:
                    sub = fallen[pos[0]:pos[0]+size[0], pos[1]:pos[1]+size[1]]
                    combined = sub + rock_grid
                    if (combined > 1).sum() != 0:  # cant move right, hits rock
                        pos -= right
            else:  # left
                pos += left

                if pos[0] + size[0] > 7 or pos[0] < 0:  # cant move left, hits wall
                    pos -= left
                else:
                    sub = fallen[pos[0]:pos[0] + size[0], pos[1]:pos[1] + size[1]]
                    combined = sub + rock_grid
                    if (combined > 1).sum() != 0:  # cant move left, hits rock
                        pos -= left

            pos += down

            if pos[1] < 0:
                fallen[pos[0]:pos[0] + size[0], 0:size[1]] += rock_grid
                top = 0 + size[1]
                break

            sub = fallen[pos[0]:pos[0] + size[0], pos[1]:pos[1] + size[1]]
            combined = sub + rock_grid
            if (combined > 1).sum() != 0:  # cant move down, hits rock
                pos -= down
                fallen[pos[0]:pos[0] + size[0], pos[1]:pos[1] + size[1]] += rock_grid
                top = max(top, pos[1] + size[1])
                break

    return top


def task2(input):
    fallen = np.zeros((7, 10000 * 4), dtype=int)

    top = 0
    right = np.array([1, 0])
    left = np.array([-1, 0])
    down = np.array([0, -1])
    wind_index = 0

    total_rocks = 1000000000000
    tops = []
    ptop = 0

    rock_grids = []
    for rock_lines in rock_shapes:
        rock_grids.append(np.array([[0 if c == "." else 1 for c in line] for line in reversed(rock_lines.split("\n"))]).transpose())

    for rock in range(10000):
        rock_grid = rock_grids[rock % 5]
        size = rock_grid.shape
        pos = np.array([2, top + 3])

        while True:
            wind = input[wind_index]
            wind_index += 1
            wind_index %= len(input)

            if wind == ">":  # right
                pos += right

                if pos[0] + size[0] > 7 or pos[0] < 0:  # cant move right, hits wall
                    pos -= right
                else:
                    sub = fallen[pos[0]:pos[0] + size[0], pos[1]:pos[1] + size[1]]
                    combined = sub + rock_grid
                    if (combined > 1).sum() != 0:  # cant move right, hits rock
                        pos -= right
            else:  # left
                pos += left

                if pos[0] + size[0] > 7 or pos[0] < 0:  # cant move left, hits wall
                    pos -= left
                else:
                    sub = fallen[pos[0]:pos[0] + size[0], pos[1]:pos[1] + size[1]]
                    combined = sub + rock_grid
                    if (combined > 1).sum() != 0:  # cant move left, hits rock
                        pos -= left

            pos += down
            if pos[1] < 0:
                fallen[pos[0]:pos[0] + size[0], 0:size[1]] += rock_grid
                top = 0 + size[1]
                if rock == 0:
                    tops.append(top - ptop)
                    ptop = top
                break

            sub = fallen[pos[0]:pos[0] + size[0], pos[1]:pos[1] + size[1]]
            combined = sub + rock_grid
            if (combined > 1).sum() != 0:  # cant move down, hits rock
                pos -= down
                fallen[pos[0]:pos[0] + size[0], pos[1]:pos[1] + size[1]] += rock_grid
                top = max(top, pos[1] + size[1])

                tops.append(top - ptop)
                ptop = top
                break

    for loop_length in range(len(tops) // 2, 1, -2):
        for loop_start in range(loop_length):
            for i in range(loop_start, loop_length + loop_start):
                if tops[i] != tops[i + loop_length // 2]:
                    break
            else:
                large_top: float = reduce(lambda a, b: a + b, tops[0:loop_start])

                loop = reduce(lambda a, b: a + b, tops[loop_start:loop_length // 2 + loop_start])
                loop_rocks = loop_length // 2
                large_top += float(loop) * float((total_rocks - loop_start) // loop_rocks)

                remaining = total_rocks - loop_rocks * ((total_rocks - loop_start) // loop_rocks) - loop_start

                if remaining > 0:
                    large_top += reduce(lambda a, b: a + b, tops[loop_start:remaining + loop_start - 1])

                return int(large_top)


def parse(data: str):
    return data


def main():
    data: str = util.get(17, 2022)
    # data = test_data
    input = parse(data)
    print(timeit.timeit(lambda: print(task1(input)), number=1))
    print(timeit.timeit(lambda: print(task2(input)), number=1))


if __name__ == "__main__":
    main()
