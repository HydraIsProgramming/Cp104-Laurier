"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-02-03"
-------------------------------------------------------
"""
# Imports

import math

# Constants

FREEZING = 32

DAYS = 86400
HOURS = 3600
MINUTES = 60
SECONDS = 1


def circumference(radius):
    """
    -------------------------------------------------------
    Calculates and returns circumference of a circle.
    Use: circ = circumference(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        circ - circumference of a circle (float)
    ------------------------------------------------------
    """
    x = 2*(math.pi)*radius
    return x


def right_triangle(adjacent, opposite):
    """
    -------------------------------------------------------
    Calculates and returns the hypotenuse, circumference, and
    area of a right triangle given two non-hypotenuse sides.
    Use: hyp, circ, area = right_triangle(adjacent, opposite)
    -------------------------------------------------------
    Parameters:
        adjacent - length of side right triangle (float > 0)
        opposite - length of side right triangle (float > 0)
    Returns:
        hyp - hypotenuse of the triangle (float)
        circ - circumference of the triangle (float)
        area - area of the triangle (float)
    ------------------------------------------------------
    """
    hyp = math.sqrt(adjacent**2 + opposite**2)
    circ = hyp + adjacent + opposite
    area = (adjacent * opposite)/2
    return hyp, circ, area


def computer_costs(computer_cost, computers_bought, commission_percent):
    """
    -------------------------------------------------------
    Calculates purchase costs of computers
    Use: pre_commission_cost, total_cost = computer_costs(computer_cost,
        computers_bought, commission_percent)
    -------------------------------------------------------
    Parameters:
        computer_cost - per unit cost (float >= 0)
        computers_bought - units bought (int >= 0)
        commission_percent - wholesaler commission (float >= 0)
    Returns:
        pre_commission_cost - cost before commission (float)
        total_cost - cost after commission (float)
    -------------------------------------------------------
    """
    pre_commission_cost = computer_cost * computers_bought
    commission = (pre_commission_cost *
                  (1 + (commission_percent/100)))-pre_commission_cost
    total_cost = pre_commission_cost + commission
    return pre_commission_cost, total_cost


def c_to_f(celsius):
    """
    -------------------------------------------------------
    Converts temperatures in celsius to fahrenheit.
    Use: fahrenheit = c_to_f(celsius)
    -------------------------------------------------------
    Parameters:
        celsius - temperature in celsius (int >= -273)
    Returns:
        fahrenheit - equivalent to celsius (float)
    -------------------------------------------------------
    """
    fahrenheit = (celsius * (9/5)) + FREEZING
    return fahrenheit


def time_split(initial_seconds):
    """
    -------------------------------------------------------
    Converts total seconds into days, hours, minutes, and seconds.
    Use: days, hours, minutes, seconds = time_split(initial_seconds)
    -------------------------------------------------------
    Parameters:
        initial_seconds - time elapsed (int >= 0)
    Returns:
        days - number of days in initial_seconds (int)
        hours - remaining hours in initial_seconds (int)
        minutes - remaining minutes in initial_seconds (int)
        seconds - remaining seconds in initial_seconds (int)
    -------------------------------------------------------
    """
    days = initial_seconds // DAYS
    initial_seconds = initial_seconds % DAYS

    hours = initial_seconds // HOURS
    initial_seconds = initial_seconds % HOURS

    minutes = initial_seconds // MINUTES
    initial_seconds = initial_seconds % MINUTES

    seconds = initial_seconds // SECONDS
    initial_seconds = initial_seconds % SECONDS

    return days, hours, minutes, seconds,
