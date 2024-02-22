#!/usr/bin/python3
"""Function that returns True.
If the obj is exactly an instance of the specified class.
Otherwise False."""


def is_same_class(obj, a_class):
    """function checking for object of a specified class"""
    return (type(obj) == a_class)
