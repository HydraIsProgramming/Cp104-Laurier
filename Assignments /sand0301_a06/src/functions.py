"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-03-17"
-------------------------------------------------------
"""


def total_wins():
    """
    -------------------------------------------------------
    Returns how many times blue and grey teams won.
    Use: wins = total_wins()
    -------------------------------------------------------
    Parameters:
        none
    Returns:
        None
    -------------------------------------------------------
    """
    blue_won = 0
    grey_won = 0
    user_input = 0
    while user_input != '':
        user_input = input("Enter the winning team: ")
        if user_input == "blue":
            blue_won += 1
        elif user_input == "grey":
            grey_won += 1

    return blue_won, grey_won


def is_prime_number(num):
    """
    -------------------------------------------------------
    Determines if num is a prime number.
    Use: prime = is_prime_number(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int > 1)
    Returns:
        prime - True if num is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    prime = True
    i = 2

    while i <= (num / 2):

        if (num % i) == 0:
            prime = False
            break
        i += 1

    return prime


def interest_data(principal, rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_data(principal, rate, payment)
    -------------------------------------------------------
    Parameters:
        principal - original value of a loan (float > 0)
        rate - yearly interest rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    print(f'Principal: ${principal}')
    print(f'Interest rate: {rate}%')
    print(f'Monthly payment: ${payment}')
    print("---------------------------------")
    print("Month  Interest  Payment  Balance")
    print("---------------------------------")

    balance = principal
    month = 1
    monthly_payment = payment
    interest = (rate / 12) * 10

    while balance > 0:

        interest = (balance / rate) / 12
        if (balance <= monthly_payment) and (balance >= 0):
            monthly_payment = balance + interest
        balance -= monthly_payment - interest
        print(f'{month:>4d}', end="     ")
        print(f'{interest:>4.2f}', end="    ")
        print(f'{monthly_payment:>6.2f}', end="    ")
        print(f'{balance:>6.2f}')
        month += 1

    return


def count_digits(num):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: count = count_digits(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int)
    Returns:
        count - the number of digits in num (int)
    ------------------------------------------------------
    """
    num = abs(num)
    count = 0
    i = True
    while i is True:
        count += 1
        num = num // 10
        if num < 1:
            i = False

    return count


def sum_of_factors(num):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = sum_of_factors(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int >= 1)
    Returns:
        total - the total of num's factors (int)
    ------------------------------------------------------
    """
    total = 0
    factor = 1

    while num != 0 and factor < num:
        if num % factor == 0:
            total += factor
            factor += 1
        else:
            factor += 1
    return total
