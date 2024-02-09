#!/usr/bin/python3
"""Rectangle module"""


class Rectangle(BaseGeometry):
    """Rectangle Class"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """method for retangle area"""
        return (self.__width * self.__height)

    def perimetre(self):
        """method for rectangle perimetre)"""
        return 2 * (self.__width + self.__height)
