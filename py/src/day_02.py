#!python
from typing import Dict


def main() -> int:
    print("Advent of code day 01")

    return 0


def check_freq(input_str: str) -> Dict[str, int]:
    freq: Dict[str, int] = {}
    for c in input_str:
        freq[c] = input_str.count(c)
    return freq

