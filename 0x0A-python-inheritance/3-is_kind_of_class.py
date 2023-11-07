#!/usr/bin/python3
"""
File: 3-is_kind_of_class.py
Desc: This module contains one function;
is_kind_of_class(obj, a_class)
Author: IAN OTIENO (Ian12467)
Date Created: 26 Sep 2022
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or
    if the object is an instance of a class that
    inherited from, the specified class; otherwise
    False
    """
    return isinstance(obj, a_class)
