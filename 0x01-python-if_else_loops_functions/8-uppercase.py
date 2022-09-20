#!/usr/bin/python3


def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) in range(97, 123):
            upper_value = ord(str[i]) - 32
            if i + 1 < len(str):
                print("{}".format(chr(upper_value)), end='')
            else:
                print(chr(upper_value))
        else:
            print(str[i], end='')
