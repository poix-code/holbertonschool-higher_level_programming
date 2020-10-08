#!/usr/bin/python3
"""
The script adds arguments from the main to a Python list.
"""

import os
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = 'add_item.json'
if os.path.exists(filename):
    l = load_from_json_file(filename)
    l.extend(sys.argv[1:])
    save_to_json_file(l, filename)
else:
    save_to_json_file(sys.argv[1:], filename)
