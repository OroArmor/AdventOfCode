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
    grid, width, height = input
    def neighbors(node: Node):
        for direction in cardinal_directions():
            next_node: Node = Node(
                node.position + direction,
                direction,
                (node.steps_in_direction + 1) if node.direction is not None and direction == node.direction else 1
            )

            in_grid = 0 <= next_node.position.x < width and 0 <= next_node.position.y < height

            if in_grid:
                if node.direction is None or next_node.direction != -node.direction:
                    if next_node.steps_in_direction <= 3:
                        yield next_node, grid[next_node.position]

    def is_goal(node: Node):
        return node.position == Point(width - 1, height - 1)

    _, _, min_cost = dijkstra(
        Node(Point(0, 0), None, 0),
        neighbors,
        is_goal)

    return int(min_cost)


def task2(input):
    grid, width, height = input

    def neighbors(node: Node):
        for direction in cardinal_directions():
            next_node: Node = Node(
                node.position + direction,
                direction,
                (node.steps_in_direction + 1) if node.direction is not None and direction == node.direction else 1
            )

            in_grid = 0 <= next_node.position.x < width and 0 <= next_node.position.y < height

            if in_grid:
                if node.direction is None or next_node.direction != -node.direction:
                    if next_node.steps_in_direction <= 10 and not (next_node.steps_in_direction == 1 and node.steps_in_direction < 4):
                        yield next_node, grid[next_node.position]

    def is_goal(node: Node):
        return node.position == Point(width - 1, height - 1)

    _, _, min_cost = dijkstra(
        Node(Point(0, 0), None, 5),
        neighbors,
        is_goal)

    return int(min_cost)


def parse(data: str):
    grid_raw, width, height = util.as_grid(data)

    grid = dict()

    for y, row in enumerate(grid_raw):
        for x, c in enumerate(row):
            grid[Point(x, y)] = int(c)

    return grid, width, height


def main():
    data: str = util.get(17, 2023)
    # data = test_data
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
