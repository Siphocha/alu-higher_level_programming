#!/usr/bin/python3
"""Defining attribute of first class"""

class BaseGeometry:
    """Class with base attribute"""
    def area(self):
        """function for defining area"""
        raise Exception("area() is not implemented")