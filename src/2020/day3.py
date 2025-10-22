import util
from util import as_lines, get

test_data: [str] = \
    """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".split("\n")


def task1(data: [str]):
    x, y = 0, 0
    total = 0
    while y < len(data):
        if data[y][x] == '#':
            total += 1

        x += 3
        x %= len(data[y])
        y += 1
    return total


def task2(data: [str]):
    prod = 1
    for (mx, my) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        x, y = 0, 0
        total = 0
        while y < len(data):
            if data[y][x] == '#':
                total += 1

            x += mx
            x %= len(data[y])
            y += my
        prod *= total
    return prod

def parse(data):
    return as_lines(data)


def main():
    data: [str] = get(3, 2020)
    # data = test_data
    data = parse(data)
    print(task1(data))
    print(task2(data))


if __name__ == "__main__":
    main()
