import util

from util import area

test_data: str = \
    """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""


def task1(input):
    current = (0, 0)
    points = [current]

    for d, l, _ in input:
        match d:
            case "U":
                current = (current[0], current[1] - l)
            case "D":
                current = (current[0], current[1] + l)
            case "R":
                current = (current[0] + l, current[1])
            case "L":
                current = (current[0] - l, current[1])

        points.append(current)

    return area(points, True)


def task2(input):
    current = (0, 0)
    points = [current]

    for _d, _l, c in input:
        l, d = int(c[2:-2], 16), c[-2]

        match d:
            case "3":
                current = (current[0], current[1] - l)
            case "1":
                current = (current[0], current[1] + l)
            case "0":
                current = (current[0] + l, current[1])
            case "2":
                current = (current[0] - l, current[1])
        points.append(current)

    return area(points, True)


def parse(data: str):
    lines = util.as_lines(data)

    lines2 = []
    for line in lines:
        d, l, c = line.split()
        lines2.append([d, int(l), c])
    return lines2


def main():
    data: str = util.get(18, 2023)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
