#!/usr/bin/python3
<<<<<<< HEAD
class Square:
    """Represents a square.
    Private instance attribute: size.
    Instantiation with optional size.
    Public instance method: def area(self).
    """

    def __init__(self, size=0):
        """Initializes the data."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
=======
"""defines a class called square"""


class Square:
    """Initialize a square
    Args:
        __size (int): size of the square
    """
    def __init__(self, size=0):
        """Initialize a square
        Args:
            size (int): size of the square
        Returns: None
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """This computes the area of the square"""
        return (self.__size ** 2)
>>>>>>> b734e1e857971cc40fedee1a42d5c8e4b50ece53
