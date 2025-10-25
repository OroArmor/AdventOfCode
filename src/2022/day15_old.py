import re
import threading

import util
import numpy as np

test_data: str = \
    """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""


def task1(input):
    list_points = input

    y = 10 if len(list_points) == 14 else 2000000

    total = set()

    for points in list_points:
        manhattan = np.abs(points[0:2] - points[2:]).sum()
        x_man = (manhattan - abs(points[1] - y))

        if x_man > 0:
            total = total.union(set(range(points[0] - x_man, points[0] + x_man + 1)))

    for points in list_points:
        if points[3] == y and points[2] in total:
            total.remove(points[2])

    return len(total)


def skip_scanned(list_points, current):
    for point in list_points:
        m = np.abs(point[0:2] - point[2:]).sum()
        dy = abs(point[1] - current[1])
        if dy > m:
            continue

        mx = m - dy
        dx = abs(point[0] - current[0])
        if dx > mx:
            continue
        return point[0] + mx + 1, current[1]
    return current



def task2(input):
    list_points = input
    max_val = 20 if len(list_points) == 14 else 4000000

    for y in range(max_val, -1, -1):
        pp, np = (0, y), (0, y)
        first = True

        while first or (not pp == np and np[0] <= max_val):
            first = False
            pp = np
            np = skip_scanned(list_points, np)

        if np[0] <= max_val:
            return np[0] * 4000000 + np[1]


def parse(data: str):
    lines = util.as_lines(data)
    list_points = np.array(list(map(lambda l: np.array(util.list_as_ints(re.findall("-?\\d+", l))), lines)))

    return list_points


def main():
    data: str = util.get(15, 2022)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
