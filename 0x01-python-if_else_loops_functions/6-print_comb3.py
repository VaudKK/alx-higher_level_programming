#!/usr/bin/python3

for i in range(0, 10):
    for y in range(0, 10):
        if i < y and i != y:
            if i != 8:
                print("{:0<2s},".format(str(i) + str(y)), end=' ')
            else:
                print("{:0<2s}".format(str(i) + str(y)))
