import util
from util import *
import numpy as np

test_data: str = \
    """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


def task1(input):
    print(input)

    sum = 0
    for game in input:
        for sub in input[game]:
            if not (sub["red"] <= 12 and sub["green"] <= 13 and sub["blue"] <= 14):
                break
        else:
            sum += game
            continue

    return sum


def task2(input):
    sum = 0
    for game in input:
        red, green, blue = 0, 0, 0
        for sub in input[game]:
            red = max(red, sub["red"])
            green = max(green, sub["green"])
            blue = max(blue, sub["blue"])
        sum += red * green * blue

    return sum


def parse(data: str):
    lines = util.as_lines(data)

    games = {}

    for line in lines:
        a, b = util.split_on_colon(line)

        gs = b.split("; ")

        gs2 = []
        for g in gs:
            cubes = util.as_csv(g)
            res = {"red": 0, "green": 0, "blue": 0}
            for cube in cubes:
                sp = cube.split(" ")
                res[sp[1]] = int(sp[0])
            gs2.append(res)
        games[int(a[5:])] = gs2

    return games


def main():
    data: str = util.get(2, 2023)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
