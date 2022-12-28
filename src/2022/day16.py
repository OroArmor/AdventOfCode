import re
from collections import defaultdict
from functools import reduce

import util
import numpy as np

test_data: str = \
    """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""


def search(valve, minutes, mask, cache, node_ids, connections, flow_rates):
    if minutes == 0:
        return 0
    if cache[valve][minutes][mask] == -1:
        best = max(search(v, minutes - 1, mask, cache, node_ids, connections, flow_rates) for v in connections[valve])
        node_bit = 1 << node_ids[valve]
        if node_bit & mask:
            best = max(best, search(valve, minutes - 1, mask - node_bit, cache, node_ids, connections, flow_rates) + flow_rates[valve] * (minutes - 1))
        cache[valve][minutes][mask] = best
    return cache[valve][minutes][mask]


def task1(input):
    connections, flow_rates, cache, node_ids, ALL_MASK = input
    return search("AA", 30, ALL_MASK, cache, node_ids, connections, flow_rates)


def task2(input):
    connections, flow_rates, cache, node_ids, ALL_MASK = input
    return max([
        search("AA", 26, ALL_MASK - mask, cache, node_ids, connections, flow_rates) +
        search("AA", 26, mask, cache, node_ids, connections, flow_rates)
        for mask in range(ALL_MASK + 1)])


def parse(data: str):
    lines = util.as_lines(data)

    connections = {}
    flow_rates = {}

    for line in lines:
        match = re.search("Valve (\\w\\w) has flow rate=(\\d+); tunnels? leads? to valves? (.*)", line)
        groups = match.groups()

        connections[groups[0]] = util.as_csv(groups[2])
        flow_rates[groups[0]] = int(groups[1])

    node_ids = defaultdict(lambda: len(node_ids))
    [node_ids[valve] for valve in flow_rates if flow_rates[valve]]
    ALL_MASK = (1 << len(node_ids)) - 1

    cache = defaultdict(lambda: [[-1 for mask in range(ALL_MASK + 1)] for t in range(31)])

    return connections, flow_rates, cache, node_ids, ALL_MASK


def main():
    data: str = util.get(16, 2022)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
