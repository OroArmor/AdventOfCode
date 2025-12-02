import util
from util import *
import numpy as np

test_data: str = \
    """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""


def task1(input):
    total = 0
    for r in input:
        for id in r:
            id = str(id)
            ida, idb = id[:len(id) // 2], id[len(id) // 2:]
            if ida == idb:
                total += int(id)
    return total


def task2(input):
    total = 0
    for r in input:
        for id in r:
            id = str(id)
            for l in range(1, len(id) // 2 + 1):
                if len(id) % l == 0:
                    ida = id[:l]
                    if ida * (len(id) // l) == id:
                        total += int(id)
                        break
    return total


def parse(data: str):
    lines = util.as_csv(data)
    data = []
    for l in lines:
        l1, l2 = l.split("-")
        data.append(Range(int(l1), int(l2), inclusive=True))
    return data


def main():
    data: str = util.get(2, 2025)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
