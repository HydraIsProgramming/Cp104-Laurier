"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-02-16"
-------------------------------------------------------
"""

from functions import fraction_multiplier

num1 = int(input("Numerator 1:"))
denom1 = int(input("Denominator 1: "))
num2 = int(input("Numerator 2: "))
denom2 = int(input("Denominator 2: "))

numerator, denominator, product = fraction_multiplier(
    num1, denom1, num2, denom2)

print()
print(f'Result: {numerator}/{denominator} = {product}')
