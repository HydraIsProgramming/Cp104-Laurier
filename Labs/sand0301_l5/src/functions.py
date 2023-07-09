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

# Constants

GRAVITY = 9.8

INFANT = 0.00
SENIOR = 4.00
STUDENT = 3.00
STUDENTOFSCHOOL = 1.00
ADULT = 5.00
KID = 2.00

INFANTAGE = 3
SENIORAGE = 65
STUDENTAGE1 = 10
STUDENTAGE2 = 18
ADULTAGE1 = 18
ADULTAGE2 = 65


def get_weight(mass):
    """
    -------------------------------------------------------
    Describes a mass in terms of its weight. If its weight is > 1000 N,
    it is "heavy", less than 10 N it is "light", and "average" otherwise.
    weight = mass (kg)  acceleration due to gravity (9.8/m/s^2)
    Use: weight, message = get_weight(mass)
    -------------------------------------------------------
    Parameters:
        mass - mass of an object in kg (float > 0)
    Returns:
        weight - weight of an object in Newtons (float)
        message - description of weight of object (str)
    -------------------------------------------------------
    """
    weight = mass * GRAVITY

    if weight > 1000:
        message = "heavy"
    elif weight < 10:
        message = "light"
    else:
        message = "average"

    weight = round(weight, 2)
    return weight, message


def is_leap(year):
    """
    -------------------------------------------------------
    Determines if a year is a leap year. Every year that is
    exactly divisible by four is a leap year, except for years
    that are exactly divisible by 100, but these centurial years
    are leap years if they are exactly divisible by 400. For
    example, the years 1700, 1800, and 1900 are not leap years,
    but the years 1600 and 2000 are.
    Use: result = is_leap(year)
    -------------------------------------------------------
    Parameters:
        year - a year (int > 0)
    Returns:
        result - True if year is a leap year,
            False otherwise (boolean)
    ------------------------------------------------------
    """

    result = True

    if year % 400 == 0:
        result = True

    elif year % 4 == 0:

        if year % 100 == 0:
            result = False

        else:
            result = True

    else:
        result = False

    return result


def wind_speed(speed):
    """
    -------------------------------------------------------
    description
    Use: category = wind_speed(speed)
    -------------------------------------------------------
    Parameters:
        speed - wind speed in km/hr (int >= 0)
    Returns:
        category - description of wind speed (str)
    ------------------------------------------------------
    """

    if 0 <= speed <= 39:
        result = "Breeze"

    elif 39 <= speed <= 61:
        result = "Strong Wind"

    elif 62 <= speed <= 88:
        result = "Gale Winds"

    elif 89 <= speed <= 117:
        result = "Whole Gale"

    elif speed >= 117:
        result = "Hurricane"

    else:
        result = "Unknown"

    return result


def quadrant(x, y):
    """
    -------------------------------------------------------
    Determines location on a plane of an x, y coordinate.
    Use: location = quadrant(x, y)
    -------------------------------------------------------
    Parameters:
        x - x coordinate on a Cartesian plane (float)
        y - y coordinate on a Cartesian plane (float)
    Returns:
        location - one of: 'Quadrant 1', 'Quadrant 2', 'Quadrant 3'
          'Quadrant 4', 'X-Axis', 'Y-Axis', 'Origin' (str)
    -------------------------------------------------------
    """

    if x == 0 and y == 0:
        result = "Origin"

    elif x == 0:
        result = "Y-Axis"

    elif y == 0:
        result = "X-Axis"

    elif x > 0 and y > 0:
        result = "Quadrant 1"

    elif x > 0 and y < 0:
        result = "Quadrant 4"

    elif x < 0 and y > 0:
        result = "Quadrant 2"

    else:
        result = "Quadrant 3"

    return result


def ticket():
    """
    -------------------------------------------------------
    School play ticket price calculation.
    Asks user for their age, and if necessary, if they are
    a student at the school. Prices:
        Infant (age < 3): $0
        Senior (age >= 65): $4.00
        Student (10 <= age < 18): $3.00
            Student of this school: $1.00
        Adult (18 <= age < 65): $5.00
        Kid (3 <= age < 10): $2.00
    Use: price = ticket()
    -------------------------------------------------------
    Parameters:
        none
    Returns:
        price - the price of one ticket (float)
    -------------------------------------------------------
    """
    age = int(input("What is your age?: "))

    if age < INFANTAGE:
        price = INFANT
    elif age >= SENIORAGE:
        price = SENIOR
    elif ADULTAGE1 <= age < ADULTAGE2:
        price = ADULT
    elif STUDENTAGE1 <= age < STUDENTAGE2:
        school = input("Are you a student at this school?: ")
        if school == "Y":
            price = STUDENTOFSCHOOL
        else:
            price = STUDENT
    else:
        price = KID
    return price
