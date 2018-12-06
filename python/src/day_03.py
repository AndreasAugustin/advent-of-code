#!python
import re

from attr import dataclass


@dataclass
class Claim:
    id: int
    left_inches: int
    right_inches: int
    width: int
    height: int


def claim_fact(input_hash: str):
    arr = re.split(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', input_hash)
    filt = list(filter(lambda x: x != '', arr))
    dat = list(map(lambda x: int(x), filt))
    return Claim(dat[0], dat[1], dat[2], dat[3], dat[4])

