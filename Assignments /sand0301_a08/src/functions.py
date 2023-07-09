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


def insert_spaces(string):
    """
    -------------------------------------------------------
    Create a new string with added space between words. Words start
    with upper-case characters.
    Use: new_string = insert_spaces(string)
    -------------------------------------------------------
    Parameters:
        string - string that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. string has at least one
            character (str)
    Returns:
        new_string - new string in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """
    i = 0
    new_string = ""
    new_letter = ""

    while i < len(string):

        if (ord(string[i]) < 96) and i > 0:

            new_letter = ' '.join(string[i])
            new_string += ' ' + new_letter

        elif (ord(string[i]) < 96) and i == 0:

            new_letter = ' '.join(string[i])
            new_string += new_letter

        else:

            new_letter = ''.join(string[i])
            new_string += new_letter

        i += 1

    return new_string.capitalize()


def string_pluralizer(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', replace
            the 'y' with 'ies'
        - otherwise add 's'
    Use: plural = string_pluralizer(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        plural - a plural version of string (str)
    -------------------------------------------------------
    """
    plural = string

    if string.endswith("s") or string.endswith("ch") or string.endswith("sh"):

        plural += "es"

    elif string.endswith("y") and not (string.endswith("oy") or string.endswith("ay")):

        plural = string.replace(string[-1], "ies")

    else:

        plural += "s"

    return plural


def common_postfix(string1, string2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: common = common_postfix(string1, string2)
    -------------------------------------------------------
    Parameters:
        string1 - first string for ending comparison (str)
        string2 - second string for ending comparison (str)
    Returns:
        common - the longest common ending of string1 and string2 (str)
    -------------------------------------------------------
    """
    common = string2

    while not string1.endswith(common):
        common = common[1:]

    return common


def check_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: valid = check_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    i = 0
    if (len(isbn) < 18) and (isbn[-2] == '-') and (isbn.count("-") == 4):
        while i < len(isbn):

            if isbn[i].isdigit() or isbn[i] == "-":
                if isbn[i - 1] == '-' and isbn[i] == '-':
                    valid = False
                    break

                else:
                    if isbn[0:3].isdigit():
                        if (int(isbn[0:3]) == 979) or (int(isbn[0:3]) == 978):
                            valid = True

                        else:
                            valid = False
                            break
                    else:
                        valid = False
                        break
            else:
                valid = False
                break

            i += 1
    else:
        valid = False

    return valid


def check_word_chain(word_list):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = check_word_chain(word_list)
    -------------------------------------------------------
    Parameters:
        word_list - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if word_list is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    i = 1

    while i < len(word_list):

        some_word = word_list[i - 1]
        word2 = word_list[i]
        if some_word[-1] == word2[0]:
            word_chain = True
        else:
            word_chain = False

        i += 1

    return word_chain
