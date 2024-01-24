from pydantic import BaseModel

from src.common.library.pydantic.config import BaseConfig


class ValueObject(BaseModel):
    model_config = BaseConfig


class FrozenValueObject(BaseModel):
    model_config = BaseConfig
