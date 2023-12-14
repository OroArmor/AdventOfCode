import util
import numpy as np

test_data: [str] = \
    """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


def task1(input):
    total = 0

    for line in input:
        l = len(line) // 2
        f = line[0:l]
        s = line[l:]

        for c in s:
            if c in f:
                if c < 'a':
                    total += ord(c) - ord('A') + 27
                else:
                    total += ord(c) - ord('a') + 1
                break

    return total


def task2(input):
    total = 0

    for i in range(0, len(input), 3):
        a = input[i]
        b = input[i + 1]
        c = input[i + 2]

        for ch in a:
            if ch in b and ch in c:
                break

        if ch < 'a':
            total += ord(ch) - ord('A') + 27
        else:
            total += ord(ch) - ord('a') + 1

    return total

def parse(data: str):
    return util.as_lines(data)

def main():
    data: [str] = util.get(3, 2022)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
