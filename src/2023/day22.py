from collections import defaultdict
from copy import deepcopy

import util
from util import *
import numpy as np

test_data: str = \
    """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""


def create_filled(cubes) -> set[(int, int, int)]:
    filled = set()

    for (px, py, pz), size in cubes:
        for x in range(size[0]):
            for y in range(size[1]):
                for z in range(size[2]):
                    filled.add((px + x, py + y, pz + z))

    return filled


TASK_1 = (None, None)


def task1(input):
    global TASK_1
    cubes = deepcopy(input)
    cubes = sorted(cubes, key=lambda c: c[0][2])

    #                             z, cube
    max_zs = defaultdict(lambda: (0, None))

    #                         supported_by, supporting
    structure = defaultdict(lambda: (set(), set()))

    for i, ((px, py, pz), (sx, sy, sz)) in enumerate(cubes):
        z, supported_by = reduce(
            lambda acc, c: (max(c[0], acc[0]), acc[1] if c[1] is None else ({c[1]} if c[0] > acc[0] else (acc[1].union({c[1]}) if c[0] == acc[0] else acc[1]))),
            (max_zs[(px + x, py + y)] for x in range(sx) for y in range(sy)),
            (0, set()))

        for x in range(sx):
            for y in range(sy):
                max_zs[(px + x, py + y)] = (z + sz, i)

        structure[i] = (supported_by, structure[i][1])

        for j in supported_by:
            structure[j][1].add(i)

    only_supporters = set()
    for i in structure:
        if len(structure[i][0]) == 1:
            only_supporters = only_supporters.union(structure[i][0])

    TASK_1 = structure, only_supporters

    return len(cubes) - len(only_supporters)


def task2(input):
    structure, only_supporters = TASK_1

    total = 0
    for removed in only_supporters:
        fallen = set()
        could_fall = structure[removed][1]
        to_fall = {removed}
        while to_fall:
            falling = to_fall.pop()
            fallen.add(falling)

            for cube in could_fall:
                if structure[cube][0].issubset(fallen) and cube not in fallen:
                    to_fall.add(cube)
                    could_fall = could_fall.union(structure[cube][1])
                    could_fall.remove(cube)

        total += len(fallen) - 1  # Need to exclude the brick we removed

    return total


def parse(data: str):
    lines = util.as_lines(data)

    bricks = []
    for line in lines:
        start, end = line.split("~")
        pos = tuple(util.as_csv_of_ints(start))
        end = tuple(util.as_csv_of_ints(end))
        size = (end[0] - pos[0] + 1, end[1] - pos[1] + 1, end[2] - pos[2] + 1)
        assert size.count(1) >= 2, f"{line} -> {pos}, {size}"
        bricks.append((pos, size))
    return bricks


def main():
    data: str = util.get(22, 2023)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
