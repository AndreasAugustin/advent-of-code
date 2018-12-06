#!python
import re
import logging

from attr import dataclass
from .util import file_lines_to_array

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def main() -> int:
    logger.info("Advent of code day 03")
    import os
    script_directory = os.path.dirname(os.path.realpath(__file__))
    data_file = \
        os.path.join(script_directory, '..', '..', 'data', 'day_03_input.csv')
    _input = file_lines_to_array(data_file)
    return 0

@dataclass
class Claim:
    id: int
    left_inches: int
    right_inches: int
    width: int
    height: int


def claim_fact(input_hash: str) -> Claim:
    arr = re.split(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', input_hash)
    filt = list(filter(lambda x: x != '', arr))
    dat = list(map(lambda x: int(x), filt))
    return Claim(dat[0], dat[1], dat[2], dat[3], dat[4])


def claims_fact(input_hash: [str]) -> [Claim]:
    return list(map(lambda x: claim_fact(x), input_hash))


if __name__ == "__main__":
    main()
