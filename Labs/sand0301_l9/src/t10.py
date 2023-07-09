"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-03-23"
-------------------------------------------------------
"""
from functions import text_analyze


txt = input("Word?: ")


uppr, lowr, dgts, whtspc = text_analyze(txt)

print(uppr, lowr, dgts, whtspc)
