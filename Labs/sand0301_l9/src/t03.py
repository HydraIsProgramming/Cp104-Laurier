"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-03-22"
-------------------------------------------------------
"""

from functions import parse_code

product_code = input("What is the product code?: ")

pc, pi, pq = parse_code(product_code)


print(pc, pi, pq)
