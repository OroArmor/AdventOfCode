import re

import util

from lib.point_util import Point
from lib.range_util import Range

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

    ranges = find_range(list_points, y)

    for _, beacon in list_points:
        new_ranges = []
        for r in ranges:
            if beacon.y == y and beacon.x in r:
                new_ranges += list(r.split_on(beacon.x))
            else:
                new_ranges.append(r)
        ranges = new_ranges

    return sum(len(r) for r in ranges)


def find_range(list_points, y):
    ranges = []
    for sensor, beacon in list_points:
        manhattan = sensor.manhattan(beacon)
        x_man = (manhattan - abs(sensor.y - y))

        if x_man > 0:
            my_range = Range(sensor.x - x_man, sensor.x + x_man, inclusive=True)
            new_ranges = []
            for r in ranges:
                if r.intersects(my_range):
                    my_range = my_range.merge(r)
                else:
                    new_ranges.append(r)
            new_ranges.append(my_range)
            ranges = new_ranges
    return ranges


def task2(input):
    list_points = input
    max_val = 20 if len(list_points) == 14 else 4000000

    sensor_info = []
    for sensor, beacon in list_points:
        manhattan = sensor.manhattan(beacon)
        print(manhattan)
        sensor_info.append((Range(sensor.y - manhattan, sensor.y + manhattan, inclusive=True), manhattan))

    for y in range(max_val, -1, -1):
        ranges = []
        for i, (sensor, _) in enumerate(list_points):
            y_range, dist = sensor_info[i]
            if y_range.start <= y < y_range.end:
                x_dist = (dist - abs(sensor.y - y))
                ranges.append(Range(sensor.x - x_dist, sensor.x + x_dist, inclusive=True))

        ranges = sorted(ranges)
        i = 1
        r = ranges[0]
        while i < len(ranges):
            if not r.intersects(ranges[i]):
                return r.end * 4000000 + y

            if r.end < ranges[i].end:
                r = ranges[i]
            i += 1

    return


def parse(data: str):
    lines = util.as_lines(data)
    list_points = list(
        map(
            lambda pts: (Point(pts[0], pts[1]), Point(pts[2], pts[3])),
            map(
                lambda l: util.list_as_ints(re.findall("-?\\d+", l)),
                lines
            )
        )
    )

    return list_points


def main():
    data: str = util.get(15, 2022)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
