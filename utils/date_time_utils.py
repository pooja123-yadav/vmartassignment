import datetime as main_datetime
from datetime import datetime

import pytz
from django.utils import timezone


def obj_converter(o):
    if isinstance(o, datetime):
        return o.__str__()


def add_hours_to_datetime(dt, hours):
    return dt + main_datetime.timedelta(hours=hours)


def add_minutes_to_datetime(dt, minutes):
    return dt + main_datetime.timedelta(minutes=minutes)


def add_days_to_datetime(dt, days):
    return dt + main_datetime.timedelta(days=days)


def get_current_datetime():
    return datetime.now()


def get_current_time():
    return datetime.now().time()


def get_current_date():
    return datetime.now().date()


def get_current_timestamp():
    return datetime.now().timestamp()
