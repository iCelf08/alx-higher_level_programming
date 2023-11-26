#!/usr/bin/python3
"""Square module"""

class Square:
    """Defines square"""

    def __init__(self, size=0):
        """ initialises
        Args :
              size : size of square
        """
        self.__size = size

    @property
    def size(self):
        """ property for size in square 
        Raises :
              TypeError : if size is not an integer
              ValueError : if size less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value


    def area(self):
        """calculates area of square

        Returns :
               size squared
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square"""
        for i in range (self.__size):
            for j in range (self.__size):
                print("#", end="\n" if j is self.__size - 1 and i != j else "")
        print()
