#!/usr/bin/python3
""" function that reads a text file"""


def read_file(filename=""):
    """ function that reads a text file"""
    with open(filename, 'r', encoding="UTF-8") as a:
        print(f"{a.read()}", end="")
