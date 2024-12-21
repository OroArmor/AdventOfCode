import util
from util import *

test_data: str = \
    """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""

DIST = {}


def task1(input):
    global DIST
    walls, start, end, w, h = input

    DIST = {}
    steps = 0
    while start != end:
        steps += 1
        DIST[start] = steps
        for dir in Direction.values():
            if start + dir not in DIST.keys():
                if start + dir not in walls:
                    start += dir
                    break
    DIST[end] = steps + 1

    total = 0
    for p in DIST.keys():
        for dir in Direction.values():
            if p + dir in walls and p + dir * 2 in DIST.keys():
                if DIST[p + dir * 2] - DIST[p] - 2 >= 100:
                    total += 1

    return total


def task2(input):
    global DIST

    diamond = set()
    for ud in [Direction.UP, Direction.DOWN]:
        for lr in [Direction.LEFT, Direction.RIGHT]:
            for ud_s in range(21):
                for lr_s in range(0, 21 - ud_s):
                    if ud_s > 1 or lr_s > 1:
                        diamond.add(ud * ud_s + lr * lr_s)

    total = 0
    for p in DIST.keys():
        for d in diamond:
            if (n := p + d) in DIST.keys():
                if DIST[n] - DIST[p] - d.manhattan() >= 100:
                    total += 1

    return total


def parse(data: str):
    raw, w, h = util.as_grid(data)

    walls = set()
    start = None
    end = None

    for y in range(h):
        for x in range(w):
            if raw[y][x] == "#":
                walls.add(Point(x, y))
            elif raw[y][x] == "S":
                start = Point(x, y)
            elif raw[y][x] == "E":
                end = Point(x, y)

    return walls, start, end, w, h


def main():
    data: str = util.get(20, 2024)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
