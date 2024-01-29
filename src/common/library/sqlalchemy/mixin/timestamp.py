import datetime

from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

DEFAULT_TIMEZONE: datetime.timezone = datetime.timezone.utc

DEFAULT_CREATED_AT_COLUMN_NAME: str = "created_at"
DEFAULT_UPDATED_AT_COLUMN_NAME: str = "updated_at"


class CreatedAtMixin(object):
    record_created_at: Mapped[datetime.datetime] = mapped_column(
        name=DEFAULT_CREATED_AT_COLUMN_NAME,
        type_=DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )


class UpdatedAtMixin(object):
    record_updated_at: Mapped[datetime.datetime] = mapped_column(
        name=DEFAULT_UPDATED_AT_COLUMN_NAME,
        type_=DateTime(timezone=True),
        onupdate=func.now(),
        nullable=False,
    )


# We get an error when we do 'class TimestampMixin(CreatedAtMixin, UpdatedAtMixin)'
class TimestampMixin(object):
    record_created_at: Mapped[datetime.datetime] = mapped_column(
        name=DEFAULT_CREATED_AT_COLUMN_NAME,
        type_=DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    record_updated_at: Mapped[datetime.datetime] = mapped_column(
        name=DEFAULT_UPDATED_AT_COLUMN_NAME,
        type_=DateTime(timezone=True),
        onupdate=func.now(),
        nullable=False,
    )
