from src.domain.base.entity import Entity
from src.domain.common.value import NullableCreatedAt, NullableUpdatedAt
from src.domain.server.value import ServerIdentifier, ServerName


class Server(Entity):
    created_at: NullableCreatedAt
    updated_at: NullableUpdatedAt

    identifier: ServerIdentifier
    name: ServerName
