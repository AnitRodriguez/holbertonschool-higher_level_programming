#!/usr/bin/python3
"""Write a class MyList that inherits from list."""


class MyList(list):
    """class list."""

    def print_sorted(self):
        """Function that prints the list."""
        sort = sorted(self)
        return print(sort)
