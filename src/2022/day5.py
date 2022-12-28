import re
import util
import numpy as np

test_data: str = \
    """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def task1(input):
    stack_count = (len(input[0]) + 1) // 4

    stacks = [[] for _ in range(stack_count)]

    i = 0
    while input[i + 1] != "":
        for j in range(stack_count):
            if input[i][j * 4 + 1] != " ":
                stacks[j].append(input[i][j * 4 + 1])
        i += 1


    for move in input[i + 2:]:
        moves = util.list_as_ints(re.findall("\\d+", move))
        moved = stacks[moves[1] - 1][0:moves[0]]
        for m in moved:
            stacks[moves[1] - 1].remove(m)
            stacks[moves[2] - 1].insert(0, m)

    ret = ""

    for stack in stacks:
        ret += stack[0]

    return ret


def task2(input):
    stack_count = (len(input[0]) + 1) // 4

    stacks = [[] for _ in range(stack_count)]

    i = 0
    while input[i + 1] != "":
        for j in range(stack_count):
            if input[i][j * 4 + 1] != " ":
                stacks[j].append(input[i][j * 4 + 1])
        i += 1

    for move in input[i + 2:]:
        moves = util.list_as_ints(re.findall("\\d+", move))
        moved = stacks[moves[1] - 1][0:moves[0]]
        for j, m in enumerate(moved):
            stacks[moves[1] - 1].remove(m)
            stacks[moves[2] - 1].insert(j, m)

    ret = ""

    for stack in stacks:
        ret += stack[0]

    return ret


def main():
    data: str = util.get(5, 2022)
    # data = test_data
    input = util.as_lines(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
