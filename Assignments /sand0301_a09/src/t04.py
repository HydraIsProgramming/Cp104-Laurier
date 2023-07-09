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
from functions import add_numbers

fh_in = open("wilde.txt", 'r', encoding='utf-8')
fh_out = open("wilde_numbered.txt", 'w', encoding='utf-8')

add_numbers(fh_in, fh_out)

fh_in.close()
fh_out.close()
