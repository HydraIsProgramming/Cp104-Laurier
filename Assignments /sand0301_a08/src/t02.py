"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-03-31"
-------------------------------------------------------
"""
from functions import string_pluralizer

string = input("Enter a word to pluralize: ")

plural = string_pluralizer(string)

print(f'\n{plural}')
