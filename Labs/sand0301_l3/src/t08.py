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
dirt = float(input("Enter amount of dirt (m^3): "))
gravel = float(input("Enter amount of gravel (m^3): "))
sand = float(input("Enter amount of sand (m^3): "))

total = dirt + gravel + sand

print("Material   Cubic Metres")
print(f"Dirt       {dirt: >5.1f}")
print(f"Gravel     {gravel: >5.1f}")
print(f"Sand       {sand: >5.1f}")
print(f"Total      {total: >5.1f}")
