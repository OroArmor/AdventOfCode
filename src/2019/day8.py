import util
from util import *
import numpy as np

test_data: str = \
    """123456789012"""

test_data_2: str = \
    "0222112222120000"


def task1(input):
    m = np.argmin(
        np.array(
            list(
                np.count_nonzero(s == "0") for s in input
            )
        )
    )
    return np.count_nonzero(input[m] == '1') * np.count_nonzero(input[m] == '2')


def task2(input):
    image = np.full_like(input[0], '2')
    for i in range(len(input)):
        image = np.where(image != '2', image, '') + np.where(image == '2', input[i], '')

    # for row in image:
    #     for col in row:
    #         print("#" if col == '1' else " ", end="")
    #     print()


def parse(data: str):
    size = (25, 6)
    if data == test_data:
        size = (3, 2)
    elif data == test_data_2:
        size = (2, 2)

    stride = size[0] * size[1]
    images = [np.array(list(data[i:i+stride])).reshape((size[1], size[0])) for i in range(0, len(data), stride)]

    return images


def main():
    data: str = util.get(8, 2019)
    # data = test_data
    # data = test_data_2
    input = parse(data)
    print(input)
    print(task1(input))
    print(task2(input))


if __name__ == "__main__":
    main()
