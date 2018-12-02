#!python
from ..src.day_02 import check_freq, has_two_equal_chars, \
    has_three_equal_chars, file_lines_to_array, \
    count_of_three_equal_chars, count_of_two_equal_chars, \
    calc_hash
import logging

import os
script_directory = os.path.dirname(os.path.realpath(__file__))
data_file = os.path.join(script_directory, 'data', 'day_02_input.csv')


def test_check_freq_1():
    _input = "abcdef"
    res = check_freq(_input)
    assert res == {'a': 1, 'b': 1, "c": 1, "d": 1, "e": 1, "f": 1}


def test_check_freq_2():
    _input = "bababc"
    res = check_freq(_input)
    assert res == {'a': 2, 'b': 3, "c": 1}


def test_check_freq_3():
    _input = "abbcde"
    res = check_freq(_input)
    assert res == {'a': 1, 'b': 2, "c": 1, "d": 1, "e": 1}


def test_check_freq_4():
    _input = "abcccd"
    res = check_freq(_input)
    assert res == {"a": 1, "b": 1, "c": 3, "d": 1}


def test_check_freq_5():
    _input = "aabcdd"
    res = check_freq(_input)
    assert res == {'a': 2, "b": 1, "c": 1, "d": 2}


def test_check_freq_6():
    _input = "abcdee"
    res = check_freq(_input)
    assert res == {'a': 1, "b": 1, "c": 1, "d": 1, "e": 2}


def test_check_freq_7():
    _input = "ababab"
    res = check_freq(_input)
    assert res == {"a": 3, "b": 3}


def test_has_two_equal_chars_1(caplog):
    # caplog.set_level(logging.DEBUG)
    _input = "abcdee"
    res = has_two_equal_chars(_input)
    assert res is True


def test_has_two_equal_chars_2():
    _input = "ababab"
    res = has_two_equal_chars(_input)
    assert res is False


def test_has_two_equal_chars_3():
    _input = "abcdefg"
    res = has_two_equal_chars(_input)
    assert res is False


def test_has_three_equal_chars_1():
    _input = "ababab"
    res = has_three_equal_chars(_input)
    assert res is True


def test_has_three_equal_chars_2(caplog):
    # caplog.set_level(logging.DEBUG)
    _input = "aaabcd"
    res = has_three_equal_chars(_input)
    assert res is True


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
