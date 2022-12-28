import util
import numpy as np

test_data: str = \
    """A Y
B X
C Z"""


def task1(input: [str]):

    total = 0
    for r in input:
        m = r[0]
        e = r[2]

        if e == "X":
            total += 1
        if e == "Y":
            total += 2
        if e == "Z":
            total += 3

        if m == "A" and e == "X":
            total += 3
        if m == "B" and e == "Y":
            total += 3
        if m == "C" and e == "Z":
            total += 3

        if m == "A" and e == "Y":
            total += 6
        if m == "B" and e == "Z":
            total += 6
        if m == "C" and e == "X":
            total += 6
        # print(total)

    return total


def task2(input):
    total = 0
    for r in input:
        m = r[0]
        e = r[2]

        if e == "X":
            total += 0
            if m == "A":
                total += 3
            elif m == "B":
                total += 1
            else:
                total += 2
        if e == "Y":
            total += 3
            if m == "A":
                total += 1
            elif m == "B":
                total += 2
            else:
                total += 3
        if e == "Z":
            total += 6
            if m == "A":
                total += 2
            elif m == "B":
                total += 3
            else:
                total += 1

        # print(total)

    return total


def main():
    data: str = util.get(2, 2022)
    # data = test_data
    input = util.as_lines(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
