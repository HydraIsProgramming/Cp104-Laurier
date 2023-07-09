"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-03-02"
-------------------------------------------------------
"""

from functions import draw_triangle

height = int(input("What is the height?: "))
char = input("What charaters do you want the traingle to be made of?: ")

print(draw_triangle(height, char))
