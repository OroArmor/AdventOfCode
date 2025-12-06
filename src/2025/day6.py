import util
from util import *
import numpy as np

test_data: str = \
    """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

def task1(input):
    ops = util.as_ssv(input[-1])
    nums = list(map(lambda line: as_ssv_ints(line), input[:-1]))

    total = 0
    for i, op in enumerate(ops):
        acc = 1 if op == "*" else 0
        for j in range(len(nums)):
            if op == "*":
                acc *= nums[j][i]
            elif op == "+":
                acc += nums[j][i]
        total += acc

    return total

def task2(input):
    ops = []
    nums = [[]]

    for j in range(len(input[0])):
        line = ""
        for i in range(len(input)):
            line += input[i][j]

        if line.endswith("*"):
            ops.append("*")
            line = line[:-1]
        elif line.endswith("+"):
            ops.append("+")
            line = line[:-1]

        if line.strip().isdigit():
            nums[-1].append(int(line.strip()))

        if line.isspace():
            nums.append([])


    total = 0
    for i, op in enumerate(ops):
        acc = 1 if op == "*" else 0
        for j in range(len(nums[i])):
            if op == "*":
                acc *= nums[i][j]
            elif op == "+":
                acc += nums[i][j]
        total += acc

    return total


def parse(data: str):
    return util.as_lines(data)


def main():
    data: str = util.get(6, 2025)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
