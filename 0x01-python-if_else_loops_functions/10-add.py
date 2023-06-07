#!/usr/bin/python3
def remove_char_at(str, num):
    """Create a copy of the string without the character at position n"""
    if num < 0:
        return (str)
    return (str[:num] + str[num+1:])
