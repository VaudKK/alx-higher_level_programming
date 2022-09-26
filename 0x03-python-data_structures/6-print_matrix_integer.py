#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for n in row:
            if row[-1] == n:
                print("{}".format(n))
            else:
                print("{}".format(n), end=" ")
