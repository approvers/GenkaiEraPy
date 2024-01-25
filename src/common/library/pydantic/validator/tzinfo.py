import datetime


def value_must_have_tzinfo(
    v: datetime.datetime,
) -> datetime.datetime:
    if v.tzinfo is None:
        raise ValueError("the value must have tzinfo.")

    return v
