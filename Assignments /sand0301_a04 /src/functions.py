"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-03-03"
-------------------------------------------------------
"""
# Imports

# Constants

first_day = "Sunday"
second_day = "Monday"
third_day = "Tuesday"
fourth_day = "Wednesday"
fifth_day = "Thursday"
sixth_day = "Friday"
seventh_day = "Saturday"

quality1 = "Good"
quality2 = "Moderate"
quality3 = "Unhealthy for Densitive Groups"
quality4 = "Unhealthy"
quality5 = "Very Unhealthy"
quality6 = "Hazardous"

colour1 = "fuchsia"
colour2 = "yellow"
colour3 = "aqua"
colour4 = "red"
colour5 = "blue"
colour6 = "green"


def day_of_the_week(day_number):
    """
    -------------------------------------------------------
    Returns the day of the week depending on the user integer.
        1 = Monday
        2 = Tuesday
        3 = Wednesday
        4 = Thursday
        5 = Friday
        6 = Saturday
        7 = Sunday
    Returns "Error" if number is less than 1 or greater
    than 7.
    Use: day = day_of_the_week(day_number)
    -------------------------------------------------------
    Parameters:
        day_number - an integer (int > 0)
    Returns:
        day - the day of the week (str)
    ------------------------------------------------------
    """

    if (day_number < 1) or (day_number > 7):
        day = "Error"
    elif day_number == 1:
        day = first_day
    elif day_number == 2:
        day = second_day
    elif day_number == 3:
        day = third_day
    elif day_number == 4:
        day = fourth_day
    elif day_number == 5:
        day = fifth_day
    elif day_number == 6:
        day = sixth_day
    else:
        day = seventh_day
    return day


def level_of_pollution(air_quality_index):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if air_quality_index is negative.
    Use: pollution_level = level_of_pollution(air_quality_index)
    -------------------------------------------------------
    Parameters:
        air_quality_index - Air Quality Index (int)
    Returns:
        pollution_level - name of pollution pollution_level (str)
    ------------------------------------------------------
    """

    if air_quality_index < 0:
        pollution_level = "Error"
    elif air_quality_index >= 0 and air_quality_index <= 50:
        pollution_level = quality1
    elif air_quality_index >= 51 and air_quality_index <= 100:
        pollution_level = quality2
    elif air_quality_index >= 101 and air_quality_index <= 150:
        pollution_level = quality3
    elif air_quality_index >= 151 and air_quality_index <= 200:
        pollution_level = quality4
    elif air_quality_index >= 201 and air_quality_index <= 300:
        pollution_level = quality5
    else:
        pollution_level = quality6
    return pollution_level


def largest_product(val1, val2, val3):
    """
    -------------------------------------------------------
    Returns the product of the two largest values of
    val1, val2, and val3.
    Use: product = largest_product(val1, val2, val3)
    -------------------------------------------------------
    Parameters:
        val1 - a number (float)
        val2 - a number (float)
        val3 - a number (float)
    Returns:
        product - the product of the two largest values of
            val1, val2, and val3 (float)
    ------------------------------------------------------
    """
    product = 0
    if val1 < val2 and val1 < val3:
        product = val2 * val3
    elif val2 < val1 and val2 < val3:
        product = val1 * val3
    elif val3 < val2 and val3 < val1:
        product = val2 * val1
    else:
        product = "Error"
    return product


def colour_mix(rgb_colour1, rgb_colour2):
    """
    -------------------------------------------------------
    Determines the secondary rgb_colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the rgb_colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: rgb_colour = colour_mix(rgb_colour1, rgb_colour2)
    -------------------------------------------------------
    Parameters:
        rgb_colour1 - a primary RGB rgb_colour (str)
        rgb_colour2 - a primary RGB rgb_colour (str)
    Returns:
        rgb_colour - a secondary RGB rgb_colour (str)
    -------------------------------------------------------
    """

    if rgb_colour1 == "red" and rgb_colour2 == "blue" or rgb_colour1 == "blue" and rgb_colour2 == "red":
        rgb_colour = colour1
    elif rgb_colour1 == "red" and rgb_colour2 == "green" or rgb_colour1 == "green" and rgb_colour2 == "red":
        rgb_colour = colour2
    elif rgb_colour1 == "green" and rgb_colour2 == "blue" or rgb_colour1 == "blue" and rgb_colour2 == "green":
        rgb_colour = colour3
    elif rgb_colour1 == "red" and rgb_colour2 == "red":
        rgb_colour = colour4
    elif rgb_colour1 == "blue" and rgb_colour2 == "blue":
        rgb_colour = colour5
    else:
        rgb_colour = colour6
    return rgb_colour


def yee_ha(number):
    """
    -------------------------------------------------------
    Determines if program is divisible by 3, or 7, or both.
    Returns "Yee" if number is evenly divisible by 3, "Ha"
    if number is evenly divisible by 7, "Yee Ha" if number
    is evenly divisible by both 3, and 7, and "Nada" if
    number is none of the above.
    Use: result = yee_ha(number)
    -------------------------------------------------------
    Parameters:
        number - an integer
    Returns:
        result = the result of the quotient
    ------------------------------------------------------
    """
    YEE = "Yee"
    HA = "Ha"
    YEE_HA = "Yee Ha"
    NADA = "Nada"

    remainder_one = number % 3
    remainder_two = number % 7

    if remainder_one == 0 and remainder_two == 0:
        result = YEE_HA
    elif remainder_one == 0:
        result = YEE
    elif remainder_two == 0:
        result = HA
    else:
        result = NADA
    return result
