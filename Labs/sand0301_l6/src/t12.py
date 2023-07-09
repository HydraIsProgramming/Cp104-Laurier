"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-03-07"
-------------------------------------------------------
"""

from functions import gic

value = int(input("What is the GICs initial value?: "))
years = int(input("Number of years to maturity?: "))
rate = float(input("What is the percent increase value per year?: "))


print()

print(gic(value, years, rate))
