"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-02-02"
-------------------------------------------------------
"""
cost_one_slice = float(input("Cost of 1 pizza slice: $"))
num_of_slices = int(input("Number of slices: "))

total_cost = float(cost_one_slice * num_of_slices)

print()
print(f'Total cost of {num_of_slices} pizza slices: ${total_cost:.2f}')
