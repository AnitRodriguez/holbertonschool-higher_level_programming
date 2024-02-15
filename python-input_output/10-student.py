#!/usr/bin/python3

"""class Student that defines a student."""


class Student:
    """Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        if not isinstance(attrs, list=[]):
            return self.__dict__
        else:
            dicc = {}
            for a in attrs:
                if a in self.__dict__:
                    dicc[a] = self.__dict__[a]
        return dicc
