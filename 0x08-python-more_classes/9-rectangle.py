#!/usr/bin/python3
"""Rectangle module"""

class Rectangle:
    """Defines Rectangle"""
    number_of_instances = 0
    print_symbol = '#'
    def __init__(self, width=0, height=0):
        """Construct:
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height
        
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """clss method returns new triangle with width == height == size"""
        return cls(size, size)

    @property
    def width(self):
        """Property getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        
    @property
    def height(self):
        """Property getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter for height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value


    def area(self):
        """Calculates area"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculates perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.__height + self.__width)



    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))


    def __repr__(self):
        """Return the string representation of rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
    

    def __del__(self):
        type(self).number_of_instances -= 1
        """prints Bye rectangle... when Rectangle is deleted"""
        print("Bye rectangle...")
