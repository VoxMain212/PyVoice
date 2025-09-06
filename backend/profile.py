from dataclasses import dataclass, asdict
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import json
import base64

from config import SETTINGS_PATH, USER_PROFILES_PATH


@dataclass
class UserProfile:
    nickname: str
    unique_code: str
    hash_mac: str

    def __init__(self, nickname: str, unique_code: str, user_hash: str):
        self.nickname = nickname
        self.unique_code = unique_code
        self.hash_mac = user_hash


@dataclass
class UserSettings:
    pass


def generate_key_from_password(password: str, salt: bytes) -> bytes:
    """Генерация ключа из пароля с помощью PBKDF2"""
    password_bytes = password.encode('utf-8')
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password_bytes))
    return key


def encrypt_profile_info(profile: UserProfile, password: str):
    salt = os.urandom(16)
    
    # Получаем ключ из пароля
    key = generate_key_from_password(password, salt)
    fernet = Fernet(key)
    data = asdict(profile)
    
    # Шифруем данные
    encrypted_data = fernet.encrypt(data)
    with open(f"{profile.nickname}_profile", 'wb') as f:
        f.write(salt + encrypted_data)
    return True

    
def get_profile_info(nickname: str, password: str):
    if not os.path.exists(f'{USER_PROFILES_PATH}\\{nickname}_profile'):
        return None
    with open(f"{USER_PROFILES_PATH}\\{nickname}_profile", "rb") as f:
        data = f.read()

    salt = data[:16]
    enc_data = data[16:]

    key = generate_key_from_password(password, salt)
    fernet = Fernet(key)

    try:
        dec_data = fernet.decrypt(enc_data)
        json_data = json.loads(dec_data)

        return json_data
    except:
        return None
    
def load_user_settings(nickname=None):
    if not os.path.exists(f'{SETTINGS_PATH}\\{nickname}_settings'):
        return None
    with open(f'{SETTINGS_PATH}\\{nickname}_settings', 'r', encoding='utf-8') as f:
        settings = json.load(f)
    return settings
