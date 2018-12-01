#!python
from typing import List

from ..src.day_01 import sum_iterate, file_lines_to_array, first_duplicate

import os
script_directory = os.path.dirname(os.path.realpath(__file__))
data_file = os.path.join(script_directory, 'data', 'day_01_input.csv')


def test_first_duplicate_1():
    _input = [1, 3, 5, 3, 6, 8, 1]
    res = first_duplicate(_input)
    assert res == 3


def test_first_duplicate_2():
    data_arr = file_lines_to_array(data_file)
    first_dupl = first_duplicate(data_arr)
    assert first_dupl == -2


def test_sum_iterate_1():
    _input: List[int] = [+1, -2, +3, +1]
    res = sum_iterate(0, _input)
    assert res[-1] == 3


def test_sum_iterate_2():
    _input: List[int] = [+1, +1, +1]
    res = sum_iterate(0, _input)
    assert res[-1] == 3


def test_sum_iterate_3():
    _input: List[int] = [+1, +1, -2]
    res = sum_iterate(0, _input)
    assert res[-1] == 0


def test_sum_iterate_4():
    _input: List[int] = [-1, -2, -3]
    res = sum_iterate(0, _input)
    assert res[-1] == -6


def test_file_lines_to_array():
    res = file_lines_to_array(data_file)
    assert res == [1, -2, 4, -2, 2]
