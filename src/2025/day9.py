import util
from util import *
import numpy as np

test_data: str = \
    """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

P1 = None


def task1(input):
    global P1
    I, J = np.triu_indices(len(input), k=2)
    areas = np.multiply.reduce(
        np.abs(
            input[I] - input[J]
        )
        +
        np.array([1, 1]),
        axis=1
    )
    P1 = areas, I, J
    return np.max(areas)


def task2(input):
    areas, I, J = P1
    min = np.min([input[I], input[J]], axis=0)
    max = np.max([input[I], input[J]], axis=0)

    valid = np.ones_like(I, dtype=bool)

    px = input[:, 0]
    py = input[:, 1]

    minx = min[:, 0]
    maxx = max[:, 0]
    miny = min[:, 1]
    maxy = max[:, 1]

    tmp = px > minx[:, None]
    np.bitwise_and(tmp, px < maxx[:, None], out=tmp)
    inline_x = tmp

    tmp = py > miny[:, None]
    np.bitwise_and(tmp, py < maxy[:, None], out=tmp)
    inline_y = tmp

    # Remove rects with a corner in the middle
    valid &= np.logical_not(
        np.logical_or.reduce(
            np.logical_and(
                inline_x,
                inline_y
            ),
            axis=1
        )
    )

    lines = np.stack([input, np.roll(input, -1, axis=0)])
    vert = lines[0, :, 0] == lines[1, :, 0]
    hor = lines[0, :, 1] == lines[1, :, 1]

    lines_y = np.sort(lines[:, hor, 0], axis=0)
    lines_x = np.sort(lines[:, vert, 1], axis=0)

    # Remove lines that cross horizontally
    bad_hor = np.any(
        np.logical_and(
            inline_y[:, hor, None],
            np.logical_and(
                lines_y[0, :, None] <= min[:, None, None, 0],
                lines_y[1, :, None] >= max[:, None, None, 0],
            )
        ),
        axis=(1, 2),
    )
    valid &= np.logical_not(bad_hor)

    # Remove lines that cross vertically
    bad_vert = np.any(
        np.logical_and(
            inline_x[:, vert, None],
            np.logical_and(
                lines_x[0, :, None] <= min[:, None, None, 1],
                lines_x[1, :, None] >= max[:, None, None, 1],
            )
        ),
        axis=(1, 2),
    )
    valid &= np.logical_not(bad_vert)

    return np.max(areas[valid])


def parse(data: str):
    lines = util.as_csv_lines_of_ints(data)
    return np.array(lines, dtype=int)


def main():
    data: str = util.get(9, 2025)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
