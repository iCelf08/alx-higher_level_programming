#!/usr/bin/python3
"""module for lookup method"""

def lookup(obj):
    """ function retrievs methods of an object 
    Args:
        obj (object): the object to list
    Returns:
         list of attributes
    """
    return dir(obj)
