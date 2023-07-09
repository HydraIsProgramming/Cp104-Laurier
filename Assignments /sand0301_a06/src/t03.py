"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-03-17"
-------------------------------------------------------
"""
from functions import interest_data

principal = float(input("Principal: $"))
rate = float(input("Interest rate (%): "))
payment = float(input("Monthly payment: $"))

interest_data(principal, rate, payment)
