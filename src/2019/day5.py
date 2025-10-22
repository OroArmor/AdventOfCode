from collections import defaultdict

import util
from util import *
import numpy as np

test_data: str = \
    """3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"""


def task1(input):
    input_dict = defaultdict(lambda: 0)
    for (i, val) in enumerate(input):
        input_dict[i] = val
    input = input_dict
    # input = {i: input[i] for i in range(len(input))}
    index = 0
    output = ""
    while input[index] != 99:
        op, params = input[index] % 100, util.list_as_ints(list(reversed(f"{input[index]:05d}"[:3])))

        vals = []
        for (i, param) in enumerate(params):
            vals.append((input[input[index + 1 + i]], input[index + 1 + i]))

        # print(f"{input[index]:05d}", op, params, vals)
        if op == 1:
            input[vals[2][1]] = vals[0][params[0]] + vals[1][params[1]]
            index += 4
        elif op == 2:
            input[vals[2][1]] = vals[0][params[0]] * vals[1][params[1]]
            index += 4
        elif op == 3:
            input[vals[0][1]] = 1
            index += 2
        elif op == 4:
            output += str(vals[0][params[0]]) + "\n"
            index += 2
            # print(str(vals[0][params[0]]))
        elif op == 5:
            if vals[0][params[0]] != 0:
                index = vals[1][params[1]]
            else:
                index += 3
        elif op == 6:
            if vals[0][params[0]] == 0:
                index = vals[1][params[1]]
            else:
                index += 3
        elif op == 7:
            if vals[0][params[0]] < vals[1][params[1]]:
                input[vals[2][1]] = 1
            else:
                input[vals[2][1]] = 0
            index += 4
        elif op == 8:
            if vals[0][params[0]] == vals[1][params[1]]:
                input[vals[2][1]] = 1
            else:
                input[vals[2][1]] = 0
            index += 4
        else:
            print("ERROR")
            break

        # print(input)
    return util.as_lines(output)[-2]


def task2(input):
    input_dict = defaultdict(lambda: 0)
    for (i, val) in enumerate(input):
        input_dict[i] = val
    input = input_dict
    # input = {i: input[i] for i in range(len(input))}
    index = 0
    output = ""
    while input[index] != 99:
        op, params = input[index] % 100, util.list_as_ints(list(reversed(f"{input[index]:05d}"[:3])))

        vals = []
        for (i, param) in enumerate(params):
            vals.append((input[input[index + 1 + i]], input[index + 1 + i]))

        # print(f"{input[index]:05d}", op, params, vals)
        if op == 1:
            input[vals[2][1]] = vals[0][params[0]] + vals[1][params[1]]
            index += 4
        elif op == 2:
            input[vals[2][1]] = vals[0][params[0]] * vals[1][params[1]]
            index += 4
        elif op == 3:
            input[vals[0][1]] = 5
            index += 2
        elif op == 4:
            output += str(vals[0][params[0]]) + "\n"
            index += 2
            # print(str(vals[0][params[0]]))
        elif op == 5:
            if vals[0][params[0]] != 0:
                index = vals[1][params[1]]
            else:
                index += 3
        elif op == 6:
            if vals[0][params[0]] == 0:
                index = vals[1][params[1]]
            else:
                index += 3
        elif op == 7:
            if vals[0][params[0]] < vals[1][params[1]]:
                input[vals[2][1]] = 1
            else:
                input[vals[2][1]] = 0
            index += 4
        elif op == 8:
            if vals[0][params[0]] == vals[1][params[1]]:
                input[vals[2][1]] = 1
            else:
                input[vals[2][1]] = 0
            index += 4
        else:
            print("ERROR")
            break

        # print(input)
    return output


def parse(data: str):
    lines = util.as_csv_of_ints(data)
    return lines


def main():
    data: str = util.get(5, 2019)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
