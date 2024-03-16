#!/usr/bin/python3

class BaseGeometry:

    def area(self):
        """function for defining area"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """validation for integers for use"""
        if type(value) != int:
            raise TypeError ("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))