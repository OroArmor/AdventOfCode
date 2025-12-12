import util
from util import *
import numpy as np

test_data: str = \
    """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""


DFS_SOLUTION = False


def try_place(grid, transformed_shapes, counts, width, cache):
    cache_index = (tuple(grid), tuple(counts))
    if cache_index in cache:
        return cache[cache_index]

    if len(cache) % 1000 == 0:
        print("Cache size:", len(cache))

    if np.sum(counts) == 0:
        return True

    for i, shape in enumerate(transformed_shapes):
        if counts[i] > 0:
            for transform in shape:
                for j in range(len(grid) - transform[-1]):
                    if j % width > width - 3:
                        continue
                    if not np.any(grid[transform + j]):
                        grid[transform + j] = True
                        counts[i] -= 1
                        if try_place(grid, transformed_shapes, counts, width, cache):
                            grid[transform + j] = False
                            print(counts)
                            for y in range(len(grid) // width):
                                for x in range(width):
                                    if grid[x + y * width]:
                                        print("#", end="")
                                    else:
                                        print(".", end="")
                                print()
                            print()

                            return True
                        counts[i] += 1
                        grid[transform + j] = False
    cache[cache_index] = False
    return False


def task1(input):
    shapes, regions = input

    total = 0
    for region, counts in regions:
        if not DFS_SOLUTION:
            if region[0] * region[1] >  np.sum(counts * shapes):
                total += 1
        else:
            transformed_shapes = []
            for shape in shapes:
                transformed_shapes.append([])
                for subshape in shape:
                    offset = np.vstack([
                        np.full((len(subshape[0])), region[0], dtype=int),
                        np.ones((len(subshape[0])), dtype=int),

                    ], dtype=int)
                    transformed_shapes[-1].append(
                        np.sum(subshape * offset, axis=0)
                    )

                    print(subshape)
                    print(transformed_shapes[-1][-1])
                    print()

            if try_place(np.zeros((region[0] * region[1],), dtype=bool), transformed_shapes, counts, region[0], {}):
                total += 1

    return total


def parse(data: str):
    lines = util.as_double_lines(data)

    shapes = []
    for shape in lines[:-1]:
        if not DFS_SOLUTION:
            shapes.append(shape.count("#"))
        else:
            shape = util.as_lines(shape)[1:]
            shape = np.array([np.fromiter(s, dtype="U1") for s in shape]) == "#"

            seen = set()
            subshapes = []
            for subshape in [shape, np.rot90(shape), np.rot90(shape, 2), np.rot90(shape, 3),
                                  np.flip(shape), np.rot90(np.flip(shape)), np.rot90(np.flip(shape), 2), np.rot90(np.flip(shape), 3)]:
                if tuple(subshape.flatten()) not in seen:
                    seen.add(tuple(subshape.flatten()))
                    subshapes.append(np.vstack(np.where(subshape), dtype=int))


            shapes.append(subshapes)

    regions = []
    for region in util.as_lines(lines[-1]):
        shape, counts = region.split(": ")
        shape = tuple(util.list_as_ints(shape.split("x")))
        counts = np.array(util.as_ssv_ints(counts))
        regions.append((shape, counts))

    return shapes, regions


def main():
    data: str = util.get(12, 2025)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))


if __name__ == "__main__":
    main()
