#!/usr/bin/python3
"""Square module"""

class Square:
    """Defines square"""

    def __init__(self, size=0):
        """ initialises
            Args :
                size : size of square
            Raises :
              TypeError : if size is not an integer
              ValueError : if size less than 0
       """
        
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """calculates area of square
           
        Returns : 
               size squared
        """
        return self.__size ** 2
    
