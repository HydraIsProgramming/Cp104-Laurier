"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-04-08"
-------------------------------------------------------
"""
from functions import text_stats

fh = open("addresses.txt", 'r', encoding='utf-8')

ucount, lcount, dcount, wcount = text_stats(fh)
fh.close()

print(f'{ucount}, {lcount}, {dcount}, {wcount}')
