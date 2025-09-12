from types import FunctionType
from ..base.users import User
import socket



class AudioSendConnection:
    send_sock: socket.socket
    addr: tuple[str, int]

    def __init__(self, address: tuple[str, int]):
        self.addr = address
        self.send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def connect(self):
        self.send_sock.connect(self)

    def send_data(self, data):
        self.send_sock.send(data)


class AudioGetConnection:
    get_sock: socket.socket
    port: int
    is_work: bool = True

    def __init__(self):
        self.get_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.get_sock.bind(('', 0))
        self.port = self.get_sock.getsockname()[1]        
    
    def recv_data(self, handler: FunctionType):
        while self.is_work:
            data = self.get_sock.recv(8192)
            if data:
                handler(data)

    def close(self):
        self.is_work = False
        self.get_sock.close()

    def __del__(self):
        self.close()


class AudioChannel:
    user: User

    def __init__(self, user: User):
        self.user = user
