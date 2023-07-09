"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-02-16"
-------------------------------------------------------
"""


from functions import date_extraction

date_number_format = int(input("Enter a date in the format MMDDYYYY: "))

year, month, day = date_extraction(date_number_format)

print(f'The reformatted date: {year}/{month:02d}/{day:02d}')
