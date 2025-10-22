import util
import numpy as np

# test_data: str = \
#     """light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags."""

test_data: str = \
    """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""


class Bag:
    def __init__(self, t: str, holds: [(int, str)]):
        self.t = t
        self.holds = holds


def task1(input):
    target = "shiny gold"

    total = 0
    for t in input.keys():
        found = False
        holds = []
        holds += input[t].holds
        while not found and len(holds) > 0:
            hold = holds.pop()
            if hold[1] == target:
                found = True
                total += 1
            else:
                holds += input[hold[1]].holds

    return total


def get_count_for_bag(t: str, bags: dict):
    total = 1
    for hold in bags[t].holds:
        total += hold[0] * get_count_for_bag(hold[1], bags)
    return total


def task2(input):
    return get_count_for_bag("shiny gold", input) - 1


def parse(data) -> dict:
    lines = util.as_lines(data)
    bags = {}

    for line in lines:
        tokens = line.split(" ")
        t = tokens[0] + " " + tokens[1]

        holds = []
        for i in range(4, len(tokens), 4):
            if tokens[i] == "no":
                break
            c = int(tokens[i])
            n = tokens[i + 1] + " " + tokens[i + 2]
            holds.append((c, n))

        bags[t] = Bag(t, holds)

    return bags


def main():
    data: str = util.get(7, 2020)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
