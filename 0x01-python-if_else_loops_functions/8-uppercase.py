#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase."""
    for cr in str:
        if ord(cr) >= 97 and ord(cr) <= 123:
            cr = chr(ord(cr) - 32)
        print("{}".format(cr), end="")
    print("")
