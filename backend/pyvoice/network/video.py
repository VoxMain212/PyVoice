import socket


class VideoSendConnection:
    send_sock: socket.socket
    port: int

    def __init__(self):
        self.send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.send_sock.bind(('', 0))
        self.port = self.send_sock.getsockname()

class VideoGetConnection:
    get_sock: socket.socket

    def __init__(self):
        pass


class VideoChannel:
    def __init__(self):
        pass

