"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-03-07"
-------------------------------------------------------
"""

from functions import gic

value = int(input("What is the GICs initial value?: "))
years = int(input("Number of years to maturity?: "))
rate = float(input("What is the percent increase value per year?: "))


print()

print(gic(value, years, rate))
