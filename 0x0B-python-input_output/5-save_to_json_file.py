#!/usr/bin/python3
"""
File: 5-save_to_json_file.py
Desc: This module contains one function; save_to_json_file(my_obj, filename)
Author: Ian Otieno (Ian12467)
Date Created: 26 Sep 2022
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
