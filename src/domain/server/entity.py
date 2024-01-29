from src.domain.base.entity import Entity
from src.domain.server.value import (
    ServerIdentifier,
    ServerName,
    ServerRecordCreatedAt,
    ServerRecordUpdatedAt,
    ServerRecordUID,
)


class Server(Entity):
    record_uid: ServerRecordUID
    record_created_at: ServerRecordCreatedAt
    record_updated_at: ServerRecordUpdatedAt

    identifier: ServerIdentifier

    name: ServerName
