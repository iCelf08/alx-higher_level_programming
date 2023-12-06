#!/usr/bin/python3
"""module save_to_json function"""

import json

def save_to_json_file(my_obj, filename):
    """writs objct to txt file"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dumps(my_obj, file)
