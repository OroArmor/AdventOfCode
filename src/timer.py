import sys
from collections import defaultdict
from copy import deepcopy
from typing import Callable, Any, Tuple

import util
from time import time
from importlib import import_module


def time_lambda(input: Any, l: Callable[[Any], Any], print_output: str, max_iterations: int = 1000, max_time: float = 60.0) -> Tuple[float, Any]:
    total_time = 0.0
    iterations = 0
    output = None

    while iterations < max_iterations and total_time < max_time:
        this_input = deepcopy(input)
        t = time()
        output = l(this_input)
        total_time += time() - t
        iterations += 1
        percent = iterations / max_iterations
        if max_time / (total_time / iterations) < max_iterations:
            percent = total_time / max_time
        print(f"{print_output}{percent:>9.2%}", end="\r")

    return total_time / iterations, output


def time_day(year, day, max_iterations: int = 1000, max_time: float = 60.0) -> Tuple[float, float, float, float]:
    try:
        day_module = import_module(f"{year}.day{day}")
    except:
        return

    import re
    raw_day = int(re.findall(r"\d+", day)[0])

    raw_data = util.get(raw_day, year)
    output = ""
    output += f"Day {day:>2}: "
    print(output, end="\r")
    sys.stdout.flush()

    parse_time, parsed = time_lambda(raw_data, day_module.parse, output, max_iterations, max_time)
    output += f"{parse_time:.3E}, "
    print(output, end="\r")
    sys.stdout.flush()

    task1_time, _ = time_lambda(parsed, day_module.task1, output, max_iterations, max_time)
    output += f"{task1_time:.3E}, "
    print(output, end="\r")
    sys.stdout.flush()

    if day != 25:
        task2_time, _ = time_lambda(parsed, day_module.task2, output, max_iterations, max_time)
    else:
        task2_time = 0.0
    output += f"{task2_time:.3E}, {parse_time + task1_time + task2_time:.3E}"
    print(output, end="\r\n")
    return parse_time, task1_time, task2_time, parse_time + task1_time + task2_time


def main():
    args = sys.argv

    selected_year = None
    selected_day = None
    iterations = 1000
    max_time = 60.0

    if any([arg.startswith("--") for arg in args]):
        if "--year" in args:
            selected_year = int(args[args.index("--year") + 1])
        if "--day" in args:
            selected_day = args[args.index("--day") + 1]
        if "--iterations" in args:
            iterations = int(args[args.index("--iterations") + 1])
        if "--time" in args:
            max_time = float(args[args.index("--time") + 1])
    else:
        selected_year = None if len(args) < 2 else int(args[1])
        selected_day = None if len(args) < 3 else int(args[2] or 0)

    results = defaultdict(list)
    for year in [selected_year] if selected_year else range(2015, util.CURRENT_YEAR + 1):
        print(f"y{year:>5}:   Parsing,   Part 01,   Part 02,  Combined")
        total_parse, total_task1, total_task2, total = 0, 0, 0, 0
        for day in [selected_day] if selected_day else range(1, 25 + 1):
            result = time_day(year, str(day), max_iterations=iterations, max_time=max_time)
            if result:
                par, p1, p2, tot = result
                total_parse += par
                total_task1 += p1
                total_task2 += p2
                total += tot
                results[year].append((day, (par, p1, p2, tot)))
        if not selected_day:
            print(f"Total : {total_parse:.3E}, {total_task1:.3E}, {total_task2:.3E}, {total:.3E}")

    if "--graph" in args:
        import matplotlib.pyplot as plt
        plt.figure()
        plt.xlabel("Day")
        plt.ylabel("Time (s)")
        for year in sorted(results.keys()):
            days = []
            pars = []
            p1s = []
            p2s = []
            tots = []
            for day, (par, p1, p2, tot) in results[year]:
                days.append(day)
                pars.append(par)
                p1s.append(p1)
                p2s.append(p2)
                tots.append(tot)

            if len(days) != 0:
                plt.semilogy(days, tots, label=f"{year}")
                # plt.semilogy(days, pars, linestyle=":", label=f"{year} Parse", color=l.get_color())
                # plt.semilogy(days, p1s, linestyle="--", label=f"{year} P1", color=l.get_color())
                # plt.semilogy(days, p2s, linestyle="-.", label=f"{year} P2", color=l.get_color())
        plt.legend()
        plt.xlim([1, 25])
        plt.show()


if __name__ == "__main__":
    main()
