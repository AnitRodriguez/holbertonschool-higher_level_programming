#!/usr/bin/python3
"""function"""


def append_write(filename="", text=""):
    """this function"""
    with open(filename, 'a', encoding="UTF-8") as a:
        a.write(text)
        return len(text)
