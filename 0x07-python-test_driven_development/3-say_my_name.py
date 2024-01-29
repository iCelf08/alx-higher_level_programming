#!/usr/bin/python3
"""Module prints first and last name"""

def say_my_name(first_name, last_name=""):
    """function prints first and last name

    Args:
        first_name: as it says
        last_name: as it says

    Raise:
        TypeError: if one or both arguments aren't strings

    """
    if not first_name:
        raise TypeError("say_my_name() missing 1 required positional argument: 'first_name'")

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
