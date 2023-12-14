import util
from util import *
import numpy as np

test_data: str = \
    """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""


def connects(pos, delta, grid):
    if grid[tuple(pos)] == ".":
        return False

    if not tuple(pos + delta) in grid:
        return False

    check = grid[tuple(pos + delta)]
    delta = tuple(delta)

    if check not in "-|" and check == grid[tuple(pos)]:
        return False

    if grid[tuple(pos)] == "S":
        if delta[1] == -1:  # up
            return check in ["F", "|", "7"]
        elif delta[1] == 1:  # down
            return check in ["L", "|", "J"]
        elif delta[0] == 1:  # right
            return check in ["7", "-", "J"]
        elif delta[0] == -1:  # left
            return check in ["F", "-", "L"]

    if check == "F":
        return delta in [(0, -1), (-1, 0)]
    elif check == "|":
        return delta in [(0, 1), (0, -1)]
    elif check == "L":
        return delta in [(0, 1), (-1, 0)]
    elif check == "-":
        return delta in [(1, 0), (-1, 0)]
    elif check == "J":
        return delta in [(0, 1), (1, 0)]
    elif check == "7":
        return delta in [(0, -1), (1, 0)]

    return False


def dirs(shape):
    if shape == ".":
        return []

    if shape == "S":
        return [c for c in cardinal_directions()]

    if shape == "F":
        return [(0, 1), (1, 0)]
    elif shape == "|":
        return [(0, -1), (0, 1)]
    elif shape == "L":
        return [(0, -1), (1, 0)]
    elif shape == "-":
        return [(-1, 0), (1, 0)]
    elif shape == "J":
        return [(0, -1), (-1, 0)]
    elif shape == "7":
        return [(0, 1), (-1, 0)]


PATH = []


def task1(input):
    global PATH
    grid, start = input

    PATH = []
    check = start
    while tuple(check) != tuple(start) or len(PATH) < 1:
        for card in dirs(grid[tuple(check)]):
            if tuple(check + card) == tuple(start) and len(PATH) > 3:
                PATH.append(tuple(check))
                return (len(PATH)) // 2

            if tuple(check + card) in PATH:
                continue

            if connects(check, card, grid):
                PATH.append(tuple(check))
                check = check + card
                break


VISUALIZE = False


def task2(input):
    global PATH
    grid, start = input

    deltas = sorted([
        (-PATH[0][0] + PATH[1][0], -PATH[0][1] + PATH[1][1]),
        (-PATH[0][0] + PATH[-1][0], -PATH[0][1] + PATH[-1][1])
    ])

    for k in "FJL7-|":
        deltas_maybe = sorted(dirs(k))
        if deltas == deltas_maybe:
            grid[PATH[0]] = k
            break

    end = max(grid.keys())
    count = 0
    for y in range(end[1] + 1):
        crosses = 0
        crossing = False
        open = None
        for x in range(end[0] + 1):
            if (x, y) in PATH and crossing:
                crossing = grid[(x, y)] in "-"
                if not crossing:
                    if open == "F" and grid[(x, y)] == "7":
                        pass
                    elif open == "L" and grid[(x, y)] == "J":
                        pass
                    else:
                        crosses += 1
                    open = None
                if VISUALIZE: print(grid[(x, y)], end="")
            elif (x, y) in PATH:
                crossing = connects(np.array([x, y]), np.array([1, 0]), grid) and not grid[(x, y)] == "|"
                if not crossing:
                    crosses += 1
                open = grid[(x, y)]
                if VISUALIZE: print(grid[(x, y)], end="")
            else:
                count += crosses % 2
                if VISUALIZE: print(f"{('█' if crosses % 2 == 1 else ' ')}", end="")

        if VISUALIZE: print("")

    return count


def parse(data: str):
    lines = util.as_lines(data)

    grid = {}
    start = None

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[(x, y)] = c
            if c == "S":
                start = (x, y)

    return grid, np.array(start)


def main():
    data: str = util.get(10, 2023)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
