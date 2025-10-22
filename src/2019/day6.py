from collections import defaultdict

import util
from util import *
import numpy as np

test_data: str = \
    """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""


def task1(input):
    todo = ["COM"]

    vals = {"COM": 0}
    while len(todo) > 0:
        cur = todo.pop()

        for sub in input[cur]:
            vals[sub] = vals.get(cur) + 1
            todo.append(sub)

    return sum(vals.values())


def task2(input):
    flipped = {}

    for parent, subs in input.items():
        for sub in subs:
            flipped[sub] = parent

    you_path = []
    cur = "YOU"
    while cur != "COM":
        cur = flipped[cur]
        you_path.append(cur)

    san_path = []
    cur = "SAN"
    while cur not in you_path:
        cur = flipped[cur]
        san_path.append(cur)

    return len(san_path) + you_path.index(cur) - 1


def parse(data: str):
    lines = util.as_lines(data)

    orbits = defaultdict(list)
    for line in lines:
        orbits[line.split(")")[0]].append(line.split(")")[1])
    return orbits


def main():
    data: str = util.get(6, 2019)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
