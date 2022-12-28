import collections
import util
import numpy as np

test_data: str = \
    """....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#.."""


class Elf:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.order = [0, 1, 2, 3]


def pt_open(x, y, grid):
    return (x, y) not in grid.keys()


def search(x, y, grid):
    all_open = True
    for xs in range(-1, 2):
        for ys in range(-1, 2):
            if xs == 0 and ys == 0:
                continue
            all_open &= pt_open(x + xs, y + ys, grid)

    if all_open:
        return (x, y), True

    elf = grid[(x, y)]

    for direction in elf.order:
        if direction == 0 and pt_open(x, y - 1, grid) and pt_open(x - 1, y - 1, grid) and pt_open(x + 1, y - 1, grid):  # north
            return (x, y - 1), False
        if direction == 1 and pt_open(x, y + 1, grid) and pt_open(x - 1, y + 1, grid) and pt_open(x + 1, y + 1, grid):  # south
            return (x, y + 1), False
        if direction == 2 and pt_open(x - 1, y, grid) and pt_open(x - 1, y - 1, grid) and pt_open(x - 1, y + 1, grid):  # west
            return (x - 1, y), False
        if direction == 3 and pt_open(x + 1, y, grid) and pt_open(x + 1, y - 1, grid) and pt_open(x + 1, y + 1, grid):  # east
            return (x + 1, y), False

    return (x, y), False


def update_order(elf):
    elf.order.append(elf.order.pop(0))


def task1(input):
    elves = input
    for i in range(10):
        proposed = collections.defaultdict(lambda: 0)

        for elf in elves.values():
            proposed[search(elf.x, elf.y, elves)[0]] += 1

        new_elves = {}
        for elf in elves.values():
            movement = search(elf.x, elf.y, elves)
            update_order(elf)
            if proposed[movement[0]] == 1:
                elf.x = movement[0][0]
                elf.y = movement[0][1]
            new_elves[(elf.x, elf.y)] = elf

        elves = new_elves

    min_x, min_y, max_x, max_y = 0, 0, 0, 0

    for elf in elves.keys():
        min_x = min(min_x, elf[0])
        max_x = max(max_x, elf[0])
        min_y = min(min_y, elf[1])
        max_y = max(max_y, elf[1])

    return (max_x - min_x + 1) * (max_y - min_y + 1) - len(elves)


def task2(input):
    elves = input
    i = 0
    while True:
        proposed = collections.defaultdict(lambda: 0)

        for elf in elves.values():
            proposed[search(elf.x, elf.y, elves)[0]] += 1

        new_elves = {}
        none_move = True
        for elf in elves.values():
            movement = search(elf.x, elf.y, elves)
            update_order(elf)
            none_move &= movement[1]
            if proposed[movement[0]] == 1:
                elf.x = movement[0][0]
                elf.y = movement[0][1]
            new_elves[(elf.x, elf.y)] = elf

        i += 1
        elves = new_elves

        if none_move:
            return i


def parse(data: str):
    lines = util.as_lines(data)

    elves = {}

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                elves[(x, y)] = Elf(x, y)

    return elves


def main():
    data: str = util.get(23, 2022)
    # data = test_data
    input = parse(data)
    print(task1(input))
    input = parse(data)
    print(task2(input))


if __name__ == "__main__":
    main()
