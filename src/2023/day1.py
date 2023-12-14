import util
from util import *
import numpy as np

test_data: str = \
    """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

def task1(input):
    lines2 = []
    for line in input:
        line2 = ""
        for c in line:
            if c.isnumeric():
                line2 += c
        lines2.append(int(line2[0] + line2[-1]))

    return sum(lines2)


def task2(input):
    lines2 = []
    for line in input:
        line2 = ""

        line = line.replace("one", "o1e")
        line = line.replace("two", "t2o")
        line = line.replace("three", "t3e")
        line = line.replace("four", "f4r")
        line = line.replace("five", "f5e")
        line = line.replace("six", "s6x")
        line = line.replace("seven", "s7n")
        line = line.replace("eight", "e8t")
        line = line.replace("nine", "n9e")

        for c in line:
            if c.isnumeric():
                line2 += c
        lines2.append(int(line2[0] + line2[-1]))

    return sum(lines2)


def parse(data: str):
    lines = util.as_lines(data)
    return lines


def main():
    data: str = util.get(1, 2023)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
