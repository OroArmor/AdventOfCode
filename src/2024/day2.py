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


def find_issue(line: Iterable[int]) -> int:
    dir = None
    for (i, (a, b)) in enumerate(itertools.pairwise(line)):
        if dir is None:
            dir = a < b
        if 0 < abs(a - b) < 4 and (dir == (a < b)):
            continue
        return i
    return len(line)


def task1(input):
    total = 0

    for line in input:
        if is_safe(line):
            total += 1

    return total


def task2(input):
    total = 0

    for line in input:
        issue = find_issue(line)
        if issue == len(line):
            total += 1
        elif is_safe(line[:issue] + line[issue + 1:]): # We only know the gap that has the issue, so we need to try both sides
            total += 1
        elif is_safe(line[:issue + 1] + line[issue + 2:]):
            total += 1
        elif issue == 1 and is_safe(line[1:]): # This can happen because if the issue is on the 2nd gap, it could be caused by a bad first value, and then a changing direction
            total += 1

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
