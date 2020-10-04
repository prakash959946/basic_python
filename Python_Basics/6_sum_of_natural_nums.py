# sum of first N natural numbers

"""


Example 1:
Input : 5
Output : 10 

Input : 6
Output : 16 

"""
# user input number
num = int(input("Enter the number: ")) 

# storage of sum from intial value 0
sum = 0

for n in range(0, num + 1):
    sum += n
    
print(sum)

# sum of first N natural numbers throungh while loop

