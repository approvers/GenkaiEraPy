from pydantic_settings import BaseSettings, SettingsConfigDict


class GenkaiEraConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="GENKAIERA_", case_sensitive=True)

    IS_CI: int = 0
    IS_TEST: int = 0

    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB_NAME: str = "genkaiera"
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    POSTGRES_CONNECT_ARGS: dict[str, str] = {}
    POSTGRES_EXPIRE_ON_COMMIT: bool = False
    POSTGRES_AUTOCOMMIT: bool = False
    POSTGRES_AUTOFLUSH: bool = False

    def get_postgres_dsn(self) -> str:
        result: str = (
            f"postgresql+asyncpg://"
            f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/"
            f"{self.POSTGRES_DB_NAME}"
        )

        return result


test_settings = SettingsConfigDict(
    env_prefix="GENKAIERA_",
    case_sensitive=True,
    env_file="./test.env",
)


class GenkaiEraTestConfig(GenkaiEraConfig):
    model_config = test_settings

    POSTGRES_DB_NAME: str = "genkaiera_test"
