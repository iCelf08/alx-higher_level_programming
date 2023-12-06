#!/usr/bin/python3
""" module to write a text file"""

def append_write(filename="", text=""):
    """ reads filename with utf-8"""
    with open(filename, "a", encoding='utf-8') as file:
        return file.write(text)
