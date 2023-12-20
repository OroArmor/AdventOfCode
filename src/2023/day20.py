import copy
from collections import defaultdict

import util
from util import *
import numpy as np

test_data: str = \
    """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""

BROAD, FF, CON = 0, 1, 2


def update_state(node, high, from_node, tasks, con_state, ff_state, nodes):
    if node in nodes:
        t, receivers = nodes[node]

        if t == BROAD:
            for r in receivers:
                tasks.append((r, high, node))
        elif t == FF and not high:
            ff_state[node] = not ff_state[node]
            for r in receivers:
                tasks.append((r, ff_state[node], node))
        elif t == CON:
            con_state[node][from_node] = high
            val = not all(con_state[node].values())
            for r in receivers:
                tasks.append((r, val, node))


def task1(nodes):
    high_count, low_count = 0, 0

    ff_state = defaultdict(lambda: False)
    con_state = {
        con: {
            n: False for n in nodes if con in nodes[n][1]
        } for con in nodes if nodes[con][0] == CON
    }

    for _ in range(1000):
        tasks = [("broadcaster", False, "button")]
        while tasks:
            node, high, from_node = tasks.pop(0)

            if high:
                high_count += 1
            else:
                low_count += 1

            update_state(node, high, from_node, tasks, con_state, ff_state, nodes)

    return high_count * low_count


def task2(nodes):
    ff_state = defaultdict(lambda: False)
    con_state = {
        con: {
            n: False for n in nodes if con in nodes[n][1]
        } for con in nodes if nodes[con][0] == CON
    }

    before_rx = [n for n in nodes if "rx" in nodes[n][1]][0]
    cycles = {n: None for n in con_state if before_rx in nodes[n][1]}

    press = 0
    while any(v is None for v in cycles.values()):
        press += 1
        tasks = [("broadcaster", False, "button")]
        while tasks:
            node, high, from_node = tasks.pop(0)

            if node in cycles and not high:
                cycles[node] = press

            if node == "rx" and not high:
                return press

            update_state(node, high, from_node, tasks, con_state, ff_state, nodes)

    return lcm(cycles.values())


def parse(data: str):
    lines = util.as_lines(data)

    data = {}

    for line in lines:
        f, t = line.split(" -> ")
        t = util.as_csv(t)

        if f == "broadcaster":
            data[f] = (BROAD, t)
        else:
            data[f[1:]] = (FF if f[0] == "%" else CON, t)

    return data


def main():
    data: str = util.get(20, 2023)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
