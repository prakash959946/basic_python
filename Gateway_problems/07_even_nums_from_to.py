# -*- coding: utf-8 -*-
"""
Even numbers from one number to another number

"""
# Take inputs from user for start value and end value
start = int(input("Please enter start number: "))
end = int(input("Please enter end number: "))

# Even and odd numbers between start number and end number which was taken from user
for i in range(start, end + 1):
    if (i % 2 == 0):
        print(i, end = ' ')
    else:
        print(end = 'odd ')
