"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-03-22"
-------------------------------------------------------
"""

from functions import parse_code

product_code = input("What is the product code?: ")

pc, pi, pq = parse_code(product_code)


print(pc, pi, pq)
