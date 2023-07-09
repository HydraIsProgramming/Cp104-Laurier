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

from functions import total_range

start = int(input("Enter value to start from: "))
increment = int(input("Enter the value for increments: "))
count = int(input("Enter the number of values: "))

total = total_range(start, increment, count)

print()
print(total)
