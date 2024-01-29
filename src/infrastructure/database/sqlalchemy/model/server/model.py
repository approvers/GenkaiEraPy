from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.common.library.sqlalchemy.mixin.timestamp import TimestampMixin
from src.common.library.sqlalchemy.mixin.uid import UIDMixin
from src.infrastructure.database.sqlalchemy.model.base.model import SABaseModel
from src.infrastructure.database.sqlalchemy.model.name import SATableNames


class SAServer(SABaseModel, UIDMixin, TimestampMixin):
    __tablename__: str = SATableNames.MEMBER.value

    identifier: Mapped[str] = mapped_column(
        type_=String(length=255),
        nullable=False,
        unique=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        type_=String(),
        nullable=False,
    )
