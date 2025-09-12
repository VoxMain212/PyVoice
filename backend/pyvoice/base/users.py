from dataclasses import dataclass


class User:
    nickname: str
    id: int
    user_hash: str


class SelfUser(User):
    jwt_token: str


class Friend(User):
    avatar: bytes
