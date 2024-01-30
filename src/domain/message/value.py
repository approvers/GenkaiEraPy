import datetime
from typing import Self, Optional

from pydantic import Field, field_validator

from src.common.library.pydantic.validator.tzinfo import value_must_have_tzinfo
from src.domain.base.value import ValueObject
from src.domain.common.value import RecordCreatedAt, RecordUID


class MessageRecordUID(RecordUID):
    pass


class MessageRecordCreatedAt(RecordCreatedAt):
    pass


class MessageRecordUpdatedAt(RecordCreatedAt):
    pass


class MessageSentAt(ValueObject):
    value: datetime.datetime = Field(
        description="Datetime, must have dt.tzinfo.",
    )

    # noinspection PyNestedDecorators
    @field_validator("value")
    @classmethod
    def value_must_have_tzinfo(
        cls: Self,
        v: datetime.datetime,
    ) -> datetime.datetime:
        value_must_have_tzinfo(v)

        return v


class MessageEditedAt(ValueObject):
    value: Optional[datetime.datetime] = Field(
        description="Datetime, must have dt.tzinfo.",
    )

    # noinspection PyNestedDecorators
    @field_validator("value")
    @classmethod
    def value_must_have_tzinfo(
        cls: Self,
        v: datetime.datetime,
    ) -> datetime.datetime:
        value_must_have_tzinfo(v)

        return v


class MessageIdentifier(ValueObject):
    value: str = Field(
        description="Unique ID, must be unique and cannot be changed.",
    )


class MessageContent(ValueObject):
    value: str = Field(
        description="Content of message.",
    )
