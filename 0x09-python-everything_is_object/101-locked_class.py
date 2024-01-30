#!/usr/bin/python3
class LockedClass:
    """ Class with no class or object attribut"""
    __slots__ = ("first_name")

    def __setattr__(self, name, value):
        if name != "first_name":
        raise AttributeError("'LockedClass' object has no attribute '%s'", %name)
       self.__dict__[name] = value
