#!/usr/bin/python3
"""Module Mylist """

class MyList(list):
    """ class that inhirits from list """
    def print_sorted(self):
        """ Methode for printing sorted list"""
        print(sorted(self))
