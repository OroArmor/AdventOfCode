from collections import defaultdict, deque

import util
from util import *
import numpy as np

test_data: str = \
    """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""


def task1(input):
    grid, w, h = input

    values = []
    seen = set()

    for y in range(h):
        for x in range(w):
            if (x, y) in seen:
                continue

            val = grid[y][x]
            to_check = deque([(x, y)])
            perimeter = 0
            area = 0
            seen.add((x, y))

            while len(to_check) > 0:
                x2, y2 = to_check.popleft()

                if x2 == 0 or grid[y2][x2 - 1] != val:
                    perimeter += 1
                elif (x2 - 1, y2) not in seen:
                    seen.add((x2 - 1, y2))
                    to_check.append((x2 - 1, y2))

                if x2 == w - 1 or grid[y2][x2 + 1] != val:
                    perimeter += 1
                elif (x2 + 1, y2) not in seen:
                    seen.add((x2 + 1, y2))
                    to_check.append((x2 + 1, y2))

                if y2 == 0 or grid[y2 - 1][x2] != val:
                    perimeter += 1
                elif (x2, y2 - 1) not in seen:
                    seen.add((x2, y2 - 1))
                    to_check.append((x2, y2 - 1))

                if y2 == h - 1 or grid[y2 + 1][x2] != val:
                    perimeter += 1
                elif (x2, y2 + 1) not in seen:
                    seen.add((x2, y2 + 1))
                    to_check.append((x2, y2 + 1))

                area += 1
            values.append((area, perimeter))
    return sum(a * b for a, b in values)


def task2(input):
    grid, w, h = input

    values = []
    seen = set()

    for y in range(h):
        for x in range(w):
            if (x, y) in seen:
                continue

            val = grid[y][x]
            to_check = deque([(x, y)])
            area = 0
            this_seen = set()
            this_seen.add((x, y))

            while len(to_check) > 0:
                x2, y2 = to_check.popleft()

                if x2 == 0 or grid[y2][x2 - 1] != val:
                    pass
                elif (x2 - 1, y2) not in this_seen:
                    this_seen.add((x2 - 1, y2))
                    to_check.append((x2 - 1, y2))

                if x2 == w - 1 or grid[y2][x2 + 1] != val:
                    pass
                elif (x2 + 1, y2) not in this_seen:
                    this_seen.add((x2 + 1, y2))
                    to_check.append((x2 + 1, y2))

                if y2 == 0 or grid[y2 - 1][x2] != val:
                    pass
                elif (x2, y2 - 1) not in this_seen:
                    this_seen.add((x2, y2 - 1))
                    to_check.append((x2, y2 - 1))

                if y2 == h - 1 or grid[y2 + 1][x2] != val:
                    pass
                elif (x2, y2 + 1) not in this_seen:
                    this_seen.add((x2, y2 + 1))
                    to_check.append((x2, y2 + 1))

                area += 1
            seen |= this_seen

            min_x = min((p[0] for p in this_seen))
            max_x = max((p[0] for p in this_seen))
            min_y = min((p[1] for p in this_seen))
            max_y = max((p[1] for p in this_seen))

            perimeter = 0
            for y2 in range(min_y, max_y + 1):
                top = (min_x, y2 - 1) not in this_seen and (min_x, y2) in this_seen
                bottom = (min_x, y2 + 1) not in this_seen and (min_x, y2) in this_seen
                for x2 in range(min_x, max_x + 1):
                    if (x2, y2) in this_seen:
                        if (x2, y2 - 1) in this_seen:
                            perimeter += top
                        top = (x2, y2 - 1) not in this_seen

                        if (x2, y2 + 1) in this_seen:
                            perimeter += bottom
                        bottom = (x2, y2 + 1) not in this_seen
                    else:
                        perimeter += top
                        top = False
                        perimeter += bottom
                        bottom = False
                perimeter += top
                perimeter += bottom
            values.append((area, perimeter * 2))

    return sum(a * b for a, b in values)


def parse(data: str):
    lines = util.as_grid(data)
    return lines


def main():
    data: str = util.get(12, 2024)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
