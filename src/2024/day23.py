from collections import defaultdict
import util
from util import *

test_data: str = \
    """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""


def task1(input: dict[str, set]):
    valid = set()
    seen = set()
    for a in input.keys():
        seen.add(a)
        for b in input[a]:
            if b not in seen:
                overlap = input[a].intersection(input[b])
                for c in overlap:
                    if c not in seen:
                        if a.startswith("t") or b.startswith("t") or c.startswith("t"):
                            valid.add(tuple(sorted([a, b, c])))
    return len(valid)


def task2(input: dict[str, set]):
    best = set()
    seen = set()
    for a in input.keys():
        if a in seen:
            continue
        seen.add(a)

        all_combinations = []
        for r in range(len(best), len(input[a]) + 1):
            combinations = itertools.combinations(input[a], r)
            all_combinations.extend(combinations)

        for combination in all_combinations:
            this_comb = (*combination, a)
            for sub in combination:
                if not all(c in input[sub] for c in this_comb if c != sub):
                    break
            else:
                if len(this_comb) > len(best):
                    best = this_comb

        seen |= input[a]
    return ",".join(sorted(best))


def parse(data: str):
    lines = util.as_lines(data)

    graph = defaultdict(set)
    for line in lines:
        a, b = line.split("-")
        graph[a].add(b)
        graph[b].add(a)

    return graph


def main():
    data: str = util.get(23, 2024)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
