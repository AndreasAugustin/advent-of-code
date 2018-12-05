#!python
import pytest
from ..src.day_01 import sum_iterate, file_lines_to_array, first_duplicate

import os

script_directory = os.path.dirname(os.path.realpath(__file__))
data_file = os.path.join(script_directory, 'data', 'day_01_input.csv')


@pytest.mark.parametrize("dup_input, dup_exp", [
    [[1, 3, 5, 3, 6, 8, 1], 3],
    [file_lines_to_array(data_file), -2]
])
def test_first_duplicate(dup_input, dup_exp):
    res = first_duplicate(dup_input)
    assert res == dup_exp


@pytest.mark.parametrize("it_input, it_exp", [
    [[+1, -2, +3, +1], 3],
    [[+1, +1, +1], 3],
    [[+1, +1, -2], 0],
    [[-1, -2, -3], -6]
])
def test_sum_iterate(it_input, it_exp):
    res = sum_iterate(0, it_input)
    assert res[-1] == it_exp


def test_file_lines_to_array():
    res = file_lines_to_array(data_file)
    assert res == [1, -2, 4, -2, 2]
