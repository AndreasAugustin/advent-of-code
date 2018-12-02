#!python
from ..src.day_02 import check_freq, has_exactly_two
import logging


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


def test_has_exactly_two(caplog):
    caplog.set_level(logging.DEBUG)
    _input = "abcdee"
    res = has_exactly_two(_input)
    assert res is True
