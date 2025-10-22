import re

import util
from util import *
import numpy as np

test_data: str = \
    """class: 1-3 or 5-7
row: 6-11 or 33-44
departure seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""


def task1(input):
    _, ranges, _, nearby = input

    result = 0

    for ticket in nearby:
        for val in ticket:
            for range in ranges:
                if range[0][0] <= val <= range[0][1]:
                    break
                if range[1][0] <= val <= range[1][1]:
                    break
            else:
                result += val

    return result


def task2(input):
    deps, ranges, my_ticket, nearby = input

    valid = []
    for ticket in nearby:
        for val in ticket:
            for r in ranges:
                if r[0][0] <= val <= r[0][1]:
                    break
                if r[1][0] <= val <= r[1][1]:
                    break
            else:
                break
        else:
            valid.append(ticket)

    columns = {}

    for i, dep_range in enumerate(ranges):
        r_col = []
        for column in range(len(valid[0])):
            for v in valid:
                if not(dep_range[0][0] <= v[column] <= dep_range[0][1] or dep_range[1][0] <= v[column] <= dep_range[1][1]):
                    break
            else:
                r_col.append(column)
        columns[i] = r_col


    while any([len(col) > 1 for col in columns.values()]):
        for col in columns.keys():
            if len(columns[col]) == 1:
                for col2 in columns.keys():
                    if col != col2 and columns[col][0] in columns[col2]:
                        columns[col2].remove(columns[col][0])

    result = 1
    for col in deps:
        result *= my_ticket[columns[col][0]]

    return result


def parse(data: str):
    lines = util.as_double_lines(data)

    ranges = util.as_lines(lines[0].strip())

    deps = [i for i in range(len(ranges)) if ranges[i].startswith("departure")]
    ranges = [re.match("[\\w\\s]+: (\\d+)-(\\d+) or (\\d+)-(\\d+)", line).groups() for line in ranges]
    ranges = [((int(r[0]), int(r[1])), (int(r[2]), int(r[3]))) for r in ranges]

    my_ticket = util.as_csv_of_ints(util.as_lines(lines[1])[1])
    nearby = [util.as_csv_of_ints(line) for line in util.as_lines(lines[2])[1:]]


    return deps, ranges, my_ticket, nearby


def main():
    data: str = util.get(16, 2020)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
