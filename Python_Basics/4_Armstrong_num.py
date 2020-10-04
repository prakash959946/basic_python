
# Armstrong number check

"""
Example1:
Input : 153
Output : Yes
153 is an Armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153


Example2:
Input : 120
Output : No
120 is not a Armstrong number.
1*1*1 + 2*2*2 + 0*0*0 = 9

"""

num = int(input("Enter a number: ")) # input from user

sum = 0       # storage of sum of digits was start from 0
org_num = num  # user inputted number 

# sum of the cube of every digit of user input number

while org_num > 0:
    digit = org_num % 10 
    sum += digit ** 3 # sum of every digit cubes
    org_num //= 10  
    
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstron number")
