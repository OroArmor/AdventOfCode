import util
from util import *
import numpy as np

test_data: str = \
    """1 + 2 * 3 + 4 * 5 + 6
1 + (2 * 3) + (4 * (5 + 6))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""

def evaluate_1(line: str) -> int:
    index = 0
    val = 0
    op = None
    while index < len(line):
        c: str = line[index]

        pos = None
        if c == "(":
            start = index
            par_count = 1
            while not(c == ")" and par_count == 0):
                index += 1
                c = line[index]
                if c == "(":
                    par_count += 1
                if c == ")":
                    par_count -= 1
            pos = evaluate_1(line[start + 1:index])
        elif c.isdigit():
            pos = int(c)
        elif c == "+":
            op = "+"
        elif c == "*":
            op = "*"

        if pos is not None:
            if op is None:
                val = pos
            elif op == "+":
                val += pos
            elif op == "*":
                val *= pos

        index += 1

    return val
def task1(input):
    return sum([evaluate_1(line) for line in input])

def evaluate_2(line: str) -> int:
    index = 0
    val = 0
    op = None

    fixed_line = ""
    while index < len(line):
        c: str = line[index]

        pos = None
        if c == "(":
            start = index
            par_count = 1
            while not(c == ")" and par_count == 0):
                index += 1
                c = line[index]
                if c == "(":
                    par_count += 1
                if c == ")":
                    par_count -= 1
            fixed_line += str(evaluate_2(line[start + 1:index]))
        else:
            fixed_line += c

        index += 1

    vals = fixed_line.split(" ")
    index = 0
    while index < len(vals):
        if vals[index] == "+":
            a = int(vals[index - 1])
            b = int(vals[index + 1])
            vals[index] = a + b
            del vals[index - 1]
            del vals[index]
            index -= 2
        index += 1

    index = 0
    while index < len(vals):
        if vals[index] == "*":
            a = int(vals[index - 1])
            b = int(vals[index + 1])
            vals[index] = a * b
            del vals[index - 1]
            del vals[index]
            index -= 2
        index += 1

    return vals[0]

def task2(input):
    return sum([evaluate_2(line) for line in input])


def parse(data: str):
    lines = util.as_lines(data)
    return lines


def main():
    data: str = util.get(18, 2020)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
