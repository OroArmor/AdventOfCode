import util
from util import as_lines, get


def task1(data: [str]):
    total: int = 0
    for line in data:
        min:int = int(line[0:line.index('-')])
        max:int = int(line[line.index('-')+1:line.index(' ')])
        char = line[line.index(':')-1]

        count = line[line.index(':')+1:].count(char)
        if min <= count <= max:
            total += 1
    return total

def task2(data):
    total: int = 0
    for line in data:
        min: int = int(line[0:line.index('-')])
        max: int = int(line[line.index('-') + 1:line.index(' ')])
        char = line[line.index(':') - 1]

        pw = line[line.index(':') + 2:]
        if (pw[min-1] == char and pw[max-1] != char) or (pw[min-1] != char and pw[max-1] == char):
            total += 1
    return total

def parse(data):
    return util.as_lines(data)

def main():
    data = get(2, 2020)
#     data = """1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc""".split("\n")
    data = parse(data)
    print(task1(data))
    print(task2(data))


if __name__ == "__main__":
    main()