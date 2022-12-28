import collections
import re
import util
import numpy as np

test_data: str = \
    """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""


def task1(input):
    grid, instructions, start = input
    pos = start.copy()
    direction = np.array([1, 0])

    turn_right = {
        (1, 0): (0, 1),
        (-1, 0): (0, -1),
        (0, 1): (-1, 0),
        (0, -1): (1, 0)
    }
    turn_left = {
        (1, 0): (0, -1),
        (-1, 0): (0, 1),
        (0, 1): (1, 0),
        (0, -1): (-1, 0)
    }
    facing = {
        (1, 0): 0,
        (0, 1): 1,
        (-1, 0): 2,
        (0, -1): 3
    }

    for instruction in instructions:
        if type(instruction) == str:
            if instruction == "R":
                direction = np.array(turn_right[tuple(direction)])
            else:
                direction = np.array(turn_left[tuple(direction)])
        else:
            for steps in range(instruction):
                start_step = pos.copy()
                pos[2:] += direction
                if pos[2] < 0:
                    for gx in range(pos[0] - 1, pos[0] - len(grid) - 2, -1):
                        if grid[gx % len(grid), pos[1], 0, 0] != -1:
                            pos[0] = gx % len(grid)
                            pos[2] = grid.shape[2] - 1
                            break
                elif pos[2] >= grid.shape[2]:
                    for gx in range(pos[0] + 1, pos[0] + len(grid) + 1):
                        if grid[gx % len(grid), pos[1], 0, 0] != -1:
                            pos[0] = gx % len(grid)
                            pos[2] = 0
                            break
                elif pos[3] < 0:
                    for gy in range(pos[1] - 1, pos[1] - len(grid[0]) - 2, -1):
                        if grid[pos[0], gy % len(grid[0]), 0, 0] != -1:
                            pos[1] = gy % len(grid[0])
                            pos[3] = grid.shape[3] - 1
                            break
                elif pos[3] >= grid.shape[3]:
                    for gy in range(pos[1] + 1, pos[1] + len(grid[0]) + 1):
                        if grid[pos[0], gy % len(grid[0]), 0, 0] != -1:
                            pos[1] = gy % len(grid[0])
                            pos[3] = 0
                            break

                if grid[pos[0], pos[1], pos[2], pos[3]] == 1:
                    pos = start_step
                    break

    # for y in range(grid.shape[1] * grid.shape[3]):
    #     for x in range(grid.shape[0] * grid.shape[2]):
    #         val = grid[x // grid.shape[2], y // grid.shape[3], x % grid.shape[2], y % grid.shape[3]]
    #         if val == -1:
    #             print(" ", end="")
    #         elif val == 0:
    #             print(".", end="")
    #         elif val == 1:
    #             print("#", end="")
    #         elif val == 2:
    #             print(">", end="")
    #         elif val == 3:
    #             print("v", end="")
    #         elif val == 4:
    #             print("<", end="")
    #         elif val == 5:
    #             print("^", end="")
    #     print()

    return (pos[1] * grid.shape[3] + pos[3] + 1) * 1000 + (pos[0] * grid.shape[2] + pos[2] + 1) * 4 + facing[tuple(direction)]


def task2(input):
    grid, instructions, start = input
    pos = start.copy()
    direction = np.array([1, 0])

    turn_right = {
        (1, 0): (0, 1),
        (-1, 0): (0, -1),
        (0, 1): (-1, 0),
        (0, -1): (1, 0)
    }
    turn_left = {
        (1, 0): (0, -1),
        (-1, 0): (0, 1),
        (0, 1): (1, 0),
        (0, -1): (-1, 0)
    }
    facing = {
        (1, 0): 0,  # right
        (0, 1): 1,  # down
        (-1, 0): 2,  # left
        (0, -1): 3  # up
    }

    if len(instructions) == 13:  # test data
        changes = {
            ((2, 0), 1): lambda pos: (np.array([2, 1, pos[2], 0]), np.array([0, 1])),
            ((0, 1), 0): lambda pos: (np.array([1, 1, 0, pos[3]]), np.array([1, 0])),
            ((2, 1), 0): lambda pos: (np.array([3, 2, 3 - pos[3], 0]), np.array([0, 1])),
            ((3, 2), 2): lambda pos: (np.array([2, 2, 3, pos[3]]), np.array([-1, 0])),
            ((2, 2), 1): lambda pos: (np.array([0, 1, 3 - pos[2], 3]), np.array([0, -1])),
            ((1, 1), 3): lambda pos: (np.array([2, 0, 0, pos[2]]), np.array([0, -1]))
        }
    else:
        #  12
        #  3
        # 45
        # 6
        changes = {
            ((1, 0), 0): lambda pos: (np.array([2, 0, 0, pos[3]]), np.array([1, 0])),  # 1 -> 2
            ((1, 0), 1): lambda pos: (np.array([1, 1, pos[2], 0]), np.array([0, 1])),  # 1 -> 3
            ((1, 0), 2): lambda pos: (np.array([0, 2, 0, 49 - pos[3]]), np.array([1, 0])),  # 1 -> 4
            ((1, 0), 3): lambda pos: (np.array([0, 3, 0, pos[2]]), np.array([1, 0])),  # 1 -> 6

            ((2, 0), 0): lambda pos: (np.array([1, 2, 49, 49 - pos[3]]), np.array([-1, 0])),  # 2 -> 5
            ((2, 0), 1): lambda pos: (np.array([1, 1, 49, pos[2]]), np.array([-1, 0])),  # 2 -> 3
            ((2, 0), 2): lambda pos: (np.array([1, 0, 49, pos[3]]), np.array([-1, 0])),  # 2 -> 1
            ((2, 0), 3): lambda pos: (np.array([0, 3, pos[2], 49]), np.array([0, -1])),  # 2 -> 6

            ((1, 1), 0): lambda pos: (np.array([2, 0, pos[3], 49]), np.array([0, -1])),  # 3 -> 2
            ((1, 1), 1): lambda pos: (np.array([1, 2, pos[2], 0]), np.array([0, 1])),  # 3 -> 5
            ((1, 1), 2): lambda pos: (np.array([0, 2, pos[3], 0]), np.array([0, 1])),  # 3 -> 4
            ((1, 1), 3): lambda pos: (np.array([1, 0, pos[2], 49]), np.array([0, -1])),  # 3 -> 1

            ((0, 2), 0): lambda pos: (np.array([1, 2, 0, pos[3]]), np.array([1, 0])),  # 4 -> 5
            ((0, 2), 1): lambda pos: (np.array([0, 3, pos[2], 0]), np.array([0, 1])),  # 4 -> 6
            ((0, 2), 2): lambda pos: (np.array([1, 0, 0, 49 - pos[3]]), np.array([1, 0])),  # 4 -> 1
            ((0, 2), 3): lambda pos: (np.array([1, 1, 0, pos[2]]), np.array([1, 0])),  # 4 -> 3

            ((1, 2), 0): lambda pos: (np.array([2, 0, 49, 49 - pos[3]]), np.array([-1, 0])),  # 5 -> 2
            ((1, 2), 1): lambda pos: (np.array([0, 3, 49, pos[2]]), np.array([-1, 0])),  # 5 -> 6
            ((1, 2), 2): lambda pos: (np.array([0, 2, 49, pos[3]]), np.array([-1, 0])),  # 5 -> 4
            ((1, 2), 3): lambda pos: (np.array([1, 1, pos[2], 49]), np.array([0, -1])),  # 5 -> 3

            ((0, 3), 0): lambda pos: (np.array([1, 2, pos[3], 49]), np.array([0, -1])),  # 6 -> 5
            ((0, 3), 1): lambda pos: (np.array([2, 0, pos[2], 0]), np.array([0, 1])),  # 6 -> 2
            ((0, 3), 2): lambda pos: (np.array([1, 0, pos[3], 0]), np.array([0, 1])),  # 6 -> 1
            ((0, 3), 3): lambda pos: (np.array([0, 2, pos[2], 49]), np.array([0, -1])),  # 6 -> 4
        }

    for instruction in instructions:
        if type(instruction) == str:
            if instruction == "R":
                direction = np.array(turn_right[tuple(direction)])
            else:
                direction = np.array(turn_left[tuple(direction)])
        else:
            for steps in range(instruction):
                grid[pos[0], pos[1], pos[2], pos[3]] = facing[tuple(direction)] + 2
                start_step = pos.copy()
                start_direction = direction.copy()
                pos[2:] += direction
                change_tuple = (tuple(pos[0:2]), facing[tuple(direction)])
                if pos[2] < 0 or pos[2] >= grid.shape[2] or pos[3] < 0 or pos[3] >= grid.shape[3]:
                    pos, direction = changes[change_tuple](pos)

                if grid[pos[0], pos[1], pos[2], pos[3]] == 1:
                    pos = start_step
                    direction = start_direction
                    break

    # for y in range(grid.shape[1] * grid.shape[3]):
    #     for x in range(grid.shape[0] * grid.shape[2]):
    #         val = grid[x // grid.shape[2], y // grid.shape[3], x % grid.shape[2], y % grid.shape[3]]
    #         if val == -1:
    #             print(" ", end="")
    #         elif val == 0:
    #             print(".", end="")
    #         elif val == 1:
    #             print("#", end="")
    #         elif val == 2:
    #             print(">", end="")
    #         elif val == 3:
    #             print("v", end="")
    #         elif val == 4:
    #             print("<", end="")
    #         elif val == 5:
    #             print("^", end="")
    #     print()
    # print()

    return (pos[1] * grid.shape[3] + pos[3] + 1) * 1000 + (pos[0] * grid.shape[2] + pos[2] + 1) * 4 + facing[tuple(direction)]


def parse(data: str):
    lines = util.as_double_lines(data)

    grid_lines = lines[0].split("\n")
    height = len(grid_lines)
    width = max(map(lambda s: len(s), grid_lines))
    block_size = np.gcd(width, height)
    grid = np.zeros((width // block_size, height // block_size, block_size, block_size), dtype=int)

    start = np.array([100, 0, 0, 0])

    for gy in range(height // block_size):
        for gx in range(width // block_size):
            if len(grid_lines[gy * block_size]) <= gx * block_size or grid_lines[gy * block_size][gx * block_size] == " ":
                grid[gx, gy, :, :] = -1
            else:
                if gy == 0:
                    start[0] = min(start[0], gx)
                for y in range(block_size):
                    for x in range(block_size):
                        if grid_lines[gy * block_size + y][gx * block_size + x] == "#":
                            grid[gx, gy, x, y] = 1

    instructions = re.findall("\\d+|[RL]", lines[1])

    instructions = list(map(lambda s: int(s) if s.isdigit() else s, instructions))

    return grid, instructions, start


def main():
    data: str = util.get(22, 2022)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
