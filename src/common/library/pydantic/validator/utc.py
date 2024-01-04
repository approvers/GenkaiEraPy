import datetime


def datetime_must_be_utc(value: datetime.datetime) -> None:
    if not hasattr(value, "tzinfo"):
        raise ValueError(
            "ValueError: `datetime.datetime` value must be UTC, "
            "but the object doesn't have attribute 'tzinfo'.\n"
        )

    if value.tzinfo != datetime.timezone.utc:
        raise ValueError(
            f"ValueError: `datetime.datetime` value must be UTC, but got {value.tzinfo}.\n"
            f"(tzinfo: {value.tzinfo})"
        )
