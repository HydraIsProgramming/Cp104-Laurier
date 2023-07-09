"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-03-17"
-------------------------------------------------------
"""
from functions import generate_integer_list

n = int(input("Enter the range of values: "))
low = int(input("Enter the lowest value: "))
high = int(input("Enter the highest value: "))

values = generate_integer_list(n, low, high)

print()
print(values)
