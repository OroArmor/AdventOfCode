import os
import re
import util
import numpy as np
from PIL import Image

test_data: str = \
    """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

VISUALIZATION = False

def save_grid(grid, p2, i):
    img = np.zeros((len(grid), len(grid[0]), 3), dtype="uint8")
    img[grid == 1, :] = [255, 255, 255]
    img[grid == 2, :] = [255, 255, 0]

    image = Image.fromarray(img, mode="RGB")
    image.save(f"visualization/day14/part{2 if p2 else 1}/frame_{i}.png")


def task1(input):
    grid = input[0].copy()

    start = np.array([0, 500])
    pos = start.copy()
    down = np.array([1, 0])
    left = np.array([1, -1])
    right = np.array([1, 1])

    while True:
        if grid[(pos + down)[0], (pos + down)[1]] == 0:
            pos += down
            if pos[0] == input[1] + 1:
                return (grid == 2).sum()
        elif grid[(pos + left)[0], (pos + left)[1]] == 0:
            pos += left
        elif grid[(pos + right)[0], (pos + right)[1]] == 0:
            pos += right
        else:
            grid[pos[0], pos[1]] = 2
            pos = start.copy()
            if VISUALIZATION:
                save_grid(grid, False, (grid == 2).sum())


def task2(input):
    grid: np.ndarray = input[0].copy()
    max_y = input[1]

    grid[max_y + 2] = 1

    start = np.array([0, 500])
    pos = start.copy()

    down = np.array([1, 0])
    left = np.array([1, -1])
    right = np.array([1, 1])

    while grid[start[0], start[1]] != 2:
        if grid[(pos + down)[0], (pos + down)[1]] == 0:
            pos += down
        elif grid[(pos + left)[0], (pos + left)[1]] == 0:
            pos += left
        elif grid[(pos + right)[0], (pos + right)[1]] == 0:
            pos += right
        else:
            grid[pos[0], pos[1]] = 2
            pos = start.copy()
            if VISUALIZATION:
                save_grid(grid, True, (grid == 2).sum())

    return (grid == 2).sum()


def parse(data: str):
    lines = util.as_lines(data)
    list_points: [int] = list(map(lambda l: util.list_as_ints(re.findall("\\d+", l)), lines))

    grid = np.zeros((200, 800))

    max_y = 0
    for points in list_points:
        for i in range(0, len(points) - 2, 2):
            max_y = max(max_y, points[i+1], points[i+3])

            if points[i] == points[i + 2]:
                grid[min(points[i+1], points[i+3]):max(points[i+1], points[i+3]) + 1, points[i]] = 1
            else:
                grid[points[i + 1], min(points[i], points[i+2]):max(points[i], points[i+2]) + 1] = 1

    return grid, max_y


def main():
    if VISUALIZATION:
        os.makedirs("./visualization/day14/part1", exist_ok=True)
        os.makedirs("./visualization/day14/part2", exist_ok=True)

    data: str = util.get(14, 2022)
    # data = test_data
    input = parse(data)
    # p1 = task1(input)
    # p2 = task2(input)

    p1 = 799
    p2 = 29076

    print(p1)
    print(p2)

    if VISUALIZATION:
        imgs = [Image.open(f"./visualization/day14/part1/frame_{img_id}.png") for img_id in range(1, p1 + 1, 10)]
        imgs[0].save(f"./visualization/day14/part1.gif", save_all=True, append_images=imgs[1:], duration=1, loop=0)

        imgs = []
        for img_id in range(1, p2 + 1, 100):
            img = Image.open(f"./visualization/day14/part2/frame_{img_id}.png")
            img.load()
            imgs.append(img)
        imgs[0].save(f"./visualization/day14/part2.gif", save_all=True, append_images=imgs[1:], duration=1, loop=0)


if __name__ == "__main__":
    main()
