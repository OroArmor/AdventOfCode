import typing
from functools import *

import aocd
import numpy as np
from lib.range_util import *

CURRENT_YEAR: int = 2023

UP = np.array([0, 1])
DOWN = np.array([0, -1])
LEFT = np.array([-1, 0])
RIGHT = np.array([1, 0])


def get(day: int, year: int = CURRENT_YEAR):
    return aocd.get_data(year=year, day=day)


def list_as_ints(ints: [str]):
    return list(map(lambda x: int(x), [i.strip() for i in ints if i.strip()]))


def as_lines(s: str) -> [str]:
    return s.split("\n")


def as_double_lines(s: str) -> [str]:
    return s.split("\n\n")


def as_csv(s: str) -> [str]:
    return list(map(str.strip, s.split(",")))


def as_lines_of_int(s: str) -> [int]:
    return list_as_ints(as_lines(s))


def as_csv_of_ints(s: str) -> [int]:
    return list_as_ints(as_csv(s))


def as_csv_lines(s: str) -> [[str]]:
    return list(map(lambda x: x.split(","), as_lines(s)))


def as_csv_lines_of_ints(s: str) -> [[int]]:
    return list(map(lambda x: list_as_ints(x.split(",")), as_lines(s)))


def as_ssv(s: str) -> [str]:
    return s.replace("\n", " ").split(" ")


def as_ssv_ints(s: str) -> [int]:
    return list_as_ints(s.replace("\n", " ").split(" "))


def split_on_colon(s: str) -> [str]:
    return s.split(":")


def as_list_of_colon_split(s: [str]) -> [[str]]:
    return list(map(lambda x: split_on_colon(x), s))


def adjacent_directions() -> (int, int):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx != 0 or dy != 0:
                yield dx, dy
    return


def cardinal_directions() -> (int, int):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if (dx == 0 or dy == 0) and not (dx == dy):
                yield dx, dy
    return


def adjacent_directions_3d() -> (int, int, int):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                if not (dx == 0 and dy == 0 and dz == 0):
                    yield dx, dy, dz
    return


def rotate(point: np.ndarray, degrees: float):
    rad = np.deg2rad(degrees)
    rotation: np.ndarray = np.array([[np.cos(rad), -np.sin(rad)], [np.sin(rad), np.cos(rad)]]) @ point
    return rotation.astype(point.dtype)


def gcd(a: int | List[int], b: int | None = None) -> int:
    if isinstance(a, list):
        return reduce(gcd, a, 1)
    if b is None:
        raise ValueError('b must be set for non-lists!')

    while b:
        a, b = b, a % b
    return a


def lcm(a: int | List[int], b: int | None = None) -> int:
    if isinstance(a, list):
        return reduce(lcm, a, 1)
    if b is None:
        raise ValueError('b must be set for non-lists!')

    return a * (b // gcd(a, b))


def inv_modulo(value: int, modulo: int) -> int:
    modulo0 = modulo
    x0, x1 = 0, 1

    if modulo == 1:
        return 0

    while value > 1:
        quotient = value // modulo
        value, modulo = modulo, value % modulo
        x0, x1 = x1 - quotient * x0, x0

    if x1 < 0:
        x1 += modulo0

    return x1


def chinese_remainder_theorem(divisors: [int], remainders: [int]) -> int:
    product = reduce(int.__mul__, divisors, 1)
    return sum((product // divisor * inv_modulo(product // divisor, divisor) * remainder for divisor, remainder in zip(divisors, remainders))) % product
