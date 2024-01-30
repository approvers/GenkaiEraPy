from pydantic import BaseModel

from src.common.library.pydantic.config import FrozenConfig


class Entity(BaseModel):
    model_config = FrozenConfig
