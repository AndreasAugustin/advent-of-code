#! python

import os

import util

script_directory = os.path.dirname(os.path.realpath(__file__))
data_file = os.path.join(script_directory, 'data', 'day_01_input.csv')


def test_file_lines_to_array():
    res = util.file_lines_to_array(data_file)
    assert res == ['1', '-2', '4', '-2', '2']


def test_file_lines_to_int_array():
    res = util.file_lines_to_int_array(data_file)
    assert res == [1, -2, 4, -2, 2]
