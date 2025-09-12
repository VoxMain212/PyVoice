from dataclasses import dataclass
from types import FunctionType
import socket
import json


@dataclass
class Packet:
    head: str
    data: dict


class ActionConnection:
    action_sock: socket.socket
    port: int
    is_work: bool
    hendlers:dict[str, FunctionType] = {}

    def __init__(self, port=12011):
        self.port = port
        self.action_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.action_sock.bind(('', port))

    def recv_data(self):
        while self.is_work:
            try:
                data = self.action_sock.recv(8192)
                if data:
                    json_data = json.loads(data)
                    packet = Packet(**json_data)
                    self.analize_data(packet)
            except:
                pass

    def set_handler(self, header: str, handler: FunctionType):
        self.hendlers.setdefault(header, handler)

    def analize_data(self, packet: Packet):
        if not packet.head in self.hendlers.keys():
            return
            #TODO сделать обработчик ошибок
        hendler = self.hendlers[packet.head]
        hendler(packet.data)

    def close(self):
        self.is_work = False
        self.action_sock.close()
        