import util
from util import *

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


def run_perms(s, vs) -> int:
    global VALID
    if s in VALID:
        return s

    if run(s, vs, len(vs) - 1):
        VALID.add(s)
        return s
    return 0

PART_2 = False
def run(current, vs, i) -> bool:
    global PART_2
    if i == 0:
        return current == vs[0]

    q, r = divmod(current, vs[i])
    if r == 0:
       if run(q, vs, i - 1):
           return True

    if run(current - vs[i], vs, i - 1):
        return True

    if PART_2 and str(current).endswith(str(vs[i])):
        if run(current // (10 ** len(str(vs[i]))), vs, i - 1):
            return True

    return False


def task1(input):
    global VALID, PART_2
    VALID = set()
    PART_2 = False
    return sum(run_perms(s, vs) for s, vs in input)


def task2(input):
    global PART_2
    PART_2 = True
    return sum(run_perms(s, vs) for s, vs in input)


def parse(data: str):
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
