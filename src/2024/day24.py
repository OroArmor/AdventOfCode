import enum
from collections import defaultdict
from copy import deepcopy

import sympy
import sympy as sym

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

class Operation(enum.Enum):
    AND = 0
    OR = 1
    XOR = 2

    def op(self, a, b):
        if self == Operation.AND:
            return a & b
        elif self == Operation.OR:
            return a | b
        elif self == Operation.XOR:
            return a ^ b


def task1(input):
    inputs, gates = input
    inputs = deepcopy(inputs)

    @cache
    def solve(output):
        if output in inputs:
            return inputs[output]

        (op, a, b) = gates[output]
        a = solve(a)
        b = solve(b)

        return op.op(a, b)

    bin_val = "".join("1" if solve('z' + f"{bit:02d}") else "0" for bit in range(45, -1, -1))
    return int(bin_val, 2)


def task2(input):
    inputs, gates = input

    @cache
    def solve(output):
        if output in inputs:
            return sym.symbols(output)

        (op, a, b) = gates[output]
        a = solve(a)
        b = solve(b)

        return op.op(a, b)
    solve('z45')

    carries = {'44': 'z45'}
    for bit in range(44, -1, -1):
        z = 'z' + f"{bit:02d}"
        x = sym.symbols('x' + f"{bit:02d}")
        y = sym.symbols('y' + f"{bit:02d}")
        to_check = [z]
        seen = set()
        while to_check:
            g = to_check.pop(0)

            if g.startswith('x') or g.startswith('y'):
                continue

            eq = solve(g)

            if x not in eq.free_symbols and y not in eq.free_symbols:
                carries[f"{bit - 1:02}"] = g
                break

            (_, a2, b2) = gates[g]
            if a2 not in seen:
                to_check.append(a2)
                seen.add(a2)
            if b2 not in seen:
                to_check.append(b2)
                seen.add(b2)

    for bit in range(44, 0, -1):
        if f"{bit - 1:02}" not in carries:
            x = sym.symbols('x' + f"{bit - 1:02d}")
            y = sym.symbols('y' + f"{bit - 1:02d}")
            c = solve(carries[f"{bit - 2:02}"])
            carry_this = x & y | ((x ^ y) & c)
            for out, (op, _, _) in gates.items():
                if op == Operation.OR and solve(out) == carry_this:
                    carries[f"{bit - 1:02}"] = out

    swaps = set()
    for bit in range(44, 0, -1):
        bit_inputs = ['x' + f"{(int(bit)):02d}", 'y' + f"{(int(bit)):02d}", carries[f"{(int(bit) - 1):02d}"]]
        bit_outputs = ['z' + f"{(int(bit)):02d}", carries[f"{(int(bit)):02d}"]]
        bit_wires = set(bit_inputs) | set(bit_outputs) | {gates[bit_outputs[0]][1], gates[bit_outputs[0]][2], gates[bit_outputs[1]][1], gates[bit_outputs[1]][2]}

        x, y, c = sym.symbols('x y c')
        z_real = sym.logic.Xor(x, y, c)
        c_real = x & y | ((x ^ y) & c)

        def dfs(out, swap={}, depth=0):
            if depth > 3:
                return False

            if out.startswith("x"):
                return x
            elif out.startswith("y"):
                return y
            elif out == carries[f"{(int(bit) - 1):02d}"]:
                return c

            if out in swap.keys():
                out = swap[out]
            op, a, b = gates[out]
            return op.op(dfs(a, swap, depth + 1), dfs(b, swap, depth + 1))

        z_actual = dfs(bit_outputs[0])
        c_actual = dfs(bit_outputs[1])

        correct = z_real == z_actual and c_real == c_actual

        if not correct:
            for (a, b) in itertools.combinations(bit_wires - set(bit_inputs), 2):
                swap = {a: b, b: a}
                new_z = dfs(bit_outputs[0], swap)
                new_c = dfs(bit_outputs[1], swap)
                if new_z == z_real and new_c == c_real:
                    swaps.add(a)
                    swaps.add(b)

    return ",".join(sorted(swaps))


def parse(data: str):
    raw_inputs, raw_gates = util.as_double_lines(data)

    inputs = defaultdict(bool)
    for input in util.as_lines(raw_inputs):
        inp, v = input.split(": ")
        inputs[inp] = bool(int(v))

    gates = {}
    for gate in util.as_lines(raw_gates):
        gate, out = gate.split(" -> ")
        a, raw_op, b = gate.split(" ")
        op = None
        match raw_op:
            case "XOR":
                op = Operation.XOR
            case "OR":
                op = Operation.OR
            case "AND":
                op = Operation.AND
        gates[out] = (op, a, b)

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
