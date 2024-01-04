from injector import Injector

from src.di.module.config import GenkaiEraConfigModule
from src.di.module.database import GenkaiEraSADatabaseModule

container = Injector(
    [
        GenkaiEraConfigModule,
        GenkaiEraSADatabaseModule,
    ]
)
