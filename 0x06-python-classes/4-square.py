#!/usr/bin/python3
<<<<<<< HEAD
class Square:
    """Represents a square.
    Private instance attribute: size:
        - property def size(self)
        - property setter def size(self, value)
    Instantiation with optional size.
    Public instance method: def area(self).
    """

    def __init__(self, size=0):
        """Initializes the data."""
        self.__size = size

    @property
    def size(self):
        """Retrieves the size."""
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
        self.size = size

    @property
    def size(self):
        """getter of the size"""
>>>>>>> b734e1e857971cc40fedee1a42d5c8e4b50ece53
        return self.__size

    @size.setter
    def size(self, value):
<<<<<<< HEAD
        """Sets the size to a value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
=======
        """sets the value for size"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """This computes the area of the square"""
        return (self.__size ** 2)
>>>>>>> b734e1e857971cc40fedee1a42d5c8e4b50ece53
