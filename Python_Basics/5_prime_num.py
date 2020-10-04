
# Print all Prime numbers in an Interval

"""
Example 1:
Input: 
start = 11
end = 25
Output:
11 , 13, 17, 19, 23

"""

start = int(input("Enter starting number: ")) # starting number of user input
end = int(input("Enter ending number: "))    # ending number of user input

# range function can't give the last number so we add +1
for num in range(start, end + 1): 
    # all prime numbers are greater than 1 , that's why our condition is > 1
    if num > 1:
        for i in range(2, num):
            if num % i == 0: 
                break
        else:
            print(num)
            
