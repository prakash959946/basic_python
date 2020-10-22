# -*- coding: utf-8 -*-
"""
Add Two Numbers

"""
# Basic method for add two number
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))

sum = num1 + num2

print("The sum of {} and {} is {}".format(num1, num2, sum))

# add two numbers using function

def add_nums(num1, num2):
    return num1+num2

print(add_nums(num1, num2))


