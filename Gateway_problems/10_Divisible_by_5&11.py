# -*- coding: utf-8 -*-
"""
Check number divisible by 5 and 11

"""

num = int(input("Enter any positive integer: "))

if (num % 5 == 0) and (num % 11 == 0):
    print("{0} divisible by 5 and 11".format(num))
else:
    print("Givne number {0} is not divisible by 5 and 11".format(num))
