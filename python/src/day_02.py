#!python
from typing import Dict, List, Optional
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def file_lines_to_array(file_path: str) -> List[str]:
    fh = open(file_path)
    x = [str(i) for i in fh.readlines()]

    fh.close()
    return x


def main() -> int:
    logger.info("Advent of code day 01")
    import os
    script_directory = os.path.dirname(os.path.realpath(__file__))
    data_file = \
        os.path.join(script_directory, '..', '..', 'data', 'day_02_input.csv')
    _input = file_lines_to_array(data_file)

    input_arr = file_lines_to_array(data_file)

    calculated_hash = calc_hash(input_arr)

    logger.info(f"Hash: {calculated_hash}")

    return 0


def check_freq(input_str: str) -> Dict[str, int]:
    freq: Dict[str, int] = {}
    for c in input_str:
        freq[c] = input_str.count(c)
    return freq


def has_two_equal_chars(input_str: str) -> bool:
    return has_number_equal_chars(2, input_str)


def has_three_equal_chars(input_str: str) -> bool:
    return has_number_equal_chars(3, input_str)


def has_number_equal_chars(number: int, input_str: str) -> bool:
    freq = check_freq(input_str)
    for key, value in freq.items():
        logging.debug(f"key: {key}, value: {value}")
        if value == number:
            return True
    return False


def count_of_two_equal_chars(input_arr: List[str]) -> int:
    res = 0
    for s in input_arr:
        if has_two_equal_chars(s) is True:
            res += 1
    return res


def count_of_three_equal_chars(input_arr: List[str]) -> int:
    res = 0
    for s in input_arr:
        if has_three_equal_chars(s) is True:
            res += 1
    return res


def calc_hash(input_arr: List[str]) -> int:
    return count_of_two_equal_chars(input_arr) \
           * count_of_three_equal_chars(input_arr)


def differ_by_exactly_one_char_at_same_pos(input_arr: List[str]) -> Optional[List[List[str]]]:
    res = []
    if not input_arr:
        return res
    for i in range(len(input_arr) - 1):
        r = differ_by_exactly_one_char_at_same_pos_for(input_arr.pop(0), input_arr)
        if r:
            res.append(r)

    return res


def differ_by_exactly_one_char_at_same_pos_for(comp: str, input_arr: List[str]) -> List[str]:
    res = []
    for s in input_arr:
        dif = 0
        for i in range(len(comp) - 1):
            if s[i] != comp[i]:
                dif += 1
        if dif == 1:
            res.append(s)
    if res:
        res.append(comp)
    return res


if __name__ == "__main__":
    main()
