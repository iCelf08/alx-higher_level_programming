#!/usr/bin/python3
"""Write a function that adds 2 integers.

Prototype: def add_integer(a, b=98):
a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
a and b must be first casted to integers if they are float
Returns an integer: the addition of a and b
"""

def add_integer(a, b=98):
    """
    Adds two numbers together and returns the result as an integer.

    :param a: The first number (integer or float).
    :param b: The second number (integer or float). Default value is 98.
    :return: The addition of `a` and `b` as an integer.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = round(a)
    if isinstance(b, float):
        b = round(b)
    return int(a + b)
