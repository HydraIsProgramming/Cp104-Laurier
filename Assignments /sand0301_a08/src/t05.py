"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-03-31"
-------------------------------------------------------
"""
from functions import check_word_chain

word_list = input("Enter a list of words: ")

word_chain = check_word_chain(word_list)

print(f'\n{word_chain}')
