import util
import numpy as np

test_data: str = \
    """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""


def calc(monkeys, monkey):
    if type(monkeys[monkey]) is int:
        return monkeys[monkey]
    else:
        vals = monkeys[monkey]
        a = calc(monkeys, vals[0])
        b = calc(monkeys, vals[2])
        if vals[1] == "+":
            return a + b
        elif vals[1] == "-":
            return a - b
        elif vals[1] == "*":
            return a * b
        elif vals[1] == "/":
            return a // b


def task1(input):
    return calc(input, "root")


def reverse_search(monkeys, monkey, val):
    if monkey == "humn":
        return val

    start_val = calc(monkeys, monkeys[monkey][0])
    monkeys["humn"] += 100
    side = 0 if start_val != calc(monkeys, monkeys[monkey][0]) else 2

    vals = monkeys[monkey]
    if side == 0:
        if vals[1] == "+":
            # val = a + b => a = val - b
            val = val - calc(monkeys, vals[2])
        elif vals[1] == "-":
            # val = a - b => a = val + b
            val = val + calc(monkeys, vals[2])
        elif vals[1] == "*":
            # val = a * b => a = val // b
            val = val // calc(monkeys, vals[2])
        elif vals[1] == "/":
            # val = a // b => a = val * b
            val = val * calc(monkeys, vals[2])
    else:
        if vals[1] == "+":
            # val = a / b => b = val - a
            val = val - calc(monkeys, vals[0])
        elif vals[1] == "-":
            # val = a - b => b = a - val
            val = calc(monkeys, vals[0]) - val
        elif vals[1] == "*":
            # val = a * b => b = val // a
            val = val // calc(monkeys, vals[0])
        elif vals[1] == "/":
            # val = a // b => b = a // val
            val = calc(monkeys, vals[0]) // val

    return reverse_search(monkeys, monkeys[monkey][side], val)



def task2(input):
    start_val = calc(input, input["root"][0])
    input["humn"] = 0
    side = 0 if start_val != calc(input, input["root"][0]) else 2
    start_val = calc(input, input["root"][2 - side])

    input["humn"] = reverse_search(input, input["root"][side], start_val)

    return input["humn"]


def parse(data: str):
    lines = util.as_lines(data)

    monkeys = {}

    for line in lines:
        halves = line.split(": ")
        second_split = halves[1].split(" ")

        if len(second_split) == 1:
            monkeys[halves[0]] = int(second_split[0])
        else:
            monkeys[halves[0]] = second_split

    return monkeys


def main():
    data: str = util.get(21, 2022)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
