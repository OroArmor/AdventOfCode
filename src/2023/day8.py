import util
from util import *
import numpy as np

test_data: str = \
    """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


def task1(input):
    inst, path = input

    steps = 0
    current = "AAA"
    while current != "ZZZ":
        dir = inst[steps % len(inst)]
        if dir == "R":
            current = path[current][1]
        else:
            current = path[current][0]

        steps += 1


    return steps


def task2(input):
    inst, path = input

    s = []
    for start in path:
        if start[-1] != "A":
            continue

        steps = 0
        current = start
        while current[-1] != "Z":
            dir = inst[steps % len(inst)]
            if dir == "R":
                current = path[current][1]
            else:
                current = path[current][0]
            steps += 1

        s.append(steps)

    return lcm(s)


def parse(data: str):
    inst, nodes = util.as_double_lines(data)

    path = {}
    for line in as_lines(nodes):
        s, r = line.split(" = (")
        r = r[:-1].split(", ")
        path[s] = tuple(r)

    return inst, path


def main():
    data: str = util.get(8, 2023)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
