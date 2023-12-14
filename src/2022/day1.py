import util
import numpy as np

test_data: [str] = \
    """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


def task1(data: [str]):
    return max([sum(util.as_lines_of_int(elf)) for elf in data])


def task2(data: [str]):
    return sum(list(sorted([sum(util.as_lines_of_int(elf)) for elf in data]))[::-1][0:3])


def parse(data: str):
    return util.as_double_lines(data)

def main():
    data: [str] = util.get(1, 2022)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
