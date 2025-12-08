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


def add_link(i, j, junctions):
    if junctions[i] != junctions[j]:
        to = min(junctions[i], junctions[j])
        _from = max(junctions[i], junctions[j])
        junctions[junctions == _from] = to


P1_CHECKPOINT = None


def task1(input):
    global DISTANCES, P1_CHECKPOINT

    points = np.array(input)
    I, J = np.triu_indices(len(points), k=1)
    diff = points[I] - points[J]
    dist_sq = np.einsum('ij,ij->i', diff, diff)

    upper_bound = (10_000 / len(dist_sq) * (dist_sq.max() - dist_sq.min()) + dist_sq.min()) * 2
    mask = dist_sq < upper_bound
    DISTANCES = np.argsort(dist_sq[mask])
    DISTANCES = np.where(mask)[0][DISTANCES]

    junctions = np.arange(len(points))
    for k in range(10 if len(input) == 20 else 1000):
        i, j = I[DISTANCES[k]], J[DISTANCES[k]]
        add_link(i, j, junctions)

    P1_CHECKPOINT = (junctions, I, J)

    return np.multiply.reduce(np.sort(np.unique_counts(junctions).counts)[-3:])


def task2(input):
    junctions, I, J = P1_CHECKPOINT
    for k in itertools.count(10 if len(input) == 20 else 1000):
        i, j = I[DISTANCES[k]], J[DISTANCES[k]]
        add_link(i, j, junctions)

        if np.all(junctions == 0):
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
