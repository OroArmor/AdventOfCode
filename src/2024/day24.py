from collections import defaultdict
from copy import deepcopy

import sympy

import util
from util import *
import numpy as np

test_data: str = \
    """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""


def task1(input):
    inputs, gates = input
    inputs = deepcopy(inputs)

    # past_len = 0
    # while past_len != len(inputs.keys()):
    for _ in range(100):
        for (op, a, b, out) in gates:
            if a in inputs and b in inputs:
                inputs[out] = op(inputs[a], inputs[b])

    zs = []
    for k in inputs.keys():
        if k.startswith("z"):
            zs.append((k, inputs[k]))

    zs = sorted(zs)
    bin_val = "".join("1" if z[1] else "0" for z in reversed(zs))

    return int(bin_val, 2)


def task2(input):
    inputs, gates = input
    input_keys = inputs.keys()
    inputs = {}
    for input in sorted(input_keys):
        inputs[input] = sympy.symbols(input)

    swaps = {"gmt": "z07", "z07": "gmt", "cbj": "qjj", "qjj": "cbj", "z18": "dmn", "dmn": "z18", "cfk": "z35", "z35": "cfk"}

    for _ in range(100):
        for (op, a, b, out) in gates:
            if a in inputs and b in inputs:
                if out in swaps:
                    out = swaps[out]
                inputs[out] = op(inputs[a], inputs[b])

    zs = []
    for k in inputs.keys():
        if k.startswith("z"):
            zs.append((k, inputs[k]))

    # for (op, a, b, out) in gates:
    #     o = op(True, True) and op(True, False)
    #     xor = op(True, False)
    #
    #     print(f"{out}[shape=\"{'oval' if o else ('Mdiamond' if xor else 'box')}\"];")
    #     print(f"{a} -> {out}; {b} -> {out};")


    zs = sorted(zs)
    for i, z in enumerate(zs):
        print(z[0], z[1])
        # bin_val = "".join("1" if z[1] else "0" for z in reversed(zs))
        # print(input, bin_val)

    return ",".join(sorted(swaps.keys()))


def parse(data: str):
    raw_inputs, raw_gates = util.as_double_lines(data)

    inputs = defaultdict(bool)
    for input in util.as_lines(raw_inputs):
        inp, v = input.split(": ")
        inputs[inp] = bool(int(v))

    gates = []
    for gate in util.as_lines(raw_gates):
        gate, out = gate.split(" -> ")
        a, raw_op, b = gate.split(" ")
        op = None
        match raw_op:
            case "XOR":
                op = lambda c, d: sympy.logic.Xor(c, d)
            case "OR":
                op = lambda c, d: sympy.logic.Or(c, d)
            case "AND":
                op = lambda c, d: sympy.logic.And(c, d)
        gates.append((op, a, b, out))

    return inputs, gates


def main():
    data: str = util.get(24, 2024)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
