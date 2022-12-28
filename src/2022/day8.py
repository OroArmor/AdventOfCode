import util
import numpy as np

test_data: str = \
    """30373
25512
65332
33549
35390"""


def task1(input):
    visible: np.ndarray = np.zeros((len(input) - 2, len(input) - 2), dtype=int)

    for x in range(len(visible)):
        for y in range(len(visible[0])):
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for dir in dirs:
                pos = [x + 1, y + 1]
                shorter = True
                while 0 < pos[0] < len(input) - 1 and 0 < pos[1] < len(input) - 1:
                    pos = [pos[0] + dir[0], pos[1] + dir[1]]
                    if input[pos[0], pos[1]] >= input[x + 1, y + 1]:
                        shorter = False
                        break

                if shorter:
                    visible[x, y] = 1

    return visible.sum() + 4 * (len(input) - 1)


def task2(input):
    visible: np.ndarray = np.ones((len(input) - 2, len(input) - 2), dtype=int)

    for x in range(len(visible)):
        for y in range(len(visible[0])):
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for dir in dirs:
                pos = [x + 1, y + 1]
                vis = 0
                while 0 < pos[0] < len(input) - 1 and 0 < pos[1] < len(input) - 1:
                    pos = [pos[0] + dir[0], pos[1] + dir[1]]
                    vis += 1
                    if input[pos[0], pos[1]] >= input[x + 1, y + 1]:
                        break

                visible[x, y] *= vis

    return visible.max()

def parse(input: [str]) -> np.ndarray:
    grid = np.zeros((len(input), len(input)), dtype=int)

    for i, line in enumerate(input):
        for j, c in enumerate(line):
            grid[i, j] = int(c)
    return grid


def main():
    data: str = util.get(8, 2022)
    # data = test_data
    input = util.as_lines(data)
    input = parse(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
