"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-03-10"
-------------------------------------------------------
"""

from functions import cal_burned

per_minute = float(input("Enter the number of calories burned per minute: "))
minutes = int(input("Enter the total minutes ran: "))

total_calories = cal_burned(per_minute, minutes)
