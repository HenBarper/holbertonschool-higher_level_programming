#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_len = len(row)
        for element in range(row_len):
            if(element != row_len - 1):
                print("{:d}".format(row[element]), end=' ')
            else:
                print("{:d}".format(row[element]))
