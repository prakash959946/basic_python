# -*- coding: utf-8 -*-
"""
Calendar Example

"""
# import calendar module
import calendar

# Take inputs for year and month from the user
year = int(input("Please enter the year: "))
month = int(input("Please enter the month: "))

# Display the calendar of particular month
print(calendar.month(year, month))