import re
from functools import cmp_to_key

import util
import numpy as np

test_data: str = \
    """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


def compare(a, b):
    ret = None
    for i in range(len(a)):
        if len(b) == i:  # right out of items
            ret = False
        elif type(a[i]) == int and type(b[i]) == int:  # Left is smaller than right
            if a[i] < b[i]:  # Left is smaller than right
                ret = True
            elif a[i] > b[i]:  # Left is larger than right
                ret = False
        elif type(a[i]) == list and type(b[i]) == list:
            ret = compare(a[i], b[i])
        elif type(a[i]) == int and type(b[i]) == list:
            ret = compare([a[i]], b[i])
        elif type(a[i]) == list and type(b[i]) == int:
            ret = compare(a[i], [b[i]])

        if ret != None:
            return ret

    return None if len(a) == len(b) else len(a) < len(b)


def task1(input):
    total = 0
    for i in range(0, len(input), 3):
        if compare(input[i], input[i + 1]):
            total += i // 3 + 1

    return total


def task2(input):
    input = list(filter(lambda p: len(p[0]) > 0, input))

    input.append([[[2]]])
    input.append([[[6]]])

    ordered = sorted(input, key=cmp_to_key(lambda a, b: -1 if compare(a, b) else 1))
    return (ordered.index([[[2]]]) + 1) * (ordered.index([[[6]]]) + 1)


def parse(data: str):
    lines = util.as_lines(data)

    packet_groups = []

    for pair in lines:
        group = []
        for line in pair.split("\n"):
            stack = []
            packet = []
            current = packet
            for c in line:
                if c == "[":
                    stack.append([])
                    current = []
                elif c == "]":
                    stack[-1].append(current)
                    current = stack.pop()
                elif c == ",":
                    stack[-1].append(current)
                    current = None
                else:
                    if type(current) == int:
                        current *= 10
                        current += int(c)
                    else:
                        current = int(c)
            group.append(current)

        packet_groups.append(group)

    return packet_groups


def main():
    data: str = util.get(13, 2022)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
