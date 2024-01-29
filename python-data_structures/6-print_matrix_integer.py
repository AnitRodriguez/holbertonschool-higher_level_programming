#!/usr/bin/python3def
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        b = 0
        for c in a:
            len_matrix = len(a)
            b += 1
            print("{}".format(c), end=" ")
            if b != len_matrix:
                print(" ", end="")
        print("")
        