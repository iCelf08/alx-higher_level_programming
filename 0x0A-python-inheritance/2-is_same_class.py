#!/usr/bin/python3
""" module for is_same_classe """

def is_same_clase(obj, a_class):

    """  function that check is exactly an instance
         of the specified class
      Returns: true for yes otherwise false
    """
    return type(obj) == a_class
