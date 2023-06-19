#!/usr/bin/python3
"""
This module define a square class
"""


class Square:
    """This defines a class square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Constructor for the square class
        Args:
            size(int): size of square
        Raises:
            TypeError: if size not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if not isinstance(position, tuple) or \
                len(position) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """
        retrieves private attribut size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        property setter to set private attribute size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Instance method that returns current square area
        """
        return self.__size * self.__size

    @property
    def position(self):
        """
        retrieves private attribute position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        sets private attributes position
        """
        if not isinstance(value, tuple) or \
                len(value) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """
        public instance that prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
