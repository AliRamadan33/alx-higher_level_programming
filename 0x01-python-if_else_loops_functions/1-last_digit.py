#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if (number < 0):
    number *= -1
    a = number % 10
    a *= -1
    number *= -1
else:
    a = number % 10

if a == 0:
    print(f"Last digit of {number} is 0 and is 0")
elif a > 5:
    print(f"Last digit of {number} is {a} and is greater than 5")
else:
    print(f"Last digit of {number} is {a} and is less than 6 and not 0")
