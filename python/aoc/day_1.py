#!python
from typing import List
from aoc import util


def main() -> int:

    import os
    script_directory = os.path.dirname(os.path.realpath(__file__))
    data_file = \
        os.path.join(script_directory, '..', '..', 'data', 'day_01_input.csv')
    _input = util.file_lines_to_int_array(data_file)

    first_dupl = None
    tmp = []
    frequency = 0
    while first_dupl is None:
        res = sum_iterate(frequency, _input)
        tmp = tmp + res
        first_dupl = first_duplicate(tmp)
        frequency = res[-1]
        print(f"result is: {frequency}")
        print(f"first duplicate frequency: {first_dupl}")

    return 0


def first_duplicate(a: List):
    set_ = set()
    for item in a:
        if item in set_:
            return item
        set_.add(item)
    return None


def sum_iterate(start: int, arr: List[int]) -> List[int]:
    a = start
    res = []
    for x in arr:
        a = a + x
        res.append(a)
    return res


if __name__ == "__main__":
    main()
