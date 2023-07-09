"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-02-03"
-------------------------------------------------------
"""


# Constants
TAX_RATE = 0.185

projected_sales = float(input("Enter the total sales: $"))

tax_paid = float(projected_sales * TAX_RATE)
printed_tax_rate = TAX_RATE * 100

print()
print("Projected Tax Report")
print("-----------------------")
print(f'Total Sales: ${projected_sales:,.2f}')
print(f'Annual Tax:  %{printed_tax_rate:.2f}')
print("-----------------------")
print(f"Tax:         ${tax_paid:,.2f}")
