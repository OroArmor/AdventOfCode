import os
from collections import defaultdict

import util
from util import *
import numpy as np
import re

test_data: str = \
    """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

# WIDTH = 11
# HEIGHT = 7

WIDTH = 101
HEIGHT = 103

def task1(input):
    quads = [0, 0, 0, 0]

    for pos, vel in input:
        pos += vel * 100
        x = pos.x % WIDTH
        y = pos.y % HEIGHT

        if x < WIDTH // 2:
            if y < HEIGHT // 2:
                quads[0] += 1
            elif y > HEIGHT // 2:
                quads[1] += 1
        elif x > WIDTH // 2:
            if y < HEIGHT // 2:
                quads[2] += 1
            elif y > HEIGHT // 2:
                quads[3] += 1

    return reduce(int.__mul__, quads, 1)


def task2(inputs):
    for s in range(WIDTH * HEIGHT):
        pts = set()
        for pos, vel in inputs:
            pt = pos + vel * s
            pt.x %= WIDTH
            pt.y %= HEIGHT
            if pt in pts:
                break
            pts.add(pt)
        else:
            if len(pts) == len(inputs):
                return s


def parse(data: str):
    lines = util.as_lines(data)

    vals = []

    for line in lines:
        pts = util.list_as_ints(re.findall("(-?\\d+)", line))
        vals.append((Point(pts[0], pts[1]), Point(pts[2], pts[3])))

    return vals


def main():
    data: str = util.get(14, 2024)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
