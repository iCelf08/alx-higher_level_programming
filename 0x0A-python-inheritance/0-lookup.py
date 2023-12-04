#!/usr/bin/python3
def lookup(obj):
    """ function retrievs methods of an object """
    attributes = dir(obj)
    methodes = [attr for attr in attributes
                if callable(getattr(obj, attr))]
    return attributes + methodes
