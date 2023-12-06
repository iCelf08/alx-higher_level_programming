#!/usr/bin/python3
"""module for to_json_srtring"""

import json

def to_json_string(my_obj):
    """ returns json repr of an obj"""
    return json.dumps(my_obj)
