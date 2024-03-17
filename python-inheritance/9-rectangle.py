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

    def area(self):
        """Gets area of rectangle"""
        return self.__width * self.__height
    
    def __str__(self):
        """returns print() rep of rectangle shape"""
        string = "[" + str(self.__class__.___name___) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string


