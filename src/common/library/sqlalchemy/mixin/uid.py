import uuid

from sqlalchemy.orm import Mapped, mapped_column

from src.common.library.sqlalchemy.field.sauuid import SAUUID

DEFAULT_UID_COLUMN_NAME: str = "uid"


class UIDMixin(object):
    record_uid: Mapped[uuid.UUID] = mapped_column(
        name=DEFAULT_UID_COLUMN_NAME,
        type_=SAUUID,
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
    )
