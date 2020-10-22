# -*- coding: utf-8 -*-
"""
Find largest number of Two

"""

a = int(input("Please enter the first value a: "))
b = int(input("Please enter the second value b: "))

if(a > b):
    print("{} is Greater than {}".format(a,b))
elif(b > a):
    print("{} is Greater than {}".format(b,a))
else:
    print("Both a and b are Equal")