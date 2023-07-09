"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-02-06"
-------------------------------------------------------
"""
pieces_of_cake = int(input("Number of pieces of cake: "))
party_members = int(input("Number of party-goers: "))

pieces_per_member = int(pieces_of_cake // party_members)

pieces_left_over = int(pieces_of_cake % party_members)

print()
print(f'Each party-goer receives {pieces_per_member} pieces of cake')
print(f'Pieces of cake that won’t be distributed: {pieces_left_over}')
