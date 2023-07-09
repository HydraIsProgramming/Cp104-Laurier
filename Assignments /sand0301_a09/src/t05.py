"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-04-08"
-------------------------------------------------------
"""
from functions import student_data

students = open("students.txt", 'r', encoding='utf-8')

l_id, h_id, avg = student_data(students)

students.close()

print(f'{l_id}, {h_id}, {avg:.2f}')
