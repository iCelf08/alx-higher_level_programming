#!/Usr/bin/python3
"""Module prints first and last name"""

def say_my_name(first_name, last_name=""):
    """function prints first and last name
    
    Args:
         first_name: as it says
         last_name: as it says
   
    Raise:
         TypepeError : if one or both arguments arent string

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
