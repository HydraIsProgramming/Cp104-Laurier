"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-03-17"
-------------------------------------------------------
"""
from functions import interest_data

principal = float(input("Principal: $"))
rate = float(input("Interest rate (%): "))
payment = float(input("Monthly payment: $"))

interest_data(principal, rate, payment)
