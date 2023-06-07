#!/usr/bin/python3
for i in range(122, 64, -1):
    if i % 2 == 0:
        print(f"{chr(i)}", end="")
    else:
        print(f"{chr(i).upper()}", end="")
