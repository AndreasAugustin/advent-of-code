#!python

import pytest
from ..src.day_03 import Claim, claim_fact

import os

script_directory = os.path.dirname(os.path.realpath(__file__))
data_file = os.path.join(script_directory, 'data', 'day_03_input.csv')


def test_init_claim():
    claim = Claim(0, 1, 2, 3, 4)
    assert claim.id == 0
    assert claim.left_inches == 1
    assert claim.right_inches == 2
    assert claim.width == 3
    assert claim.height == 4


@pytest.mark.parametrize('_hash, _exp',
                         [
                             ["#2 @ 3,1: 4x4", Claim(2, 3, 1, 4, 4)],
                             ["#3 @ 5,5: 2x2", Claim(3, 5, 5, 2, 2)]
                         ])
def test_claim_fact(_hash, _exp):
    res = claim_fact(_hash)
    assert res == _exp
