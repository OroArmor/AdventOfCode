from collections import defaultdict
import util
from util import *
import numpy as np
import z3

test_data: str = \
    """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""


def bool_array_to_int(array: np.ndarray) -> int:
    return np.sum(array * np.power(2, np.arange(len(array))))


class Machine:
    def __init__(self, line):
        goal, *raw_buttons, joltage = line.split()

        self.goal = bool_array_to_int(np.array(list(goal))[1:-1] == "#")
        self.buttons = []
        self.int_buttons = []

        for raw in raw_buttons:
            button = np.zeros(len(goal) - 2, dtype=bool)
            raw = util.as_csv_of_ints(raw[1:-1])
            button[raw] = True
            self.int_buttons.append(bool_array_to_int(button))
            self.buttons.append(button)
        self.joltage = np.array(util.as_csv_of_ints(joltage[1:-1])).flatten()

    def __repr__(self):
        return f"{self.goal}: [{self.int_buttons}] | {self.joltage}"


def min_presses(machine, state, presses, cache, uses):
    if state in cache.keys():
        if cache[state][0] <= presses:
            return cache[state][1]

    min_press = 10000000000000000000
    for button in machine.int_buttons:
        if uses[button] >= 1:
            continue
        uses[button] += 1
        next_state = state ^ button
        if next_state != machine.goal:
            min_press = min(
                min_press,
                min_presses(machine, next_state, presses + 1, cache, uses)
            )
        else:
            min_press = presses + 1
        uses[button] -= 1

    cache[state] = (presses, min_press)
    return min_press


def task1(input):
    return sum(min_presses(machine, 0, 0, {}, defaultdict(int)) for machine in input)


def joltage_presses(machine):
    buttons = [z3.Int(f"b{i}") for i in range(len(machine.int_buttons))]

    opt = z3.Optimize()
    h = opt.minimize(z3.Sum(*buttons))

    eqs = [
        0 for _ in range(len(machine.joltage))
    ]
    for i, button in enumerate(machine.buttons):
        opt.add(buttons[i] >= 0)
        for j, a in enumerate(button):
            if a:
                eqs[j] += buttons[i]
    for j, joltage in enumerate(machine.joltage):
        opt.add(eqs[j] == joltage)
    opt.check()
    return opt.lower(h).as_long()


def task2(input):
    return sum(joltage_presses(machine) for machine in input)


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
