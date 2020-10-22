# -*- coding: utf-8 -*-
"""
Sum and Average of N natural numbers 

"""
# Take input from users
num = int(input("Enter any number: "))

# store total value in variable 'total'
total = 0


for i in range(1 , num + 1):
    total += i

average = total / num

print("The sum of Natural numbers from 1 to {0} = {1}".format(num, total))
print("The average of Natural number from 1 to {0} = {1}".format(num, average))