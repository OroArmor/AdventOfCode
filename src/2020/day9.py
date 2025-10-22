import util
import numpy as np

test_data: str = \
    """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

SIZE = 25

RESULT = None
def task1(input):
    global RESULT

    for i in range(SIZE, len(input)):
        prev_25 = set(input[i - SIZE:i])
        found = False
        for prev in prev_25:
            if (input[i] - prev) in prev_25:
                found = True

        if not found:
            RESULT = input[i]
            return input[i]
    return "Error"


def task2(input):
    for start in range(len(input)):
        for end in range(start, len(input)):
            if sum(input[start:end]) == RESULT:
                return min(input[start:end]) + max(input[start:end])

    return "Error"


def parse(data: str):
    lines = util.as_lines_of_int(data)
    return lines


def main():
    data: str = util.get(9, 2020)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()