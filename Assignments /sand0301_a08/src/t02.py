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
from functions import string_pluralizer

string = input("Enter a word to pluralize: ")

plural = string_pluralizer(string)

print(f'\n{plural}')
