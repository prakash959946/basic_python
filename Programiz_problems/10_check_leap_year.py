# -*- coding: utf-8 -*-
"""
Check leap year

"""
year = int(input("Enter year: "))

def leap_year_check(year):
    return year % 4 and 400 == 0