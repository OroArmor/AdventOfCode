from collections import defaultdict

import util
from util import *
import numpy as np

test_data: str = \
    """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

CORRECT = []

def task1(input):
    global CORRECT
    orders, updates = input
    CORRECT = []

    total = 0
    for e, update in enumerate(updates):
        for i in range(len(update)):
            if not set(update[i+1:]).issubset(orders[update[i]]):
                break
        else:
            CORRECT.append(e)
            total += update[len(update)//2]

    return total


def task2(input):
    global CORRECT
    orders, updates = input

    total = 0
    for e, update in enumerate(updates):
        if e in CORRECT:
            continue

        i = 0
        remaining = set(update[i + 1:])
        while i < len(update):
            if not remaining.issubset(orders[update[i]]):
                j = i + 1
                while update[j] in orders[update[i]]:
                    j += 1

                temp = update[i]
                remaining.add(temp)
                update[i] = update[j]
                remaining.remove(update[j])
                update[j] = temp
            else:
                i += 1
                if i != len(update):
                    remaining.remove(update[i])
                continue
        total += update[len(update) // 2]

    return total


def parse(data: str):
    orders, updates = util.as_double_lines(data)

    order_pairs = [util.list_as_ints(line.split("|")) for line in util.as_lines(orders)]
    orders = defaultdict(set)
    for pair in order_pairs:
        orders[pair[0]].add(pair[1])

    updates = util.as_csv_lines_of_ints(updates)

    return orders, updates


def main():
    data: str = util.get(5, 2024)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
