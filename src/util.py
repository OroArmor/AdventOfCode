import aocd

CURRENT_YEAR: int = 2022


def get(day: int, year: int = CURRENT_YEAR):
    return aocd.get_data(year=year, day=day)


def list_as_ints(ints: [str]):
    return list(map(lambda x: int(x), ints))


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


def split_on_colon(s: str) -> [str]:
    return s.split(":")


def as_list_of_colon_split(s: [str]) -> [[str]]:
    return list(map(lambda x: split_on_colon(x), s))
