# -*- coding: utf-8 -*-
"""

Add two lists

"""
"""
# Initializing lists
list1 = [4, 5, 6, 7, 8]
list2 = [9, 10, 11, 12, 13]

# Using navie method to concat
for i in list2:
    list1.append(i)

# Display the concatenated list    
print("Concatenated list using navie method: " + str(list1))

"""

list1 = [4, 5, 6, 7, 8]
list2 = [9, 10, 11, 12, 13]

list3 = list1 + list2

print("Concatenated list using + operator : " + str(list3))


