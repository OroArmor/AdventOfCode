import util
import numpy as np

test_data: str = \
    """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""


def task1(input):
    total = [0]
    val = 1
    inst = 1

    def check():
        if inst in [20, 60, 100, 140, 180, 220]:
            total[0] += inst * val

    for line in input:
        if line != "noop":
            inst += 1
            check()
            val += int(line.split(" ")[1])

        inst += 1
        check()
    return total[0]


def add_to_output(inst, output, val):
    row = inst // 40
    col = inst % 40

    if col == 0:
        output.append("")

    output[row] += "\u2588\u2588" if abs(val - col) < 2 else "  "


def task2(input):
    val = 1
    inst = 0
    output = []
    for line in input:
        if line != "noop":
            add_to_output(inst, output, val)
            inst += 1
            add_to_output(inst, output, val)
            inst += 1
            val += int(line.split(" ")[1])
        else:
            add_to_output(inst, output, val)
            inst += 1

    return output


def parse(data: str):
    return util.as_lines(data)


def main():
    data: str = util.get(10, 2022)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print("\n".join(task2(input)))


if __name__ == "__main__":
    main()
