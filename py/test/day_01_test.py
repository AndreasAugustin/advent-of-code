#!python
from typing import List

from ..src.day_01 import sum_array, file_lines_to_array


def test_sum_array_1():
    _input: List[int] = [+1, -2, +3, +1]
    res = sum_array(_input)
    assert res == 3


def test_sum_array_2():
    _input: List[int] = [+1, +1, +1]
    res = sum_array(_input)
    assert res == 3


def test_sum_array_3():
    _input: List[int] = [+1, +1, -2]
    res = sum_array(_input)
    assert res == 0


def test_sum_array_4():
    _input: List[int] = [-1, -2, -3]
    res = sum_array(_input)
    assert res == -6


def test_file_lines_to_array():
    import os
    script_directory = os.path.dirname(os.path.realpath(__file__))
    data_file = os.path.join(script_directory, 'data', 'day_01_input.csv')
    res = file_lines_to_array(data_file)
    assert res == [1, -2, 4, 2]
