#!/usr/bin/python3
"""based off 9-student.py this function  below the class 
elaborates more on the Student class attribute to_json."""

class Student:
    """Class to create Student attributes"""

    def __init__(self, first_name, last_name, age):
        """initalising attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attributes=None):
        """attribute returns directory description"""
        object = self.__dict__.copy()
        if type(attributes) is list:
            for item in attributes:
                if type(item) is not str:
                    return object
                
            dict_list = {}

            for inattribute in range(len(attributes)):
                for satr in object:
                    if attributes[inattribute] == satr:
                        dict_list[satr] = object[satr]
            return dict_list
        
        return object