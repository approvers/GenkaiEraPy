from src.domain.base.entity import Entity
from src.domain.message.value import MessageRecordUID, MessageContent


class Message(Entity):
    record_uid: MessageRecordUID
    record_created_at: MessageRecordUID
    record_updated_at: MessageRecordUID

    content: MessageContent
