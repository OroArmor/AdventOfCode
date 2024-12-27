import util
from util import *

test_data: str = \
    """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""

SIZE = 71

def task1(input):
    walls = set(input[0:1024])

    def neighbors(current):
        for dir in Direction.values():
            if (next := dir + current) not in walls:
                if 0 <= next.x < SIZE and 0 <= next.y < SIZE:
                    yield next, 1

    def is_end(current):
        return current == Point(SIZE - 1, SIZE - 1)

    _, _, cost = util.dijkstra(Point(0, 0), neighbors, is_end)
    return int(cost)


def task2(input):
    i = (1024, len(input))
    while i[0] != i[1] - 1:
        walls = set(input[0:(i[0] + i[1]) // 2])

        def neighbors(current):
            for dir in Direction.values():
                if (next := dir + current) not in walls:
                    if 0 <= next.x < SIZE and 0 <= next.y < SIZE:
                        yield next, 1

        def is_end(current):
            return current == Point(SIZE - 1, SIZE - 1)

        _, _, cost = util.dijkstra(Point(0, 0), neighbors, is_end)
        if cost is None:
            i = (i[0], (i[0] + i[1]) // 2)
        else:
            i = ((i[0] + i[1]) // 2, i[1])
    return f"{input[i[0]].x},{input[i[0]].y}"


def parse(data: str):
    bad = [Point(int(l.split(",")[0]), int(l.split(",")[1])) for l in data.split("\n")]

    return bad


def main():
    data: str = util.get(18, 2024)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
