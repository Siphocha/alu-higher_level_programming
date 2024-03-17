#!/usr/bin/python3
"""Student class and its attributes"""

class Student:
    """Class to create Student attributes"""

    def __init__(self, first_name, last_name, age):
        """initalising attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """attribute returns directory description"""
        return self.__dict__.copy()