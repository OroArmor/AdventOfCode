from util import *
import numpy as np

test_data: str = \
    """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""


def task1(input):
    seats = input

    loops = 0
    changed = True
    while changed:
        changed = False
        next_seats = {}

        for seat in seats.keys():
            nearby = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    check = (seat[0] + dx, seat[1] + dy)
                    if seat != check and check in seats:
                        nearby += 1 if seats[check] else 0

            if seats[seat] and nearby >= 4:
                next_seats[seat] = False
                changed = True
            else:
                if not seats[seat] and nearby == 0:
                    changed = True
                    next_seats[seat] = True
                else:
                    next_seats[seat] = seats[seat]

        seats = next_seats
        # changed = False
        loops += 1

    return len([0 for seat in seats if seats[seat]])


def task2(input):
    seats = input

    loops = 0
    changed = True

    max_size = max([max(seat) for seat in seats.keys()])

    while changed:
        changed = False
        next_seats = {}

        for seat in seats.keys():
            nearby = 0

            for dir in adjacent_directions():
                dist = 1

                check = seat
                while 0 <= check[0] <= max_size and 0 <= check[1] <= max_size:
                    check = (seat[0] + dir[0] * dist, seat[1] + dir[1] * dist)
                    if check in seats:
                        nearby += 1 if seats[check] else 0
                        break
                    dist += 1

            if seats[seat] and nearby >= 5:
                next_seats[seat] = False
                changed = True
            else:
                if not seats[seat] and nearby == 0:
                    changed = True
                    next_seats[seat] = True
                else:
                    next_seats[seat] = seats[seat]

        seats = next_seats
        loops += 1
        # print(seats)

    return len([0 for seat in seats if seats[seat]])


def parse(data: str):
    lines = as_lines(data)
    seats = {}

    for x, line in zip(range(len(lines)), lines):
        for y,c in zip(range(len(line)), line):
            if c == 'L':
                seats[x, y] = False

    return seats


def main():
    data: str = get(11, 2020)
    # data = test_data
    input = parse(data)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
