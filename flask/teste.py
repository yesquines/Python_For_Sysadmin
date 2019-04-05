#!/usr/bin/python3
import os, time, requests

time.sleep(5)

APP_PORT = os.environ['APP_PORT']

try:
    response = requests.get('http://127.0.0.1:{0}'.format(APP_PORT))
except:
    print('Endpoint não encontrado')
    exit(1)

print('Testes Realizados com Sucesso')
