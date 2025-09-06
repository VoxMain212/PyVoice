from dotenv import load_dotenv
import os


load_dotenv('.env')

DEBUG=True


LOCAL_DB_PATH = '.\\local'

SETTINGS_PATH='.\\settings'
USER_PROFILES_PATH='.\\profiles'
MESSAGES_DB_PATH=f"{LOCAL_DB_PATH}\\messages"
BASE_DB_PATH=f"{LOCAL_DB_PATH}\\base"

if DEBUG:
    API_URL="127.0.0.1:8000"
else:
    API_URL=""