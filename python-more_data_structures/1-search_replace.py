#!/usr/bin/python3def
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for x in range(len(my_list)):
        if new_list[x] == search:
            new_list[x] = replace
    return (new_list)
