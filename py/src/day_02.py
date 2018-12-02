#!python
from typing import Dict
import logging


def main() -> int:
    logging.info("Advent of code day 01")

    return 0


def check_freq(input_str: str) -> Dict[str, int]:
    freq: Dict[str, int] = {}
    for c in input_str:
        freq[c] = input_str.count(c)
    return freq


def has_exactly_two(input_str: str) -> bool:
    return has_exactly(2, input_str)


def has_exactly(number: int, input_str: str) -> bool:
    freq = check_freq(input_str)
    found_once = False
    for key, value in freq.items():
        logging.debug(f"key: {key}, value: {value}")
        if value == number:
            if found_once is True:
                return False
            found_once = True

    return found_once
