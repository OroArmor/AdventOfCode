import util
from util import *
import numpy as np

test_data: str = \
    """.#.
..#
###"""


def task1(input):
    points = input

    for _ in range(6):
        new_points = set()
        inactive = {}
        active = {}

        for point in points:
            count = 0

            for dir in adjacent_directions_3d():
                n = (point[0] + dir[0], point[1] + dir[1], point[2] + dir[2])

                if n not in points:
                    if n in inactive.keys():
                        inactive[n] += 1
                    else:
                        inactive[n] = 1
                else:
                    count += 1

            active[point] = count
            if count == 2 or count == 3:
                new_points.add(point)

        for in_p in inactive.keys():
            if inactive[in_p] == 3:
                new_points.add(in_p)

        points = new_points

    return len(points)


def task2(input):
    points = input

    for _ in range(6):
        new_points = set()
        inactive = {}

        for point in points:
            count = 0

            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    for dz in range(-1, 2):
                        for dw in range(-1, 2):
                            if not (dx == 0 and dy == 0 and dz == 0 and dw == 0):
                                n = (point[0] + dx, point[1] + dy, point[2] + dz, point[3] + dw)

                                if n not in points:
                                    if n in inactive.keys():
                                        inactive[n] += 1
                                    else:
                                        inactive[n] = 1
                                else:
                                    count += 1

            if count == 2 or count == 3:
                new_points.add(point)

        for in_p in inactive.keys():
            if inactive[in_p] == 3:
                new_points.add(in_p)

        points = new_points

    return len(points)


def parse(data: str):
    lines = util.as_lines(data)

    points = set()

    for x, line in enumerate(lines):
        for y, c in enumerate(line):
            if c == "#":
                points.add((x, y, 0, 0))

    return points


def main():
    data: str = util.get(17, 2020)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
