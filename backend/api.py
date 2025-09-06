from uuid import uuid4
import requests

from config import API_URL

"""
Модуль отвечающий за общение с 
триггер сервером
"""

class ServerAPI:
    user_hash: str

    def __init__(self, user_hash):
        self.user_hash = user_hash

    @classmethod
    def register(cls, nickname, user_hash):
        data = {
            'nickname': nickname,
            'hash_mac': user_hash,
            'unique_code': uuid4().hex 
        }
        requests.post(f"{API_URL}/register", json=data)
    
    def login(self, id: int, nickname: str, unique_code: str, hash_mac: str):
        data = {
            'id': id,
            'nickname':nickname,
            'hash_mac': hash_mac,
            'unique_code': unique_code
        }
        requests.post(f"{API_URL}/login", json=data)

    def get_servers(self, invited_server_list: list):
        data = {
            'servers': invited_server_list
        }
        requests.get(f"{API_URL}/get_servers", json=data)

    def get_friends(self, friends_id_list: list[int]):
        data = {
            'friends': friends_id_list
        }
        requests.get(f"{API_URL}/get_friends", json=data)
        
