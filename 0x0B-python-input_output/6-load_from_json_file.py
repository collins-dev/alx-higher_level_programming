#!/usr/bin/python3
"""
File: 6-load_from_json_file.py
Desc: This module contains one function; load_from_json_file(filename)
Author: Ian Otieno (Ian12467)
Date Created: 26 Sep 2022
"""

import json


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”
    """
    with open(filename, "r") as f:
        return json.load(f)
