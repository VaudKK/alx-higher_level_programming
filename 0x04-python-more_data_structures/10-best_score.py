#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    if len(a_dictionary.keys()) == 0:
        return None
    maximum = max(a_dictionary.values())
    for x in a_dictionary.keys():
        if a_dictionary[x] == maximum:
            return x
