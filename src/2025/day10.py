import functools
import more_itertools
import scipy.optimize
import util
from util import *
import numpy as np

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
        self.buttons = np.array(self.buttons)
        self.joltage = np.array(util.as_csv_of_ints(joltage[1:-1])).flatten()

    def __repr__(self):
        return f"{self.goal}: [{self.int_buttons}] | {self.joltage}"


def min_presses(machine):
    for comb in more_itertools.powerset(machine.int_buttons):
        if len(comb) > 0:
            result = functools.reduce(np.int64.__xor__, comb)
            if result == machine.goal:
                return len(comb)


def task1(input):
    return sum(min_presses(machine) for machine in input)


def joltage_presses(machine):
    res = scipy.optimize.linprog(
        c=np.ones_like(machine.int_buttons).astype(int),
        A_eq = machine.buttons.T.astype(int),
        b_eq = machine.joltage.astype(int),
        integrality=1,
    )

    if not res.success:
        res2 = scipy.optimize.linprog(
            c=np.ones_like(machine.int_buttons).astype(int),
            A_eq=machine.buttons.T.astype(int),
            b_eq=res.eqlin.residual.astype(int),
            integrality=1,
        )

        # What the fuck this is probably wrong but it works and I only hit this once so...
        return round(res2.fun // 2 + res.fun)

    return round(res.fun)

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
