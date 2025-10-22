import util
from util import *
import numpy as np
import re

test_data: str = \
    """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""


def task1(input):
    mem = {}

    for program in input:
        zero_mask = sum(2 ** i for i in range(36) if program[0][35 - i] != "0")
        ones_mask = sum(2 ** i for i in range(36) if program[0][35 - i] == "1")

        for op in program[1]:
            mem[op[0]] = op[1] & zero_mask | ones_mask

    return sum(mem.values())


def task2(input):
    mem = {}

    for program in input:
        for op in program[1]:
            addr_str = f"{op[0]:036b}"

            mask = ""
            for i in range(len(addr_str)):
                if program[0][i] == "X":
                    mask += "X"
                elif addr_str[i] == "1" or program[0][i] == "1":
                    mask += "1"
                else:
                    mask += "0"

            split_mask = mask.split("X")
            for loc in range(2 ** program[0].count("X")):
                b = f"{loc:036b}"[::-1]
                addr = split_mask[0]
                for bit in range(program[0].count("X")):
                    addr += (b[bit])
                    addr += (split_mask[bit + 1])
                mem[int(addr, 2)] = op[1]

    return sum(mem.values())


def parse(data: str):
    program_strs = data.split("mask = ")

    programs = []

    for program in program_strs:
        if program.strip() == "":
            continue

        lines = util.as_lines(program.strip())
        mask = lines[0].strip()
        ops = []
        for line in lines[1:]:
            op = re.search("mem\\[(\d+)] = (\d+)", line).groups()
            ops.append((int(op[0]), int(op[1])))

        programs.append((mask, ops))

    return programs


def main():
    data: str = util.get(14, 2020)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
