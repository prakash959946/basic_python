
# Simple Interest

"""
Example 1:
Input : P = 10000
           R = 5
           T = 5
Output :2500

"""
P = float(input("Enter Principle amount: "))
T = float(input("Enter rate Time period: "))
R = float(input("Rate of Interest per annuam: "))

si = P * T * R / 100
print(si)