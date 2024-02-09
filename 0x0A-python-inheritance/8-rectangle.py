#!/usr/bin/python3
"""Rectangle module"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class"""
    def __init__(self, width, height):
        """ constructor for Rectangle"""
        self.integer_validator("width", self.__width)
        self.__width = width
        self.integer_validator("height", self.__height)
        self.__height = height
