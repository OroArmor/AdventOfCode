import util
import numpy as np

test_data: [str] = \
    """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def contains(a: str, b: str):
    a_s = util.list_as_ints(a.split("-"))
    b_s = util.list_as_ints(b.split("-"))

    return a_s[0] >= b_s[0] and a_s[1] <= b_s[1]


def task1(input):
    total = 0

    for pair in input:
        vals = util.as_csv(pair)

        if contains(vals[0], vals[1]) or contains(vals[1], vals[0]):
            total += 1

    return total


def task2(input):
    total = 0

    for pair in input:
        vals = util.as_csv(pair)

        a_s = util.list_as_ints(vals[0].split("-"))
        b_s = util.list_as_ints(vals[1].split("-"))

        for a in range(a_s[0], a_s[1] + 1):
            if b_s[0] <= a <= b_s[1]:
                total += 1
                break

    return total


def main():
    data: str = util.get(4, 2022)
    # data = test_data
    input = util.as_lines(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
