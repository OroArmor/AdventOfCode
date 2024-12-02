import util
from collections import Counter

test_data: str = \
    """3   4
4   3
2   5
1   3
3   9
3   3"""


def task1(input):
    a, b = input
    a = sorted(a)
    b = sorted(b)

    total = 0
    for i in range(len(a)):
        total += abs(a[i] - b[i])

    return total


def task2(input):
    a, b = input
    b = Counter(b)

    total = 0
    for i in range(len(a)):
        total += a[i] * b.get(a[i], 0)

    return total


def parse(data: str):
    lines = util.as_lines_of_ints(data)

    vals = [[], []]
    for line in lines:
        vals[0].append(line[0])
        vals[1].append(line[1])

    return vals


def main():
    data: str = util.get(1, 2024)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
