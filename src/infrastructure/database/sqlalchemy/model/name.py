from enum import Enum, unique


@unique
class SATableNames(Enum):
    MEMBER = "member"
    SERVER = "server"
    USER = "user"
