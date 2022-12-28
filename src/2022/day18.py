import timeit

import util
import numpy as np

test_data: str = \
    """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""

directions = np.array([
    [1, 0, 0],
    [-1, 0, 0],
    [0, 1, 0],
    [0, -1, 0],
    [0, 0, 1],
    [0, 0, -1]
])


def task1(input):
    points, grid = input

    total_faces = 0

    for point in points:
        for direction in directions:
            offset = point + direction
            if 0 <= offset[0] < grid.shape[0] and 0 <= offset[1] < grid.shape[1] and 0 <= offset[2] < grid.shape[2]:
                if grid[offset[0], offset[1], offset[2]] != 1:
                    total_faces += 1

    return total_faces


def task2(input):
    points, grid = input

    total_faces = 0
    for point in points:
        for direction in directions:
            offset = point + direction
            if 0 <= offset[0] < grid.shape[0] and 0 <= offset[1] < grid.shape[1] and 0 <= offset[2] < grid.shape[2]:
                if grid[offset[0], offset[1], offset[2]] == 2:
                    total_faces += 1

    return total_faces


def parse(data: str):
    lines = util.as_lines(data)

    points = np.array([np.array(util.as_csv_of_ints(line)) for line in lines])

    max_vals = np.max(points, axis=0)
    max_vals += 3

    grid = np.zeros(max_vals)

    points += 1
    for point in points:
        grid[point[0], point[1], point[2]] = 1

    points_to_fill = [np.array([0, 0, 0])]

    while len(points_to_fill) != 0:
        next_pts = []
        for point in points_to_fill:
            for direction in directions:
                offset = point + direction
                if 0 <= offset[0] < grid.shape[0] and 0 <= offset[1] < grid.shape[1] and 0 <= offset[2] < grid.shape[2]:
                    if grid[offset[0], offset[1], offset[2]] == 0:
                        next_pts.append(offset)
                        grid[offset[0], offset[1], offset[2]] = 2
        points_to_fill = next_pts

    return points, grid


def main():
    data: str = util.get(18, 2022)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
