import util
import numpy as np

test_data: str = \
    """abc

a
b
c

ab
ac

a
a
a
a

b"""


def task1(input):
    total = 0
    for group in input:
        qs = ""
        for c in group:
            if c.isalpha() and (c not in qs):
                qs += c
        total += len(qs)
    return total


def task2(input):
    total = 0
    for group in input:
        answers = util.as_lines(group)
        qs = answers[0]

        for answer in answers[1:]:
            n_qs = ""
            for c in answer:
                if c in qs:
                    n_qs += c
            qs = n_qs
        total += len(qs)
    return total


def parse(data):
    return util.as_double_lines(data)

def main():
    data: str = util.get(6, 2020)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
