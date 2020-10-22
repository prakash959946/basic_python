# -*- coding: utf-8 -*-
"""
Print natural numbers in Reverse order

"""
"""
num = int(input("Enter enter any number: "))

i = num
print("List of natural numbers from {} to 1 in reverse oder:".format(num))

while (i >= 1):
    print(i, end=' ')
    i = i - 1
"""

max = int(input("Please enter the maximum integer value: "))
min = int(input("Please enter the minimum integer value: "))

print("List of Natural numbers from {0} to {1}:".format(max,min))

while (max >= min):
    print(max, end = ' ')
    max -= 1