#!/usr/bin/python3
"""Defining a different shape child class"""

Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    """Represents Square"""

    def __init__(self, size):
        """making new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size