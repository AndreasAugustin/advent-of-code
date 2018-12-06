#!python

from typing import List


def file_lines_to_int_array(file_path: str) -> List[int]:
    return list(map(lambda x: int(x), file_lines_to_array(file_path)))


def file_lines_to_array(file_path: str) -> List[str]:
    fh = open(file_path)
    x = [str(i).replace("\n", "") for i in fh.readlines()]

    fh.close()
    return x
