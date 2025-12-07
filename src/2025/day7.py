from collections import defaultdict
import util
from util import *
import numpy as np

test_data: str = \
    """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""


def task1(input):
    s, splitters = input
    beams = {s.x}

    total = 0

    for splitter_line in splitters:
        splits = splitter_line.intersection(beams)
        new_beams = splits.symmetric_difference(beams)
        for split in splits:
            new_beams.add(split - 1)
            new_beams.add(split + 1)
        total += len(splits)
        beams = new_beams

    return total


def task2(input):
    s, splitters = input
    beams = {s.x: 1}

    for splitter_line in splitters:
        splits = splitter_line.intersection(set(beams.keys()))
        new_beams = defaultdict(int)
        for split in splits:
            new_beams[split - 1] += beams[split]
            new_beams[split + 1] += beams[split]
        for old_beam in set(beams.keys()).difference(splitter_line):
            new_beams[old_beam] += beams[old_beam]
        beams = new_beams

    return sum(beams.values())


def parse(data: str):
    lines = util.as_lines(data)

    s = None
    splitters: List[set] = []
    for y, line in enumerate(lines):
        if y % 2 == 0:
            splitters.append(set())
            for x, c in enumerate(line):
                if c == 'S':
                    s = Point(x, y)
                elif c == '^':
                    splitters[y // 2].add(x)

    return s, splitters


def main():
    data: str = util.get(7, 2025)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
