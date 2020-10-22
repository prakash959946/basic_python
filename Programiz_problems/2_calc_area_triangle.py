# -*- coding: utf-8 -*-
"""
Calculate the Area of a Triangle

"""
# take user iputs 
base = float(input("Enter the base of triangle: "))
height = float(input("Enter the height of triangle: "))

# formula of area of triangle
area = height * base / 2

print(area)

# if triangle sides are given 

a = float(input("Enter the side of triangle: "))
b = float(input("Enter the side of triangle: "))
c = float(input("Enter the side of triangle: "))

# calaculate the semi perimeter of the triangle

s = (a + b + c) / 2

# calaculate the area

area1= s * (s - a) * (s - b) * (s - c) / 2

print("Area of triangle is{0}".format(area1))