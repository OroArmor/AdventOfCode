import util
from util import *
import numpy as np

test_data: str = \
    """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."""


def task1(input):
    board_edges = {}

    for board, pixels in input.items():
        left = [pixel[1] for pixel in pixels if pixel[0] == 0]
        right = [pixel[1] for pixel in pixels if pixel[0] == 9]
        up = [pixel[0] for pixel in pixels if pixel[1] == 0]
        down = [pixel[0] for pixel in pixels if pixel[1] == 9]

        board_edges[board] = (left, right, up, down)

    result = 1
    edge_match = {}

    for board in board_edges:
        matches = 0
        for i, edge in enumerate(board_edges[board]):
            for second_board in board_edges:
                if second_board != board:
                    for j, second_edge in enumerate(board_edges[second_board]):
                        match_normal = all(edge2 in edge for edge2 in second_edge) and all(edge1 in second_edge for edge1 in edge)
                        match_flipped = all((9 - edge2) in edge for edge2 in second_edge) and all((9 - edge1) in second_edge for edge1 in edge)

                        if match_normal or match_flipped:
                            matches += 1

                            if not board in edge_match:
                                edge_match[board] = {}

                            edge_match[board][i] = (second_board, j, match_normal)

        if matches == 2:
            result *= int(board)

    return result, edge_match


def task2(input):
    # boards, matches = input
    # print(matches)
    # print(len(matches))

    # image = np.zeros((int(10 * np.sqrt(len(boards))), int(10 * np.sqrt(len(boards)))))
    # board_images = {}
    # for board in boards:
    #     board_image = np.zeros((10, 10))
    #     for pixel in boards[board]:
    #         board_image[pixel[1], pixel[0]] = 1
    #
    #     board_images[board] = board_image
    #
    # start_board = None
    # for board in matches:
    #     if len(matches[board]) == 2:
    #         start_board = board
    #         break

    # print(start_board, matches[start_board])


    return


def parse(data: str):
    lines = util.as_double_lines(data)

    boards = {}

    for board in lines:
        board_lines = util.as_lines(board)
        board_id = board_lines[0][5:-1]

        pixels = []
        for y in range(1, len(board_lines)):
            for x in range(len(board_lines[y])):
                if board_lines[y][x] == "#":
                    pixels.append((x, y - 1))

        boards[board_id] = set(pixels)

    return boards


def main():
    data: str = util.get(20, 2020)
    data = test_data
    input = parse(data)
    result, matches = task1(input)
    print(result)
    print(task2((input, matches)))


if __name__ == "__main__":
    main()
