#!/usr/bin/python3
"""
File: 100-my_int.py
Desc: This module Defines a class MyInt that inherits from int
Author: IAN OTIENO (Ian12467)
Date Created: 26 Sep 2022
"""


class MyInt(int):
    """
    Invert int operators == and !=
    """

    def __eq__(self, value):
        """
        Override == opeartor with != behavior
        """
        return self.real != value

    def __ne__(self, value):
        """
        Override != operator with == behavior
        """
        return self.real == value
