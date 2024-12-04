import util
from util import *
import numpy as np

test_data: str = \
    """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


def task1(input):
    grid, w, h = input

    total = 0
    for x in range(w):
        for y in range(h):
            val = grid[x][y]
            if val == "X":
                for (dx, dy) in adjacent_directions():
                    if x + dx < 0 or y + dy < 0:
                        continue
                    if x + 2 * dx < 0 or y + 2 * dy < 0:
                        continue
                    if x + 3 * dx < 0 or y + 3 * dy < 0:
                        continue

                    try:
                        if grid[x + dx][y + dy] == "M" and grid[x + 2 * dx][y + 2 * dy] == "A" and grid[x + 3 * dx][y + 3 * dy] == "S":
                            total += 1
                    except:
                        pass
    return total


def task2(input):
    grid, w, h = input

    total = 0
    for x in range(w):
        for y in range(h):
            val = grid[x][y]
            if val == "A":
                if 0 < x < w - 1 and 0 < y < h - 1:
                    (ul, ur, bl, br) = (grid[x - 1][y - 1], grid[x - 1][y + 1], grid[x + 1][y - 1], grid[x + 1][y + 1])

                    if ul == ur and bl == br and ul in "MS" and bl in "MS" and ul != bl:
                        total += 1
                    elif ur == br and ul == bl and ul in "MS" and ur in "MS" and ul != ur:
                        total += 1
    return total


def parse(data: str):
    lines = util.as_grid(data)
    return lines


def main():
    data: str = util.get(4, 2024)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
