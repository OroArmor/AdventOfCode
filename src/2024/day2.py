import util
from util import *
import itertools

test_data: str = \
    """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


def is_safe(line: Iterable[int]) -> bool:
    dir = None
    for (a, b) in itertools.pairwise(line):
        if dir is None:
            dir = a < b
        if 0 < abs(a - b) < 4 and (dir == (a < b)):
            continue
        return False
    return True


def task1(input):
    total = 0

    for line in input:
        if is_safe(line):
            total += 1

    return total


def task2(input):
    total = 0

    for line in input:
        if is_safe(line):
            total += 1
            continue

        for perm in itertools.combinations(line, len(line) - 1):
            if is_safe(perm):
                total += 1
                break

    return total


def parse(data: str):
    lines = util.as_lines_of_ints(data)
    return lines


def main():
    data: str = util.get(2, 2024)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
