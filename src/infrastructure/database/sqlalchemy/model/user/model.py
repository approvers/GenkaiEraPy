from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.common.library.sqlalchemy.mixin.timestamp import CreatedAtMixin
from src.common.library.sqlalchemy.mixin.uid import UIDMixin
from src.infrastructure.database.sqlalchemy.model.base.model import SABaseModel
from src.infrastructure.database.sqlalchemy.model.name import SATableNames


class SAUser(SABaseModel, UIDMixin, CreatedAtMixin):
    __tablename__: str = SATableNames.USER

    identifier: Mapped[str] = mapped_column(
        type_=String(length=255),
        nullable=False,
        unique=True,
        index=True,
    )

    nickname: Mapped[str] = mapped_column(
        type_=String(),
        nullable=False,
    )
