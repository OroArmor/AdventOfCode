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

    last = set()
    current = create_filled(cubes)

    while last != current:
        new_cubes = []
        for (px, py, pz), (sx, sy, sz) in cubes:
            if pz - 1 > 0:  # bottom check
                if sx == sy and (px, py, pz - 1) not in current:  # If the brick is straight up, check if we can drop
                    new_cubes.append(((px, py, pz - 1), (sx, sy, sz)))
                elif all([(px + x, py, pz - 1) not in current for x in range(sx)]) and all([(px, py + y, pz - 1) not in current for y in range(sy)]):  # Else check all below and see if cube can go down
                    new_cubes.append(((px, py, pz - 1), (sx, sy, sz)))
                else:  # Else keep old cube
                    new_cubes.append(((px, py, pz), (sx, sy, sz)))
            else:  # Else keep old cube
                new_cubes.append(((px, py, pz), (sx, sy, sz)))

        last = current
        current = create_filled(new_cubes)
        cubes = new_cubes

    supporting = defaultdict(set)
    for i, cube in enumerate(cubes):
        this_blocks = create_filled([cube])
        for j, other in enumerate(cubes):
            if i == j:
                continue
            other_blocks = create_filled([other])

            for (x, y, z) in other_blocks:
                if (x, y, z - 1) in this_blocks:
                    supporting[j].add(i)

    only_supporters = set()
    for i in supporting:
        if len(supporting[i]) == 1:
            only_supporters = only_supporters.union(supporting[i])

    TASK_1 = supporting, only_supporters

    return len(cubes) - len(only_supporters)


def task2(input):
    supporting, only_supporters = TASK_1

    total = 0
    for removed in only_supporters:
        fallen = set()
        to_fall = {removed}
        while to_fall:
            falling = to_fall.pop()
            fallen.add(falling)

            for cube in supporting:
                if supporting[cube].issubset(fallen) and cube not in fallen:
                    to_fall.add(cube)

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
