import sys
from copy import deepcopy

import util
from time import time
from importlib import import_module


def time_day(year, day):
    try:
        day_module = import_module(f"{year}.day{day}")
    except:
        return

    raw_data = util.get(day, year)

    parsed = None
    i = 0
    t = time()
    while i < 1000 and (time() - t) < 60:
        parsed = day_module.parse(raw_data)
        i += 1
    parse_time = (time() - t) / i

    i = 0
    t = time()
    while i < 1000 and (time() - t) < 60:
        day_module.task1(deepcopy(parsed))
        i += 1
    task1_time = (time() - t) / i

    if day != 25:
        i = 0
        t = time()
        while i < 1000 and (time() - t) < 60:
            day_module.task2(deepcopy(parsed))
            i += 1
        task2_time = (time() - t) / i
    else:
        task2_time = 0.0

    print(f"Day {day:>2}: {parse_time:.3E}, {task1_time:.3E}, {task2_time:.3E}, {parse_time + task1_time + task2_time:.3E}")
    return parse_time, task1_time, task2_time, parse_time + task1_time + task2_time


def main():
    args = sys.argv

    selected_year = None
    selected_day = None

    if any([arg.startswith("--") for arg in args]):
        if "--year" in args:
            selected_year = int(args[args.index("--year") + 1])
        if "--day" in args:
            selected_day = int(args[args.index("--day") + 1])
    else:
        selected_year = None if len(args) < 2 else int(args[1])
        selected_day = None if len(args) < 3 else int(args[2] or 0)

    for year in [selected_year] if selected_year else range(2015, util.CURRENT_YEAR + 1):
        print(f"y{year:>5}:   Parsing,   Part 01,   Part 02,  Combined")
        total_parse, total_task1, total_task2, total = 0, 0, 0, 0
        for day in [selected_day] if selected_day else range(1, 25 + 1):
            par, p1, p2, tot = time_day(year, day)
            total_parse += par
            total_task1 += p1
            total_task2 += p2
            total += tot
        if not selected_day:
            print(f"Total : {total_parse:.3E}, {total_task1:.3E}, {total_task2:.3E}, {total:.3E}")


if __name__ == "__main__":
    main()
