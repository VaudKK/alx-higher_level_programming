#!/usr/bin/python3


def common_elements(set_1, set_2):
    return set(x for x, y in zip(set_1, set_2) if x in set_1 and x in set_2)
