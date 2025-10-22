import util
from util import *
import numpy as np

test_data: str = \
    """0,3,6"""


def task1(input):
    nums = {n : (i, i) for i, n in enumerate(input)}

    last = input[-1]
    for turn in range(len(nums), 2020):
        next = nums[last][0] - nums[last][1]
        nums[next] = (turn, nums[next][0] if next in nums.keys() else turn)
        last = next

    return last


def task2(input):
    nums = {n: (i, i) for i, n in enumerate(input)}

    last = input[-1]
    for turn in range(len(nums), 30000000):
        next = nums[last][0] - nums[last][1]
        nums[next] = (turn, nums[next][0] if next in nums.keys() else turn)
        last = next

    return last


def parse(data: str):
    lines = util.as_csv_of_ints(data)
    return lines


def main():
    data: str = util.get(15, 2020)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
