#!/usr/bin/python3
"""Nothing here"""
class Square:
    """Goes below here"""

    def __init__(self, size=0):
        """Logic statements on numerical size"""
        if not isinstance(size,int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size