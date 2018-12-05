#!python

import pytest
from ..src.day_02 import check_freq, has_two_equal_chars, \
    has_three_equal_chars, file_lines_to_array, \
    count_of_three_equal_chars, count_of_two_equal_chars, \
    calc_hash, differ_by_exactly_one_char_at_same_pos, common_letters

import os

script_directory = os.path.dirname(os.path.realpath(__file__))
data_file = os.path.join(script_directory, 'data', 'day_02_input.csv')


@pytest.mark.parametrize("_input, _exp",
                         [
                             ["abcdef", {'a': 1, 'b': 1, "c": 1, "d": 1, "e": 1, "f": 1}],
                             ["bababc", {'a': 2, 'b': 3, "c": 1}],
                             ["abbcde", {'a': 1, 'b': 2, "c": 1, "d": 1, "e": 1}],
                             ["abcccd", {"a": 1, "b": 1, "c": 3, "d": 1}],
                             ["aabccd", {'a': 2, "b": 1, "c": 2, "d": 1}],
                             ["abcdee", {'a': 1, "b": 1, "c": 1, "d": 1, "e": 2}],
                             ["ababab", {"a": 3, "b": 3}]
                         ]
                         )
def test_check_freq(_input, _exp):
    res = check_freq(_input)
    assert res == _exp


@pytest.mark.parametrize("_input, _exp", [
    ["abcdee", True],
    ["ababab", False],
    ["abcdefg", False]
])
def test_has_two_equal_chars(_input, _exp):
    res = has_two_equal_chars(_input)
    assert res is _exp


@pytest.mark.parametrize("_input, _exp", [
    ["ababab", True],
    ["aaabcd", True]
])
def test_has_three_equal_chars(_input, _exp):
    res = has_three_equal_chars(_input)
    assert res is _exp


def test_count_has_two_equal_chars():
    data_arr = file_lines_to_array(data_file)
    res = count_of_two_equal_chars(data_arr)
    assert res == 4


def test_count_has_three_equal_chars():
    data_arr = file_lines_to_array(data_file)
    res = count_of_three_equal_chars(data_arr)
    assert res == 3


def test_calc_hash():
    data_arr = file_lines_to_array(data_file)
    res = calc_hash(data_arr)
    assert res == 12


def test_differ_by_exactly_one_char_at_same_pos():
    _input = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]
    res = differ_by_exactly_one_char_at_same_pos(_input)
    _exp = [["fguij", "fghij"]]
    assert res == _exp


def test_common_letters():
    _input1 = "fguij"
    _input2 = "fghij"
    res = common_letters(_input1, _input2)
    _exp = "fgij"
    assert res == _exp
