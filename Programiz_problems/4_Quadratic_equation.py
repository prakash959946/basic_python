# -*- coding: utf-8 -*-
"""
Solve Quadratic Equation

"""
# import math module
import math

# take inputs from user
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

# calaculate the discriminant
d = (b ** 2) - (4 * a * c)

# find two solutions
sol1 = (-b - math.sqrt(d)) / (2*a)
sol2 = (-b + math.sqrt(d)) / (2*a)

# display the answer using f'string
print("The solutions are {} and {}".format(sol1, sol2))
