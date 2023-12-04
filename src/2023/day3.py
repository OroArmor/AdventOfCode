import util
from util import *
import numpy as np

test_data: str = \
    """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def task1(input):
    print(input)
    symbols, numbers = input

    sum = 0

    for pos in numbers:
        number = numbers[pos]
        found = False

        for i in range(len(number)):
            pos2 = np.array([pos[0] - i, pos[1]])

            for dir in adjacent_directions():
                check = pos2 + dir

                if tuple(check) in symbols.keys():
                    found = True
                    break

            if found:
                break

        if found:
            sum += int(number)


    return sum


def task2(input):
    symbols, numbers = input

    sum = 0

    for symbol_loc in symbols:
        if symbols[symbol_loc] != "*":
            continue

        prod = 1
        finds = 0

        for pos in numbers:
            if abs(pos[1] - symbol_loc[1]) > 1:
                continue

            found = False
            number = numbers[pos]

            for i in range(len(number)):
                pos2 = np.array([pos[0] - i, pos[1]])

                for dir in adjacent_directions():
                    check = tuple(pos2 + dir)

                    if symbol_loc == check:
                        found = True
                        finds += 1
                        break

                if found:
                    break

            if found:
                prod *= int(number)
        sum += prod if prod > 1 and finds == 2 else 0


    return sum


def parse(data: str):
    lines = util.as_lines(data)

    symbols = {}

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c != "." and not c.isnumeric():
                symbols[(j, i)] = c

    numbers = {}

    for i, line in enumerate(lines):
        number = ""
        for j, c in enumerate(line):
            if c.isnumeric():
                number += c
            elif number != "":
                numbers[(j - 1, i)] = number
                number = ""
        if number != "":
            numbers[(len(line) - 1, i)] = number
            number = ""

    return symbols, numbers


def main():
    data: str = util.get(3, 2023)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
