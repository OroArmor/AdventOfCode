import util
from util import *

test_data: str = \
    """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


def task1(input):
    grid, s, w, h = input

    seen = set()
    assert not traverse(grid, seen, s, 0, w, h)

    return len(set([s for s, _ in seen]))

def traverse(grid, seen, s, dir, w, h) -> bool:
    dirs = [Direction.DOWN, Direction.RIGHT, Direction.UP, Direction.LEFT]
    while True:
        i = 1
        while not (next := s + dirs[dir] * i) in grid:
            if (next, dir) in seen:
                return True
            if next.x == -1 or next.x == w or next.y == -1 or next.y == h:
                return False
            seen.add((next, dir))
            i += 1
        s += dirs[dir] * (i - 1)
        dir += 1
        dir %= 4


def task2(input):
    grid, s, w, h = input

    dirs = [Direction.DOWN, Direction.RIGHT, Direction.UP, Direction.LEFT]
    seen = set()
    loops = 0

    dir = 0
    while 0 < s.x < w and 0 < s.y < h:
        seen.add((s, dir))
        next = s + dirs[dir]
        if next not in grid and not ((next, 0) in seen or (next, 1) in seen or (next, 2) in seen or (next, 3) in seen):
            grid.add(next)
            if traverse(grid, set(seen), s, (dir + 1) % 4, w, h):
                loops += 1
            grid.remove(next)

        if next in grid:
            dir += 1
            dir %= 4
        else:
            s += dirs[dir]

    return loops


def parse(data: str):
    grid_raw, w, h = util.as_grid(data)

    grid = set()
    s = None
    for x in range(w):
        for y in range(h):
            if grid_raw[y][x] == "#":
                grid.add(Point(x, y))
            elif grid_raw[y][x] == "^":
                s = Point(x, y)

    return grid, s, w, h


def main():
    data: str = util.get(6, 2024)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
