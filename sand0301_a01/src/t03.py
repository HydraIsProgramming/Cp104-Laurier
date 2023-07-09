"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-01-30"
-------------------------------------------------------
"""
ONE_METRE_OF_AN_INCH = 0.0254

user_length = float(input("Length in inches: "))

inches_to_metres = user_length * ONE_METRE_OF_AN_INCH

print()
print(f'Length in metres: {inches_to_metres}')
