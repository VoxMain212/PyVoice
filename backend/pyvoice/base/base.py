from dataclasses import dataclass, asdict
from .users import User
from datetime import datetime
import json


class Pin:
    name: str
    size: str


class ImagePin(Pin):
    __file_ext = [
        'png',
        'jpeg',
    ]
    image_bytes: bytes

class FilePin(Pin):
    __file_ext = [
        '*'
    ]
    file_bytes: bytes


@dataclass
class Message:
    text: str
    owner: User
    date: datetime
    pin: Pin = None

    def json(self):
        return json.dumps(asdict(self))
