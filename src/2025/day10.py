import functools
from collections import defaultdict
import more_itertools
import scipy.optimize
import util
from util import *
import numpy as np

test_data: str = \
    """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""


def pack_array(where: np.ndarray) -> int:
    mask = 0
    for w in where:
        mask |= 1 << w
    return np.int16(mask)


class Machine:
    def __init__(self, line):
        goal, *raw_buttons, joltage = line.split()

        self.goal = pack_array(np.where(np.array(list(goal))[1:-1] == "#")[0])
        self.buttons = []
        self.int_buttons = []

        for raw in raw_buttons:
            button = np.zeros(len(goal) - 2, dtype=bool)
            raw = util.as_csv_of_ints(raw[1:-1])
            button[raw] = True
            self.int_buttons.append(pack_array(raw))
            self.buttons.append(button)
        self.buttons = np.array(self.buttons)
        self.joltage = np.array(util.as_csv_of_ints(joltage[1:-1])).astype(int).flatten()

    def __repr__(self):
        return f"{self.goal}: [{self.int_buttons}] | {self.joltage}"


def min_presses(machine):
    for comb in more_itertools.powerset(machine.int_buttons):
        if len(comb) > 0:
            result = functools.reduce(np.int16.__xor__, comb)
            if result == machine.goal:
                return len(comb)


def task1(input):
    return sum(min_presses(machine) for machine in input)


def joltage_presses(machine):
    combos = defaultdict(dict)
    combos[0] = {tuple(np.zeros_like(machine.joltage)): 0}
    for comb in zip(more_itertools.powerset(machine.int_buttons), more_itertools.powerset(machine.buttons)):
        ints, buttons = comb
        result = functools.reduce(np.int16.__xor__, ints, np.int16(0))

        if buttons:
            pattern = buttons[0].astype(int)
            for b in buttons[1:]:
                pattern += b
            pattern = tuple(pattern)
        else:
            pattern = (0, ) * len(machine.joltage)

        if pattern not in combos[result]:
            combos[result][pattern] = len(buttons)

    cache = {
        tuple(np.zeros_like(machine.joltage)): 0,
    }

    def recurse(joltage):
        if tuple(joltage) in cache:
            return cache[tuple(joltage)]

        valid_to_reduce = np.where(np.logical_and(joltage % 2 == 1, joltage > 0))[0]
        parity = pack_array(valid_to_reduce)
        patterns = combos[parity]


        min_recurse = np.inf
        next_joltage = np.zeros_like(joltage)
        for pattern, cost in patterns.items():
            np.subtract(joltage, pattern, out=next_joltage)
            if next_joltage.min() < 0:
                continue
            next_joltage //= 2
            min_recurse = min(min_recurse, 2 * recurse(next_joltage) + cost)

        cache[tuple(joltage)] = min_recurse
        return min_recurse

    result = recurse(machine.joltage)
    return result


def task2(input):
    return round(sum(joltage_presses(machine) for machine in input))


def parse(data: str):
    lines = util.as_lines(data)
    return [Machine(line) for line in lines]


def main():
    data: str = util.get(10, 2025)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
