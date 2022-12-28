import re
import timeit

import util
import numpy as np

test_data: str = \
    """Blueprint 1:  Each ore robot costs 4 ore.  Each clay robot costs 2 ore.  Each obsidian robot costs 3 ore and 14 clay.  Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2:  Each ore robot costs 2 ore.  Each clay robot costs 3 ore.  Each obsidian robot costs 3 ore and 8 clay.  Each geode robot costs 3 ore and 12 obsidian."""


def set_index(i):
    vals = np.zeros(4)
    vals[i] = 1
    return vals


def get_possible_robot_purchases(costs, materials) -> [(np.ndarray, np.ndarray)]:
    if np.min(materials - costs[3]) >= 0:
        return [(set_index(3), materials - costs[3])]
    elif np.min(materials - costs[2]) >= 0:
        return [(set_index(2), materials - costs[2])]

    possibilities = []
    for i, robot_cost in enumerate(reversed(costs[0:2])):
        new_materials = materials - robot_cost
        if np.min(new_materials) >= 0:
            purchase = set_index(1 - i)
            possibilities.append((purchase, new_materials))

    return possibilities


def find_max_geodes(costs, robots, materials, minutes_remaining, max_costs, cache):
    if minutes_remaining == 0:
        return robots[3]

    cache_key = (robots[0],
                 robots[1],
                 robots[2],
                 robots[3],
                 min(materials[0], max_costs[0] + 3),  # the +3 is because idk, it doesnt work otherwise, and not too hard of a perf hit
                 min(materials[1], max_costs[1] + 3),
                 min(materials[2], max_costs[2] + 3),
                 materials[3], minutes_remaining)

    if cache_key in cache.keys():
        return cache[cache_key]

    max_geodes = find_max_geodes(costs, robots, materials + robots, minutes_remaining - 1, max_costs, cache)  # dont buy any new robots

    for new_robots, new_materials in get_possible_robot_purchases(costs, materials):
        new_robots = robots + np.array(new_robots)

        for i in range(3):
            if new_robots[i] > max_costs[i]:
                break
        else:
            max_geodes = max(max_geodes, find_max_geodes(costs, new_robots, np.array(new_materials) + robots, minutes_remaining - 1, max_costs, cache))

    max_geodes += robots[3]

    if cache_key not in cache.keys() or cache[cache_key] < max_geodes:
        cache[cache_key] = max_geodes

    return max_geodes


def task1(input):
    quality_level = 0
    for i, cost in enumerate(input):
        geodes = find_max_geodes(cost, np.array([1, 0, 0, 0]), np.array([0, 0, 0, 0]), 23, np.max(cost, axis=0), {})
        quality_level += (i + 1) * geodes
    return int(quality_level)


def task2(input):
    max_geodes = 1
    for i, cost in enumerate(input):
        if i >= 3:
            break
        geodes = find_max_geodes(cost, np.array([1, 0, 0, 0]), np.array([0, 0, 0, 0]), 31, np.max(cost, axis=0), {})
        max_geodes *= geodes
    return int(max_geodes)


def parse(data: str):
    lines = util.as_lines(data)

    costs = []
    for blueprint in lines:
        ints = util.list_as_ints(re.findall("\\d+", blueprint))
        costs.append([[ints[1], 0, 0, 0], [ints[2], 0, 0, 0], [ints[3], ints[4], 0, 0], [ints[5], 0, ints[6], 0]])

    return np.array(costs)


def main():
    data: str = util.get(19, 2022)
    # data = test_data
    input = parse(data)

    def run():
        print(f"Time for task 1: {timeit.timeit(lambda: print(task1(input)), number=1)}")
        print(f"Time for task 2: {timeit.timeit(lambda: print(task2(input)), number=1)}")
    print(f"Total time: {timeit.timeit(run, number=1)}")


if __name__ == "__main__":
    main()
