import util
from util import *
import numpy as np

test_data: str = \
    """"""


def task1(input):
    total = 0
    for mass in input:
        total += mass // 3 - 2

    return total


def calc_fuel(mass: int):
    f = mass // 3 - 2
    if (f <= 0):
        return 0
    return f + calc_fuel(f)


def task2(input):
    total = 0
    for mass in input:
        total += calc_fuel(mass)

    return total


def parse(data: str):
    lines = util.as_lines_of_int(data)
    return lines


def main():
    data: str = util.get(1, 2019)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
