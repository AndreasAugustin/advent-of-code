#!python
import re
import logging
from attr import dataclass

from .util import file_lines_to_array

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

MAX_FABRIC_INCHES = 1000


def main() -> int:
    logger.info("Advent of code day 03")
    import os
    script_directory = os.path.dirname(os.path.realpath(__file__))
    data_file = \
        os.path.join(script_directory, '..', '..', 'data', 'day_03_input.csv')
    _input = file_lines_to_array(data_file)

    claims = claims_fact(_input)
    logger.info(f"got claims with size: {len(claims)}")

    fab = Fabric()
    fab.add_claims(claims)
    often = fab.get_often_entries()
    logger.info(f"got often with size: {len(often)}")

    return 0


@dataclass
class Claim:
    id: int
    left_inches: int
    top_inches: int
    width: int
    height: int


class Fabric:

    def __init__(self, dim: int = MAX_FABRIC_INCHES):
        self._dim = dim
        self._m = []
        for i in range(dim):
            self._m.append([])
            mi = self._m[i]
            for j in range(dim):
                mi.append([])

    def add_claim(self, claim: Claim):
        for w in range(claim.width):
            for h in range(claim.height):
                sq = self._m[claim.left_inches + w]
                sq[claim.top_inches + h].append(claim.id)

    def add_claims(self, claims: [Claim]):
        for claim in claims:
            self.add_claim(claim)

    def get_often_entries(self) -> [[int]]:
        res = []
        for i in range(self._dim):
            for j in range(self._dim):
                v = self._m[i][j]
                if v:
                    if len(v) > 1:
                        res.append(v)
        return res


def claim_fact(input_hash: str) -> Claim:
    arr = re.split(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', input_hash)
    filt = list(filter(lambda x: x != '', arr))
    dat = list(map(lambda x: int(x), filt))
    return Claim(dat[0], dat[1], dat[2], dat[3], dat[4])


def claims_fact(input_hash: [str]) -> [Claim]:
    return list(map(lambda x: claim_fact(x), input_hash))


if __name__ == "__main__":
    main()
