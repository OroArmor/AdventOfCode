import util
from util import *
import numpy as np

test_data: str = \
    """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""

GRAPH = None


@cache
def get_paths(node, target):
    paths = 0

    if node not in GRAPH:
        return 0

    for edge in GRAPH[node]:
        if edge == target:
            paths += 1
        else:
            paths += get_paths(edge, target)

    return paths


def task1(input):
    get_paths.cache_clear()
    global GRAPH
    GRAPH = input
    return get_paths("you", "out")


def task2(input):
    get_paths.cache_clear()
    middle_paths = get_paths("fft", "dac")
    if middle_paths == 0:
        return get_paths("svr", "dac") * get_paths("dac", "fft") * get_paths("fft", "out")

    return get_paths("svr", "fft") * middle_paths * get_paths("dac", "out")


def parse(data: str):
    lines = util.as_lines(data)

    graph = {}
    for line in lines:
        n, others = line.split(': ')
        graph[n] = set(others.split())

    return graph


def main():
    data: str = util.get(11, 2025)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
