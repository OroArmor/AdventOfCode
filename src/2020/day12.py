import util
from util import *
import numpy as np

test_data: str = \
    """F10
N3
F7
R90
F11"""


def task1(input):
    ship = np.array([0, 0])
    facing = RIGHT

    for line in input:
        op, l = line[0], int(line[1:])
        if op == "F":
            ship += facing * l
        elif op == "N":
            ship += UP * l
        elif op == "E":
            ship += RIGHT * l
        elif op == "S":
            ship += DOWN * l
        elif op == "W":
            ship += LEFT * l
        elif op == "R":
            facing = util.rotate(facing, -l)
        elif op == "L":
            facing = util.rotate(facing, l)
        else:
            print("AAAAAAA")
        # print(ship)

    return int(np.sum(np.abs(ship)))


def task2(input):
    ship = np.array([0, 0])
    waypoint = np.array([10, 1])

    for line in input:
        op, l = line[0], int(line[1:])
        if op == "F":
            ship += waypoint * l
        elif op == "N":
            waypoint += UP * l
        elif op == "E":
            waypoint += RIGHT * l
        elif op == "S":
            waypoint += DOWN * l
        elif op == "W":
            waypoint += LEFT * l
        elif op == "R":
            waypoint = util.rotate(waypoint, -l)
        elif op == "L":
            waypoint = util.rotate(waypoint, l)
        else:
            print("AAAAAAA")
        # print(ship)

    return int(np.sum(np.abs(ship)))


def parse(data: str):
    lines = util.as_lines(data)
    return lines


def main():
    data: str = util.get(12, 2020)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
