"""
Challenge Description : Given a time in -hour AM/PM format, convert it to military (24-hour) time.
  Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
  - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
"""


def timeConversion(s: str) -> str:
    """
    parameters:
    s (str): Time in 12 - hour format (hh:mm:ssAM or hh:mm:ssPM)

    returns:
    str: The time in 24-hour militarty time

    Example usage:
    >>> timeConversion("12:01:00AM")
    '00:01:00'
    """

    # Declare variable we will need for conversion in AM and PM
    am_time = '00'
    pm_time = ''

    # solve for the morning
    #  Check if the time is in morning and specifically 12AM
    if 'AM' in s and '12' in s:
        # then convert the hour to '00'
        return am_time + s[2:8]

    #  Check if it is 12 in the Afternoon for which we no need to modify
    elif 'PM' in s and '12' in s:
        return s[:8]

    #  Finally check if it is past 12 in the afternoon, which we have to modify to militarty time
    # By adding 12 to the current hour and keeping the minutes and seconds the
    # same
    elif 'PM' in s:
        hours = s[:2]
        hours = int(hours) + 12
        pm_time = str(hours) + s[2:8]
        return pm_time

    # otherwise we just return the time with no AM or PM preceding it to show
    # 24 hour military time
    else:
        return s[:8]
