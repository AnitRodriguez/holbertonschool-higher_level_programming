#!/usr/bin/python3
"""Function that returns True.
If the obj is exactly an instance of the specified class.
Otherwise False."""


def is_same_class(obj, a_class):
    """function checking for object of a specified class"""
    if type(obj) is a_class:
        return True
    else:
        return False
