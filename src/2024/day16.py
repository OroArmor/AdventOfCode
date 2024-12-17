import util
from util import *

test_data: str = \
    """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

test_data: str = \
    """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""

PART_2_DATA = (None, None)


def task1(input):
    global PART_2_DATA
    start, end, walls = input

    def neighbors(current):
        if current[0] + current[1] not in walls:
            yield (current[0] + current[1], current[1]), 1
        if (n := current[0] + (d := Point(current[1].y, current[1].x))) not in walls:
            yield (n, d), 1001
        if (n := current[0] + (d := Point(-current[1].y, -current[1].x))) not in walls:
            yield (n, d), 1001

    def is_end(current):
        return current[0] == end

    came_from, ends, cost = util.dijkstra((start, Direction.RIGHT), neighbors, is_end)
    PART_2_DATA = (came_from, ends)
    return int(cost)


def task2(input):
    global PART_2_DATA
    came_from, ends = PART_2_DATA

    stack = [*ends]
    in_best = set(stack)
    while len(stack) > 0:
        next = stack.pop(0)
        for other in came_from[next]:
            if other not in in_best:
                in_best.add(other)
                stack.append(other)

    return len(set((v[0] for v in in_best)))


def parse(data: str):
    raw, w, h = util.as_grid(data)

    start = None
    end = None
    walls = set()

    for y in range(h):
        for x in range(w):
            if raw[y][x] == "#":
                walls.add(Point(x, y))
            elif raw[y][x] == "S":
                start = Point(x, y)
            elif raw[y][x] == "E":
                end = Point(x, y)

    return start, end, walls


def main():
    data: str = util.get(16, 2024)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
