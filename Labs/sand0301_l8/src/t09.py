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

from functions import many_search

value = 96

values = [94, 96, -22, -79, -28, 96, -50, 71, 24, -32]

indexes = many_search(values, value)

print(indexes)
