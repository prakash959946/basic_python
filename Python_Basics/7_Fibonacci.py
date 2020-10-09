#  Check if given number  is a Fibonacci number

"""
Example 1:
Input : 34
Output : Yes

Example 2:
Input : 41
Output : No
"""

import math
# Check quareroot of number
def PerfectSquare(x):
    s = int(math.sqrt(x))
    return s **2 == x
# user input 
n = int(input("Enter the number: "))
result1 = 5 * (n ** 2) + 4
result2 = 5 * (n ** 2) - 4

if PerfectSquare(result1) or PerfectSquare(result2):
    print("Yes")
else:
    print("No")



"""
def fibonacci(n):
    if n <= 0:
        print("Enter positer number")
    # First fibonacci number is 0
    elif n == 1:
        return 0
    # Second fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(9))

"""
