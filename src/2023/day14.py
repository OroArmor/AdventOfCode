import util

test_data: str = \
    """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""


def roll_north(blocks, walls, size):
    new_blocks = set()
    for (x, y) in blocks:
        while (x, y) in new_blocks:
            y += 1
        while ((x, y) not in walls) and ((x, y) not in new_blocks) and (y > -1):
            y -= 1
        new_blocks.add((x, y + 1))
    return new_blocks


def roll_south(blocks, walls, size):
    new_blocks = set()
    for (x, y) in blocks:
        while (x, y) in new_blocks:
            y -= 1
        while ((x, y) not in walls) and ((x, y) not in new_blocks) and (y < size[1]):
            y += 1
        new_blocks.add((x, y - 1))
    return new_blocks


def roll_west(blocks, walls, size):
    new_blocks = set()
    for (x, y) in blocks:
        while (x, y) in new_blocks:
            x += 1
        while ((x, y) not in walls) and ((x, y) not in new_blocks) and (x > -1):
            x -= 1
        new_blocks.add((x + 1, y))
    return new_blocks


def roll_east(blocks, walls, size):
    new_blocks = set()
    for (x, y) in blocks:
        while (x, y) in new_blocks:
            x -= 1
        while ((x, y) not in walls) and ((x, y) not in new_blocks) and (x < size[0]):
            x += 1
        new_blocks.add((x - 1, y))
    return new_blocks


def print_grid(walls, blocks, size):
    for y in range(size[1]):
        for x in range(size[0]):
            print(" " + ("#" if (x, y) in walls else "O" if (x, y) in blocks else "."), end="")
        print()


def task1(input):
    size, walls, blocks = input
    blocks = roll_north(blocks, walls, size)
    return sum([size[1] - block[1] for block in blocks])


def task2(input):
    size, walls, blocks = input

    # blocks -> turn
    seen = {}
    t = 0
    while True:
        blocks = roll_north(blocks, walls, size)
        blocks = roll_west(blocks, walls, size)
        blocks = roll_south(blocks, walls, size)
        blocks = roll_east(blocks, walls, size)
        t += 1

        vals = tuple(sorted(blocks))
        if vals in seen:
            break

        seen[vals] = t

    correct = int((1000000000 - seen[vals]) % (t - seen[vals]) + seen[vals])
    for val in seen:
        if seen[val] == correct:
            return sum([size[1] - block[1] for block in val])


def parse(data: str):
    lines = util.as_lines(data)

    size = (len(lines[0]), len(lines))
    blocks = set()
    walls = set()

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                walls.add((x, y))
            if c == "O":
                blocks.add((x, y))

    return size, walls, blocks


def main():
    data: str = util.get(14, 2023)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
