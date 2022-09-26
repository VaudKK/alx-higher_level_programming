#!/usr/bin/python3


def get_value(tp, index):
    if index > len(tp) - 1:
        return 0
    return tp[index]


def add_tuple(tuple_a=(), tuple_b=()):
    first = get_value(tuple_a, 0) + get_value(tuple_b, 0)
    second = get_value(tuple_a, 1) + get_value(tuple_b, 1)
    return (first, second)
