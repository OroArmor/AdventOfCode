import util
import numpy as np

test_data: str = \
    """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


def search(grid, start, target):
    steps_to_reach = np.zeros_like(grid)

    current_pos = [start]

    while True:
        new_poses = []
        for pos in current_pos:
            steps = steps_to_reach[pos[0], pos[1]]
            height = grid[pos[0], pos[1]]

            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dir in dirs:
                new_pos = [pos[0] + dir[0], pos[1] + dir[1]]
                if (0 <= new_pos[0] < len(grid)) and (0 <= new_pos[1] < len(grid[0])) and new_pos not in new_poses:
                    height2 = grid[new_pos[0], new_pos[1]]
                    steps2 = steps_to_reach[new_pos[0], new_pos[1]]

                    if (height - height2 >= -1) and steps2 == 0:
                        if type(target) == int and height2 == target or type(target) == list and new_pos == target:
                            return steps + 1
                        steps_to_reach[new_pos[0], new_pos[1]] = steps + 1
                        new_poses.append(new_pos)
        current_pos = new_poses


def task1(input):
    return search(input[0], list(input[1]), list(input[2]))


def task2(input):
    return search(28 - input[0], list(input[2]), 27)


def parse(data: str):
    lines = util.as_lines(data)
    s = None
    e = None
    grid = np.zeros((len(lines), len(lines[0])), dtype=int)

    for i, l in enumerate(lines):
        for j, c in enumerate(l):
            if c == "S":
                s = (i, j)
                grid[i, j] = 1
            elif c == "E":
                e = (i, j)
                grid[i, j] = 27
            else:
                grid[i, j] = ord(c) - ord('a') + 1

    return grid, s, e


def main():
    data: str = util.get(12, 2022)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
