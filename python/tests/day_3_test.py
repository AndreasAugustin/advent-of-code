#!python

import pytest

from aoc.day_3 import Claim, claims_fact, claim_fact, Fabric
import util
import os

script_directory = os.path.dirname(os.path.realpath(__file__))
data_file = os.path.join(script_directory, 'data', 'day_03_input.csv')


def test_init_claim():
    claim = Claim(0, 1, 2, 3, 4)
    assert claim.id == 0
    assert claim.left_inches == 1
    assert claim.top_inches == 2
    assert claim.width == 3
    assert claim.height == 4


def test_claim_fact_read():
    _in = util.file_lines_to_array(data_file)
    res = claims_fact(_in)
    _exp = [
        Claim(1, 1, 3, 4, 4),
        Claim(2, 3, 1, 4, 4),
        Claim(3, 5, 5, 2, 2)
    ]
    assert res == _exp


@pytest.mark.parametrize('_hash, _exp',
                         [
                             ["#2 @ 3,1: 4x4", Claim(2, 3, 1, 4, 4)],
                             ["#3 @ 5,5: 2x2", Claim(3, 5, 5, 2, 2)]
                         ])
def test_claim_fact(_hash, _exp):
    res = claim_fact(_hash)
    assert res == _exp


def test_fabric_get_often_entries():
    claims = claims_fact(util.file_lines_to_array(data_file))
    fab = Fabric(10)
    fab.add_claims(claims)
    res = fab.get_often_entries()
    assert len(res) == 4


def test_get_intact_claims():
    claims = claims_fact(util.file_lines_to_array(data_file))
    fab = Fabric(10)
    fab.add_claims(claims)
    res = fab.get_intact_claims()
    assert len(res) == 1
    assert res[0] == 3
