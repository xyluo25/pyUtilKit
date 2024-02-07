# -*- coding:utf-8 -*-
##############################################################
# Created Date: Tuesday, February 6th 2024
# Contact Info: luoxiangyong01@gmail.com
# Author/Copyright: Mr. Xiangyong Luo
##############################################################


import zoneinfo
import datetime


def list_all_timezones() -> set:
    """this function is used to list all available timezones

    Returns:
        set : a set of all available timezones

    Example:
        >>> from pyufunc import list_all_timezones
        >>> list_all_timezones()
        {'Africa/Abidjan',
        'Africa/Accra',
        'Africa/Addis_Ababa',
        'Africa/Algiers',
        'Africa/Asmara',
        'Africa/Asmera',
        'Africa/Bamako',
        'Africa/Bangui',
        ...}

    """
    return zoneinfo.available_timezones()


def get_timezone() -> str:
    """this function is used to check the current timezone

    Returns:
        str : the current timezone

    Example:
        >>> from pyufunc import get_current_timezone
        >>> get_current_timezone()
        'Asia/Shanghai'
    """
    return str(datetime.datetime.now().astimezone().tzinfo)


#  convert current datetime to another timezone datetime
def cvt_dt_to_tz(dt: datetime = datetime.datetime.now(),
                             timezone: str = "UTC") -> datetime:
    """this function is used to convert datetime to another timezone datetime

    Args:
        dt (datetime, optional): the datetime to be converted. Defaults to datetime.datetime.now().
        timezone (str, optional): desired timezone. Defaults to "UTC".

    Returns:
        datetime: the converted datetime

    Example:
        >>> from pyufunc import convert_dt_to_another_tz
        >>> convert_dt_to_another_tz(datetime.datetime.now(), "Asia/Shanghai")
        datetime.datetime(2024, 2, 6, 14, 10, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='Asia/Shanghai'))

    """

    # check if the timezone is valid
    try:
        # Attempt to create a ZoneInfo object with the given timezone string
        zoneinfo.ZoneInfo(timezone)
        isValid_tz = True
    except zoneinfo.ZoneInfoNotFoundError:
        isValid_tz = False  # Exception means it's not a valid timezone
    except Exception as e:
        print(f"An error occurred while checking the timezone: {e}")
        isValid_tz = False

    if isValid_tz:
        return dt.astimezone(zoneinfo.ZoneInfo(timezone))

    print(f"Invalid timezone: {timezone}, will return original datetime.")
    return dt
