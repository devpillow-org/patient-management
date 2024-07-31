import datetime


def get_current_timestamp():
    return datetime.datetime.now().timestamp()


def has_past_lease(timestamp: float, lease: int = 10):
    now = datetime.datetime.fromtimestamp(get_current_timestamp())
    token_created_time = datetime.datetime.fromtimestamp(timestamp)
    difference_time = now - token_created_time
    return difference_time >= datetime.timedelta(minutes=lease)