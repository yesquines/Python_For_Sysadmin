#!/usr/bin/python3
#TENTAR Cadastrar o usuário pela API
from requests import post #Chamada do modulo especifico da biblioteca requests
from requests import get #Chamada do modulo especifico da biblioteca requests

nome = input("Digite o Nome: ")
email = input("Digite o Email: ")
idade = input("Digite o Idade: ")

data = {"nome":nome,"email":email,"idade":idade}
response = post('http://172.16.0.106/usuarios', json=data)

if response.status_code == 200:
    print(response.text)
    getando = get('http://172.16.0.106/usuarios')
    if getando.status_code == 200:
        print(getando.json()[-1])
else:
    print("DEU RUIM")
