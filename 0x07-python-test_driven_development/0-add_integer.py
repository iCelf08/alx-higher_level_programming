#!/usr/bin/python3
"""Add integer"""
def add_integer(a, b=98):
    """Adds two integers
    Args:
     a: first integer
     b: second integer, initialised 98
    Raise:
     TypeError: args aren't integers or floaf
    Return:
     sum of two integers
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == '__main__':
    import doctest
    doctest.testfile("test/0-add_integer.txt")
