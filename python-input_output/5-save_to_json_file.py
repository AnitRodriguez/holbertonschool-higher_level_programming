#!/usr/bin/python3
"""function that writes an Object to a text file"""

import json


def save_to_json_file(my_obj, filename):
    """json"""
    with open(filename, "w") as a:
        json.dump(my_obj, a)
