"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-03-20"
-------------------------------------------------------
"""


from functions import find_indexes

values = find_indexes()
target = int(input("Enter the number to find the index for: "))

locations = find_indexes(values, target)

print()
print(locations)
