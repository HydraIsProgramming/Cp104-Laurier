"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-02-17"
-------------------------------------------------------
"""
# Imports
from random import randint


# Constants


def footage_to_acres(square_feet):
    """
    -------------------------------------------------------
    Converts square footage to acres.
    Use: acres = footage_to_acres(square_feet)
    -------------------------------------------------------
    Parameters:
        square_feet - area in square feet (float >= 0)
    Returns:
        acres - square_footage in acres (float)
    ------------------------------------------------------
    """

    acres = square_feet / 43560

    return acres


def lawn_mowing(width, length, speed):
    """
    -------------------------------------------------------
    Determines how long it takes to mow a rectangular lawn.
    Use: time = lawn_mowing(width, length, speed)
    -------------------------------------------------------
    Parameters:
        width - width of a lawn in metres (float > 0)
        length - length of a lawn in metres (float > 0)
        speed - square metres cut per minute (float > 0)
    Returns:
        time_minutes - time required to mow the lawn (float)
    ------------------------------------------------------
    """

    result = (width * length) // speed

    return result


def date_extraction(date_number_format):
    """
    -------------------------------------------------------
    Extracts the year, month, and day from a date number in the format MMDDYYYY.
    Use: year, month, day = date_extraction(date_number_format)
    -------------------------------------------------------
    Parameters:
        date_number_format - a date number in the format MMDDYYYY (int > 0)
    Returns:
        year - year portion of date_number (int)
        month - month portion of date_number (int)
        day - day portion of date_number (int)
    ------------------------------------------------------
    """
    year = int(date_number_format % 10000)
    month = int(date_number_format // 1000000)
    day = int((date_number_format // 10000) % 100)

    return year, month, day


def fraction_multiplier(num1, denom1, num2, denom2):
    """
    -------------------------------------------------------
    Multiplies two fractions together and returns the results
    Use: numerator, denominator, product = fraction_multiplier(num1, denom1, num2, denom2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of the first fraction (int)
        denom1 - denominator of the first fraction (int)
        num2 - numerator of the second fraction (int)
        denom2 - denominator of the second fraction (int)
    Returns:
        numerator - numerator of the resulting fraction (int)
        denominator - denominator of the resulting fraction  (int)
        product - numerator divided by denominator (float)
    ------------------------------------------------------
    """
    numerator = num1 * num2
    denominator = denom1 * denom2
    product = numerator / denominator
    return numerator, denominator, product


def math_quiz():
    """
    -------------------------------------------------------
    Generates two random numbers between 0 and 999 and asks the user to enter the sum
    Use: result = math_quiz()
    -------------------------------------------------------
    Parameters:
        None
    Returns:
        None
    ------------------------------------------------------
    """
    num1 = randint(0, 999)
    num2 = randint(0, 999)

    answer = num1 + num2

    print(f'  {num1}')
    print(f'+ {num2}')

    print()
    user_answer = int(input("Your answer: "))

    print()
    print(f'Your answer:     {user_answer}')
    print(f"Expected answer: {answer}")
    return
