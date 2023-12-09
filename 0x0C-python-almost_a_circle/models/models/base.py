#!/usr/bin/python3
'''Module for Bqse class '''

class Base:
    ''' Base of OOP hierarchy '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''intialiser'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            
