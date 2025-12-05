from typing import Tuple, List, Union


class Range:
    def __init__(self, start: int, end: int, inclusive: bool = False):
        if inclusive and start > end:
            raise AssertionError(f"start: {start} is > end: {end}")
        if start >= end and not inclusive:
            raise AssertionError(f"start: {start} is >= to end: {end}")

        self.start = start
        self.end = end + (1 if inclusive else 0)
        self.inclusive = inclusive

    def __contains__(self, item):
        if item.__class__ is Range:
            return self.start <= item.start and item.end < self.end
        return self.start <= item < self.end

    def intersects(self, other) -> bool:
        if other.start <= self.start < other.end:
            return True
        if self.start <= other.start < self.end:
            return True
        if other.start <= self.end < other.end:
            return True
        if self.start <= other.end < self.end:
            return True
        return False

    def merge(self, other) -> Union["Range", None]:
        """
        Requires that the two ranges already intersect. (or not if you want that)
        :param other: other range
        :return: ``[min(start,other.start),max(end,other.end))`` (inclusive if this is inclusive)
        """
        return Range(min(self.start, other.start), max(self.end, other.end) - (1 if self.inclusive else 0), self.inclusive)

    def intersection(self, other) -> Tuple[Union["Range", None], List["Range"]]:
        if other.start <= self.start and self.end < other.end:  # Self contained in other
            return self, []
        elif other.end <= self.start or self.end <= other.start:  # Self and other do not intersect
            return None, []
        elif other.start <= self.start < other.end <= self.end:  # Self start within other
            if other.end == self.end:
                return Range(self.start, other.end), []
            return Range(self.start, other.end), [Range(other.end, self.end)]
        elif self.start <= other.start < self.end <= other.end:  # Other start within self
            if self.start == other.start:
                return Range(other.start, self.end), []
            return Range(other.start, self.end), [Range(self.start, other.start)]
        elif self.start <= other.start < other.end <= self.end:
            return other, [Range(self.start, other.start), Range(other.end, self.end)]
        else:
            print(self, other)
            raise Exception("ohno")

    def split_on(self, val: int) -> Union[Tuple["Range"], Tuple["Range", "Range"]]:
        if val == self.start:
            return Range(self.start + 1, self.end - (1 if self.inclusive else 0), self.inclusive),
        elif val == self.end:
            return Range(self.start, self.end - 1 - (1 if self.inclusive else 0), self.inclusive),
        return Range(self.start, val - (1 if self.inclusive else 0), self.inclusive), Range(val, self.end - (1 if self.inclusive else 0), self.inclusive)

    def __str__(self):
        return f"{self.start}..{('=' if self.inclusive else '')}{self.end - (1 if self.inclusive else 0)}"

    def __repr__(self):
        return f"{self.start}..{('=' if self.inclusive else '')}{self.end - (1 if self.inclusive else 0)}"

    def __len__(self):
        return self.end - self.start

    def __iter__(self):
        yield from range(self.start, self.end)

    def __lt__(self, other):
        return self.start < other.start or self.start == other.start and self.end < other.end

    def __le__(self, other):
        return self.start <= other.start

    def __gt__(self, other):
        return self.start > other.start or self.start == other.start and self.end > other.end

    def __ge__(self, other):
        return self.start >= other.start

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    @staticmethod
    def reduce_ranges(ranges: List["Range"]) -> List["Range"]:
        sorted_ranges = sorted(ranges)

        ranges = []
        range = sorted_ranges[0]

        for r in sorted_ranges[1:]:
            if r.start <= range.end:
                if r.end > range.end:
                    range.end = r.end
            else:
                ranges.append(range)
                range = r
        ranges.append(range)

        return ranges


if __name__ == "__main__":
    test = Range(0, 100)

    print(test.intersection(Range(-100, 200)))

    print(test.intersection(Range(100, 200)))
    print(test.intersection(Range(-100, 0)))

    print(test.intersection(Range(-50, 50)))

    print(test.intersection(Range(50, 150)))

    print(test.intersection(Range(25, 75)))

    print(test < Range(-50, 50))
    print(test < Range(50, 150))
    inc = Range(0, 100, True)
    print(inc, len(inc))
