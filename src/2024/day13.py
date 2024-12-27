import re

import util
from util import *

test_data: str = \
    """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""


def solve(group: List[int], p2: bool) -> int:
    x = group[4] + (10000000000000 if p2 else 0)
    y = group[5] + (10000000000000 if p2 else 0)
    a, b = util.linear_system_of_equations(group[0], group[2], x, group[1], group[3], y)
    if a.is_integer() and b.is_integer():
        return 3 * int(a) + int(b)
    return 0


def task1(input):
    return sum(solve(group, False) for group in input)


def task2(input):
    return sum(solve(group, True) for group in input)


def parse(data: str):
    lines = util.as_double_lines(data)

    groups = []
    for line in lines:
        line = util.list_as_ints(re.findall("\\d+", line))
        groups.append(line)

    return groups


def main():
    data: str = util.get(13, 2024)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
