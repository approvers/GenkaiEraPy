import datetime
import uuid
from typing import Self, Optional

from pydantic import Field, field_validator

from src.common.library.pydantic.validator.tzinfo import value_must_have_tzinfo
from src.domain.base.value import ValueObject


class UID(ValueObject):
    value: uuid.UUID = Field(
        description="Unique ID, must be unique and cannot be changed.",
    )

    @staticmethod
    def generate() -> "UID":
        generated: UID = UID(value=uuid.uuid4())

        return generated


class NullableUID(ValueObject):
    value: Optional[uuid.UUID] = Field(
        description="Unique ID, must be unique and cannot be changed.",
    )

    @staticmethod
    def generate() -> "NullableUID":
        generated: NullableUID = NullableUID(value=uuid.uuid4())

        return generated


class CreatedAt(ValueObject):
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


class UpdatedAt(ValueObject):
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


class NullableCreatedAt(ValueObject):
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


class NullableUpdatedAt(ValueObject):
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
