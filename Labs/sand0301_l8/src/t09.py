"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-03-17"
-------------------------------------------------------
"""

from functions import many_search

value = 96

values = [94, 96, -22, -79, -28, 96, -50, 71, 24, -32]

indexes = many_search(values, value)

print(indexes)
