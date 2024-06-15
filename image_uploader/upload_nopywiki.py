import os
import json
import requests

S = requests.Session()

url = 'https://www.tfd.wiki/api.php'

# Login
params = {
    "action": "query",
    "meta": "tokens",
    "type": "login",
    "format": "json"
}
lgtoken = S.get(url, params=params).json()['query']['tokens']['logintoken']

file = open('user-password.py', 'r')
botPassword = json.loads(file.read().strip(' \n').split('\n')[-1].replace('BotPassword', '').replace("'", '"').replace('(', '[').replace(')', ']'))
params = {
    "action": "login",
    "format": "json",
    "lgname": f"{botPassword[0]}@{botPassword[1][0]}",
    "lgpassword": botPassword[1][1],
    "lgtoken": lgtoken
}
resp = S.post(url, data=params)

params = {
    "action": "query",
    "meta": "tokens",
    "format": "json"
}
csrf_token = S.get(url, params=params).json()["query"]["tokens"]["csrftoken"]

#Upload Files
description = """== Licensing ==
{{From NEXON}}
"""
directory = './toUpload'
for filename in os.listdir(directory):

    file_path = os.path.join(directory, filename)
    filename = filename.replace('_', ' ')

    params = {
        "action": "upload",
        "format": "json",
        "filename": filename,
        "text": description,
        "token": csrf_token
    }

    file = open(file_path, 'rb')
    file = {'file':(filename, file, 'multipart/form-data')}

    resp = S.post(url, data=params, files=file).json()