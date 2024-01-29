from enum import Enum, unique


@unique
class SATableNames(Enum):
    # Order: alphabetically
    MEMBER = "member"
    SERVER = "server"
    USER = "user"
