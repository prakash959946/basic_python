# -*- coding: utf-8 -*-
"""
Check if a number is positive, negative or 0

"""

num = float(input("Enter a number: "))

if num <= 0:
    if num == 0:
        print("number is 0")
    else:
        print("number is negative")
else:
    print("number is postive")