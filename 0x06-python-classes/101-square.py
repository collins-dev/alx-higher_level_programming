#!/usr/bin/python3
<<<<<<< HEAD
class Square:
    """Represents a square.
    Private instance attribute: size:
        - property def size(self)
        - property setter def size(self, value)
    Private instance attribute: position:
        - property def position(self)
        - property setter def position(self, value)
    Instantiation with optional size and optional position.
    Public instance method: def area(self).
    Public instance method: def my_print(self).
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data."""
        self.__size = size
        self.__position = position

    def __str__(self):
        """Str method for print from main module."""
        my_str = ""
        if self.__size == 0:
            return ''
        else:
            my_str += '\n' * self.__position[1]
            for i in range(0, self.__size):
                my_str += ' ' * self.__position[0]
                my_str += '#' * self.__size
                my_str += '\n'
            return my_str[:-1]

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
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square
        Args:
            size (int): size of the square
        Returns: None
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves the position."""
=======
        """sets the value for size"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """getter for position"""
>>>>>>> b734e1e857971cc40fedee1a42d5c8e4b50ece53
        return self.__position

    @position.setter
    def position(self, value):
<<<<<<< HEAD
        """Sets the position to a value."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints to stdout the square with the character #,
        at the position given by the position attribute.
        """
        if self.__size == 0:
            print()
        else:
            for y in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for x in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print()
            return ''
=======
        """sets for posution"""
        if (type(value) is tuple and len(value) == 2
                and type(value[0]) is int and type(value[1])
                is int and value[0] >= 0 and value[1] >= 0):
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """This computes the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """ prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for z in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    def __repr__(self):
        """defines the print representation of Square"""
        ret = ""
        if self.__size == 0:
            return ret
        for s in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            if i < (self.__size - 1):
                print("")
        return ret
>>>>>>> b734e1e857971cc40fedee1a42d5c8e4b50ece53
