#!/usr/bin/python3
"""
Get peak value with lowerst complexity
"""


def find_peak(list_of_integers):
    """Find peak"""
    if len(list_of_integers) == 0:
        return None

    for i,n in enumerate(list_of_integers):
        for y,m in enumerate(list_of_integers):
            if list_of_integers[i] > list_of_integers[y]:
                temp = m
                list_of_integers[y] = n
                list_of_integers[i] = temp
    
    return list_of_integers[0]
