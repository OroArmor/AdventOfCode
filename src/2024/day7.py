import itertools

import util
from util import *
import numpy as np

test_data: str = \
    """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

VALID = set()


def run_perms(s, vs, perms) -> int:
    global VALID
    if s in VALID:
        return s

    invalid = set()
    # print(s, vs)
    for perm in itertools.product(perms, repeat=len(vs)-1):

        perm = "".join(perm)
        for inv in invalid:
            if perm.endswith(inv):
                break
        else:
            current = s
            for i in reversed(range(0, len(vs) - 1)):
                match perm[i]:
                    case "0":
                        q, r = divmod(current, vs[i + 1])
                        if r != 0:
                            # invalid.add(perm[i:])
                            break
                        current = q
                    case "1":
                        current -= vs[i + 1]
                    case "2":
                        if not str(current).endswith(str(vs[i + 1])):
                            # invalid.add(perm[i:])
                            break
                        current = current // (10 ** len(str(vs[i + 1])))

                if i > 0 and current < vs[i]:
                    invalid.add(perm[i:])
                    break
            else:
                if current == vs[0]:
                    VALID.add(s)
                    return s
    return 0


def task1(input):
    global VALID
    VALID = set()
    return sum([run_perms(s, vs, '01') for s, vs in input])


def task2(input):
    return sum([run_perms(s, vs, '012') for s, vs in input])


def parse(data: str):
    # data = test_data
    lines = []
    for line in util.as_lines(data):
        s, vs = line.split(": ")
        lines.append((int(s), util.as_ssv_ints(vs)))
    return lines


def main():
    data: str = util.get(7, 2024)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
