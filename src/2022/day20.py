import util
import numpy as np

test_data: str = \
    """1
2
-3
3
-2
0
4"""


def task1(input):
    for i in range(len(input)):
        for i2, j in enumerate(input):
            if i == j[0]:
                input.remove(j)
                new_index = ((i2 + j[1]) % len(input) + len(input)) % len(input)
                input.insert(new_index, j)
                break

    zero_idx = -1
    for i, v in enumerate(input):
        if v[1] == 0:
            zero_idx = i
            break

    return input[(1000 + zero_idx) % len(input)][1] + input[(2000 + zero_idx) % len(input)][1] + input[(3000 + zero_idx) % len(input)][1]


def task2(input):
    input = [(x[0], x[1] * 811589153) for x in input]

    for _ in range(10):
        for i in range(len(input)):
            for i2, j in enumerate(input):
                if i == j[0]:
                    input.remove(j)
                    new_index = ((i2 + j[1]) % len(input) + len(input)) % len(input)
                    input.insert(new_index, j)
                    break

    zero_idx = -1
    for i, v in enumerate(input):
        if v[1] == 0:
            zero_idx = i
            break

    return input[(1000 + zero_idx) % len(input)][1] + input[(2000 + zero_idx) % len(input)][1] + input[(3000 + zero_idx) % len(input)][1]


def parse(data: str):
    lines = util.list_as_ints(util.as_lines(data))

    ints = [x for x in enumerate(lines)]
    return ints


def main():
    data: str = util.get(20, 2022)
    # data = test_data
    input = parse(data)
    print(task1(input))
    input = parse(data)
    print(task2(input))


if __name__ == "__main__":
    main()
