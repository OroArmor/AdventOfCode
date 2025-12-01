import util
from util import *
import numpy as np

test_data: str = \
    """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##"""

# test_data = \
# """.#..#
# .....
# #####
# ....#
# ...##"""

BEST_STATION = None

@cache
def possible_directions(width, height):
    used_directions = set()
    for dx in range(-width, width):
        for dy in range(-height, height):
            if dx == 0 and dy == 0:
                continue

            gcd_abs = abs(gcd(dx, dy))

            if gcd_abs == 1:
                dP = Point(dx // gcd_abs, dy // gcd_abs)
                if dP in used_directions:
                    print(":(")
                used_directions.add(dP)
    def sort(p):
        return -np.atan2(p.x, p.y)
    return sorted(list(used_directions), key=sort)

def task1(input):
    grid, width, height = input

    total = 0

    directions = possible_directions(width, height)

    for asteroid in grid:
        a_total = 0

        for direction in directions:
            a = asteroid + direction
            while 0 <= a.x < width and 0 <= a.y < height:
                if a in grid:
                    a_total += 1
                    break
                a = a + direction
        if a_total > total:
            total = a_total
            global BEST_STATION
            BEST_STATION = asteroid

    return total


def task2(input):
    grid, width, height = input

    dirs = possible_directions(width, height)

    hit = 0
    dir_check = 0
    while True:
        a = BEST_STATION
        while 0 <= a.x < width and 0 <= a.y < height:
            a = a + dirs[dir_check % len(dirs)]
            if a in grid:
                hit += 1

                if hit == 200:
                    return a.x * 100 + a.y
                grid.remove(a)
                break
        dir_check += 1


def parse(data: str):
    lines = util.as_lines(data)

    width = len(lines[0])
    height = len(lines)

    grid = set()

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                grid.add(Point(x, y))

    return grid, width, height


def main():
    data: str = util.get(10, 2019)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
