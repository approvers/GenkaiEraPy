import datetime
import uuid
from typing import Self, Optional, Type

from pydantic import Field, field_validator

from src.common.library.pydantic.validator.tzinfo import value_must_have_tzinfo
from src.domain.base.value import ValueObject


class RecordUID(ValueObject):
    value: uuid.UUID = Field(
        description="Unique ID, must be unique and cannot be changed.",
    )

    @classmethod
    def generate(cls: Type[Self]) -> Self:
        return RecordUID(value=uuid.uuid4())


class NullableRecordUID(ValueObject):
    value: Optional[uuid.UUID] = Field(
        description="Unique ID, must be unique and cannot be changed.",
    )

    @classmethod
    def generate(cls: Type[Self]) -> Self:
        return NullableRecordUID(value=uuid.uuid4())


class RecordCreatedAt(ValueObject):
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


class RecordUpdatedAt(ValueObject):
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


class NullableRecordCreatedAt(ValueObject):
    value: Optional[datetime.datetime] = Field(
        description="Datetime, must have dt.tzinfo.",
    )

    # noinspection PyNestedDecorators
    @field_validator("value")
    @classmethod
    def value_must_have_tzinfo(
        cls: Self,
        v: Optional[datetime.datetime],
    ) -> Optional[datetime.datetime]:
        if v is None:
            return v

        value_must_have_tzinfo(v)

        return v


class NullableRecordUpdatedAt(ValueObject):
    value: Optional[datetime.datetime] = Field(
        description="Datetime, must have dt.tzinfo.",
    )

    # noinspection PyNestedDecorators
    @field_validator("value")
    @classmethod
    def value_must_have_tzinfo(
        cls: Self,
        v: Optional[datetime.datetime],
    ) -> Optional[datetime.datetime]:
        if v is None:
            return v

        value_must_have_tzinfo(v)

        return v
