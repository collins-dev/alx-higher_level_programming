#!/usr/bin/python3
"""
File: 2-append_write.py
Desc: This module contains one function;
append_write(filename="", text="")
Author: Ian Otieno (Ian12467)
Date Created: 26 Sep 2022
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    with open(filename, mode="a", encoding="UTF-8") as f:
        return f.write(text)
