"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-03-23"
-------------------------------------------------------
"""
from functions import text_analyze


txt = input("Word?: ")


uppr, lowr, dgts, whtspc = text_analyze(txt)

print(uppr, lowr, dgts, whtspc)
