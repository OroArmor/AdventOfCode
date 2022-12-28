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


def task1(input):
    total = 0

    for dir in input.keys():
        if input[dir] <= 100000:
            total += input[dir]

    return total


def task2(input):
    total = 0

    for dir in input.keys():
        if input[dir] >= input["/"] - 40000000:
            if total == 0:
                total = input[dir]
            total = min(total, input[dir])

    return total


def parse(input: [str]):
    dirs = {}

    i = 0
    name = []
    while i < len(input):
        if input[i].startswith("$ cd "):
            if ".." not in input[i]:
                name.append(input[i][5:])
                i += 1  # skip "$ ls"
            else:
                name.pop()
        else:
            tokens = input[i].split(" ")
            if tokens[0] != "dir":
                for j in range(len(name)):
                    path = "/".join(name[:len(name) - j])
                    if path not in dirs.keys():
                        dirs[path] = 0
                    dirs[path] += int(tokens[0])

        i += 1

    return dirs


def main():
    data: str = util.get(7, 2022)
    # data = test_data
    input = util.as_lines(data)
    input = parse(input)

    print(input)
    print(len(input))

    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
