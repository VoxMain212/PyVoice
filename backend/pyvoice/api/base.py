import requests


class PyVoiceAPI:
    __instance = None
    jwt_token: str
    __api_url = ""

    def __new__(self, data):
        if self.__instance is None:
            self.__instance = super().__new__(self)
            self.__instance.__initialize(**data)
        return self.__instance
    
    def __initialize(self, jwt_token):
        pass

    @staticmethod
    def register(nickname: str, user_hash: str):
        pass

    def heartbeat(self):
        pass

    def get_friend_info(self, friend_id: int):
        pass

    def get_server_info(self, server_id: int):
        pass
