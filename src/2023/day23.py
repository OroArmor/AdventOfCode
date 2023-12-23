from collections import defaultdict
from copy import deepcopy

import util
from util import *
import numpy as np

test_data: str = \
    """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""


def task1(input):
    grid, width, height = input

    intersections = [Point(1, 0)]

    for x in range(1, width - 1):
        for y in range(1, height - 1):
            if grid[y][x] != "#":
                if len([Point(x, y) + dir for dir in cardinal_directions() if grid[y + dir.y][x + dir.x] != "#"]) >= 3:
                    intersections.append(Point(x, y))

    intersections.append((Point(width - 2, height - 1)))

    graph = defaultdict(dict)

    for start in intersections:
        to_check = [(start, {start})]

        while to_check:
            point, seen = to_check.pop()
            n = []
            for direction in cardinal_directions():
                np = point + direction
                if 0 <= np.x < width and 0 <= np.y < height and not grid[np.y][np.x] == "#":
                    if not (grid[np.y][np.x] == ">" and direction == Direction.LEFT):
                        if not (grid[np.y][np.x] == "<" and direction == Direction.RIGHT):
                            if not (grid[np.y][np.x] == "^" and direction == Direction.UP):
                                if not (grid[np.y][np.x] == "v" and direction == Direction.DOWN):
                                    n.append(np)

            for neighbor in n:
                if neighbor not in seen:
                    if neighbor in intersections:
                        graph[start][neighbor] = len(seen)
                    else:
                        to_check.append((neighbor, seen.union({neighbor})))

    paths = [[Point(1, 0)]]
    final_paths = []

    changed = True
    while changed:
        new_paths = []
        changed = False
        for path in paths:
            for d in graph[path[-1]]:
                if d == Point(width - 2, height - 1):
                    new_path = deepcopy(path)
                    new_path.append(d)
                    final_paths.append(new_path)
                    continue

                if d not in path:
                    new_path = deepcopy(path)
                    new_path.append(d)
                    new_paths.append(new_path)
                    changed = True
        paths = new_paths

    max_path = 0
    for path in final_paths:
        length = 0
        for a, b in itertools.pairwise(path):
            length += graph[a][b]

        max_path = max(max_path, length)
    return max_path


def task2(input):
    grid, width, height = input

    intersections = [Point(1, 0)]

    for x in range(1, width - 1):
        for y in range(1, height - 1):
            if grid[y][x] != "#":
                if len([Point(x, y) + dir for dir in cardinal_directions() if grid[y + dir.y][x + dir.x] != "#"]) >= 3:
                    intersections.append(Point(x, y))

    intersections.append((Point(width - 2, height - 1)))

    graph = defaultdict(list)
    max_dist = 0
    for start in intersections:
        to_check = [(start, {start})]

        while to_check:
            point, seen = to_check.pop()
            n = []
            for direction in cardinal_directions():
                np = point + direction
                if 0 <= np.x < width and 0 <= np.y < height and not grid[np.y][np.x] == "#":
                    n.append(np)

            for neighbor in n:
                if neighbor not in seen:
                    if neighbor in intersections:
                        graph[start].append((neighbor, len(seen)))
                        max_dist = max(max_dist, len(seen))
                    else:
                        to_check.append((neighbor, seen.union({neighbor})))

    SEEN = {p: False for p in intersections}
    max_path = 0

    def dfs(current, distance):
        nonlocal max_path
        if SEEN[current]:
            return 0

        SEEN[current] = True

        if current.y == height - 1:
            max_path = max(max_path, distance)

        for n, d in graph[current]:
            dfs(n, distance + d)

        SEEN[current] = False

    dfs(Point(1, 0), 0)
    return max_path


def parse(data: str):
    lines = util.as_grid(data)
    return lines


def main():
    data: str = util.get(23, 2023)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
