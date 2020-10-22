# -*- coding: utf-8 -*-
"""
Multiplication table

"""
"""
print("Multiplication Table")

for i in range(8, 10):
    for j in range(1 , 11):
        print("{0} * {1} = {2}".format(i, j, i * j))
    print("===========")
    
"""

num = int(input("Please enter any positive integer lessthan 10: "))

print("Multiplication Table")

while (num <= 10):
    j = 1
    while (j <= 10):
        print("{0} * {1} = {2}".format(num, j, num * j))
        j += 1
    print("========")
    num += 1
