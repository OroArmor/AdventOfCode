import re
import util

test_data: str = \
    """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""


def task1(input):
    matches = re.findall("mul\\((\\d{1,3}),(\\d{1,3})\\)", input)
    total = 0
    for match in matches:
        total += int(match[0]) * int(match[1])
    return total


def task2(input):
    matches = re.findall("mul\\((\\d{1,3}),(\\d{1,3})\\)|do(n't)?\\(\\)", input)
    on = True
    total = 0
    for match in matches:
        if match[0] == '':
            on = match[2] != "n't"
        elif on:
            total += int(match[0]) * int(match[1])
    return total


def parse(data: str):
    return data


def main():
    data: str = util.get(3, 2024)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
