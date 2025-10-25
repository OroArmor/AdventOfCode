import util
from util import *

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
    if grid[pos] == ".":
        return False

    if not (pos + delta) in grid:
        return False

    check = grid[pos + delta]

    if check not in "-|" and check == grid[pos]:
        return False

    if grid[pos] == "S":
        if delta == Direction.DOWN:  # up
            return check in ["F", "|", "7"]
        elif delta == Direction.DOWN:  # down
            return check in ["L", "|", "J"]
        elif delta == Direction.RIGHT:  # right
            return check in ["7", "-", "J"]
        elif delta == Direction.LEFT:  # left
            return check in ["F", "-", "L"]

    return delta in [-dir for dir in dirs(check)]

def dirs(shape):
    if shape == ".":
        return []

    if shape == "S":
        return [c for c in cardinal_directions()]

    if shape == "F":
        return [Direction.UP, Direction.RIGHT]
    elif shape == "|":
        return [Direction.DOWN, Direction.UP]
    elif shape == "L":
        return [Direction.DOWN, Direction.RIGHT]
    elif shape == "-":
        return [Direction.RIGHT, Direction.LEFT]
    elif shape == "J":
        return [Direction.DOWN, Direction.LEFT]
    elif shape == "7":
        return [Direction.UP, Direction.LEFT]


PATH = []


def task1(input):
    global PATH
    grid, start = input

    PATH = []
    check = start
    while check != start or len(PATH) < 1:
        for card in dirs(grid[check]):
            if check + card == start and len(PATH) > 3:
                PATH.append(check)
                return (len(PATH)) // 2

            if check + card in PATH:
                continue

            if connects(check, card, grid):
                PATH.append(check)
                check = check + card
                break


VISUALIZE = False


def task2(input):
    global PATH
    grid, start = input

    deltas = sorted([
        Point(-PATH[0][0] + PATH[1][0], -PATH[0][1] + PATH[1][1]),
        Point(-PATH[0][0] + PATH[-1][0], -PATH[0][1] + PATH[-1][1])
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
            if Point(x, y) in PATH and crossing:
                crossing = grid[Point(x, y)] in "-"
                if not crossing:
                    if open == "F" and grid[Point(x, y)] == "7":
                        pass
                    elif open == "L" and grid[Point(x, y)] == "J":
                        pass
                    else:
                        crosses += 1
                    open = None
                if VISUALIZE: print(grid[Point(x, y)], end="")
            elif Point(x, y) in PATH:
                crossing = connects(Point(x, y), Direction.RIGHT, grid) and not grid[Point(x, y)] == "|"
                if not crossing:
                    crosses += 1
                open = grid[Point(x, y)]
                if VISUALIZE: print(grid[Point(x, y)], end="")
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
            grid[Point(x, y)] = c
            if c == "S":
                start = Point(x, y)

    return grid, start


def main():
    data: str = util.get(10, 2023)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
