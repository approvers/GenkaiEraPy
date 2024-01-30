from injector import Injector

from src.di.module.config import GenkaiEraConfigModule
from src.di.module.database import GenkaiEraSADatabaseModule
from src.di.module.message import GenkaiEraMessageModule

container = Injector(
    [
        GenkaiEraConfigModule,
        GenkaiEraSADatabaseModule,
        GenkaiEraMessageModule,
    ]
)
