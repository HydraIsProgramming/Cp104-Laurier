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
from functions import file_header

fh = open("random.py", "r", encoding="utf-8")
linecount = int(input("Enter the number of lines to print: "))

file_header(fh, linecount)

fh.close()
