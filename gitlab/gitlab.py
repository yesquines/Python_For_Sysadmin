#!/usr/bin/python3
import requests

GITLAB='http://172.10.10.20/api/v4/'
TOKEN='zuYXzT1VyZy_x-X87kAK'
headers = {'Private-Token' : TOKEN}
user = {"name":"Yago","username":"yago","email":"yago.almeida@4linux.com.br","password":"4linux123"}

users = requests.post(GITLAB + 'users', json=user, headers=headers)
if users.status_code != 201:
    print(users.text)
    exit(1)

users = requests.get(GITLAB + 'users', headers=headers)
for u in users.json():
    print(u)
