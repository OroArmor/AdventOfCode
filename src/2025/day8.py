from collections import defaultdict

import util
from util import *
import numpy as np

test_data: str = \
    """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

DISTANCES = None


def add_link(i, j, junctions, circuits):
    if i in junctions.keys() and j in junctions.keys():
        if junctions[i] == junctions[j]:
            pass
        else:
            to = min(junctions[i], junctions[j])
            _from = max(junctions[i], junctions[j])
            for junc in circuits[_from]:
                junctions[junc] = to
                circuits[to].add(junc)
            circuits[_from] = set()
    elif i in junctions.keys():
        junctions[j] = junctions[i]
        circuits[junctions[i]].add(j)
    elif j in junctions.keys():
        junctions[i] = junctions[j]
        circuits[junctions[j]].add(i)
    else:
        c = len(circuits)
        junctions[i] = c
        junctions[j] = c
        circuits[c].add(i)
        circuits[c].add(j)


P1_CHECKPOINT = None


def task1(input):
    global DISTANCES, P1_CHECKPOINT

    points = np.array(input)
    diff = points[:, None, :] - points[None, :, :]
    dist_sq = np.sum(diff ** 2, axis=-1)
    I, J = np.triu_indices(len(points), k=1)
    dist_sq = dist_sq[I, J]
    DISTANCES = np.argsort(dist_sq)

    circuits = defaultdict(set)
    junctions = {}
    for k in range(10 if len(input) == 20 else 1000):
        i, j = I[DISTANCES[k]], J[DISTANCES[k]]
        add_link(i, j, junctions, circuits)

    P1_CHECKPOINT = (junctions, circuits, I, J)

    return reduce(int.__mul__, list(sorted(map(len, circuits.values())))[-3:], 1)


def task2(input):
    junctions, circuits, I, J = P1_CHECKPOINT
    for k in itertools.count(10 if len(input) == 20 else 1000):
        i, j = I[DISTANCES[k]], J[DISTANCES[k]]
        add_link(i, j, junctions, circuits)

        if len(circuits[junctions[j]]) == len(input) or len(circuits[junctions[i]]) == len(input):
            return input[i][0] * input[j][0]


def parse(data: str):
    points = util.as_csv_lines_of_ints(data)
    return points


def main():
    data: str = util.get(8, 2025)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
