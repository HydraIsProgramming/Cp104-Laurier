"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-03-10"
-------------------------------------------------------
"""

from functions import cal_burned

per_minute = float(input("Enter the number of calories burned per minute: "))
minutes = int(input("Enter the total minutes ran: "))

total_calories = cal_burned(per_minute, minutes)
