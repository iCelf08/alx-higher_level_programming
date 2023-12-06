#!/usr/bin/python3
"""module for read file"""

def read_file(filename=""):
    """ reads filename with uft-8"""
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
        
         
    
