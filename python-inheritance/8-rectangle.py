#!/usr/bin/python3

"""This class Rectangle is a subclass of BaseGeometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """Child class using parent attributes"""
    def __init__(self, width, height):
        """initlaising new rectangle shape adding variables"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height 