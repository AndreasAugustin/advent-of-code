#!python
from typing import List

_input: List[int] = [1, -2, 10]


def main() -> int:
    """
    main function
    :rtype: int the status code
    """
    print("Advent of code day 01")
    res = sum_array(_input)
    print(f"result is: {res}")
    return 0


def sum_array(arr: List[int]) -> int:
    """
    sums all elements in the array
    :rtype: int
    :param arr:
    :return:
    """
    return sum(arr)


if __name__ == "__main__":
    main()
