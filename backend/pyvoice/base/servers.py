from dataclasses import dataclass
from .base import Message
from .users import User

class ServerMember(User):
    pass


class Room:
    title: str


class VoiceRoom:
    pass


class TextRoom:
    messages: list[Message]


class Server:
    members: list[ServerMember]
    title: str
    owner: User
    rooms: list[Room]
