#!python
from typing import Dict, List, Optional
import logging

from .util import file_lines_to_array

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


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

    similar_ids = differ_by_exactly_one_char_at_same_pos(input_arr)

    logger.info(f"similiar ids: {similar_ids}")
    # because of logs I know that it is only one id
    # not production ready
    res = common_letters(similar_ids[0][0], similar_ids[0][1])
    logger.info(f"res: {res}")

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


def differ_by_exactly_one_char_at_same_pos(input_arr: List[str]) \
        -> Optional[List[List[str]]]:
    res = []
    if not input_arr:
        return res
    for i in range(len(input_arr)):
        r = differ_by_exactly_one_char_at_same_pos_for(
            input_arr.pop(0), input_arr)
        if r:
            res.append(r)

    return res


def differ_by_exactly_one_char_at_same_pos_for(
        comp: str, input_arr: List[str]) -> List[str]:
    res = []
    for s in input_arr:
        dif = 0
        for i in range(len(comp)):
            if s[i] != comp[i]:
                dif += 1
        if dif == 1:
            res.append(s)
    if res:
        res.append(comp)
    return res


def common_letters(_input1: str, _input2: str) -> str:
    # we need here to have only one char differ for both inputs
    # not nice code
    res = []
    print(range(len(_input1)))
    for i in range(len(_input1)):
        if _input1[i] == _input2[i]:
            # possible to refactor for performance here
            res.append(_input1[i])

    return "".join(res)


if __name__ == "__main__":
    main()
