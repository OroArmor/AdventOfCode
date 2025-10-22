import util
from util import *
import numpy as np

test_data: str = \
    """R8,U5,L5,D3
U7,R6,D4,L4"""


def task1(input):
    seen_1 = set()
    seen_2 = set()

    origin = Point(0, 0)
    for jump in input[0]:
        for pt in jump.iterate_internals():
            seen_1.add(origin + pt)
        origin += jump

    origin = Point(0, 0)
    for jump in input[1]:
        for pt in jump.iterate_internals():
            seen_2.add(origin + pt)
        origin += jump

    crossings = seen_1.intersection(seen_2)
    crossings.remove(Point(0, 0))
    return min(map(lambda c: c.manhattan(), crossings))


def task2(input):
    seen_1 = []
    seen_2 = []

    origin = Point(0, 0)
    for jump in input[0]:
        for pt in jump.iterate_internals():
            seen_1.append(origin + pt)
        origin += jump

    origin = Point(0, 0)
    for jump in input[1]:
        for pt in jump.iterate_internals():
            seen_2.append(origin + pt)
        origin += jump

    crossings = set(seen_1).intersection(set(seen_2))
    crossings.remove(Point(0, 0))

    return min(map(lambda c: seen_1.index(c) + seen_2.index(c), crossings))


def parse(data: str):
    lines = util.as_csv_lines(data)

    vals = []
    for line in lines:
        wire = []
        for val in line:
            match val[0]:
                case "R":
                    wire.append(Direction.RIGHT * int(val[1:]))
                case "L":
                    wire.append(Direction.LEFT * int(val[1:]))
                case "U":
                    wire.append(Direction.UP * int(val[1:]))
                case "D":
                    wire.append(Direction.DOWN * int(val[1:]))
        vals.append(wire)

    return vals


def main():
    data: str = util.get(3, 2019)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
