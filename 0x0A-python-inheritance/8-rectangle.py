#!/usr/bin/python3
"""Rectangle module"""


class Rectangle(BaseGeometry):
    """Rectangle Class"""
    def __init__(self, width, height):
    """ constructor for Rectangle"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
