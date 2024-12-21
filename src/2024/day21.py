import itertools

import util
from util import *
import numpy as np

test_data: str = \
    """029A
980A
179A
456A
379A"""

NUM_KEYPAD = ["789", "456", "123", " 0A"]
ARROW_KEYPAD = [" ^A", "<v>"]

PART_2 = False


@cache
def pt_on_grid(c, num) -> Point:
    grid = NUM_KEYPAD if num else ARROW_KEYPAD
    y = [i for i, line in enumerate(grid) if c in line][0]
    x = [i for i, ch in enumerate(grid[y]) if c == ch][0]
    return Point(x, y)


@cache
def valid_path(start, path, num) -> bool:
    grid = NUM_KEYPAD if num else ARROW_KEYPAD
    current = start
    for i in range(len(path) - 1):
        match path[i]:
            case "^":
                current += Direction.DOWN
            case "v":
                current += Direction.UP
            case "<":
                current += Direction.LEFT
            case ">":
                current += Direction.RIGHT
        if grid[current.y][current.x] == " ":
            return False
    return True


@cache
def find_shortest(s, depth):
    global PART_2
    start = Point(2, 3) if depth == 0 else Point(2, 0)

    length = 0
    c = 0
    while c != len(s):
        next = pt_on_grid(s[c], depth == 0)
        ds = next - start
        path = max(0, ds.x) * ">" + max(0, -ds.x) * "<" + max(0, ds.y) * "v" + max(0, -ds.y) * "^"
        if depth == (25 if PART_2 else 2):
            length += len(path) + 1
        else:
            paths = set(map(lambda t: "".join(t) + "A", itertools.permutations(path)))
            length += min(find_shortest(path, depth + 1) for path in paths if valid_path(start, path, depth == 0))
        start = next
        c += 1
    return length


def task1(input):
    global PART_2
    PART_2 = False
    find_shortest.cache_clear()
    total = 0
    for code in input:
        len = find_shortest(code, 0)
        total += len * int(code[0:3])
    return total


def task2(input):
    global PART_2
    PART_2 = True
    find_shortest.cache_clear()
    total = 0
    for code in input:
        len = find_shortest(code, 0)
        total += len * int(code[0:3])
    return total


def parse(data: str):
    lines = util.as_lines(data)
    return lines


def main():
    data: str = util.get(21, 2024)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
