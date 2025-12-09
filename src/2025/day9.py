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
    bot, top = len(input) // 2, len(input) // 2 + 1
    if input[top][1] < input[bot][1]:
        top, bot = bot, top

    top_max_y, bot_min_y = input[top][1], input[bot][1]
    for a, b in itertools.pairwise(input[:top]):
        if a[0] == b[0] and a[0] == input[top][0]: # vertical line
            top_max_y = max(a[1], b[1])
            break
        elif a[0] <= input[top][0] <= b[0] or a[0] >= input[top][0] >= b[0]: # horizontal line
            top_max_y = a[1]
            break
    for a, b in itertools.pairwise(reversed(input[bot:])):
        if a[0] == b[0] and a[0] == input[bot][0]: # vertical line
            bot_min_y = max(a[1], b[1])
            break
        elif a[0] <= input[bot][0] <= b[0] or a[0] >= input[bot][0] >= b[0]:
            bot_min_y = a[1]
            break

    max_area = 0
    best_pair = None
    top_x, bot_x = 0, 0
    for i, point in enumerate(input[bot:]):
        if bot_min_y <= point[1] <= input[bot][1] and bot_x <= point[0]:
            bot_x = point[0]
            s = np.multiply.reduce(np.abs(input[bot] - point) + 1)
            if s > max_area:
                best_pair = (i + bot, bot)
                max_area = s
    for i, point in enumerate(reversed(input[:top])):
        if point[1] <= top_max_y and top_x <= point[0]:
            top_x = point[0]
            s = np.multiply.reduce(np.abs(input[top] - point) + 1)
            if s > max_area:
                best_pair = (top - i - 1, top)
                max_area = s

    if not numpy_valid_areas(input, np.array((best_pair[0], )).reshape(1), np.array((best_pair[1], )).reshape(1))[0]:
        print("Found incorrect answer - improve solution")
        areas, I, J = P1
        valid = numpy_valid_areas(input, I, J)
        return np.max(areas[valid])

    return max_area


def numpy_valid_areas(input, I, J):
    # areas, I, J = P1
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
    return valid


def parse(data: str):
    lines = util.as_csv_lines_of_ints(data)
    return np.array(lines, dtype=int)


def main():
    data: str = util.get(9, 2025)
    data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
