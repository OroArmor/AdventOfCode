import dataclasses

import util
from util import *
import numpy as np

from util import dijkstra

test_data: str = \
    """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""


@dataclasses.dataclass(frozen=True, order=True)
class Node:
    position: (int, int)
    direction: (int, int)
    steps_in_direction: int


def task1(input):
    def cost(node: Node):
        return input[node.position]

    def neighbors(node: Node):
        for direction in cardinal_directions():
            next_node: Node = Node(
                (node.position[0] + direction[0], node.position[1] + direction[1]),
                direction,
                (node.steps_in_direction + 1) if direction == node.direction else 1
            )

            in_grid = 0 <= next_node.position[0] < input.shape[0] and 0 <= next_node.position[1] < input.shape[1]

            if in_grid:
                if not (next_node.direction[0] != 0 and next_node.direction[0] == -node.direction[0] or next_node.direction[1] != 0 and next_node.direction[1] == -node.direction[1]):
                    if next_node.steps_in_direction <= 3:
                        yield next_node

    def is_goal(node: Node):
        return node.position == (input.shape[0] - 1, input.shape[1] - 1)

    _, min_cost = dijkstra(
        Node((0, 0), (0, 0), 0),
        cost,
        neighbors,
        is_goal)

    return int(min_cost)


def task2(input):
    def cost(node: Node):
        return input[node.position]

    def neighbors(node: Node):
        for direction in cardinal_directions():
            next_node: Node = Node(
                (node.position[0] + direction[0], node.position[1] + direction[1]),
                direction,
                (node.steps_in_direction + 1) if direction == node.direction else 1
            )

            in_grid = 0 <= next_node.position[0] < input.shape[0] and 0 <= next_node.position[1] < input.shape[1]

            if in_grid:
                if not (next_node.direction[0] != 0 and next_node.direction[0] == -node.direction[0] or next_node.direction[1] != 0 and next_node.direction[1] == -node.direction[1]):
                    if next_node.steps_in_direction <= 10 and not (next_node.steps_in_direction == 1 and node.steps_in_direction < 4):
                        yield next_node

    def is_goal(node: Node):
        return node.position == (input.shape[0] - 1, input.shape[1] - 1) and node.steps_in_direction >= 4

    _, min_cost = dijkstra(
        Node((0, 0), (0, 0), 5),
        cost,
        neighbors,
        is_goal)

    return int(min_cost)


def parse(data: str):
    grid_raw, width, height = util.as_grid(data)

    grid = np.zeros((width, height)).astype(int)

    for y, row in enumerate(grid_raw):
        for x, c in enumerate(row):
            grid[x, y] = int(c)

    return grid


def main():
    data: str = util.get(17, 2023)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
