"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-03-20"
-------------------------------------------------------
"""


def list_of_factors(num):
    """
    -------------------------------------------------------
    Determines the factors of num.
    Use: li = llist_of_factors(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int > 1)
    Returns:
        li - list of factors (list int > 0)
    ------------------------------------------------------
    """
    factor = 1
    li = []

    while (num != 0) and (factor < num):
        if num % factor == 0:
            li.append(factor)
            factor += 1
        else:
            factor += 1

    return li


def list_of_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: numbers = list_of_positives()
    -------------------------------------------------------
    Returns:
        numbers - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    user_input = int(input("Enter a positive number: "))
    numbers = []

    if user_input > 0:
        numbers.append(user_input)

    while user_input != 0:
        user_input = int(input("Enter a positive number: "))
        if user_input > 0:
            numbers.append(user_input)

    print()
    print(numbers)

    return numbers


def find_indexes(values, target):
    """
    -------------------------------------------------------
    Finds the indexes of target in values.
    Use: indexes = find_indexes(values, target)
    -------------------------------------------------------
    Parameters:
        values - list of value (list of int)
        target - value to look for in num_list (int)
    Returns:
        locations - list of indexes of target (list of int)
    -------------------------------------------------------
    """
    locations = []

    for i in range(len(values)):
        if values[i] == target:
            locations.append(i)

    return locations


def list_subtraction(minuend, subtrahend):
    """
    -------------------------------------------------------
    Updates the list minuend removing from it the values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are not included in the updated list.
    subtrahend is unchanged
    Use: list_subtraction(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to remove from minuend (list)
    Returns:
        None
    ------------------------------------------------------
    """
    i = 0

    while i < len(subtrahend):

        if subtrahend[i] in minuend:
            target = subtrahend[i]
            for j in range(len(minuend) - 1, -1, -1):
                if minuend[j] == target:
                    minuend.pop(j)

        i += 1

    return


def check_sorted(values):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = check_sorted(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list)
    Returns:
        in_order - True if values is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    in_order = True
    index = -1
    min_val = values[0]

    for i in values:
        if i != 0:
            current_value = i
            if current_value < min_val:
                min_val = current_value

    if values[0] == min_val:
        in_order = True
        index = -1

    else:
        in_order = False
        index = min_val

    return in_order, index
