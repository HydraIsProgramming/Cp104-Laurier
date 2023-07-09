"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-01-31"
-------------------------------------------------------
"""
principal = float(input("Principal: $"))
interest = float(input("Interest: "))
num_of_years = int(input("Number of years: "))
interest_compounded_per_year = int(
    input("Number of times interest compounded per year: "))

interest_decimal = interest/100

accumulated_money = principal * \
    ((1 + (interest_decimal / interest_compounded_per_year))
     ** (interest_compounded_per_year * num_of_years))

print(f'Balance: ${accumulated_money}')
