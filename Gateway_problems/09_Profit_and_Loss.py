# -*- coding: utf-8 -*-
"""
Profit and Loss

"""

cost_price = float(input("Enter cost price of item: "))
selling_price = float(input("Enter selling price of item: "))

if (cost_price < selling_price):
    price = selling_price - cost_price
    print("Total porfit amount = {0}".format(price))
elif (cost_price > selling_price):
    price = cost_price - selling_price
    print("Total loss amount = {0}".format(price))
else:
    print("No profit, No loss")