import datetime


def utcnow() -> datetime.datetime:
    """
    Return the current time in UTC.
    """
    now_in_utc: datetime.datetime = datetime.datetime.now(tz=datetime.timezone.utc)

    return now_in_utc
