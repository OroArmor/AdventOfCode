import util
import numpy as np

test_data: str = \
    """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


def task1(input):
    acc = 0
    pc = 0

    visited_pcs = []

    while True:
        if pc in visited_pcs:
            break
        visited_pcs.append(pc)

        op = input[pc].split(" ")
        if op[0] == "nop":
            pc += 1
        elif op[0] == "acc":
            acc += int(op[1])
            pc += 1
        elif op[0] == "jmp":
            pc += int(op[1])

    return acc


def task2(input):
    for i in range(len(input)):
        acc = 0
        pc = 0

        visited_pcs = []

        infinite = False
        while pc < len(input):
            if pc in visited_pcs:
                infinite = True
                break
            visited_pcs.append(pc)

            op = input[pc].split(" ")
            if pc == i:
                op[0] = "jmp" if op[0] == "nop" else "nop"

            if op[0] == "nop":
                pc += 1
            elif op[0] == "acc":
                acc += int(op[1])
                pc += 1
            elif op[0] == "jmp":
                pc += int(op[1])

        if not infinite:
            return acc

    return -1

def parse(data):
    return util.as_lines(data)


def main():
    data: str = util.get(8, 2020)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
