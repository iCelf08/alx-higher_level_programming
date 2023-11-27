#!/usr/bin/python3
"""Rectangle module"""

class Rectangle:
    """Defines Rectangle"""
    def __init__(self, width=0, height=0):
        """Construct:
        Arg:
            width : width of rectangle
            height : height of rectangle
        """
        self.__width = width
        self.__height = height
        
    
    @property
    """property instance width
    Return:
         value of width
    """
    def width(self):
        """Property getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter"""
        if not isinstance(value, int):
            raise TypeError('width must be integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value


    @property
    def height(self):
        """Property getter for height"""
        return self.__height

    @height.setter:
    def height(self, value):
        """Property setter for height"""
        if not isinstance(value, int):
            raise TypeError('height must be integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
