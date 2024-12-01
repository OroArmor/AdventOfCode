import util

test_data: str = \
    """3   4
4   3
2   5
1   3
3   9
3   3"""


def task1(input):
    a, b = input
    a.sort()
    b.sort()

    total = 0
    for i in range(len(a)):
        total += abs(a[i] - b[i])

    return total


def task2(input):
    a, b = input

    total = 0
    for i in range(len(a)):
        total += a[i] * b.count(a[i])

    return total


def parse(data: str):
    lines = util.as_lines(data)
    lines = [util.as_ssv_ints(line) for line in lines]

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
