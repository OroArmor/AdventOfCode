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


def task2(_):
    global DIST

    reachable = set()
    path = list(p for p, _ in sorted(DIST.items(), key=lambda k: k[1]))
    for ud in [Direction.UP, Direction.DOWN]:
        for s2 in [Direction.LEFT, Direction.RIGHT]:
            for s in range(21):
                for lr_s in range(0, 21 - s):
                    # if s > 1 or lr_s > 1:
                    potential = path[0] + ud * s + s2 * lr_s
                    if potential in DIST and DIST[potential] - potential.manhattan(path[0]) >= 100:
                        reachable.add(potential)

    ud_add = set()
    lr_add = set()
    for s in range(21):
        point = Direction.UP * s + Direction.RIGHT * (20 - s)
        lr_add.add(point)
        lr_add.add(Point(point.x, -point.y))

        ud_add.add(Point(-point.y, point.x))
        ud_add.add(Point(point.y, point.x))

    total = len(reachable)
    for step in itertools.pairwise(path):
        ds = step[1] - step[0]
        added = set()
        for s2 in (lr_add if ds.x != 0 else ud_add):
            remove = step[0] - s2 * (ds.x + ds.y)
            add = step[1] + s2 * (ds.x + ds.y)
            if remove in reachable:
                reachable.remove(remove)

            if add in DIST and DIST[add] - DIST[step[1]] >= 120:
                reachable.add(add)
                added.add(add)

        too_far = set()
        for value in reachable:
            if DIST[value] - DIST[step[1]] - value.manhattan(step[1]) >= 100:
                total += 1
            else:
                too_far.add(value)
        reachable -= too_far

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
