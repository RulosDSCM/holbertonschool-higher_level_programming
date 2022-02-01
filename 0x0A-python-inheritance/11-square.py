#!/usr/bin/python3
"""Creates a new subclass"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creates a new subclass"""

    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
