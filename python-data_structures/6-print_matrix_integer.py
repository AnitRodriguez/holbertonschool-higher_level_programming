#!/usr/bin/python3def
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        b = 0
        for c in a:
            len_matrix = len(a)
            b += 1
            print("{:d}".format(c), end="")
            if b != len_matrix:
                print(" ", end="")
        print("")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()