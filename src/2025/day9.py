import util
from util import *
import numpy as np

test_data: str = \
    """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""


def task1(input):
    max_size = 0

    for i, a in enumerate(input):
        for b in input[i + 1:]:
            s = (1 + abs(a[0] - b[0])) * (1 + abs(a[1] - b[1]))
            if s > max_size:
                max_size = s

    return max_size


def task2(input):
    max_size = 0

    for i, a in enumerate(input):
        for j, b in enumerate(input[i + 1:]):
            s = (1 + abs(a[0] - b[0])) * (1 + abs(a[1] - b[1]))
            mini = Point(min(a.x, b.x), min(a.y, b.y))
            maxi = Point(max(a.x, b.x), max(a.y, b.y))

            past = None
            first = None
            bad = False
            for d in input:
                e, f = d - mini, maxi - d

                dir = Point(
                    2 if f.x < 0 else
                    1 if f.x == 0 else
                    -1 if e.x == 0 else
                    -2 if e.x < 0 else
                    0,
                    2 if f.y < 0 else
                    1 if f.y == 0 else
                    -1 if e.y == 0 else
                    -2 if e.y < 0 else
                    0)

                if past is None:
                    first = dir
                elif (dir.x == 0 and dir.y == 0 or
                  dir.x == 0 and dir.y * past.y < 0 or
                  dir.y == 0 and dir.x * past.x < 0):
                    bad = True
                    break
                past = dir
            if (dir.x == 0 and dir.y == 0 or
                    dir.x == 0 and dir.y * first.y < 0 or
                    dir.y == 0 and dir.x * first.x < 0):
                bad = True

            if s > max_size and not bad:
                max_size = s

    return max_size


def parse(data: str):
    lines = util.as_csv_lines_of_ints(data)
    return [Point(x, y) for x, y in lines]


def main():
    data: str = util.get(9, 2025)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
