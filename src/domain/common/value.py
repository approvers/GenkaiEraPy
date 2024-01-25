import datetime
from typing import Self, Optional

from pydantic import Field, field_validator

from src.common.library.pydantic.validator.tzinfo import value_must_have_tzinfo
from src.domain.base.value import ValueObject


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
