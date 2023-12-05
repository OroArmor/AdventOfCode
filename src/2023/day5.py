import util
from util import *
import numpy as np

test_data: str = \
    """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def task1(input):
    print(input)

    seeds, maps = input

    for map in maps:
        next = []

        for seed in seeds:
            res = seed
            for m_range in map:
                if 0 <= seed - m_range[1] < m_range[2]:
                    res = seed - m_range[1] + m_range[0]
            next.append(res)

        seeds = next

    return min(seeds)


def task2(input):
    seeds, maps = input

    seeds2 = []
    for i in range(0, len(seeds), 2):
        seeds2.append((seeds[i], seeds[i] + seeds[i + 1] - 1))
    seeds = seeds2

    for i, map in enumerate(maps):
        next = []

        for seed in seeds:
            res = []
            for m_range in map:
                if 0 <= seed[0] - m_range[1] < m_range[2]:  # lower end is within the range
                    if 0 <= seed[1] - m_range[1] < m_range[2]: # upper end is within the range
                        # map whole seed
                        res.append((seed[0] - m_range[1] + m_range[0], seed[1] - m_range[1] + m_range[0]))
                        seed = (0, 0)
                    else:
                        # map low to range top, keep range top to high as seed
                        res.append((seed[0] - m_range[1] + m_range[0], m_range[0] + m_range[2] - 1))
                        seed = (m_range[2] + m_range[1], seed[1])
                else:
                    if 0 <= seed[1] - m_range[1] < m_range[2]: # upper end is within the range
                        # keep low to range bottom, map range bottom to high as seed
                        res.append((m_range[0], seed[1] - m_range[1] + m_range[0]))
                        seed = (seed[0], m_range[1] - 1)
                    else:
                        if seed[0] < m_range[1] and m_range[1] + m_range[2] < seed[1]: # completely enclosed
                            # res.append((seed[0] - m_range[1] + m_range[0], seed[0] + m_range[2] - m_range[1] + m_range[0]))
                            # res.append((seed[1] - m_range[2] - m_range[1] + m_range[0], seed[1] - m_range[1] + m_range[0]))
                            # seed = (seed[0] + m_range[2] + 1, seed[1] - m_range[2])
                            print("mid")
            if len(res) == 0 or seed != (0, 0):
                res += [seed]

            next += res
        seeds = next

    return min([seed[0] for seed in seeds])

def parse(data: str):
    lines = util.as_double_lines(data)

    seeds = as_ssv_ints(split_on_colon(lines[0])[1])

    maps = []
    for i in range(1, len(lines)):
        map_lines = as_lines(lines[i])[1:]
        maps.append([as_ssv_ints(map_line) for map_line in map_lines])

    return seeds, maps


def main():
    data: str = util.get(5, 2023)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
