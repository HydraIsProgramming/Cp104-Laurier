"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-04-08"
-------------------------------------------------------
"""
from functions import extract_integers

fh = open("numbers.txt", "r", encoding="utf-8")

numbers = extract_integers(fh)

print(numbers)
