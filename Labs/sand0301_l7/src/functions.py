"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-03-10"
-------------------------------------------------------
"""
# Imports
from random import randint
# Constants


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    guess = 0
    count = 0
    number = randint(1, high)
    while guess != number:
        guess = int(input("What is the number?: "))
        count += 1
        if guess > number:
            print("Too high")

        elif guess < number:
            print("Too low")

        else:
            print("Congratulations")

    return count


def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """

    n = 0
    y = 2 ** n
    power = 2 ** n
    while target >= y:
        if 2 ** n >= target:
            break
        else:
            y = 2 ** n
        power = 2 ** (n + 1)
        n += 1
    return power


def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """
    count = 1
    number = float(input("First positive value: "))
    minimum = number
    maximum = number
    total = number
    number = float(input("Next positive value: "))
    while number >= 0:
        count += 1
        if number < minimum:
            minimum = number
        elif number > maximum:
            maximum = number
        total += number
        number = float(input("Next positive value: "))
    average = total/count

    return minimum, maximum, total, average


def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expenses in a month. Calculate the
    total expenses and determines whether the user is in "Surplus",
    "Deficit", or "Balanced" status.
    Use: expenses, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
        available - money currently available (float >= 0)
    Returns:
        expenses - total monthly expenses (float)
        balance - remaining balance (float)
        status - One of (str):
            "Surplus" if user budget is in surplus
            "Deficit" if user budget is in deficit
            "Balanced" if user budget is balanced
    ------------------------------------------------------
    """
    number = float(input("Enter an expense (0 to quit): $"))
    expense = 0

    while number > 0:
        expense += number

        number = float(input("Enter another expense (0 to quit): $"))
    balance = available - expense
    if balance > 0:
        status = "Surplus"
    elif balance < 0:
        status = "Deficit"
    else:
        status = "Balanced"

    return expense, balance, status


def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """

    OVERTIME = 40
    OVERTIME_RATE = 1.5
    TAX = 3.625

    number = int(input('Employee ID: '))
    total = 0
    count = 0
    while number > 0:
        count += 1
        wage = int(input("Hourly wage rate: "))
        hours = int(input("Hours worked: "))
        if hours > OVERTIME:
            regular_pay = OVERTIME * wage
            extra_hours = hours - OVERTIME
            pay = extra_hours * (wage * OVERTIME_RATE)
            gross = pay + regular_pay

        else:
            gross = wage * hours

        net = gross - ((gross * TAX)/100)
        print(f"Net payment for employee {number}: $ {net:,.2f}")
        total += net
        print()
        number = int(input('Employee ID: '))

    average = total / count

    return total, average
