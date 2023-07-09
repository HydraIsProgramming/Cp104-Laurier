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


def file_header(fh, linecount):
    """
    -------------------------------------------------------
    Prints first linecount lines of fh. Line numbering starts at 0.
    If length of file is shorter than linecount, stops printing after
    last line of file.
    Use: file_header(fh, linecount)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
        linecount - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0

    while i < linecount:
        line = fh.readline()
        print(line.strip())
        i += 1
    return


def extract_integers(fh):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: numbers = extract_integers(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process ( (file handle - open for reading)
    Returns:
        numbers - a list of integers from fh (list of int)
    -------------------------------------------------------
    """
    line = fh.readline()
    numbers = []

    while line != "":

        new_line = line.strip('\n').split(",")

        i = 0
        while i < len(new_line):
            if new_line[i].isdigit():
                numbers.append(int(new_line[i]))

            i += 1
        line = fh.readline()

    return numbers


def text_stats(fh):
    """
    -------------------------------------------------------
    Evaluates the contents of a file.
    Use: ucount, lcount, dcount, wcount = text_stats(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
    Returns:
        ucount - The number of uppercase letters in the file (int)
        lcount - The number of lowercase letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of whitespace characters in the file (int)
    -------------------------------------------------------
    """
    line = fh.readline()
    ucount = 0
    lcount = 0
    dcount = 0
    wcount = 0

    while line != "":

        i = 0
        while i < len(line):

            if line[i].isupper():
                ucount += 1
            elif line[i].islower():
                lcount += 1
            elif line[i].isdigit():
                dcount += 1
            elif line[i] == " ":
                wcount += 1
            i += 1

        line = fh.readline()

    return ucount, lcount, dcount, wcount


def add_numbers(fh_in, fh_out):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_out contain contents
    of fh_in where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: add_numbers(fh_in, fh_out)
    -------------------------------------------------------
    Parameters:
        fh_in - file to read (file - open for reading)
        fh_out - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    line = fh_in.readline()
    i = 0

    while line != "":

        fh_out.write(f'[{i}] {line}')
        i += 1
        line = fh_in.readline()

    return


def student_data(students):
    """
    -------------------------------------------------------
    Get information from a file of students and grades.
    Use: l_id, h_id, avg = student_data(students)
    -------------------------------------------------------
    Parameters:
        students - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
    line = students.readline()
    new_line = line.strip("\n").split(",")
    l_id = new_line[2]
    h_id = new_line[2]
    lowest_mark = int(new_line[3])
    highest_mark = int(new_line[3])
    total = 0
    i = 0
    avg = 0

    while line != "":

        new_line = line.strip("\n").split(",")
        current_mark = int(new_line[3])

        if current_mark < lowest_mark:
            l_id = new_line[2]
            lowest_mark = current_mark
        elif current_mark > highest_mark:
            h_id = new_line[2]
            highest_mark = current_mark
        total += float(new_line.pop(3))
        i += 1
        line = students.readline()
    avg = float(total / i)

    return l_id, h_id, avg
