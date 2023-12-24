import decimal

import scipy
import sympy as sym
import sympy.solvers

import util
from util import *
import numpy as np

test_data: str = \
    """19, 13, 30 @ -2, 1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @ 1, -5, -3"""


def task1(input):
    mi, ma = 200000000000000, 400000000000000
    if len(input) < 100:
        mi, ma = 7, 27

    total = 0
    for ai, a in enumerate(input):
        for bi, b in enumerate(input):
            if bi <= ai:  # only check unique pairs
                continue

            (ax, ay, _), (avx, avy, _) = a
            (bx, by, _), (bvx, bvy, _) = b

            if avy / avx == bvy / bvx:  # parallel
                continue

            x = (avy / avx * ax - bvy / bvx * bx - ay + by) / (avy / avx - bvy / bvx)
            y = bvy / bvx * (x - bx) + by

            if mi <= x <= ma and mi <= y <= ma:  # inside box
                if (x - ax) / avx > 0:  # meet in the future
                    if (x - bx) / bvx > 0:
                        if (y - ay) / avy > 0:
                            if (y - by) / bvy > 0:
                                total += 1
                                # assert (x - ax) / avx > 0, (x - ax) / avx

    return total


def task2(input):
    # rx + t * rvx == tx + t * tvx
    # ry + t * rvy == ty + t * tvy
    # rz + t * rvz == tz + t * tvz

    tx, ty, tz, tvx, tvy, tvz = sym.var("tx, ty, tz, tvx, tvy, tvz", integer=True)
    ts = sym.var("t1, t2, t3", positive=True, integer=True)

    eqs = []
    for i, ((rx, ry, rz), (rvx, rvy, rvz)) in enumerate(input[:3]):
        eqs.append(int(rx) + ts[i] * int(rvx) - (tx + ts[i] * tvx))
        eqs.append(int(ry) + ts[i] * int(rvy) - (ty + ts[i] * tvy))
        eqs.append(int(rz) + ts[i] * int(rvz) - (tz + ts[i] * tvz))

    res = sympy.solvers.solve(eqs, (*ts, tx, ty, tz, tvx, tvy, tvz))[0]
    _, _, _, x, y, z, _, _, _ = res

    return x + y + z


def parse(data: str):
    lines = util.as_lines(data)

    stones = []

    for line in lines:
        stone, v = line.split(" @ ")
        stone, v = util.as_csv_of_ints(stone), util.as_csv_of_ints(v)
        stones.append((stone, v))

    return stones


def main():
    data: str = util.get(24, 2023)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
