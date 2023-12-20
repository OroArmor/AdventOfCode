from collections import defaultdict
from copy import deepcopy

import util
from util import *

test_data: str = \
    """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""


class Rule:
    def __init__(self, partpart: int, cond, val, to):
        self.partpart = partpart
        self.cond = cond
        self.val = val
        self.to = to

    def test(self, part) -> bool:
        if self.cond is None:  # Last condition
            return True
        elif self.cond == "<":
            return part[self.partpart] < self.val
        elif self.cond == ">":
            return part[self.partpart] > self.val


def task1(input):
    mappings, rules = input

    to_map = {"in": rules}

    accepted = []
    while to_map:
        new_map = defaultdict(list)

        for mapping in to_map:
            for part in to_map[mapping]:
                to = next(filter(lambda rule: rule.test(part), mappings[mapping])).to

                if to == "A":
                    accepted.append(part)
                elif to != "R":
                    new_map[to].append(part)

        to_map = new_map

    return sum([sum(part) for part in accepted])


def task2(input):
    mappings, _ = input

    start: [Range] = [Range(1, 4000, True), Range(1, 4000, True), Range(1, 4000, True), Range(1, 4000, True)]

    to_map = {"in": [start]}

    accepted = []

    while to_map:
        new_map = defaultdict(list)

        for mapping_name in to_map:
            mapping = mappings[mapping_name]
            for part in to_map[mapping_name]:
                for rule in mapping:
                    keep, give = None, None
                    if rule.cond is None:
                        new_map[rule.to].append(part)
                        continue
                    elif rule.cond == "<":
                        if part[rule.partpart].end < rule.val:
                            new_map[rule.to].append(part)
                            continue
                        elif part[rule.partpart].start < rule.val:
                            give, keep = part[rule.partpart].split_on(rule.val)
                    elif rule.cond == ">":
                        if part[rule.partpart].start > rule.val:
                            new_map[rule.to].append(part)
                            continue
                        elif part[rule.partpart].end > rule.val:
                            keep, give = part[rule.partpart].split_on(rule.val + 1)

                    part_copy = deepcopy(part)
                    part_copy[rule.partpart] = give
                    new_map[rule.to].append(part_copy)
                    part[rule.partpart] = keep

        for part in new_map["A"]:
            accepted.append(part)

        if "A" in new_map:
            del new_map["A"]
        if "R" in new_map:
            del new_map["R"]

        to_map = new_map

    return sum([reduce(int.__mul__, [len(part_range) for part_range in part], 1) for part in accepted])


def parse(data: str):
    mappings, parts = util.as_double_lines(data)

    mapping_lines = util.as_lines(mappings)
    part_lines = util.as_lines(parts)

    mappings = {}

    pp_to_idx = {"x": 0, "m": 1, "a": 2, "s": 3}

    for mapping_line in mapping_lines:
        ob, cb = mapping_line.index("{"), mapping_line.index("}")

        name = mapping_line[:ob]
        rule_str = util.as_csv(mapping_line[ob + 1: cb])

        rules = []

        for rule in rule_str:
            if ":" in rule:
                pp = rule[0]
                cond = rule[1]
                val, to = util.split_on_colon(rule)

                rules.append(Rule(pp_to_idx[pp], cond, int(val[2:]), to))
            else:
                rules.append(Rule(-1, None, None, rule))

        mappings[name] = rules

    parts = []
    for part_line in part_lines:
        x, m, a, s = util.as_csv(part_line[1: -1])
        parts.append([int(x[2:]), int(m[2:]), int(a[2:]), int(s[2:])])

    return mappings, parts


def main():
    data: str = util.get(19, 2023)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
