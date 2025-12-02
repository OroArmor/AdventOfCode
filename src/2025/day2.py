import util
from util import *
import numpy as np

test_data: str = \
    """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""


def task1(input):
    total = 0
    for r in input:
        start = str(r.start)
        end = str(r.end - 1)

        if len(start) % 2 == 1 and len(end) == len(start):
            continue

        spotential = start[:len(start) // 2]
        potential = end[:len(end) // 2 + len(end) % 2]

        r2 = Range(int(spotential) if spotential != '' else 0, int(potential), inclusive=True)
        for id_half in r2:
            id = int(str(id_half) * 2)
            if id in r:
                total += id
    return total


def task2(input):
    total = 0
    for r in input:
        dups = set()
        start = str(r.start)
        end = str(r.end - 1)

        for l in range(0, len(str(r.start)) // 2 + 1):
            spotential = start[:l]
            potential = end[:l + (len(end) != len(start))]

            if spotential == '' and potential == '':
                continue

            r2 = Range(int(spotential) if spotential != '' else 0, int(potential), inclusive=True)
            for id_partial in r2:
                id = int(str(id_partial) * (len(start) // len(str(id_partial))))
                if id >= 9 and id in r and id not in dups:
                    dups.add(id)
                    total += id
                if len(end) != len(start):
                    id = int(str(id_partial) * (len(end) // len(str(id_partial))))
                    if id in r and id not in dups:
                        dups.add(id)
                        total += id

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
