import re

import util
from util import *
import numpy as np

test_data: str = \
    """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


NEXT = 0
IN_PROG = 1
GAP = 2


@cache
def calculate(line, vals, in_progress):
    if (len(line) == 0 and len(vals) == 0) or (len(vals) == 0 and line.count("#") == 0):
        return 1
    elif len(vals) == 0 or len(line) == 0:
        return 0
    else:
        if line[0] == "?":
            return calculate("#" + line[1:], tuple(vals), in_progress) + calculate("." + line[1:], tuple(vals), in_progress)
        elif line[0] == ".":
            if in_progress == IN_PROG:
                return 0
            else:
                return calculate(line[1:], tuple(vals), NEXT)
        else:
            if in_progress == GAP:
                return 0
            else:
                new_vals = [v for v in vals]
                new_vals[0] -= 1

                if new_vals[0] == 0:
                    return calculate(line[1:], tuple(new_vals[1:]), GAP)
                else:
                    return calculate(line[1:], tuple(new_vals), IN_PROG)


def task1(input):
    return sum([calculate(line, vals, NEXT) for line, vals in input])


def task2(input):
    return sum([calculate("?".join([line] * 5), vals * 5, NEXT) for line, vals in input])


def parse(data: str):
    return [(line.split()[0], tuple(as_csv_of_ints(line.split()[1]))) for line in util.as_lines(data)]


def main():
    data: str = util.get(12, 2023)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
