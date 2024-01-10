from pydantic.config import ConfigDict

BaseConfig = ConfigDict(
    validate_default=True,
    validate_assignment=True,
    extra="forbid",
    use_enum_values=True,
)

FrozenConfig = ConfigDict(
    validate_default=True,
    validate_assignment=True,
    extra="forbid",
    use_enum_values=True,
    frozen=True,
)
