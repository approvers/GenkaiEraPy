from injector import Binder, InstanceProvider, Module

from config import GenkaiEraConfig, GenkaiEraTestConfig


class GenkaiEraConfigModule(Module):
    def __init__(self) -> None:
        is_test: int = GenkaiEraConfig().IS_TEST  # type: ignore

        self.__config: GenkaiEraConfig
        if is_test == 1:
            self.__config = GenkaiEraTestConfig()  # type: ignore
        else:
            self.__config = GenkaiEraConfig()  # type: ignore

    def configure(self, binder: Binder) -> None:
        binder.bind(
            GenkaiEraConfig,
            InstanceProvider(self.__config),
        )
