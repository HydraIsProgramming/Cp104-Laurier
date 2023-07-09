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
from functions import common_postfix

string1 = input("Enter first word: ")
string2 = input("Enter second word: ")

common = common_postfix(string1, string2)

print(f'\n{common}')
