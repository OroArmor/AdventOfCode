import util
import numpy as np

test_data: str = \
    """bvwbjplbgvbhsrlpgdmjqwftvncz"""


def task1(input):
    for i in range(len(input)):
        sopm = input[i:i + 4]
        if len(set(sopm)) == 4:
            return i + 4
    return -1


def task2(input):
    for i in range(len(input)):
        sopm = input[i:i + 14]
        if len(set(sopm)) == 14:
            return i + 14
    return -1


def main():
    data: str = util.get(6, 2022)
    # data = test_data
    input = data
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
