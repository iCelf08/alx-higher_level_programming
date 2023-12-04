#!/usr/bin/python3
"""module for Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """ Constructor """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """method for counting area"""
         return self.width * self.height

    def __str__(self):
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
