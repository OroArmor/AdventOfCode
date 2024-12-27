import sys
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


def time_day(year, day):
    try:
        day_module = import_module(f"{year}.day{day}")
    except:
        return

    raw_data = util.get(day, year)
    output = ""
    output += f"Day {day:>2}: "
    print(output, end="\r")
    sys.stdout.flush()

    parse_time, parsed = time_lambda(raw_data, day_module.parse, output)
    output += f"{parse_time:.3E}, "
    print(output, end="\r")
    sys.stdout.flush()

    task1_time, _ = time_lambda(parsed, day_module.task1, output)
    output += f"{task1_time:.3E}, "
    print(output, end="\r")
    sys.stdout.flush()

    if day != 25:
        task2_time, _ = time_lambda(parsed, day_module.task2, output)
    else:
        task2_time = 0.0
    output += f"{task2_time:.3E}, {parse_time + task1_time + task2_time:.3E}"
    print(output, end="\r\n")
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
