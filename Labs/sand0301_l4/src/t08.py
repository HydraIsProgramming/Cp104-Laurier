"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-02-10"
-------------------------------------------------------
"""

from functions import computer_costs

computer_cost = float(input("What is the cost of the computer?: "))
computers_bought = int(input("How many computers did you buy?: "))
commission_percent = float(input("What is the commission percent?: "))

pre_commission_cost, total_cost = computer_costs(
    computer_cost, computers_bought, commission_percent)
print(f'{pre_commission_cost:.2f}')
print(f'{total_cost:.2f}')
