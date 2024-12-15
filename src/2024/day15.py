from collections import deque
from copy import deepcopy

import util
from util import *
import numpy as np

test_data: str = \
    """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

# test_data = """#######
# #...#.#
# #.....#
# #..OO@#
# #..O..#
# #.....#
# #######
#
# v<<^vvvvvv<<<<<<<^^^^^^^^^>>>>>>>vvvvv"""


def task1(input):
    start, boxes, walls, path = input

    for step in path:
        direction = None
        match step:
            case "v":
                direction = Direction.UP
            case "^":
                direction = Direction.DOWN
            case "<":
                direction = Direction.LEFT
            case ">":
                direction = Direction.RIGHT

        if start + direction in walls:
            continue

        box = start + direction
        while box in boxes:
            box = box + direction

        if box in walls:
            continue

        boxes.add(box)
        start += direction
        boxes.remove(start)

    return sum(100 * p.y + p.x for p in boxes)


def task2(input):
    start, boxes, walls, path = input
    start = Point(start.x * 2, start.y)
    boxes = set((Point(2 * b.x, b.y) for b in boxes))

    def is_box(pt: Point) -> Tuple[bool, Point]:
        if pt in boxes:
            return True, pt
        elif pt + Direction.LEFT in boxes:
            return True, pt + Direction.LEFT
        return False, None

    new_walls = set()
    for w in walls:
        new_walls.add(Point(w.x * 2, w.y))
        new_walls.add(Point(w.x * 2 + 1, w.y))
    walls = new_walls

    # print("Initial state:")
    for step in path:
        # for y in range(10):
        #     for x in range(20):
        #         if Point(x, y) in boxes:
        #             print("[]", end="")
        #         elif Point(x, y) in walls:
        #             print("#", end = "")
        #         elif start == Point(x, y):
        #             print("@", end = "")
        #         elif not is_box(Point(x, y))[0]:
        #             print(".", end="")
        #     print()
        # print("\n")

        direction = None
        match step:
            case "v":
                direction = Direction.UP
            case "^":
                direction = Direction.DOWN
            case "<":
                direction = Direction.LEFT
            case ">":
                direction = Direction.RIGHT

        # print(f"Move {step}:")
        if start + direction in walls:
            continue

        to_move = set()
        to_check = deque()
        to_check.append(start + direction)

        while len(to_check) > 0:
            # print(to_check)
            maybe = to_check.popleft()
            if maybe in walls:
                break

            there, box = is_box(maybe)
            if there:
                to_move.add(box)
                if step == "v" or step == "^":
                    to_check.append(box + direction)
                    to_check.append(box + direction + Point(1, 0))
                elif step == "<":
                    to_check.append(box + direction)
                else:
                    to_check.append(box + direction * 2)
        else:
            # print(to_move)
            for move in to_move:
                boxes.remove(move)
            for move in to_move:
                boxes.add(move + direction)
            start += direction

    # for y in range(10):
    #     for x in range(20):
    #         if Point(x, y) in boxes:
    #             print("[]", end="")
    #         elif Point(x, y) in walls:
    #             print("#", end = "")
    #         elif start == Point(x, y):
    #             print("@", end = "")
    #         elif not is_box(Point(x, y))[0]:
    #             print(".", end="")
    #     print()

    return sum(100 * p.y + p.x for p in boxes)


def parse(data: str):
    g, p = util.as_double_lines(data)

    raw, w, h = util.as_grid(g)

    walls = set()
    boxes = set()
    start = None

    for y in range(h):
        for x in range(w):
            if raw[y][x] == "@":
                start = Point(x, y)
            elif raw[y][x] == "#":
                walls.add(Point(x, y))
            elif raw[y][x] == "O":
                boxes.add(Point(x, y))

    path = p.replace("\n", "")

    return start, boxes, walls, path


def main():
    data: str = util.get(15, 2024)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(deepcopy(input)))
    print(task2(deepcopy(input)))


if __name__ == "__main__":
    main()
