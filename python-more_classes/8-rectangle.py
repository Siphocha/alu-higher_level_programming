#!/usr/bin/python3
"""Defining a class known as Rectangle"""
class Rectangle:
    """Initialising rectangle and definnning it"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Call property function to use attributes defined above"""
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

    def area(self):
        return(self.__width * self.__height)
    
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            """Error catching incase theres a 0 in the integers"""
            return(0)
        return ((self.__width * 2) + (self.__height * 2))
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """argument for retaining rectangle with greatest size"""
        """questions intructions specified using recet_1&2 as variable name"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return(rect_1)
        return(rect_2)


    def __str__(self):
        """Everything here is what returns a printable representation of rectangle"""
        if self.__width == 0 or self.__height == 0:
            """another error catch"""
            return("")
        
        rect_shape = []
        for i in range(self.__height):
            [rect_shape.append("#") for n in range(self.__width)]
            if i != self.__height - 1:
                rect_shape.append("\n")
        return("".join(rect_shape))
    
    def __repr__(self):
        """returns the rectangle as a string"""
        rect_shape = "Rectangle(" + str(self.__width)
        rect_shape = ", " + str(self.__height) + ")"
        return(rect_shape)
    
    def __del__(self):
        """prints message for every deleted segment of rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")