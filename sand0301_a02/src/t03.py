"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-02-06"
-------------------------------------------------------
"""
entered_date = int(input("Enter a date in the format DDMMYYYY: "))

input_year = entered_date % 10000

input_month = (entered_date // 10000) % 100


input_day = entered_date // 1000000


print()
print(f'The reformatted date: {input_year}/{input_month:02d}/{input_day:02d}')
