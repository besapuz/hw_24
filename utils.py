import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


def build_query(data: list[str], cmd: str, value: str) -> list:
    res = list(map(lambda v: v.strip(), data))
    if cmd == "filter":
        res = list(filter(lambda v: value in v, res))
    if cmd == "sort":
        revers = value == 'desc'
        res = sorted(res, reverse=revers)
    if cmd == "unique":
        res = list(set(res))
    if cmd == "limit":
        res = list(res)[:int(value)]
    if cmd == "map":
        res = list(map(lambda v: v.split(' ')[int(value)], res))
    if cmd == "regex":
        regex = re.compile(value)
        res = list(filter(lambda v: re.search(regex, v), res))
    return res


def reads_file(data: dict) -> list:
    with open(os.path.join(DATA_DIR, data["filename"])) as f:
        file_data = f.readlines()
    res = file_data
    if "cmd2" in data and "value2" in data:
        res = build_query(res, data["cmd2"], data["value2"])

    return res
