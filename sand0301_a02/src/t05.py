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
foundation_length = float(input("Foundation length (m): "))
foundation_width = float(input("Foundation width (m): "))
foundation_height = float(input("Foundation height (m): "))

wall_height = float(input("Wall height (m): "))

cost_of_concrete = float(input("Cost of concrete ($/m^3): "))
cost_of_bricks = float(input("Cost of bricks ($/m^2): "))

volume_of_foundation = foundation_length * foundation_width * foundation_height

area_of_sides = 2 * (foundation_length * wall_height)
area_of_front_and_back = 2 * (foundation_width * wall_height)

concrete_needed = volume_of_foundation
cost_for_needed_concrete = cost_of_concrete * volume_of_foundation

bricks_needed = int(area_of_sides + area_of_front_and_back)
cost_for_needed_bricks = cost_of_bricks * bricks_needed

total_cost = cost_for_needed_concrete + cost_for_needed_bricks

print()
print(f'Concrete needed for foundation (m^3): {concrete_needed:,.2f}')
print(f'Cost of concrete: ${cost_for_needed_concrete:,.2f}')
print(f'Bricks needed for walls (m^2): {bricks_needed:,}')
print(f'Cost of bricks: ${cost_for_needed_bricks:,.2f}')
print(f'Total cost: ${total_cost:,.2f}')
