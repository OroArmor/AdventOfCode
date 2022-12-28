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
    m = 0

    for elf in data:
        total = np.array(util.as_lines_of_int(elf)).sum()
        m = max(total, m)

    return m


def task2(data: [str]):
    cals = np.zeros((len(data)), dtype=int)

    for index, elf in enumerate(data):
        cals[index] = np.array(util.as_lines_of_int(elf)).sum()

    cals.sort()
    return cals[len(cals) - 3:].sum()


def main():
    data: [str] = util.get(1, 2022)
    # data = test_data
    input = util.as_double_lines(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
