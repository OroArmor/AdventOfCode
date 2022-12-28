from functools import reduce

import util
import numpy as np

test_data: str = \
    """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122"""


def snafu_to_decimal(s):
    total = 0
    for i, c in enumerate(reversed(s)):
        if c == "-":
            total += (5 ** i) * -1
        elif c == "=":
            total += (5 ** i) * -2
        else:
            total += (5 ** i) * int(c)
    return total


def decimal_to_snafu(j):
    s = ""
    i = 0
    og_j = j

    while 5 ** i < (5 * og_j):
        val = (j % (5 ** (i + 1)))
        snafu = val // (5 ** i)
        if 0 <= snafu <= 2:
            s = str(snafu) + s
            j -= (5 ** i) * snafu
        elif snafu == 3:
            s = "=" + s
            j += (5 ** i) * 2
        elif snafu == 4:
            s = "-" + s
            j += (5 ** i) * 1
        i += 1

    if s.startswith("0") and len(s) > 1:
        s = s[1:]
    return s


def task1(input):
    vals = [snafu_to_decimal(s) for s in input]
    total = reduce(lambda a, b: a + b, vals)
    return decimal_to_snafu(total)


def parse(data: str):
    lines = util.as_lines(data)
    return lines


def main():
    data: str = util.get(25, 2022)
    # data = test_data
    input = parse(data)
    print(task1(input))


if __name__ == "__main__":
    main()
