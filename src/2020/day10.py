import util
import numpy as np

test_data: str = \
    """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""


def task1(input):
    ones, threes = 0, 0
    for i in range(len(input)):
        if i == 0:
            if input[i] == 1:
                ones += 1
            else:
                threes += 1
        else:
            diff = input[i] - input[i - 1]
            if diff == 1:
                ones += 1
            else:
                threes += 1

    return ones * (threes + 1)


def task2(input):
    ways_to_reach = {0: 1}

    for val in input:
        ways = 0
        if (val - 1) in ways_to_reach:
            ways += ways_to_reach[val - 1]

        if (val - 2) in ways_to_reach:
            ways += ways_to_reach[val - 2]

        if (val - 3) in ways_to_reach:
            ways += ways_to_reach[val - 3]

        ways_to_reach[val] = ways

    return ways_to_reach[max(input)]


def parse(data: str):
    lines = util.as_lines_of_int(data)
    return sorted(lines)


def main():
    data: str = util.get(10, 2020)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
