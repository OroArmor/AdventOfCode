import util
import numpy as np

test_data: str = \
    """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


def sum_dir(dir: str, dirs: dict) -> (int, int):
    this_total = 0
    sub_totals = 0
    for sub in dirs[dir].keys():
        if type(dirs[dir][sub]) == int:
            this_total += dirs[dir][sub]
        else:
            sub_tot = sum_dir(sub, dirs[dir])
            this_total += sub_tot[0]
            sub_totals += sub_tot[1]

            if sub_tot[0] <= 100000:
                sub_totals += sub_tot[0]

    return this_total, sub_totals


def task1(input):
    return sum_dir("/", input)


def sum_dir_to_remove(dir: str, dirs: dict, total_size: int) -> int:
    this_total = 0
    min_sub = -1
    for sub in dirs[dir].keys():
        if type(dirs[dir][sub]) == int:
            this_total += dirs[dir][sub]
        else:
            sub_tot = sum_dir_to_remove(sub, dirs[dir], total_size)
            if min_sub == -1 and sub_tot > total_size:
                min_sub = sub_tot
            elif min_sub > sub_tot > total_size:
                min_sub = sub_tot

            this_total += sub_tot

    if min_sub > total_size:
        return min_sub

    return this_total


def task2(input, total_size):
    return sum_dir_to_remove("/", input, total_size)


def parse(input: [str]):
    dirs = {"/": {}}

    i = 0
    stack = []
    current_dir = dirs
    while i < len(input):
        if input[i].startswith("$ cd "):
            if ".." not in input[i]:
                stack.append(current_dir)
                current_dir = current_dir[input[i][5:]]
                i += 1  # skip "$ ls"
            else:
                current_dir = stack.pop()
        elif current_dir != "":
            tokens = input[i].split(" ")
            if tokens[0] == "dir":
                current_dir[tokens[1]] = {}
            else:
                current_dir[tokens[1]] = int(tokens[0])

        i += 1

    return dirs

def main():
    data: str = util.get(7, 2022)
    # data = test_data
    input = util.as_lines(data)
    input = parse(input)

    t1 = task1(input)
    print(task1(input)[1])
    print(task2(input, t1[0] - 40000000))


if __name__ == "__main__":
    main()
