import re

import util
from util import *
import numpy as np

test_data: str = \
    """42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"""


def run_sequence(rules, rule_seq, string):
    if not rule_seq:
        yield string
    else:
        rule, *rule_seq = rule_seq
        for s in run(rules, rule, string):
            yield from run_sequence(rules, rule_seq, s)

def run_list(rules, rule_list, string):
    for rule in rule_list:
        yield from run_sequence(rules, rule, string)

def run(rules, rule, string):
    if isinstance(rules[rule], list):
        yield from run_list(rules, rules[rule], string)
    else:
        if string and string[0] == rules[rule]:
            yield string[1:]

def task1(input):
    rules, patterns = input
    return sum(any(m == "" for m in run(rules, '0', pattern)) for pattern in patterns)


def task2(input):
    rules, patterns = input
    rules['8'] = [['42'], ['42', '8']]
    rules['11'] = [['42', '31'], ['42', '11', '31']]

    return sum(any(m == "" for m in run(rules, '0', pattern)) for pattern in patterns)


def parse(data: str):
    lines = util.as_double_lines(data)

    rules = {}

    for line in util.as_lines(lines[0]):
        k, rule = line.split(': ')
        if rule[0] == '"':
            rule = rule[1:-1]
        else:
            rule = [seq.split(' ') if ' ' in seq else [seq]
                    for seq in (rule.split(' | ') if ' | ' in rule else [rule])]
        rules[k] = rule


    patterns = util.as_lines(lines[1])

    return rules, patterns


def main():
    data: str = util.get(19, 2020)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
