import util
from util import *

test_data: str = \
    """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def get_history(line: [int]):
    histories = [line]
    while True:
        next = []

        for i in range(1, len(histories[-1])):
            next.append(histories[-1][i] - histories[-1][i - 1])

        histories.append(next)
        if all([s == 0 for s in histories[-1]]):
            break
    return histories


def task1(input):
    return sum((sum((h[-1] for h in (get_history(line)))) for line in input))


def task2(input):
    return sum((reduce(lambda x, acc: acc - x, (h[0] for h in reversed(get_history(line))), 0) for line in input))


def parse(data: str):
    lines = [util.as_ssv_ints(line) for line in util.as_lines(data)]
    return lines


def main():
    data: str = util.get(9, 2023)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
