# -*- coding: utf-8 -*-
"""
Find Large number of three numbers

"""

a = int(input("Pleae enter the first value: "))
b = int(input("Pleae enter the first value: "))
c = int(input("Pleae enter the first value: "))

if (a > b and a > c):
    print("{0} is Greater than both {1} and {2}".format(a,b,c))
elif (b > a and b > c):
    print("{1} is Greater than both {0} and {2}".format(a,b,c))
elif (c > a and c > b):
    print("{2} is Greater than both {0} and {1}".format(a,b,c))
else:
    print("All the three values are equal")    
    