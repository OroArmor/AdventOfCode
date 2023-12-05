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
    return list(map(lambda x: int(x), [i.strip() for i in ints if i.strip().isnumeric()]))


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
