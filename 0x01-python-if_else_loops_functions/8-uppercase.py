#!/usr/bin/python3


def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) in range(97, 123):
            upper_value = ord(str[i]) - 32
            print("{}".format(chr(upper_value)), end = '')
        else:
            print("{}".format(str[i]), end='');
    print("") 
