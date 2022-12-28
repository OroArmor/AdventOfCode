import util
import numpy as np

test_data: str = \
    """"""


def task1(input):
    print(input)
    return


def task2(input):
    return


def parse(data: str):
    lines = util.as_lines(data)
    return lines


def main():
    data: str = util.get(1, 2022)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
