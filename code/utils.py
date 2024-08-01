import datetime
import time


def get_current_timestamp():
    return datetime.datetime.now().timestamp()


def add_time_in(
    days, hours: int, minutes: int, seconds: int, to_add: datetime
):
    #TODO: validate if timezone is needed
    return to_add + datetime.timedelta(
        days=days, hours=hours, minutes=minutes, seconds=seconds
    )


def remove_time_in(days, hours: int, minutes: int, seconds: int, to_sub: datetime):
    #TODO: validate if timezone is needed
    return to_sub - datetime.timedelta(
        days=days, hours=hours, minutes=minutes, seconds=seconds
    )


def has_past_lease(timestamp: float, lease: int = 10):
    now = datetime.datetime.fromtimestamp(get_current_timestamp())
    token_created_time = datetime.datetime.fromtimestamp(timestamp)
    difference_time = now - token_created_time
    return difference_time >= datetime.timedelta(minutes=lease)
