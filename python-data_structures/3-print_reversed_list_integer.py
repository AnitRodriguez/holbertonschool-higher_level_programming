#!/usr/bin/python3def
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for a in range(len(my_list)):
        print("{:d}".format(my_list[a]))
