#!/usr/bin/python3

"""
File: 101-add_attribute.py
Desc: This module contains a single function defination
Author: IAN OTIENO (Ian12467)
Date Created: 26 Sep 2022
"""


def add_attribute(obj, att, value):
    """
    Adds a new attribute to an object if it’s possible.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, att, value)
    else:
        raise TypeError("can't add new attribute")
