import itertools

import util
from util import *
import numpy as np

test_data: str = \
    """"""


def is_valid(password: str) -> bool:
    ints = util.list_as_ints(password)

    if sorted(ints) != ints:
        return False

    for (a, b) in itertools.pairwise(ints):
        if a == b:
            break
    else:
        return False

    return True


def is_valid2(password: str) -> bool:
    ints = util.list_as_ints(password)

    if sorted(ints) != ints:
        return False

    current = password[0]
    pair_length = 1
    found_pair = False

    for i in range(1, len(password)):
        if password[i] == current:
            pair_length += 1
        else:
            current = password[i]
            found_pair |= pair_length == 2
            pair_length = 1

    found_pair |= pair_length == 2

    return found_pair


def task1(input):
    total = 0
    for password in range(input[0], input[1] + 1):
        if is_valid(str(password)):
            total += 1
    return total


def task2(input):
    total = 0
    for password in range(input[0], input[1] + 1):
        if is_valid2(str(password)):
            total += 1
    return total


def parse(data: str):
    lines = util.list_as_ints(data.split("-"))
    return lines


def main():
    data: str = util.get(4, 2019)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
