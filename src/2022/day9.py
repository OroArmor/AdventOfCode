import time

import util
import numpy as np

test_data: str = \
    """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

# test_data = """R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2"""

def task1(input):
    visited = np.zeros((1000, 1000), dtype=bool)
    head = np.array([0, 0])
    tail = np.array([0, 0])

    for inst in input:
        dir = inst[0]
        count = int(inst.split(" ")[1])

        # print(f"== {inst} ==\n")

        for _ in range(count):
            past_head = head.copy()
            if dir == "R":
                head += np.array([1, 0])
            elif dir == "L":
                head += np.array([-1, 0])
            elif dir == "U":
                head += np.array([0, 1])
            elif dir == "D":
                head += np.array([0, -1])


            if (head[0] == tail[0] or head[1] == tail[1]) and np.abs(head - tail).sum() > 1:
                tail = past_head
            elif np.abs(head - tail).sum() >= 3:
                tail = past_head

            visited[tail[0], tail[1]] = True



    return visited.sum()


def task2(input):
    visited = np.zeros((1000, 1000), dtype=bool)
    knots = np.zeros((10, 2), dtype=int)

    for inst in input:
        dir = inst[0]
        count = int(inst.split(" ")[1])

        for _ in range(count):
            if dir == "R":
                knots[0] += np.array([1, 0])
            elif dir == "L":
                knots[0] += np.array([-1, 0])
            elif dir == "U":
                knots[0] += np.array([0, 1])
            elif dir == "D":
                knots[0] += np.array([0, -1])

            for i in range(1, len(knots)):
                diff = knots[i - 1] - knots[i]
                if np.abs(diff).sum() == 0:
                    a = 1  # dont move
                elif np.abs(diff).sum() == np.max(np.abs(diff)):  # straight movement
                    if np.max(diff) > 2:
                        print(f"Move {i} more than two straight: {diff}")
                    if np.max(np.abs(diff)) != 1:
                        knots[i] += (diff / np.max(np.abs(diff))).astype(int)
                else:  # diagonal
                    if diff[0] == 2 and diff[1] == 1:
                        knots[i] += np.array([1, 1])
                    elif diff[0] == 1 and diff[1] == 2:
                        knots[i] += np.array([1, 1])

                    elif diff[0] == -2 and diff[1] == 1:
                        knots[i] += np.array([-1, 1])
                    elif diff[0] == -1 and diff[1] == 2:
                        knots[i] += np.array([-1, 1])

                    elif diff[0] == 2 and diff[1] == -1:
                        knots[i] += np.array([1, -1])
                    elif diff[0] == 1 and diff[1] == -2:
                        knots[i] += np.array([1, -1])

                    elif diff[0] == -2 and diff[1] == -1:
                        knots[i] += np.array([-1, -1])
                    elif diff[0] == -1 and diff[1] == -2:
                        knots[i] += np.array([-1, -1])

                    elif abs(diff[0]) == abs(diff[1]):
                        if abs(diff[0]) != 1:
                            knots[i] += (diff / np.max(np.abs(diff))).astype(int)
                    else:
                        print(f"{i} fuck {diff}")

            # print(f"{knots[9][0]}, {knots[9][1]}")
            visited[knots[9][0], knots[9][1]] = True

    return visited.sum()


def parse(data: str):
    return util.as_lines(data)


def main():
    data: str = util.get(9, 2022)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
