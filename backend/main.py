from pyvoice.PyVoice import PyVoiceController
import os
import sys
import json


controller = PyVoiceController()


sys.stdout.flush()

while 1:
    line = sys.stdin.readline().strip()
    if not line:
        continue
    data = json.loads(line)

    controller.handle(data)
    sys.stdout.flush()

    # if data['type'] == "auth":
    #     if not os.path.exists("auth.json"):
    #         print(json.dumps({"type": 'auth', 'status': "not-auth"}))
    #     else:
    #         login = data['nickname']
    #         password = data['password']
    #         print(json.dumps({"type": 'auth', 'status': "auth"}))
    #     sys.stdout.flush()
    # elif data['type'] == "register":
    #     login = data['nickname']
    #     password = data['password']
    # elif data['type'] == "get-friends":
    #     print(json.dumps({"type": 'friend-list', 'friends': [{
    #         'nick': 'asd',
    #         'ip':'127.0.0.1',
    #         'online': True
    #     }]}))
    #     sys.stdout.flush()