import util
from util import *
import numpy as np

test_data: str = \
    """.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|...."""


def solve(beams, to_add, grid, width, height):
    x, y, direction = to_add

    while 0 <= x < width and 0 <= y < height and (x, y) not in grid and (x, y, direction) not in beams:
        beams.add((x, y, direction))
        x += int(direction[0])
        y += int(direction[1])

    if x < 0 or x >= width or y < 0 or y >= height or (x, y, direction) in beams:
        return

    beams.add((x, y, direction))
    if grid[(x, y)] == "/":
        match direction:
            case (1, 0):
                solve(beams, (x, y - 1, (0, -1)), grid, width, height)  # Left -> Up
            case (-1, 0):
                solve(beams, (x, y + 1, (0, 1)), grid, width, height)  # Right -> Down
            case (0, -1):
                solve(beams, (x + 1, y, (1, 0)), grid, width, height)  # Up -> Left
            case (0, 1):
                solve(beams, (x - 1, y, (-1, 0)), grid, width, height)  # Down -> Right
    elif grid[(x, y)] == "\\":
        match direction:
            case (1, 0):
                solve(beams, (x, y + 1, (0, 1)), grid, width, height)  # Left -> Down
            case (-1, 0):
                solve(beams, (x, y - 1, (0, -1)), grid, width, height)  # Right -> Up
            case (0, 1):
                solve(beams, (x + 1, y, (1, 0)), grid, width, height)  # Down -> Left
            case (0, -1):
                solve(beams, (x - 1, y, (-1, 0)), grid, width, height)  # Up -> Right
    elif grid[(x, y)] == "|":
        match direction:
            case (1, 0) | (-1, 0):  # Split
                solve(beams, (x, y, (0, -1)), grid, width, height)  # Up
                solve(beams, (x, y, (0, 1)), grid, width, height)  # Down
            case (0, 1) | (0, -1):  # Pass through
                solve(beams, (x + direction[0], y + direction[1], direction), grid, width, height)
    elif grid[(x, y)] == "-":
        match direction:
            case (0, 1) | (0, -1):  # Split
                solve(beams, (x, y, (-1, 0)), grid, width, height)  # Right
                solve(beams, (x, y, (1, 0)), grid, width, height)  # Left
            case (1, 0) | (-1, 0):  # Pass through
                solve(beams, (x + direction[0], y + direction[1], direction), grid, width, height)
    else:
        print("PANIC at the disco")


def calculate_energized(x, y, direction, grid, width, height):
    beams = set()
    solve(beams, (x, y, direction), grid, width, height)
    energized = set([(x, y) for x, y, _ in beams])
    return len(energized)


def task1(input):
    grid, width, height = input
    return calculate_energized(0, 0, (1, 0), grid, width, height)


def task2(input):
    grid, width, height = input

    best = 0

    for x in range(width):
        best = max(calculate_energized(x, 0, (0, 1), grid, width, height), best)
        best = max(calculate_energized(x, height - 1, (0, -1), grid, width, height), best)

    for y in range(height):
        best = max(calculate_energized(0, y, (1, 0), grid, width, height), best)
        best = max(calculate_energized(width - 1, y, (-1, 0), grid, width, height), best)

    return best


def parse(data: str):
    grid_raw, width, height = util.as_grid(data)
    return {(x, y): c for y, row in enumerate(grid_raw) for x, c in enumerate(row) if c != "."}, width, height


def main():
    data: str = util.get(16, 2023)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
