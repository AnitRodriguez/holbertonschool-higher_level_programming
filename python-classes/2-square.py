#!/usr/bin/python3
"""class"""


class Square:
    """class square"""

    def __init__(self, size=0):
        """__init__ is constructor that initializer"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
