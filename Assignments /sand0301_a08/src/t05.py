"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-03-31"
-------------------------------------------------------
"""
from functions import check_word_chain

word_list = input("Enter a list of words: ")

word_chain = check_word_chain(word_list)

print(f'\n{word_chain}')
