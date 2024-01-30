#!/usr/bin/python3
class LockedClass:
    """ Class with no class or object attribut"""
    __slots__ = ("first_name")

    def __init__(self):
        """construct for first_name"""
        self.first_name = "first_name"
