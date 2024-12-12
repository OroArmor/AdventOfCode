import itertools
from collections import defaultdict

import util
from util import *
import numpy as np

test_data: str = """2333133121414131402"""

def s(n: int) -> int:
    return (n * (n - 1)) // 2

def checksum(vals: dict[int, set[Tuple[int, int]]]) -> int:
    check = 0
    for n, poses in vals.items():
        for pos in poses:
            check += (s(pos[0] + pos[1]) - s(pos[0])) * n

    return check

def task1(input):
    vals = defaultdict(set)

    current_pos = 0
    front_i = 0
    back_i = len(input) - 1
    back = input[back_i]
    while front_i < back_i:
        vals[front_i].add((current_pos, input[front_i][0]))
        current_pos += input[front_i][0]

        empty = input[front_i][1]
        while back[0] < empty:
            empty -= back[0]
            vals[back_i].add((current_pos, back[0]))
            current_pos += back[0]
            back = (0, back[1])
            back_i -= 1
            if front_i == back_i:
                break
            back = input[back_i]
        else:
            vals[back_i].add((current_pos, empty))
            back = (back[0] - empty, back[1])
            current_pos += empty
            front_i += 1
    if back[0] != 0:
        vals[back_i].add((current_pos, back[0]))
        current_pos += back[0]

    return checksum(vals)


def task2(input):
    vals = defaultdict(set)

    current_pos = 0
    front_i = 0
    moved = set()
    moved_gt = len(input) - 1
    while front_i < moved_gt + 1:
        if front_i not in moved:
            vals[front_i].add((current_pos, input[front_i][0]))
        current_pos += input[front_i][0]
        empty = input[front_i][1]

        for back_i in range(moved_gt, front_i, -1):
            if back_i not in moved:
                if input[back_i][0] <= empty:
                    vals[back_i].add((current_pos, input[back_i][0]))
                    empty -= input[back_i][0]
                    current_pos += input[back_i][0]
                    moved.add(back_i)
                    if empty == 0:
                        break
        while moved_gt in moved:
            moved.remove(moved_gt)
            moved_gt -= 1
        current_pos += empty
        front_i += 1

    return checksum(vals)


def parse(data: str):
    sizes = []
    for i in range(0, len(data), 2):
        if i == len(data) - 1:
            sizes.append((int(data[i]), 0))
            break
        v = data[i:i + 2]
        sizes.append((int(v[0]), int(v[1])))
    return sizes


def main():
    data: str = util.get(9, 2024)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
