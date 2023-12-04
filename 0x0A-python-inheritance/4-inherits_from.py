#!/usr/bin/python3
""" module for inherits_from """

def inherits_from(obj, a_class):
    """ function to verify obj is subclass """
    return isinstance(obj, a_class) and type(obj) == a_class
