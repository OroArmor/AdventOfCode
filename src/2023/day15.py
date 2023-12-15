from functools import reduce

import util

test_data: str = \
    """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""


def hash(s):
    return reduce(lambda h, c: ((h + ord(c)) * 17) % 256, s, 0)


def task1(input):
    return sum([hash(s) for s in input])


def task2(input):
    data = [list() for _ in range(256)]

    for s in input:
        if s.endswith("-"):
            h = hash(s[:len(s) - 1])
            for i, d in enumerate(data[h]):
                if s.startswith(d[0]):
                    data[h].remove(d)
        else:
            n, v = s.split("=")
            h = hash(n)
            v = int(v)

            for i, d in enumerate(data[h]):
                if d[0] == n:
                    data[h][i] = (n, v)
                    break
            else:
                data[h].append((n, v))

    return sum([sum([(box_index + 1) * (slot + 1) * value for slot, (_, value) in enumerate(box)]) for box_index, box in enumerate(data)])


def parse(data: str):
    lines = util.as_csv(data)
    return lines


def main():
    data: str = util.get(15, 2023)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
