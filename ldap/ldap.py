#!/usr/bin/python3
from ldap3 import Server, Connection

server = Server('127.0.0.1', use_ssl=False)
ldap = Connection(server, user='cn=admin,dc=python,dc=com,dc=br', password='123')

if not ldap.bind():
    print("Você não conseguiu se conectar na base de dados do LDAP que você acabou de criar na aula de Python sobre OpenLDAP")
else:
    print("Show!")

