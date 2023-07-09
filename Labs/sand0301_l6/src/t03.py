"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-03-02"
-------------------------------------------------------
"""
# Imports

# Constants

from functions import sum_all

start = int(input("What number does it start with?: "))
finish = int(input("What number does it end with?: "))
increment = int(input("What are the increments?: "))

print(sum_all(start, finish, increment))
