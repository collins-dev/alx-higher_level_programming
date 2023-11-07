#!/usr/bin/python3
"""
File: 3-to_json_string.py
Desc: This module contains one function;
to_json_string(my_obj)
Author: Ian Otieno (Ian12467)
Date Created: 26 Sep 2022
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
