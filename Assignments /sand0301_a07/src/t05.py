"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-03-20"
-------------------------------------------------------
"""

from functions import check_sorted, list_of_positives

values = list_of_positives()

in_order, index = check_sorted(values)

print()
print(f'{in_order}, {index}')
