#!/usr/bin/python3
"""script that adds all arguments to a Python list, and then save
them to a file"""


import sys
import os

save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


if os.path.exists("add_item.json"):
    list = load("add_item.json")
else:
    list = []
list.extend(sys.argv[1:])
save(list, "add_item.json")
