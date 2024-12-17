import util
import z3

test_data_p1: str = \
"""Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""

test_data_p2: str = \
    """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""


def task1(input):
    reg, prog = input

    reg = [*reg]
    out = []
    i = 0
    while i < len(prog):
        op = prog[i]
        val = prog[i + 1]
        combo = val
        if val > 3 and val != 7:
            combo = reg[val - 4]

        match op:
            case 0:
                reg[0] = reg[0] // (2 ** combo)
            case 1:
                reg[1] = (reg[1] ^ val)
            case 2:
                reg[1] = combo % 8
            case 3:
                if reg[0] != 0:
                    i = val - 2
            case 4:
                reg[1] = reg[1] ^ reg[2]
            case 5:
                out.append(str(combo % 8))
            case 6:
                reg[1] = reg[0] // (2 ** combo)
            case 7:
                reg[2] = reg[0] // (2 ** combo)
        i += 2
    return ",".join(out)


def task2(input):
    reg, prog = input
    a = z3.BitVec("a", 64)

    out = 0
    opt = z3.Optimize()
    h = opt.minimize(a)

    b, c = (None, None)
    i = 0
    while True:
        op = prog[i]
        val = prog[i + 1]
        combo = val
        if val == 4:
            combo = a
        elif combo == 5:
            combo = b
        elif combo == 6:
            combo = c

        match op:
            case 0:
                a = a >> combo
            case 1:
                b = (b ^ val)
            case 2:
                b = combo % 8
            case 3:
                i = val - 2
                if out == len(prog):
                    break
            case 4:
                b = b ^ c
            case 5:
                opt.add(combo % 8 == prog[out])
                out += 1
            case 6:
                b = a >> combo
            case 7:
                c = a >> combo
        i += 2
    opt.add(a == 0)

    opt.check()
    return opt.lower(h)


def parse(data: str):
    reg, prog = util.as_double_lines(data)
    regs = [int(l.split(": ")[1]) for l in util.as_lines(reg)]
    prog = util.as_csv_of_ints(prog.split(": ")[1])
    return regs, prog


def main():
    data: str = util.get(17, 2024)
    # data = test_data_p1
    input = parse(data)
    print(input)
    print(task1(input))
    if data == test_data_p1:
        input = parse(test_data_p2)
    print(task2(input))

if __name__ == "__main__":
    main()



