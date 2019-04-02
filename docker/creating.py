#!/usr/bin/python3
#Tentar verificar se o container realmente está escutando
#na porta 1000
#Utilizando o modulo requests
import requests
import docker


DOCKER_URL='tcp://127.0.0.1:2376'

#unix://var/run/docker.sock
client = docker.DockerClient(base_url=DOCKER_URL, version='auto')

try:
    client.containers.get('apache').remove(force=True)
except:
    pass

#                                       CONTAINER
client.containers.run('httpd:alpine', ports={80 : 10000}, detach=True, name='apache', environment={'NOME' : 'Paramahannsa Yogananda'})
#                                                 HOST

#GET ALL API's INFORMATION 
print("Getting all API's INFORMATION")
response = requests.get('http://127.0.0.1:2376/containers/json')
if response.status_code == 200:
       print(response.json())

#VERIFY IF PORT 1000 IS LISTING
rep = requests.get('http://127.0.0.1:10000')
print("\nIs Container UP?")
if response.status_code == 200:
    print("O Conteiner está de pé mano")
