from pydantic import BaseModel

from src.common.library.pydantic.config import BaseConfig


class Field(BaseModel):
    model_config = BaseConfig


class FrozenField(BaseModel):
    model_config = BaseConfig
