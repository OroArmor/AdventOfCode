import util
from util import *

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
            if grid[x][y] == "X":
                for (dx, dy) in adjacent_directions():
                    if 3 < x < w - 3 and 3 < y < h - 3:
                        if grid[x + dx][y + dy] == "M" and grid[x + 2 * dx][y + 2 * dy] == "A" and grid[x + 3 * dx][y + 3 * dy] == "S":
                            total += 1
                    elif 0 <= x + dx < w and 0 <= y + dy < h and grid[x + 1 * dx][y + 1 * dy] == "M":
                        if 0 <= x + 2 * dx < w and 0 <= y + 2 * dy < h and grid[x + 2 * dx][y + 2 * dy] == "A":
                            if 0 <= x + 3 * dx < w and 0 <= y + 3 * dy < h and grid[x + 3 * dx][y + 3 * dy] == "S":
                                total += 1
    return total


def task2(input):
    grid, w, h = input

    total = 0
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            if grid[x][y] == "A":
                ul = grid[x - 1][y - 1]
                br = grid[x + 1][y + 1]

                if (ul == "M" or ul == "S") and (br == "M" or br == "S") and ul != br:
                    ur = grid[x - 1][y + 1]
                    bl = grid[x + 1][y - 1]
                    if ul == ur and bl == br or ur == br and ul == bl:
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
