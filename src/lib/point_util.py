from enum import Enum


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y

        raise AttributeError(f"Invalid item for getitem: {item}")

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        if isinstance(other, int):
            return Point(self.x * other, self.y * other)

    def __truediv__(self, other):
        if isinstance(other, int):
            return Point(self.x // other, self.y // other)

    def __hash__(self):
        return self.x * 31 + self.y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.x < other.x or self.x == other.x and self.y < other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __neg__(self):
        return Point(-self.x, -self.y)


class Direction(Point, Enum):
    RIGHT = 1, 0
    UP = 0, 1
    LEFT = -1, 0
    DOWN = 0, -1

    @classmethod
    def values(cls):
        return [Direction.RIGHT, Direction.UP, Direction.LEFT, Direction.DOWN]
