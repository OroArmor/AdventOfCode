from collections import defaultdict

import util
import igraph
from util import *
import numpy as np

test_data: str = \
    """jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr"""


def task1(input):
    cut = input.mincut()

    return len(cut.partition[0]) * len(cut.partition[1])


def parse(data: str):
    lines = util.as_lines(data)

    graph = defaultdict(set)

    for line in lines:
        f, t = line.split(": ")
        t = t.split(" ")
        graph[f].update(set(t))

        for ts in t:
            graph[ts].add(f)

    return igraph.Graph.ListDict(graph)


def main():
    data: str = util.get(25, 2023)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))


if __name__ == "__main__":
    main()
