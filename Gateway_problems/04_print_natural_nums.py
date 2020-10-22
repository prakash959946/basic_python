# -*- coding: utf-8 -*-
"""
Print Natural Numbers from 1 to N
"""

# using for loop
num = int(input("Enter your number: "))

print("The lis of natual numbers from 1 to {0} are".format(num))
for i in range(1, num+1):
    print(i, end=' ')


# using while loop
num = int(input("Enter your number: "))
i = 1

while (i <= num):
    print(i, end=' ')
    i = i + 1