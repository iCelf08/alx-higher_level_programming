#!/usr/bin/python3
"""module for same classe or inherited from"""

def is_kind_of_class(obj, a_class):

    """ function determines if the object is an instance of a                          class
     Returns: true if it's the case
              otherwise false 
    """
    return isinstance(obj, a_class)
