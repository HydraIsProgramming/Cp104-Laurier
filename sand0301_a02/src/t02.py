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
user_num = int(input("Enter a positive two digit number: "))

user_num_tenths = user_num // 10


user_num_ones = user_num % 10


user_num_product = user_num_tenths * user_num_ones

print()
print(f'The product of the digits {user_num} is {user_num_product}')
