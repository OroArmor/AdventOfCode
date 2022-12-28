import util
import numpy as np

test_data: str = \
    """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


class Monkey:
    def __init__(self, items, op, test, t, f):
        self.items = items
        self.op = op
        self.test = test
        self.t = t
        self.f = f

    def inspect(self, round_two) -> [(int, np.ndarray)]:
        new_items = self.op(np.array(self.items))
        if not round_two:
            new_items //= 3
        passed = self.test(new_items).astype(bool)

        return [(self.t, new_items[passed]), (self.f, new_items[passed == False])]


def task1(input):
    seen = [0 for _ in input]

    for _ in range(20):
        for i, m in enumerate(input):
            seen[i] += len(m.items)
            res = m.inspect(False)
            m.items = []
            input[res[0][0]].items += res[0][1].tolist()
            input[res[1][0]].items += res[1][1].tolist()

    seen.sort()
    return seen[-1] * seen[-2]


def task2(input):
    seen = [0 for _ in input]

    for _ in range(10000):
        for i, m in enumerate(input):
            seen[i] += len(m.items)
            res = m.inspect(True)
            m.items = []
            input[res[0][0]].items += res[0][1].tolist()
            input[res[1][0]].items += res[1][1].tolist()

    seen.sort()
    return seen[-1] * seen[-2]


def parse(data: str):
    monkey_s = util.as_double_lines(data)
    monkeys = []

    modulo_val = [1]

    for m_S in monkey_s:
        lines = util.as_lines(m_S)

        items = util.as_csv_of_ints(lines[1].split(": ")[1])
        op_l = lines[2].split(" ")

        def make_op():
            a_s = op_l[-3]
            b_s = op_l[-1]
            oper = op_l[-2]

            def op(old: int) -> int:
                a = old if a_s == "old" else int(a_s)
                b = old if b_s == "old" else int(b_s)

                ret = 0

                if oper == "+":
                    ret = a + b
                elif oper == "*":
                    ret = a * b
                else:
                    print(f"unknown op {oper}")

                return ret % modulo_val[0]
            return op

        def make_test():
            t = int(lines[3].split(" ")[-1])
            modulo_val[0] *= t

            def test(val: int) -> int:
                return val % t == 0
            return test

        monkeys.append(Monkey(items,
                              np.frompyfunc(make_op(), 1, 1),
                              np.frompyfunc(make_test(), 1, 1),
                              int(lines[4].split(" ")[-1]),
                              int(lines[5].split(" ")[-1])))

    return monkeys


def main():
    data: str = util.get(11, 2022)
    data = test_data
    input = parse(data)
    print(task1(input))
    input = parse(data)
    print(task2(input))


if __name__ == "__main__":
    main()
