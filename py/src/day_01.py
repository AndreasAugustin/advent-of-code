#!python
from typing import List


def file_lines_to_array(file_path: str) -> List[int]:
    fh = open(file_path)
    x = [int(i) for i in fh.readlines()]

    fh.close()
    return x


def main() -> int:
    """
    main function
    :rtype: int the status code
    """
    print("Advent of code day 01")

    import os
    script_directory = os.path.dirname(os.path.realpath(__file__))
    data_file = \
        os.path.join(script_directory, '..', '..', 'data', 'day_01_input.csv')
    _input = file_lines_to_array(data_file)
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
