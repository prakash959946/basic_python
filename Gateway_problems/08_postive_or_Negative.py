# -*- coding: utf-8 -*-
"""
Positive or Negative

"""

num = float(input("Enter any numeric value: "))

if (num < 0):
    print('{0} is a Negative number'.format(num))
elif (num > 0):
    print('{0} is a positive number'.format(num))
else:
    print("You have entered Zero")    
