#!/usr/bin/python3def
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_n = min(my_list)
    for a in my_list:
        if a > max_n:
            max_n = a
    return max_n
