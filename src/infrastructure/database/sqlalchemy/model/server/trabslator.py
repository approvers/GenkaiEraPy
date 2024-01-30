from src.domain.server.entity import Server
from src.domain.server.value import (
    ServerRecordUID,
    ServerRecordCreatedAt,
    ServerRecordUpdatedAt,
    ServerIdentifier,
    ServerName,
)
from src.infrastructure.database.sqlalchemy.model.server.model import SAServer


class SAServerTranslator:
    @staticmethod
    def to_entity(
            sa_record: SAServer,
    ) -> Server:
        entity: Server = Server(
            record_uid=ServerRecordUID(value=sa_record.record_uid),
            record_created_at=ServerRecordCreatedAt(value=sa_record.record_created_at),
            record_updated_at=ServerRecordUpdatedAt(value=sa_record.record_updated_at),
            identifier=ServerIdentifier(value=sa_record.identifier),
            name=ServerName(value=sa_record.name),
        )

        return entity

    @staticmethod
    def to_sa(
            entity: Server,
    ) -> SAServer:
        sa_record: SAServer = SAServer()

        sa_record.record_uid = entity.record_uid.value
        sa_record.record_created_at = entity.record_created_at.value
        sa_record.record_updated_at = entity.record_updated_at.value
        sa_record.identifier = entity.identifier.value
        sa_record.name = entity.name.value

        return sa_record
