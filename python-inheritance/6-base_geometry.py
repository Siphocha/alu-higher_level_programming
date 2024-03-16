#!/usr/bin/python3
"""Defining attribute of first class"""

class BaseGeometry:

    def area(self):
        """function for defining area"""
        raise Exception("area() is not implemented")