"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-03-31"
-------------------------------------------------------
"""
from functions import check_isbn

isbn = input("Enter an ISBN: ")

valid = check_isbn(isbn)

print(f'\n{valid}')
