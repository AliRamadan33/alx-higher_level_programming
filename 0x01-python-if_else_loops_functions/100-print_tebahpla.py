#!/usr/bin/python3
"""Print the alphabet in reverse order alterning upper and lower case"""
i = 0
for cr in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(cr - i)), end="")
    i = 32 if i == 0 else 0