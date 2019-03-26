#!/usr/bin/python3
#Pegar o CEP do terminal -> input
#Exibir apenas o logradouro
import requests

cep = input("Digite o CEP: ")
response = requests.get('http://viacep.com.br/ws/{0}/json/'.format(cep)) #Format pode ser chamado com indexão {0},{1},etc

if response.status_code == 200:
   print(response.json()["logradouro"])
