import itertools

import util
from util import *
import numpy as np
from collections import defaultdict
from copy import deepcopy

test_data: str = \
    """3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"""


def run_calc(instructions, config):
    prev_stage = 0
    for config_stage in range(5):
        input = deepcopy(instructions)
        index = 0
        used_config = False
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
                input[vals[0][1]] = prev_stage if used_config else config[config_stage]
                used_config = True
                index += 2
            elif op == 4:
                prev_stage = vals[0][params[0]]
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
    return prev_stage


def task1(input):
    input_dict = defaultdict(lambda: 0)
    for (i, val) in enumerate(input):
        input_dict[i] = val

    max_val = 0
    for perm in itertools.permutations([0, 1, 2, 3, 4]):
        max_val = max(max_val, run_calc(input_dict, perm))

    return max_val


def run_calc2(instructions, config):
    prev_stage = 0

    stages = {i: deepcopy(instructions) for i in [0, 1, 2, 3, 4]}
    indices = {i: 0 for i in [0, 1, 2, 3, 4]}
    used = {i: False for i in [0, 1, 2, 3, 4]}

    loops = 0
    for config_stage in itertools.cycle([0, 1, 2, 3, 4]):
        input = stages[config_stage]
        index = indices[config_stage]
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
                input[vals[0][1]] = prev_stage if used[config_stage] else config[config_stage]
                used[config_stage] = True
                index += 2
            elif op == 4:
                prev_stage = vals[0][params[0]]
                index += 2
                # print(str(vals[0][params[0]]))
                break
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
                raise Exception(f"AHHH, {index}, {config_stage}, {input[index]}")
        if input[index] != 99:
            indices[config_stage] = index
            loops += 1
        else:
            if config_stage == 4:
                break
    return prev_stage


def task2(input):
    input_dict = defaultdict(lambda: 0)
    for (i, val) in enumerate(input):
        input_dict[i] = val

    max_val = 0
    for perm in itertools.permutations([5, 6, 7, 8, 9]):
        max_val = max(max_val, run_calc2(input_dict, perm))

    return max_val


def parse(data: str):
    lines = util.as_csv_of_ints(data)
    return lines


def main():
    data: str = util.get(7, 2019)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
