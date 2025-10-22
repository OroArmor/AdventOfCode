import util
from util import *
import numpy as np
import sympy as sym

test_data: str = \
    """2,3,0,3,99"""


def task1(input):
    input = list(input)
    input[1] = 12
    input[2] = 2
    index = 0
    while input[index] != 99:
        if input[index] == 1:
            input[input[index + 3]] = input[input[index + 1]] + input[input[index + 2]]
        elif input[index] == 2:
            input[input[index + 3]] = input[input[index + 1]] * input[input[index + 2]]
        index += 4
        # print(input)
    return input[0]


def task2(input):

    for x in range(100):
        for y in range(100):
            input_reset = list(input)
            try:
                input_reset[1] = x
                input_reset[2] = y
                index = 0
                while input_reset[index] != 99:
                    if input_reset[index] == 1:
                        input_reset[input_reset[index + 3]] = input_reset[input_reset[index + 1]] + input_reset[input_reset[index + 2]]
                    elif input_reset[index] == 2:
                        input_reset[input_reset[index + 3]] = input_reset[input_reset[index + 1]] * input_reset[input_reset[index + 2]]
                    index += 4
            except:
                pass

            if input_reset[0] == 19690720:
                return (x * 100 + y)
        # print(input)
    return None


def parse(data: str):
    lines = util.as_csv_of_ints(data)
    return lines


def main():
    data: str = util.get(2, 2019)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
