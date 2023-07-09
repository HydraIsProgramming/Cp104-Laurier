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


def factorial_calculator(num):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of num.
    Use: product = factorial_calculator(num)
    -------------------------------------------------------
    Parameters:
        num - number to factorial (int > 0)
    Returns:
        product - num! (int)
    ------------------------------------------------------
    """
    product = 1
    for i in range(1, num + 1):
        product *= i
    return product


def cal_burned(per_minute, minutes):
    """
    -------------------------------------------------------
    Calculates the amount of calories burned every five
    minutes and prints a table accordingly.
    Use: total_calories = cal_burned(per_minute, minutes)
    -------------------------------------------------------
    Parameters:
        per_minute - calories burned per minute (float > 0)
        minutes - total minutes ran on the treadmill (int > 0)
    Returns:
        total_calories - total calories burned (float > 0)
    ------------------------------------------------------
    """
    if minutes > 0:
        for i in range(5, minutes, 5):
            calories_per_five_minutes = per_minute * i
            print(f"{i:>3}:   {calories_per_five_minutes:>5,.1f}")

    total_calories = minutes * per_minute
    print(f'{minutes:>3}:   {total_calories:>5,.1f}')
    return


def open_triangle_print(num_rows):
    """
    -------------------------------------------------------
    Prints a triangle with an open center depending on the
    number of rows.
    Use: design = open_triangle_print(num_rows)
    -------------------------------------------------------
    Parameters:
        num_rows - number of rows of the triangle (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    height = num_rows
    blank_space = " "
    if height != 0:
        print("##")
    for i in range(1, height, 1):
        columns = i * blank_space
        print(f'#{columns}#')
    return


def mult_table(start, stop):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start to stop.
    Use: mult_table(start, stop)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        stop - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    # Prints top x-axis
    print("        ", end="")
    for i in range(start, stop + 1):
        print(f'{i}', end="    ")
    print()
    print("     ", end="")
    for g in range(start, stop + 1):
        print("-----", end="")
    print()

    for k in range(start, stop + 1):
        # Prints the left y-axis
        print(f'  {k} |', end="   ")
        # Prints the multiplication table
        for m in range(start, stop + 1):
            total = k * m
            if total < 10:
                print(total, end="    ")
            elif (total > 9) and (total < 100):
                print(total, end="   ")
            else:
                print(total, end="  ")
        print()

    #  Returns Void
    return


def total_range(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum count values from start by increment.
    Use: total = total_range(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = 0

    for i in range(count):
        total += start
        start += increment

    return total
