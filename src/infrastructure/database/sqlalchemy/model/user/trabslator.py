from src.domain.user.entity import User
from src.domain.user.value import (
    UserRecordUID,
    UserRecordCreatedAt,
    UserRecordUpdatedAt,
    UserIdentifier,
    UserNickname,
)
from src.infrastructure.database.sqlalchemy.model.user.model import SAUser


class SAUserTranslator:
    @staticmethod
    def to_entity(
            sa_record: SAUser,
    ) -> User:
        entity: User = User(
            record_uid=UserRecordUID(value=sa_record.record_uid),
            record_created_at=UserRecordCreatedAt(value=sa_record.record_created_at),
            record_updated_at=UserRecordUpdatedAt(value=sa_record.record_updated_at),
            identifier=UserIdentifier(value=sa_record.identifier),
            name=UserNickname(value=sa_record.name),
        )

        return entity

    @staticmethod
    def to_sa(
            entity: User,
    ) -> SAUser:
        sa_record: SAUser = SAUser()

        sa_record.record_uid = entity.record_uid.value
        sa_record.record_created_at = entity.record_created_at.value
        sa_record.record_updated_at = entity.record_updated_at.value
        sa_record.identifier = entity.identifier.value
        sa_record.nickname = entity.nickname.value

        return sa_record
