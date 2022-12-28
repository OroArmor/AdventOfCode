import collections

import util
import numpy as np

test_data: str = \
    """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#"""


def normalize_pt(x, y, width, height):
    if x == 0:
        return width - 2, y
    if x == width - 1:
        return 1, y
    if y == 0:
        return x, height - 2
    if y == height - 1:
        return x, 1
    return x, y


def update_blizzards(minutes, width, height, cache):
    if minutes in cache.keys():
        return cache[minutes]

    blizzards = update_blizzards(minutes - 1, width, height, cache)

    new_blizzards = collections.defaultdict(lambda: [])
    for (x, y), dirs in blizzards.items():
        for dir in dirs:
            if dir == 0:
                new_blizzards[normalize_pt(x + 1, y, width, height)].append(dir)
            elif dir == 1:
                new_blizzards[normalize_pt(x, y + 1, width, height)].append(dir)
            elif dir == 2:
                new_blizzards[normalize_pt(x - 1, y, width, height)].append(dir)
            elif dir == 3:
                new_blizzards[normalize_pt(x, y - 1, width, height)].append(dir)

    cache[minutes] = new_blizzards
    return new_blizzards


def search(start, end, width, height, cache, start_minute=0):
    moves = np.array([
        [0, 0],
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1]
    ])

    def point_gen(point):
        pos, minutes = np.array(point[0]), point[1]
        next_blizzards = update_blizzards(minutes + 1, width, height, cache)
        for move in moves:
            new_pos = pos + move
            if new_pos[0] == end[0] and new_pos[1] == end[1]:
                yield minutes + 1, None

            if 0 < new_pos[0] < width - 1 and 0 < new_pos[1] < height - 1 or new_pos[0] == start[0] and new_pos[1] == start[1]:
                if tuple(new_pos) not in next_blizzards.keys():
                    yield -1, (tuple(new_pos), minutes + 1)

    points = [(tuple(start), start_minute)]
    while True:
        new_points = set()
        for point in points:
            for new_point in point_gen(point):
                if new_point[0] != -1:
                    return new_point[0]

                new_points.add(new_point[1])

        if len(new_points) == 0:
            return -1

        points = new_points


def task1(input):
    blizzards, width, height = input

    pos = np.array([1, 0])
    end = np.array([width - 2, height - 1])

    return search(pos, end, width, height, {0: blizzards})


def task2(input):
    blizzards, width, height = input

    start = np.array([1, 0])
    end = np.array([width - 2, height - 1])

    cache = {
        0: blizzards
    }
    first_end = search(start.copy(), end, width, height, cache)
    first_start = search(end.copy(), start, width, height, cache, start_minute=first_end)
    return search(start.copy(), end, width, height, cache, start_minute=first_start)


def parse(data: str):
    blizzards = {}
    lines = util.as_lines(data)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == ">":
                blizzards[(x, y)] = [0]
            elif c == "v":
                blizzards[(x, y)] = [1]
            elif c == "<":
                blizzards[(x, y)] = [2]
            elif c == "^":
                blizzards[(x, y)] = [3]

    return blizzards, len(lines[-1]), len(lines)


def main():
    data: str = util.get(24, 2022)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
