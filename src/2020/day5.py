import util
import numpy as np

from util import as_lines, get

test_data: [str] = \
    """BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL""".split("\n")


def task1(data: [str]):
    largest = 0
    for p in data:
        p = p.replace("B", "1")
        p = p.replace("R", "1")
        p = p.replace("F", "0")
        p = p.replace("L", "0")

        largest = max(largest, int(p, 2))

    return largest


def task2(data: [str]):
    ids = np.zeros(len(data), dtype=int)
    for i, p in enumerate(data):
        p = p.replace("B", "1")
        p = p.replace("R", "1")
        p = p.replace("F", "0")
        p = p.replace("L", "0")

        ids[i] = int(p, 2)

    ids.sort()

    for i in range(len(ids) - 1):
        if ids[i] + 2 == ids[i + 1]:
            return ids[i] + 1

    return -1

def parse(data):
    return as_lines(data)

def main():
    data: [str] = get(5, 2020)
    # data = test_data
    data = parse(data)
    print(task1(data))
    print(task2(data))


if __name__ == "__main__":
    main()
